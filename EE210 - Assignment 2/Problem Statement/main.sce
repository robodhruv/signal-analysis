exec('get_continuous_sinusoid.sci');


// You can use the function 'get_continuous_sinusoid' to obtain an array of values of the continuous time sinusoid
// The inputs to the function will be the signal amplitude 'a'(from 0 to1), fundamental frequency 'F0'(100 to 4000 Hz), phase 'phi'(in radians) and duration 'T'(in ms) 
// The outputs will be the values 'y' of the sinusoid & their time indices 't'
// You could call this function multiple times and add the different sinusoids. Finally you can plot, play the resulting signal.


// For example:

F0 = 270;       // Hz
a = 0.7;        
phi = %pi/4;    //(Radians)
T = 800;       //(ms)    

[y,t] = get_continuous_sinusoid(a,F0,phi,T);

F0 = 220;

[y1,t] = get_continuous_sinusoid(a,F0,phi,T);

// concatenate the 2 sinusoids in sequence
z = cat(2,y,y1)

 





// Plot the continuous time curve
clf();
plot(t,y,'b');
// Axis properties
a = gca();
a.x_location = "origin";
a.y_location = "origin";



// Play the sinusoid
sound(z,10000);
//sound(y1,10000);
//Save the sound to output.wav file
wavwrite(z,10000,"output.wav");
