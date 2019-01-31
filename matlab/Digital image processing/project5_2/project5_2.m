I=imread('Fig5.7(a).tif'); %读入5.7(a)图像
[height1,width1] = size(I);
J=imread('Fig5.10(a).tif');%读入5.10(a)图像
[height2,width2] = size(J);
K=imnoise(I,'salt & pepper',0.4);%给5.7(a)图像中加入Pa=0.2，Pb=0.2的椒盐噪声

subplot(2,2,1),imshow(K),title('5.7(a)加入噪声图像');%显示5.7(a)加入噪声图像
subplot(2,2,3),imshow(J),title('5.10（a）图像');%显示5.10(a)图像

A=ones(height1+2,width1+2)*255;%创建一个比K长宽都大2的全为255的矩阵
A(2:height1+1,2:width1+1)=K;%将K加入这个矩阵中心
for i=2:height1
    for j=2:width1-1
        x=[A(i-1,j-1) A(i-1,j) A(i-1,j+1) A(i,j-1) A(i,j) A(i,j+1) A(i+1,j-1) A(i+1,j) A(i+1,j+1)];
        K(i,j)=median(x);
    end
end %对K进行中值滤波
subplot(2,2,2),imshow(K),title('5.7(a)噪声中值滤波图像');%显示5.7(a)噪声中值滤波图像

B=ones(height2+2,width2+2)*255;%创建一个比J长宽都大2的全为255的矩阵
B(2:height2+1,2:width2+1)=J;%将J加入这个矩阵中心
for i=2:height2
    for j=2:width2-1
        x=[B(i-1,j-1) B(i-1,j) B(i-1,j+1) B(i,j-1) B(i,j) B(i,j+1) B(i+1,j-1) B(i+1,j) B(i+1,j+1)];
        J(i,j)=median(x);
    end
end %对K进行中值滤波
subplot(2,2,4),imshow(J),title('5.10(b)噪声中值滤波图像');%显示5.10(b)噪声中值滤波图像