wc=0.5*pi;
N=21;
r=(N-1)/2;
n=0:N-1;
hdn=sin(wc*(n-r))/pi./(n-r);
if rem(N,2)~=0
    hdn(r+1)=wc/pi;
end
wn=hamming(N);
h=hdn.*wn';
H=fft(h,512);
w=2*[0:511]/512;
subplot(2,1,1);
plot(w,abs(H));
subplot(2,1,2);
plot(w,20*log10(abs(H)));