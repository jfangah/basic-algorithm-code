             subplot(1,3,1);
              a1=0.8;B=[1,0,0];A=[1,-(a1+0.5),0.5*a1];
       [H,w]=freqz(B,A,200,'whole');
       magH=abs(H(1:101));
 
       w=w(1:101);
       plot(w/pi,magH);grid
       xlabel('a=0.8,frequency Unit:pi');ylabel('Magnitude');
       title('Magnitude Response');

 subplot(1,3,2);
              a2=0.9;B=[1,0,0];A=[1,-(a2+0.5),0.5*a2];
       [H,w]=freqz(B,A,200,'whole');
       magH=abs(H(1:101));
 
       w=w(1:101);
      plot(w/pi,magH);grid
       xlabel('a=0.9,frequency Unit:pi');ylabel('Magnitude');
       title('Magnitude Response');
 subplot(1,3,3);
             a3=1.1;B=[1,0,0];A=[1,-(a3+0.5),0.5*a3];
       [H,w]=freqz(B,A,200,'whole');
       magH=abs(H(1:101));
 
       w=w(1:101);
 
       plot(w/pi,magH);grid
       xlabel('a=1.1,frequency Unit:pi');ylabel('Magnitude');
       title('Magnitude Response');
