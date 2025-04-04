# CubeScan-Motion-Controller

CubeScan-Motion-Controller – A Python-based automation system using a 3D printer that enables programmable cuboid scanning and tag rotation via G-code control through PySerial communication. Developed to solve precision motion control for the RFID tag charachterization, this project integrates Marlin firmware with a custom Arduino subsystem (which controls a stepper motor for 180° tag rotations). The system serializes multi-axis movements (XYZ with adjustable step intervals) while ensuring hardware safety through endstop calibration.
