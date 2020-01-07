clc;
clear;
warning off

% Pre-process data location 
% remember to change folder if change machine
% Ailienware path
% dataPath = ...
%     'D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM\warmup';
% fileType = ...
%     '*.csv';
% timeFilePath = ...
%     'D:\LabWork\ThesisProject\Music_Autism_Robot\EDA_Process\C_Morlet_SVM';
% Lab path
dataPath = ...
    'D:\Howard_Feng\NAO_Music_Autism_Project\EDA_Process\C_Morlet_SVM\warmup';
fileType = ...
    '*.csv';
timeFilePath = ...
    'D:\Howard_Feng\NAO_Music_Autism_Project\EDA_Process\C_Morlet_SVM';
timeFileName = 'warm_up_time.csv';

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

% open the warmup timestemp file and select start and end in the main loop
timeFileOpen = fopen(fullfile(timeFilePath, timeFileName));
timeMtx = textscan(timeFileOpen, '%s%s%s', 'delimiter', ',', 'CollectOutput', true);
t = timeMtx{1};

startTime = '0:0.0';
endTime = '0:0.0';

% start the loop for saving all mat files and ready for vetorization
for fileNum = 1: num
    
    % save all numerical data in second col
%     data{fileNum, 2} = dlmread(fullfile(dataPath, fileNames{fileNum}));
    startTime = char(t(num, 2));
    endTime = char(t(num, 3));
    
    tempOpen = fopen(fullfile(dataPath, fileNames{fileNum}));
    tempMtx = textscan(tempOpen, '%s%s%s%s%s%s%s%s', 'delimiter', ',', 'CollectOutput',true);
    tempCol = tempMtx{fileNum}(:, 7);
     
    col = cell(size(tempCol));
%     
%     for i = 1: size(tempCol)
%         
%         col(i) = str2double(tempCol(i));
%         
%     end
    
    
    fprintf('Reading CSV data number %d ...\n', fileNum);
    % read 6th col which has all eda from the 2nd col of data
    dataQ = data{fileNum, 2}(:, 6);
    
    % do the znorm for all eda data and save in znorm, mu, and sigma
    [znormQ, muQ, sigmaQ] = zscore(dataQ);
    fprintf('Znorm done for file %d... \n', fileNum);
    
    % after znorm, do med filter to it, and save in znormFilter
    znormFilter{fileNum} = medfilt1(znormQ.', 1);
    % do the cwt using cmor1.5-2
    znormCWT = abs(cwt(znormFilter{fileNum}, scaleRange, 'cmor1.5-2'));
    % resize all data as spectrum in 100* 32
    znormCWTSpect{fileNum} = imresize(znormCWT, [100, 32], 'bicubic');
    % more process to the spectrum
    BEpoch = 1: 10;
    BaseMat = (znormCWTSpect{fileNum}(:, BEpoch))';
    BaseMean = repmat(mean(BaseMat)', 1, size(znormCWTSpect{fileNum},2));
    BaseStd = repmat(std(BaseMat)', 1, size(znormCWTSpect{fileNum}, 2));
    znormCWTSpect{fileNum} = (znormCWTSpect{fileNum} - BaseMean) ./ BaseStd;
    
    % save all the mat files
    saveFolder = ...
        sprintf('D:\\LabWork\\ThesisProject\\Music_Autism_Robot\\EDA_Process\\C_Morlet_SVM\\EDA\\');
    saveName = ...
        sprintf('%d.mat', fileNum);
    saveClip = znormCWTSpect{fileNum};
    
    save(fullfile(saveFolder, saveName), 'saveClip')
    
    id = figure;
    hold on 
    grid on
    
    subplot(2,1,1);
    plot(znormFilter{fileNum}, 'r');
    title(sprintf('File #%d, znorm filtered data plot', fileNum));
    subplot(2,1,2);
    imagesc(znormCWTSpect{fileNum});
    title(sprintf('File #%d, data spectrogram', fileNum));
    xlabel('frame(1/32)s');
    ylabel('EDA(us)');
    
    saveas(id, strcat(saveFolder, sprintf('File #%d figure.fig', fileNum)));
    saveas(id, strcat(saveFolder, sprintf('File #%d figure.tif', fileNum)))
    close all;
    
    znormCWT = [];
    saveClip = [];
    
end
