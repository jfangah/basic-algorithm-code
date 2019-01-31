clc;
clear all;
N=21;wc=0.5*pi;
r=(N-1)/2;
n=0:N-1;
hdn=sin(wc*(n-r))/pi./(n-r);
if rem(N,2)~=0;
    hdn(r+1)=wc/pi;
end
wn=hamming(N);
h=hdn.*wn';
H=fft(h,512);
w=2*[0:511]/512;
subplot(3,1,1);
stem(n,h);
title('h(n)');xlabel('n');ylabel('幅度');
subplot(3,1,2);
plot(w,abs(H));
title('H(exp(jw))');xlabel('w/pi');ylabel('幅度');
subplot(3,1,3);
plot(w,20*log10(abs(H)));
title('H(exp(jw))');
xlabel('w/pi');
ylabel('幅度（db）');

figure   
W=fft(wn,512); 
subplot(3,1,1); 
stem(n,wn); 
title('w(n)');
xlabel('n'); 
ylabel('幅度'); 
subplot(3,1,2); 
plot(w,abs(H)); 
title('W(exp(jw))');
xlabel('w/pi'); 
ylabel('幅度'); 
subplot(3,1,3);  
plot(w,20*log10(abs(W))); 
title('W(exp(jw))'); 
xlabel('w/pi'); 
ylabel('幅度（dB）'); 