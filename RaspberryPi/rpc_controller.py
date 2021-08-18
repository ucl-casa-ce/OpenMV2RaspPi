# RaspPi as Controller for OpenMV Cam (USB VCP)
# Script requires RPC library script to be installed in the same location on the Raspberry Pi.
import json, rpc, serial, serial.tools.list_ports, struct, sys
from datetime import datetime

# Fix for Python 2.x.
try: input = raw_input
except NameError: pass

# Initialise the interface by selecting the USB port connected to the OpenMV Cam
print("\nAvailable Ports:\n")
for port, desc, hwid in serial.tools.list_ports.comports():
    print("{} : {} [{}]".format(port, desc, hwid))
sys.stdout.write("\nPlease enter a port name: ")
sys.stdout.flush()
interface = rpc.rpc_usb_vcp_master(port=input())
print("")
sys.stdout.flush()

##############################################################
# Call Back Handlers
##############################################################

def exe_face_detection():
    result = interface.call("face_detection")
    if result is not None and len(result):
        print("Largest Face Detected [x=%d, y=%d, w=%d, h=%d]" % struct.unpack("<HHHH", result))

def exe_person_detection():
    result = interface.call("person_detection")
    if result is not None:
        print(result.tobytes())

def exe_face_counter():
    result = interface.call("face_counter")
    if result is not None:
        print(result.tobytes())

def exe_people_counter():
    result = interface.call("people_counter")
    if result is not None:
        print(result.tobytes())

# Execute remote functions in a loop.
while(True):
    #exe_face_detection() # Face should be about 2ft away.
    #exe_person_detection()
    exe_face_counter()
    #exe_people_counter()