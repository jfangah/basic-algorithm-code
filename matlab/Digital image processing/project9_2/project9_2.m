clc
clear

A=imread('Fig0914.tif');%读入原始图像
subplot(1,3,1);imshow(A);%显示原始图像
title('原始图像');

SE=ones(3,3);%创建一个3*3的结构元
B=imerode(A,SE);%进行图像侵蚀
subplot(1,3,2);imshow(B);%显示侵蚀图像
title('侵蚀图像');

C=A-B;%原始图像减去侵蚀图像为边界图像
subplot(1,3,3);imshow(C);%显示边界图像
title('边界图像');
