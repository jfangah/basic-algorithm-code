clc
clear

A=imread('Fig0914.tif');%����ԭʼͼ��
subplot(1,3,1);imshow(A);%��ʾԭʼͼ��
title('ԭʼͼ��');

SE=ones(3,3);%����һ��3*3�ĽṹԪ
B=imerode(A,SE);%����ͼ����ʴ
subplot(1,3,2);imshow(B);%��ʾ��ʴͼ��
title('��ʴͼ��');

C=A-B;%ԭʼͼ���ȥ��ʴͼ��Ϊ�߽�ͼ��
subplot(1,3,3);imshow(C);%��ʾ�߽�ͼ��
title('�߽�ͼ��');
