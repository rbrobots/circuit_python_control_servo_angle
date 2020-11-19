# vega-rpi
A program to allow user input to control angle of 2 servo's using Raspbery Pi and Adafruit's PCA9685 

</strong>See my blog for a more in-depth explanation of how I got this working: </strong>

https://rbrobots.com/f/phase-5---adding-a-2dof-camera-mount-and-camera-in-progress

<strong>Video demo:</strong>

https://www.youtube.com/watch?v=gVWx7c1Q3Kc&t=1s&ab_channel=RBrobots

<strong>Required libraries/resources: </strong>

<ul>
<li>Adafruit_CircuitPython_PCA9685</li>
<li>RPi 3 model B+ with Raspian headless</li>
  <li>2 degree of freedom pan-tilt camera </li>
  <li>5v battery input to the RPi either through computer or batteries</li>
  <li>4.8v battery input to the PCA9685 (Get stable voltage supply 5V maximum and be careful when wiring this to the driver - it is easy to short circuit)</li>
</ul>

<strong>Setup: </strong>

<ul>
  <li>Install Raspbian on RPi</li>
  <li>Enable SPI</li>
  <li>Download Adafruit Circuit Python Library</li>
  <li>See blog for full explanation. Link above</li>
</ul>

<strong>Required files to execute based on video demo example:</strong>
<ul>
<li>vegaMain.py - Main executeable file</li>

<li>vegaMotor.py - Includes Motor class with wheel motor and servo motor control</li>

<li>pca9685_servo.py - Simulates full motion of two servos. Adapted demo file from Adafruit's library with adapted range motion for servo's in use</li>

<li>The other two files are <strong>NOT</strong> required for this project. But have been left here for my later use.</li>

</ul>

<strong>To execute code:</strong>

<ul>
  <li>sudo python3 ./pca9685_servo.py</li>
  <li>sudo python3 ./vegaMain.py</li>
</ul>


