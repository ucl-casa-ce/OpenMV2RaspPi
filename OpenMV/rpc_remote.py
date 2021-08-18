# OpenMV as Remote Device (USB VCP)
# Script uses RPC library pre-installed on the OpenMV device 
import pyb, image, network, math, rpc, sensor, struct, tf

# Initialise the camera sensor
sensor.reset()
# Set pixel format (GRAYSCALE/RGB565/BAYER/JPEG)
sensor.set_pixformat(sensor.RGB565)
# Set frame size (QVGA/VGA/SVGA)
sensor.set_framesize(sensor.QVGA)
# Skip frames for t milliseconds to enable camera to stabilize
sensor.skip_frames(time = 2000)

# Setup LED colour and initial state (1: red/2: green/3: blue/4: IR)
led = pyb.LED(2)
led.off()

# Setup the OpenMV Cam for control over a USB VCP
interface = rpc.rpc_usb_vcp_slave()

################################################################
# Call Backs
################################################################

# Helper method to draw frames around detected features
def draw_detections(img, dects):
    for d in dects:
        c = d.corners()
        l = len(c)
        for i in range(l): img.draw_line(c[(i+0)%l] + c[(i+1)%l], color = (0, 255, 0))
        img.draw_rectangle(d.rect(), color = (255, 0, 0))

# Function returns x, y, w, and h of the largest face within view.
def face_detection(data):
    sensor.set_pixformat(sensor.GRAYSCALE)
    sensor.set_framesize(sensor.QVGA)
    faces = sensor.snapshot().gamma_corr(contrast=1.5).find_features(image.HaarCascade("frontalface"))
    if not faces: return bytes() # No detections.
    for f in faces: sensor.get_fb().draw_rectangle(f, color = (255, 255, 255))
    out_face = max(faces, key = lambda f: f[2] * f[3])
    return struct.pack("<HHHH", out_face[0], out_face[1], out_face[2], out_face[3])

# Function returns a "person" or "no_person" within view.
def person_detection(data):
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    scores = tf.classify("person_detection", sensor.snapshot())[0].output()
    return ['unsure', 'person', 'no_person'][scores.index(max(scores))].encode()

# Function returns count of faces.
def face_counter(data):
    sensor.set_pixformat(sensor.GRAYSCALE)
    sensor.set_framesize(sensor.VGA)
    # Capture image and apply post processing
    img = sensor.snapshot().gamma_corr(contrast=1.5).lens_corr(2.5)
    # Find faces
    # Note: Lower scale factor scales-down the image more and detects smaller objects.
    # Higher threshold results in a higher detection rate, with more false positives.
    faces = img.find_features(image.HaarCascade("frontalface"), threshold=0.75, scale_factor=1.25)
    
    if not faces:
        led.off()
        return bytes() # No detections.
    else:
        led.on()
        return str(len(faces)).encode()

# Function returns count of people
def people_counter(data):
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    people = tf.classify("person_detection", sensor.snapshot()).output()
    if not people: 
        led.off()
        return bytes() # No detections.
    else:
        led.on()
        return str(len(people)).encode()

# Register call backs.
interface.register_callback(face_detection)
interface.register_callback(person_detection)
interface.register_callback(face_counter)
interface.register_callback(people_counter)



# Start processing remote events. Interface.loop() does not return.
interface.loop()
