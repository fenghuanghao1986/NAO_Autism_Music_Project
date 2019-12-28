clc;
clear;
warning off

dataPath = 'D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\EDA';
fileType = '*.csv';

dd = dir(fullFile(dataPath, fileType));
fileNames = {dd.name};
num = numel(fileNames);

data = cell(num, 2);
data(:,1) = regexprep(fileNames, '.csv', '');
znormFilter = cell(num, 1);
scaleRange = 1:100;

for fileNum = 1: numel(fileNames)
    
    data{fileNum, 2} = dlmread(fullfile(dataPath, fileNames{fileNum}));
    fprintf('Reading CSV sensor data...\n');
    dataQ = data{fileNum, 2}(:, 6);
    
    [znormQ, muQ, sigmaQ] = zscore(dataQ);
    fprintf('Znorm done for file %d... \n', file_num);
    
    znormFilter{fileNum} = medfilt1(znormQ.', 1);
    
    znormCWT = abs(cwt(znormFilter{fileNum}, scaleRange, 'cmor1.5-2'));
    znormCWTSpect = imresize(znormCWT, [100, 32], 'bicubic');
    
    BEpoch = 1: 10;
    BaseMat = (znormCWTSpect(:, BEpoch))';
    BaseMean = repmat(mean(BaseMat)', 1, size(znormCWTSpect));
    BaseStd = repmat(std(BaseMat)', 1, size(znormCWTSpect),2);
    znormCWTSpect = (znormCWTSpect - BaseMean) ./ BaseStd;
    
    saveFolder = sprintf('D:\\LabWork\\ThesisProject\\Music_Autism_Robot\\EDA_Process\\C_Morlet_SVM\\EDA\\');
    saveName = sprintf('file_%d', fileNum);
    

    
end
