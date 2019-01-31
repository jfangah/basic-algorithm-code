I=imread('project4_2.tif'); %读入图像
F=fft2(im2double(I)); %FFT
F=fftshift(F); %FFT频谱平移
F=real(F);
T=log(F); %频谱对数变换
subplot(1,2,1),imshow(I),title('原始图像');
subplot(1,2,2),imshow(T,[]),title('原始图像其频谱图');

average=sum(sum(double(I)))/(size(I,1)*size(I,2));%计算图像平均灰度值