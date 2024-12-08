# PrintAnywhere
Repository for files used for a UVM CS2210 Final Project by Callie Levitt and Darby Lane, PrintAnywhere!

This project was based on the desire to optimize the 3D printing process, enabling remote control and monitoring of the process. It was implemented on two Raspberry Pis, integrating several hardware components into a fully functional website.

Hardware:
- 2 Raspberry Pi 3Bs with SD cards
- DC Motor (5V (we think))
- Motor Hat Driver
- External Battery Pack
- PiCam (several for backup, they're very finicky!)
- Prusa Mini 3D Printer
- Several custom-designed and printed parts for the conveyor belt and camera
- Various power and ethernet cables

Software:
- OctoPrint, flashed onto one Pi's SD card
- Website

There were several main components to this project, which combined produce a cohesive process to monitor and control 3D printing on the Prusa Mini printer easily:
1. Website: We designed a website which controls all of the hardware components. It was designed with HTML and CSS, and served with Flask. The Flask server was then designed to start when its respective Pi booted up, so as long as that Pi has power, the website will be available. It can be accessed remotely through its assigned IP from the private UVM network, so anyone with access to this network may navigate to the website and control all of the hardware components remotely.
2. OctoPrint: OctoPrint is an open-source operating system which we installed onto the other Raspberry Pi. Once connected to a printer, the user can remotely navigate to the OctoPrint interface through the assigned IP from the private UVM network. This interface enables remote starting and stopping of the connected printer, as well as some cool features like a GCODE Viewer and a terminal to receive the log messages from the Pi.
3. Conveyor Belt: We built a functional model for 
