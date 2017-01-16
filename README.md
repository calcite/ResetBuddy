RESET BUDDY 
==============
This device provides 9 relay outputs with a current rating up to 5A each. It can be fully powered and controlled by standard USB bus. Green LED mounted right next to corresponding relay indicates its state.

connector: 	USB mini type B
		Pluggable screw terminal AWG 16 - 26 

Board designed with KiCad 4.0.2

Box designed with freecad, based on HAMMOND 1455L1202


Controlling MCP2210:

Installation of lib_usb which in needed for running MCP2210
$apt-get update
$apt-get upgrade
$apt-get install python3-dev
$apt-get install cython3
$apt-get install libusb-1.0.0 libusb-1.0.0-dev libudev-dev
$pip3 install hidapi

Testing can be made with microchip utility: http://ww1.microchip.com/downloads/en/DeviceDoc/MCP2210Utility_v1.2.2.zip
Full control can be reached with utility attached to this project (RB utility).



RB utility control:
run python script with paramethers. Syntax is:
python RB_utility.py <operation><pin><state>[time]	parameter time is not obligatory

supported operations: 	
- set = s		– sets or clears pin (puts the pin into state 0 or 1)
- get = g	– reads state of pin
- reset = r	– sets pin for time (in seconds), then clears it
- rev_reset = rev – opposite of reset
- clearall = c	- clears all pins
- test = t	- visual test
- crazy! 		- even better test

For some operations there is no need for all other parameters but you always have to put them in (poor programming skills). 

allowed pin inputs: 1,2,3,4,5,6,7,8,9,all,a,x	(a = all, x for operations without pin input)

allowed state iputs: 0,1,x			(x for operations without state input)

time parameter only for reset operation. You must put –t ahead of the parameter itself




examples:

python RB_utility.py set 1 1	//sets pin 1 into logic 1

python RB_utility.py r 9 x –t 1	//sets pin 9 for 1 second, then clears it 

python RB_utility.py crazy! x x 	//just try it ;) 

*
