I=imread('Fig5.7(a).tif'); %����5.7(a)ͼ��
[height1,width1] = size(I);
J=imread('Fig5.10(a).tif');%����5.10(a)ͼ��
[height2,width2] = size(J);
K=imnoise(I,'salt & pepper',0.4);%��5.7(a)ͼ���м���Pa=0.2��Pb=0.2�Ľ�������

subplot(2,2,1),imshow(K),title('5.7(a)��������ͼ��');%��ʾ5.7(a)��������ͼ��
subplot(2,2,3),imshow(J),title('5.10��a��ͼ��');%��ʾ5.10(a)ͼ��

A=ones(height1+2,width1+2)*255;%����һ����K������2��ȫΪ255�ľ���
A(2:height1+1,2:width1+1)=K;%��K���������������
for i=2:height1
    for j=2:width1-1
        x=[A(i-1,j-1) A(i-1,j) A(i-1,j+1) A(i,j-1) A(i,j) A(i,j+1) A(i+1,j-1) A(i+1,j) A(i+1,j+1)];
        K(i,j)=median(x);
    end
end %��K������ֵ�˲�
subplot(2,2,2),imshow(K),title('5.7(a)������ֵ�˲�ͼ��');%��ʾ5.7(a)������ֵ�˲�ͼ��

B=ones(height2+2,width2+2)*255;%����һ����J������2��ȫΪ255�ľ���
B(2:height2+1,2:width2+1)=J;%��J���������������
for i=2:height2
    for j=2:width2-1
        x=[B(i-1,j-1) B(i-1,j) B(i-1,j+1) B(i,j-1) B(i,j) B(i,j+1) B(i+1,j-1) B(i+1,j) B(i+1,j+1)];
        J(i,j)=median(x);
    end
end %��K������ֵ�˲�
subplot(2,2,4),imshow(J),title('5.10(b)������ֵ�˲�ͼ��');%��ʾ5.10(b)������ֵ�˲�ͼ��