function [C] = conv_2D(A,B)     
//     Instead of this function , you can also use inbuilt function 'conv2', for more details on how to use type 'help conv2'
// This function performs convolution between an image A and a mask B.
// Input:      A - a grayscale image (values in [0,255])
//           B - a grayscale image (values in [0,255]) serves as a mask in the convolution.
//  Output:     C - a grayscale image (values in [0,255]) - the output of the convolution. 
//             C is the same size as A.
// Method:  Convolve A with mask B using zero padding. Assume the origin of B is at floor(size(B)/2)+1.
// convert the image A into double format
    A = double(A);
// init C to size A with zeros
    C = zeros(size(A));
// make b xy-reflection and vector
    vectB = matrix(flipdim(flipdim(B,1),2)' ,size(B,1)*size(B,2), 1);
// padding A with zeros
    tmp = [A ; A($, :) .*. zeros(floor(size(B,1)/2), 1)];
    tmp = [tmp  tmp(:, $) .*. zeros(1,floor(size(B,1)/2))];
    tmp = [tmp(1,:) .*. zeros(floor(size(B,1)/2), 1);tmp];
    paddedA = [tmp(:,1) .*. zeros(1,floor(size(B,1)/2)) tmp];
//  Loop over A matrix: 
for i = 1:size(A,1)
    for j = 1:size(A,2)
        startAi = i;
        finishAi = i + size(B,1) - 1;
        startAj = j;
        finishAj = j + size(B,2) - 1;
        vectPaddedA = matrix(paddedA(startAi :finishAi,startAj:finishAj)',1,size(B,1)*size(B,2));
        C(i,j) = vectPaddedA* vectB;
    end
end
endfunction;
