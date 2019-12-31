function music_autism_vectorization()

output = [];
cnt = 0;

for i = 1: 62
    
    addPath = ['D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\EDA\', num2str(i), '.mat'];
    
    if exist(addPath, 'file')
        load(addPath);
        cnt = cnt + 1
    else
        continue;
    end
    % this is not right saveClip is not there, don't know what exactly it
    % is need to figure that out
    temp = saveCilp;
    
    temp = imresize(temp, [size(temp, 1), size(temp, 2)], 'bicubic');
    temp = reshape(temp', 1, size(temp, 1) * size(temp, 2));
    
    output = [output; temp];
    size(output)
    
end

save('D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\EDA\vec_', 'output');



