There are two Scilab codes included: The function 'get_continuous_sinusoid.sci' and the 'main.sce' script


1) get_continuous_sinusoid.sci
This is a function file which does not need to be modified. You can use it as a black box to synthesize a single sinusoid.
The inputs to the function will be the signal amplitude 'a'(from 0 to 1), fundamental frequency 'F0'(100 to 4000 Hz), phase 'phi'(in radians)
and duration 'T'(in ms) 
The outputs will be the values 'y' of the sinusoid & their time indices 't'
You could call this function multiple times and add the different sinusoids. Finally you can plot, play the resulting signal.
		

2) main.sce: 
You need to run only the 'main.sce' code and modify it as needed. It has comments to help you out.
The main code contains an example of using the 'get_continuous_sinusoid' function. It also contains code
for plotting, playing and saving the resulting signal.  
 