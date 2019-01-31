clc;clear all;
wp=0.2*pi;ws=0.3*pi;ap=1;as=10,Fs=1;%滤波器参数
Wp=2*Fs*tan(wp/2);Ws=2*Fs*tan(ws/2);%预畸变
[n,Wn]=buttord(Wp,Ws,ap,as,'s');    %计算阶数和3db截止频率
[b,a]=butter(n,Wn,'s');             %计算模拟滤波器分子分母系数
[bz,az]=bilinear(b,a,Fs);           %计算数字滤波器分子分母系数

[H,W]=freqz(bz,az,64);              %计算幅频响应
stem(W/pi,(abs(H)));                %输出
xlabel('\omega/\pi');ylabel('db');


