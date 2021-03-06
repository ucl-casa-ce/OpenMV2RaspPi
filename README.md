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
- OpenMV RPC Python Module (Compatible with Python 2 and 3. For convenience this script is included within this project under MIT licence)

A number of other Python modules are required for the project. 
- Pyserial
- Pygame

These modules are installed using the provided script `setup.sh`. Further instructions below.

# Installation

The following guide assumes the use of a Windows PC for downloading and configuring the OpenMV camera and Raspberry Pi. This process will differ if you are using an Apple Mac or Linux computer.  

## Generate Public and Private SSH Keys on your computer for communicating with the Raspberry Pi
1. Download the PUTTY SSH client (Windows): https://www.putty.org/
2. Open the associated PUTTYgen application.
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

NOTE: Choosing a unique SSID for the device can be useful for allowing you to access the it from another machine on the same local network. This can help you connect to the device via SSH before you have established what IP address it has been assigned on that network. 

10. Check 'Enable SSH' to allow remote access to the device.
11. Select 'Allow public-key authentication only'.

NOTE: You can select 'Use password authentication' and provide a password instead. However, this is not recommended for devices connected directly to the internet or on public networks as they will be vulnerable to brute force password hacking attacks.

12. Paste the public key generated with PUTTYgen into the field 'Set authorized_keys...'.

IMPORTANT: Ensure you remove and overwrite the default value. If you don't place the public key into this field correctly you will not be able to log in to the Raspberry Pi using the corresponding private key.

13. If the device is to connect to the internet via wifi, check 'Configure wifi' and provide the SSID and password for the network the device is intended to connect to. Also set the wifi country from the dropdown e.g. 'GB'.
14. Check 'Set locale settings' and select timezone (e.g. Europe/London) and keyboard layout (e.g. 'gb').
15. Check 'Skip first-run wizard'.

IMPORTANT: The first-run wizard requires monitor, keyboard an mouse so must be disabled to successfully start the Raspberry Pi in headless mode.

16. Uncheck each of the 'Persistent settings' options.
17. Click 'Save'.
18. Click 'Write'.
19. Disconect the Micro SD card.
20. Place the Micro SD card in the Raspberry Pi and switch on the device.
21. Wait 5 minutes for the device to start up and connect to the network.
22. You can now connect to the Raspberry Pi and login.

## Connecting to the Raspberry Pi over SSH using your Private Key with PUTTY

You can connect to the Raspberry Pi with SSH via WiFi or an physical Ethernet connection. If you are on the same network you can access the device using the SSID you gave it when setting up the device. If you intend to access the device remotely via the internet you will need to assign the device a static private IP address and fixed public address. That goes beyond the scope of this guide. 

1. Open PUTTY on your computer (Windows).
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
12. You can check the device's private IP address by typing `ipconfig`. The 'inet' numbers listed against 'wlan0' and/or 'eth0' interfaces are the IP addresses for the first available wifi and ethernet connections for the device.

## Install Python Dependencies on Raspberry Pi
1. Login to the Raspberry Pi over SSH.
2. Install pip package manager: `sudo apt-get install python-pip`.
3. Install Pyserial: `pip install pyserial`.
4. Install Pygame: `pip install pygame`.

## Transferring project files to the Raspberry Pi with WinSCP
1. Download WinSCP (Windows): https://winscp.net/
2. Open the application
3. Set the 'File Protocol' to 'SFTP'. 
4. Enter the hostname for your Raspberry Pi device (SSID or IP address).
5. Set 'Port Number' as '22'.
6. Click 'Advanced' button.
7. Select 'SSH' > 'Autentication'.
8. Click on the breadcrumbs '...' next to the text box 'Private key file' and navigate to the location where you stored the private key from PUTTYgen. Select the private key (.ppk file) for authentication.
9. Click 'Ok'.
10. Click 'Login'.
11. Enter username 'pi' followed by the passphrase associated with the private key (same as with SSH login via PUTTY above).
12. You now have remote access to the file system on the Raspberry Pi. Files can be dragged and dropped onto the device.
13. Copy the files from this repos RaspberryPi folder onto the device.

## OpenMV Download and Setup
1. Download OpenMV IDE (Windows/Mac/Linux): https://openmv.io/pages/download
2. Install the OpenMV IDE on you system: https://docs.openmv.io/openmvcam/tutorial/software_setup.html#
3. Setup the OpenMV hardware: https://docs.openmv.io/openmvcam/tutorial/hardware_setup.html
4. Connect the IDE to the camera: https://docs.openmv.io/openmvcam/tutorial/openmvide_overview.html#connecting-to-your-openmv-cam
5. Open the script `rpc_remote.py` in the OpenMV IDE.
6. Copy the script to the camera device as `main.py` by clicking the following: 'Tools' > 'Save open script to OpenMV Cam (as main.py)'. Alternatively you can manually rename the file and copy it onto the device flash drive.

# Development and Testing

## Observations
1. As you cannot use USB VCP while the OpenMV IDE device is connected, debugging issues on the remote device can be difficult.
2. Iteration can be hindered by the device going into 'panic' mode when reconnecting the IDE to deploy code updates. Doing so requires the developer to go through the device unbricking process (see Troubleshooting below).

## Troubleshooting

#### The OpenMV camera is showing a flashing white light or 'panicking'
1. Start the OpenMVIDE. 
2. Press connect when the camera is not attached.
3. Follow the onscreen prompts. When the popup says 'Do you have an OpenMV Cam connected and is it bricked?' click 'Yes'. Ensure to select the correct camera model when prompted. If you have your data backed up you can erase the devices file system.
4. Connect or disconnect and reconnect the device when prompted.
5. The OpenMV IDE will now clear the camera's flash memory and load the lastest firmware version available.
6. The device is now ready for use.
 