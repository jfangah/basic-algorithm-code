wc=0.5*pi;
N=21;
b=fir1(N-1,wc/pi,hamming(N));
subplot(2,1,1);
freqz(abs(b),1,512);
subplot(2,1,2);
freqz(20*log10(abs(b)),1,512);

