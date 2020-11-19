# vega-rpi
A program to allow user input to control angle of 2 servo's using Raspbery Pi and Adafruit's PCA9685 

See my blog for a more in-depth explanation of how I got this working: https://rbrobots.com/f/phase-5---adding-a-2dof-camera-mount-and-camera-in-progress

Required libraries/resources: 

<ul>
<li>Adafruit_CircuitPython_PCA9685</li>
<li>RPi 3 model B+ with Raspian headless</li>
  <li>2 degree of freedom pan-tilt camera </li>
  <li>5v battery input to the RPi either through computer or batteries</li>
  <li>4.8v battery input to the PCA9685 (Get stable voltage supply 5V maximum and be careful when wiring this to the driver - it is easy to short circuit)</li>
</ul>

Setup: SPI turned on, using PCA9685 with 4.8v; refer to blog (https://rbrobots.com/f/phase-5---adding-a-2dof-camera-mount-and-camera-in-progress)


Required files to execute based on video demo example: https://www.youtube.com/watch?v=gVWx7c1Q3Kc&ab_channel=RBrobots
<ul>
  <li>vegaMain.py - Main executeable file</li>

<li>vegaMotor.py - Includes Motor class with wheel motor and servo motor control</li>

<li>pca9685_servo.py - Adapted demo file from Adafruit's library with adapted range motion for servo's in use</li>

</ul>
To run
======

sudo python3 ./vegaMain.py


