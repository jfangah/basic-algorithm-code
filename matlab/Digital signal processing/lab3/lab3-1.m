clc;clear all;
wp=0.2*pi;ws=0.3*pi;ap=1;as=10,Fs=1;%�˲�������
Wp=2*Fs*tan(wp/2);Ws=2*Fs*tan(ws/2);%Ԥ����
[n,Wn]=buttord(Wp,Ws,ap,as,'s');    %���������3db��ֹƵ��
[b,a]=butter(n,Wn,'s');             %����ģ���˲������ӷ�ĸϵ��
[bz,az]=bilinear(b,a,Fs);           %���������˲������ӷ�ĸϵ��

[H,W]=freqz(bz,az,64);              %�����Ƶ��Ӧ
stem(W/pi,(abs(H)));                %���
xlabel('\omega/\pi');ylabel('db');


