clc
clear

A=imread('Fig1038(a).tif');%����ԭʼͼ��
subplot(1,3,1);
imshow(A);%��ʾԭʼͼ��
title('ԭʼͼ��');
subplot(1,3,2)  
imhist(A)%��ʾԭʼͼ��ֱ��ͼ  
title('ԭʼͼ��ֱ��ͼ');

[height,width] = size(A);%���ԭʼͼ��ĳ���
T=sum(sum(double(A)))/(height*width);%�����ʼȫ����ֵ

done=false;
while ~done
    Tnext=0.5*(mean(A(A>=T))+mean(A(A<T)));%T�ĵ�������
    done=abs(T-Tnext)<0.01;
    T=Tnext;
end
      
B=im2bw(A,T/255);%ʹ�õõ���Tֵ�ָ�ͼ��
subplot(1,3,3)  
imshow(B)%��ʾ��ֵ������ͼ  
title('��ֵ����ͼ');
