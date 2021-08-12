# OpenMV as Remote Device (USB VCP)
# Script uses RPC library pre-installed on the OpenMV device 
import image, network, math, rpc, sensor, struct, tf

# Initialise the camera sensor
sensor.reset()
# Set pixel format (GRAYSCALE/RGB565/BAYER/JPEG)
sensor.set_pixformat(sensor.RGB565)
# Set frame size (QVGA/VGA/SVGA)
sensor.set_framesize(sensor.QVGA)
# Skip frames for t milliseconds to enable camera to stabilize
sensor.skip_frames(time = 2000)

# Setup the OpenMV Cam for control over a USB VCP
interface = rpc.rpc_usb_vcp_slave()

################################################################
# Call Backs
################################################################

# Helper methods used by the call backs below.
def draw_detections(img, dects):
    for d in dects:
        c = d.corners()
        l = len(c)
        for i in range(l): img.draw_line(c[(i+0)%l] + c[(i+1)%l], color = (0, 255, 0))
        img.draw_rectangle(d.rect(), color = (255, 0, 0))

# Remote control works via call back methods that the controller
# device calls via the rpc module on this device. Call backs
# are functions which take a bytes() object as their argument
# and return a bytes() object as their result. The rpc module
# takes care of moving the bytes() objects across the link.
# bytes() may be the micropython int max in size.

# When called returns x, y, w, and h of the largest face within view.
#
# data is unused
def face_detection(data):
    sensor.set_pixformat(sensor.GRAYSCALE)
    sensor.set_framesize(sensor.QVGA)
    faces = sensor.snapshot().gamma_corr(contrast=1.5).find_features(image.HaarCascade("frontalface"))
    if not faces: return bytes() # No detections.
    for f in faces: sensor.get_fb().draw_rectangle(f, color = (255, 255, 255))
    out_face = max(faces, key = lambda f: f[2] * f[3])
    return struct.pack("<HHHH", out_face[0], out_face[1], out_face[2], out_face[3])

# When called returns if there's a "person" or "no_person" within view.
#
# data is unused
def person_detection(data):
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    scores = tf.classify("person_detection", sensor.snapshot())[0].output()
    return ['unsure', 'person', 'no_person'][scores.index(max(scores))].encode()

# Register call backs.
interface.register_callback(face_detection)
interface.register_callback(person_detection)

# Start processing remote events. Interface.loop() does not return.
interface.loop()
