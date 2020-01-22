function dataVec()

output = [];
cnt = 0;

folder = 'D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\segData\game_seg\';
filePattern = fullfile(folder, '*.mat');
segFiles = dir(filePattern);

for i = 1: 1350
    
    baseName = segFiles(i).name;
    fullName = fullfile(folder, baseName);
    fprintf(1, 'Reading %s\n', fullName);
    matData = load(fullName);
    
    
    % lab path
%     address = ['D:\Howard_Feng\NAO_Music_Autism_Project\EDA_Process\C_Morlet_SVM\warmup_14_33\', num2str(i), '.mat'];
    % alienware path
%     address = ['D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\ASD0\', num2str(i), '.mat'];
    % surface path
%     address = ['C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\EDA_Process\C_Morlet_SVM\warmup\', num2str(i), '.mat'];
% 
%     if exist(folder, 'file')
%         load(folder);
%         cnt = cnt + 1
%     else
%         continue;
%     end
    
    temp = imresize(matData.saveClip, [size(matData.saveClip, 1), size(matData.saveClip, 2)], 'bicubic');
    temp1 = reshape(temp', 1, size(temp, 1) * size(temp, 2));
    
    output = [output; temp1];
    size(output)
    
end

% lab path
% save('D:\Howard_Feng\NAO_Music_Autism_Project\EDA_Process\C_Morlet_SVM\vec_warm1', 'output');
% alienware path
save('D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\vec_warm_seg', 'output');
% Surface path
% save('C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\EDA_Process\C_Morlet_SVM\vec_warm', 'output');

output = [];
cnt = 0;

folder = 'D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\segData\inter_seg\';
filePattern = fullfile(folder, '*.mat');
segFiles = dir(filePattern);

for i = 1: 1350
    
    baseName = segFiles(i).name;
    fullName = fullfile(folder, baseName);
    fprintf(1, 'Reading %s\n', fullName);
    matData = load(fullName);
    
    
    % lab path
%     address = ['D:\Howard_Feng\NAO_Music_Autism_Project\EDA_Process\C_Morlet_SVM\warmup_14_33\', num2str(i), '.mat'];
    % alienware path
%     address = ['D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\ASD0\', num2str(i), '.mat'];
    % surface path
%     address = ['C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\EDA_Process\C_Morlet_SVM\warmup\', num2str(i), '.mat'];
% 
%     if exist(folder, 'file')
%         load(folder);
%         cnt = cnt + 1
%     else
%         continue;
%     end
    
    temp = imresize(matData.saveClip, [size(matData.saveClip, 1), size(matData.saveClip, 2)], 'bicubic');
    temp1 = reshape(temp', 1, size(temp, 1) * size(temp, 2));
    
    output = [output; temp1];
    size(output)
    
end

% lab path
% save('D:\Howard_Feng\NAO_Music_Autism_Project\EDA_Process\C_Morlet_SVM\vec_warm1', 'output');
% alienware path
save('D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\vec_inter_seg', 'output');
% Surface path
% save('C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\EDA_Process\C_Morlet_SVM\vec_warm', 'output');

output = [];
cnt = 0;

folder = 'D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\segData\game_seg\';
filePattern = fullfile(folder, '*.mat');
segFiles = dir(filePattern);

for i = 1: 1350
    
    baseName = segFiles(i).name;
    fullName = fullfile(folder, baseName);
    fprintf(1, 'Reading %s\n', fullName);
    matData = load(fullName);
    
    
    % lab path
%     address = ['D:\Howard_Feng\NAO_Music_Autism_Project\EDA_Process\C_Morlet_SVM\warmup_14_33\', num2str(i), '.mat'];
    % alienware path
%     address = ['D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\ASD0\', num2str(i), '.mat'];
    % surface path
%     address = ['C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\EDA_Process\C_Morlet_SVM\warmup\', num2str(i), '.mat'];
% 
%     if exist(folder, 'file')
%         load(folder);
%         cnt = cnt + 1
%     else
%         continue;
%     end
    
    temp = imresize(matData.saveClip, [size(matData.saveClip, 1), size(matData.saveClip, 2)], 'bicubic');
    temp1 = reshape(temp', 1, size(temp, 1) * size(temp, 2));
    
    output = [output; temp1];
    size(output)
    
end

% lab path
% save('D:\Howard_Feng\NAO_Music_Autism_Project\EDA_Process\C_Morlet_SVM\vec_warm1', 'output');
% alienware path
save('D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\vec_game_seg', 'output');
% Surface path
% save('C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\EDA_Process\C_Morlet_SVM\vec_warm', 'output');

