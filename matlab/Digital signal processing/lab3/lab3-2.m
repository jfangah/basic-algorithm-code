clc;clear all;
fp=0.2;fs=0.3;Fs=1;ap=1;as=25;
wp=2*pi*fp;ws=2*pi*fs;              %�˲�������
Wp=2*Fs*tan(wp/2);Ws=2*Fs*tan(ws/2);%Ԥ����
[n,Wn]=buttord(Wp,Ws,ap,as,'s');    %���������3db��ֹƵ��
[b,a]=butter(n,Wn,'s');             %����ģ���˲������ӷ�ĸϵ��
[bz,az]=bilinear(b,a,Fs);           %���������˲������ӷ�ĸϵ��

[H,W]=freqz(bz,az,64);              %�����Ƶ��Ӧ
stem(W/pi,(abs(H)));                %���
xlabel('\omega/\pi');ylabel('db');
