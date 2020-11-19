# vega-rpi
Robot car operating on RPi

Required libraries: 

<ul>Adafruit_CircuitPython_PCA9685

<li>RPi: RPi 3 model B+ with Raspian headless</li>

Setup: SPI turned on, using PCA9685 with 4.8v; refer to blog (https://rbrobots.com/f/phase-5---adding-a-2dof-camera-mount-and-camera-in-progress)
</ul>

Required files to execute based on video demo example: https://www.youtube.com/watch?v=gVWx7c1Q3Kc&ab_channel=RBrobots

vegaMain.py - Main executeable file

vegaMotor.py - Includes Motor class with wheel motor and servo motor control

pca9685_servo.py - Adapted demo file from Adafruit's library with adapted range motion for servo's in use

To run
======

sudo python3 ./vegaMain.py


