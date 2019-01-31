x=[3,1,4,0,1,0,2,3,2,8,0,0,0,0,0,0];
X=fft4_16(x);
X1=fft(x);

n=1:1:16;
subplot(3,1,1);
stem(n,x,'filled');
title('input sequence');
axis([0,17,0,10]);

subplot(3,1,2);
stem(n,X,'filled');
title('output sequnence');
axis([0,17,-20,40]);

subplot(3,1,3);
stem(n,X1,'filled');
title('output fft sequence');
axis([0,17,-20,40]);