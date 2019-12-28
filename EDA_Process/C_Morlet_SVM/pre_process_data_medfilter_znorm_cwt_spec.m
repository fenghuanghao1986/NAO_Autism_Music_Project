clc;
clear;
warning off

% Pre-process data location 
dataPath = ...
    'D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\EDA';
fileType = ...
    '*.csv';
% create a data structure called dd by using dir()
dd = dir(fullfile(dataPath, fileType));
% get all names from dd.name
fileNames = {dd.name};
% get all file numbers for later loop times in order to go through all
% files by go through all names
num = numel(fileNames);

% create an empty num by 2 size cell
data = cell(num, 2);
% first col save all names
data(:,1) = regexprep(fileNames, '.csv', '');
% create an empty num by 1 size cell for save all normalized and filtered
% data
znormFilter = cell(num, 1);
% create a scale range for resizing and create spectrum mrtx
scaleRange = 1:100;

% start the loop for saving all mat files and ready for vetorization
for fileNum = 1: num
    
    data{fileNum, 2} = dlmread(fullfile(dataPath, fileNames{fileNum}));
    fprintf('Reading CSV data number %d ...\n', fileNum);
    dataQ = data{fileNum, 2}(:, 6);
    
    [znormQ, muQ, sigmaQ] = zscore(dataQ);
    fprintf('Znorm done for file %d... \n', fileNum);
    
    znormFilter{fileNum} = medfilt1(znormQ.', 1);
    
    znormCWT = abs(cwt(znormFilter{fileNum}, scaleRange, 'cmor1.5-2'));
    znormCWTSpect{fileNum} = imresize(znormCWT, [100, 32], 'bicubic');
    
    BEpoch = 1: 10;
    BaseMat = (znormCWTSpect{fileNum}(:, BEpoch))';
    BaseMean = repmat(mean(BaseMat)', 1, size(znormCWTSpect{fileNum},2));
    BaseStd = repmat(std(BaseMat)', 1, size(znormCWTSpect{fileNum}, 2));
    znormCWTSpect{fileNum} = (znormCWTSpect{fileNum} - BaseMean) ./ BaseStd;
    
    saveFolder = ...
        sprintf('D:\\LabWork\\ThesisProject\\Music_Autism_Robot\\EDA_Process\\C_Morlet_SVM\\EDA\\');
    saveName = ...
        sprintf('%s.mat', fileNames{fileNum});
    saveClip = znormCWTSpect{fileNum};
    
    save(fullfile(saveFolder, saveName), 'saveClip')
    
    znormCWT = [];
    saveClip = [];
    
end
