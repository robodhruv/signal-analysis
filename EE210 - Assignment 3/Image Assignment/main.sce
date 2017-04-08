exec('conv_2D.sci');


// You can use the function 'conv_2D.sci' to to do the convolution between two 2D-signals
// The inputs to the function are, the input image 'X' and the kernel 'H'.
// The output will be the resultant signal 'Y' after the convolution. 
// You can call this function multiple times depending on how many times you are performing the convolution.

// Below an example code is given to read an image and to find fft of the image. Also the magnitude of the fft (in logarithmic scale) is plotted   
// you can use this code for finding the 2D fft and ploting its spectrum

// get the input image
X = imread('sem_ic.jpg');
X = rgb2gray(X);

//display the image
imshow(X)

// convert to double format for performing calculations
X = double(X);

//finding fft of the image 
Fin = fft(X);
Fin = fftshift(Fin);

//plote of magnitude spectrum
Fin2 = log(abs(Fin));
set(gcf(),"color_map",graycolormap(128));
clf;
Fin2=flipdim(Fin2,1);
grayplot(-192:192,-142:143,Fin2')
// title and axes properties 
a=get("current_axes");
a.title.text="Magnitude Spectrum ";
a.axes_visible="on";
a.tight_limits="on";
a.x_location = "bottom";
a.y_location = "left";
a.x_label.text="v";
x_label.auto_position="on"
a.y_label.text="u";
// Now you can define the kernel H and call the convolution function here. An example is shown below
//define a kernel
H= [0 -0 0;0 1 0;0 0 0];
// Now call the fuction
Y = conv_2D(X,H);

// You can call this function as many times you needed

// Now you plot the output image, find its fft , and plot its magnitude spectrum here. Compare input and output in both the spatial domain and frequency domain
// While using the function 'imshow' to display the image check the data type of the image and do proper scaling to get a better display of the image. For more details enter 'help imshow' 






