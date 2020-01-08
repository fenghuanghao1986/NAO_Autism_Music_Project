function warmUpVec()

output = [];
cnt = 0;

for i = 1: 41
    
    address = ['D:\Howard_Feng\NAO_Music_Autism_Project\EDA_Process\C_Morlet_SVM\warmup\', num2str(i), '.mat'];
    
    if exist(address, 'file')
        load(address);
        cnt = cnt + 1
    else
        continue;
    end
    
    temp = imresize(saveClip, [size(saveClip, 1), size(saveClip, 2)], 'bicubic');
    temp1 = reshape(temp', 1, size(temp, 1) * size(temp, 2));
    
    output = [output; temp1];
    size(output)
    
end

save('D:\Howard_Feng\NAO_Music_Autism_Project\EDA_Process\C_Morlet_SVM\warmup\vec_warm', 'output');



