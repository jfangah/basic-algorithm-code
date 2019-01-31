clc
clear

A=imread('Fig1038(a).tif');%读入原始图像
subplot(1,3,1);
imshow(A);%显示原始图像
title('原始图像');
subplot(1,3,2)  
imhist(A)%显示原始图像直方图  
title('原始图像直方图');

[height,width] = size(A);%测出原始图像的长宽
T=sum(sum(double(A)))/(height*width);%计算初始全局阈值

done=false;
while ~done
    Tnext=0.5*(mean(A(A>=T))+mean(A(A<T)));%T的迭代运算
    done=abs(T-Tnext)<0.01;
    T=Tnext;
end
      
B=im2bw(A,T/255);%使用得到的T值分割图像
subplot(1,3,3)  
imshow(B)%显示阈值处理结果图  
title('阈值处理图');
