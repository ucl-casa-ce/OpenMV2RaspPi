# OpenMV2RaspPi
A project using the OpenMV cam with Raspberry Pi for face detection

## Project Summary
TBC

## Project Components
- OpenMV Cam H7 (R2 or Plus) (USB)
- OpenMV Ultra Wide lens
- Raspberry Pi 4 Model B (2GB)
- Raspberry Pi Power Cable
- Micro SD Card (minimum 8GB)
- USB A to micro B Cable
- High Speed 4K UHD HDMI Lead, Male to Micro D Male

You will need a separate computer or laptop to configure the components and load required software. You may also need an SD card reader and/or Micro SD adapter so that you can write the Raspberry Pi OS to the Micro SD using your computer or laptop (Windows or Mac).

## Software Dependencies
- OpenMV IDE 2.6.9
- OpenMV Firmware 4.0.2
- OpenMV RPC Python Module (compatible with Python 2 and 3)

# Installation

## Generate Public and Private SSH Keys for the Raspberry Pi
1. Download the PUTTY SSH client (includes PUTTYgen): https://www.putty.org/
2. Open the PUTTYgen application.
3. Click the 'Generate' button to create private and public keys for your Raspberry Pi device.
4. Move your mouse in the box provided by the application to generate random data.
5. Set a name for the SSH key e.g. 'OpenMV2RaspPi' so you remember what key is required when connecting to the device in future.
6. Enter a 'Key passphrase' for added security.
7. Save the public and private keys on your computer. Remember the location as you will need these later to connect to Raspberry Pi device using PUTTY.
8. Finally, you can 'Copy' the long public key so that it can be pasted into the Raspberry Pi Imager application to setup your device.
9. You are now ready to setup the Raspberry Pi.

## Install Raspberry Pi OS Image and Setup for Headless Operation
1. Download, install and run Raspberry Pi Imager (Windows or Mac): https://www.raspberrypi.org/software/
2. Click 'Choose OS' button.
3. Select 'Raspberry Pi OS (other)'.
4. Select 'Raspberry Pi OS Lite (32-bit)'.
5. Insert the Micro SD card into your computer.
6. Click 'Choose SD Card'.
IMPORTANT: Ensure that you select the correct SD card as this process will overwrite the data on the drive you select.
8. Open the hidden 'Advanced options' section by pressing CTRL+SHIFT+X on the keyboard.
9. Check 'Set hostname' option and provide name e.g. `raspberrypi`. This will be the device's wireless network name or SSID.
10. Check 'Enable SSH' to allow remote access to the device.
11. Select 'Allow public-key authentication only'.
NOTE: You can select 'Use password authentication' and provide a password instead. However, this is not recommended for devices connected directly to the internet or on public networks as they will be vulnerable to brute force password hacking attacks.
12. Paste the public key generated with PUTTYgen into the field 'Set authorized_keys...'.
IMPORTANT: Ensure you remove and overwrite the default value. If you don't place the public key into this field correctly you will not be able to log in to the Raspberry Pi using the corresponding private key.
13. If the device is to connect to the internet via wifi, check 'Configure wifi' and provide the SSID and password for the network the device is intended to connect to. Also set the wifi country from the dropdown e.g. 'GB'.
14. Check 'Set locale settings' and select timezone (e.g. Europe/London) and keyboard layout (e.g. 'gb').
15. Check 'Skip first-run wizard'.
IMPORTANT: The first-run wizard requires monitor, keyboard an mouse so must be disabled successfully start the Raspberry Pi in headless mode.
16. Uncheck each of the 'Persistent settings' options.
17. Click 'Save'.
18. Click 'Write'.
19. Disconect the Micro SD card.
20. Place the Micro SD card in the Raspberry Pi and switch on the device.
21. Wait 5 minutes for the device to start up and connect to the network.
22. You can now connect to the Raspberry Pi and login.

## Connecting to the Raspberry Pi using your Private Key with PUTTY
1. Open PUTTY on your computer.
2. Set the 'Connection type' to 'SSH'.
3. Set the 'Port' value to '22'. 
4. Enter the hostname for your Raspberry Pi device. If your computer is on the same local network as the device you can use the device name or SSID chosen in Raspberry Pi Imager. Otherwise you should use the numberic IP address.
5. Select 'Connection' > 'SSH' > 'Auth' in the Category list on the left of the PUTTYgen UI.
6. Click 'Browse', navigate to the location where you stored the private key from PUTTYgen, and select the private key (.ppk file) for authentication.
7. Click the 'Open' button to start the connection.
8. If the PUTTY Security Alert popup appears click 'Accept'.
9. Enter 'pi' as the login.
10. Enter the passphrase you chose when generating the private key in PUTTYgen.
11. You are now remotely logged into the Raspberry Pi.

## OpenMV Download and Setup
1. Download OpenMV IDE: https://openmv.io/pages/download
2. Install the OpenMV IDE on you system (Windows/Mac/Linux): https://docs.openmv.io/openmvcam/tutorial/software_setup.html#
3. Setup the OpenMV hardware: https://docs.openmv.io/openmvcam/tutorial/hardware_setup.html
4. Connect the IDE to the camera: https://docs.openmv.io/openmvcam/tutorial/openmvide_overview.html#connecting-to-your-openmv-cam
5. Tranfer script `main.py` to the OpenMV device.

## ------------ In Progress ------------
- Copy `RPC.py` to Raspberry Pi device from the following location on GitHub: https://github.com/openmv/openmv/blob/master/tools/rpc/rpc.py 
