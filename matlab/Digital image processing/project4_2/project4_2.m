I=imread('project4_2.tif'); %����ͼ��
F=fft2(im2double(I)); %FFT
F=fftshift(F); %FFTƵ��ƽ��
F=real(F);
T=log(F); %Ƶ�׶����任
subplot(1,2,1),imshow(I),title('ԭʼͼ��');
subplot(1,2,2),imshow(T,[]),title('ԭʼͼ����Ƶ��ͼ');

average=sum(sum(double(I)))/(size(I,1)*size(I,2));%����ͼ��ƽ���Ҷ�ֵ