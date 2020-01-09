function interVec()

output = [];
cnt = 0;

for i = 1: 33
    
    % lab path
%     address = ['D:\Howard_Feng\NAO_Music_Autism_Project\EDA_Process\C_Morlet_SVM\intervention\', num2str(i), '.mat'];
    address = ['D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\intervention\', num2str(i), '.mat'];
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

% lab path
% save('D:\Howard_Feng\NAO_Music_Autism_Project\EDA_Process\C_Morlet_SVM\intervention\vec_inter', 'output');
% alienware path
save('D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\vec_inter', 'output');


