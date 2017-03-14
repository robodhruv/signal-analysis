function [x,t] = get_continuous_sinusoid(a,F0,phi,interval)     
    a = max(a,1);
    Fc = 10000;
    t = 0:1/Fc:interval/1000;
    x = a*cos(2*%pi*F0*t + phi);
endfunction
