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

Note: You may also need an SD card reader and/or Micro SD adapter so that you can write the Raspberry Pi OS to the Micro SD using your computer or laptop (Windows or Mac).

## Software Dependencies
- OpenMV IDE 2.6.9
- OpenMV Firmware 4.0.2

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
NOTE: You can select 'Use password authentication' and provide a password. However, this is not recommended for devices connected directly to the internet or on public networks as they will be vulnerable to brute force password hacking attacks.
12. If the device is to connect to the internet via wifi, check 'Configure wifi' and provide the SSID and password for the network the device is intended to connect to. Also set the wifi country from the dropdown e.g. 'GB'.
13. Check 'Set locale settings' and select timezone (e.g. Europe/London) and keyboard layout (e.g. 'gb').
14. Check 'Skip first-run wizard'.
IMPORTANT: The first-run wizard requires monitor, keyboard an mouse so must be disabled successfully start the Raspberry Pi in headless mode.
16. Uncheck each of the 'Persistent settings' options.
17. Click 'Save'.
18. Click 'Write'.
19. Disconect the Micro SD card.
20. Place the Micro SD card in the Raspberry Pi and switch on the device.
21. Wait 5 minutes for the device to start and connect to the network.

## Login to the Raspberry Pi using Putty
1. Login to the device using the Putty SSH client: https://www.putty.org/

## OpenMV Download and Setup
1. Download OpenMV IDE: https://openmv.io/pages/download
2. Install the OpenMV IDE on you system (Windows/Mac/Linux): https://docs.openmv.io/openmvcam/tutorial/software_setup.html#
3. Setup the OpenMV hardware: https://docs.openmv.io/openmvcam/tutorial/hardware_setup.html
4. Connect the IDE to the camera: https://docs.openmv.io/openmvcam/tutorial/openmvide_overview.html#connecting-to-your-openmv-cam
5. Add Python script to the IDE.
