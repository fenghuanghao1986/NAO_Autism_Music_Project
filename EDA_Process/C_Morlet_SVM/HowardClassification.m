
% HowardClassification (SVM, Just for a single qsensor)

% Fs = 32;
% scales = [1:100];
% DesiredFrequency=scal2frq(scales,'cmor1.5-2',1/32)
% 
% fw = DesiredFrequency/2;
% scales = Fs ./ fw


clc
clear all
close all
   
%% Make Dataset

disp('Loading Data ...')
DownSamp = 100;

% C = 0.1; % for 2 events - events 2 & 3 are the best!!
% C = 10; % for 3 events

qsensor = 'q1'; % 'q1', 'q2';

event_2 = load(['C:\Users\Lab User\Desktop\Figures_spectrogram_currectVersion (1)\Event_2\event_2_', qsensor]);
event_2 = event_2.output;
event_3 = load(['C:\Users\Lab User\Desktop\Figures_spectrogram_currectVersion (1)\Event_3\event_3_', qsensor]);
event_3 = event_3.output;
event_5 = load(['C:\Users\Lab User\Desktop\Figures_spectrogram_currectVersion (1)\Event_5\event_5_', qsensor]);
event_5 = event_5.output;

DataSet = {downsample(event_2', DownSamp)', ...
           downsample(event_3', DownSamp)', ...
           downsample(event_5', DownSamp)'};

SampNumb = 32;
TaskNumb = 3;

% event_2 = load(['C:\Users\Lab User\Desktop\Figures_spectrogram_currectVersion (1)\Event_2\event_2_', qsensor]);
% event_2 = event_2.output;
% event_3 = load(['C:\Users\Lab User\Desktop\Figures_spectrogram_currectVersion (1)\Event_3\event_3_', qsensor]);
% event_3 = event_3.output;
% 
% DataSetL = {downsample(event_2', DownSamp)', ...
%            downsample(event_3', DownSamp)'};

% SampNumb = 32;
% TaskNumb = 2;

%% Kfold & PCA & Classification

disp('Kfold & PCA & Classification ...')

SVMAccuracy = zeros(1, SampNumb);
SVMConf = cell(1,SampNumb); 

SVMLabels_M = zeros(TaskNumb,SampNumb);

for k = 1 : SampNumb         
    
     TrSaLe = [];
     TeSaLe = [];
    
     for i = 1 : numel(DataSet)
    
         TempMemLe = DataSet{i};
        
         if isempty(TempMemLe)
             continue
         else
            
            [TrainLe, TestLe] = Kfold(TempMemLe, SampNumb, SampNumb, k);            
    
            TrSaLe = [TrSaLe; TrainLe];
            TeSaLe = [TeSaLe; TestLe]; 
            
         end
          
     end    
    
     TrLa = [];
     TeLa = [];
    
     for z = 1 : TaskNumb        
            
          TrLa = [TrLa; z*ones(size(TrainLe, 1),1)];
          TeLa = [TeLa; z*ones(size(TestLe, 1),1)];                        
        
     end
              
%%  PCA
    
     % Normalize the Dataset (Left) and PCA
     TrSaLe = (TrSaLe - min(TrSaLe(:)))/(max(TrSaLe(:)) - min(TrSaLe(:)));
     TeSaLe = (TeSaLe - min(TeSaLe(:)))/(max(TeSaLe(:)) - min(TeSaLe(:))); 
     PCAratio = 0.05;
     [TrFeLe, TeFeLe] = NewPCA2(TrSaLe, TeSaLe, PCAratio);
    
%%  SVM
    
     TrFeCo = TrFeLe;    
     TeFeCo = TeFeLe; 
     [model] = svmtrain(TrLa, TrFeCo, '-s 0 -c 0.1 -t 0 ');
     [SVMLabels, accuracy, DecEst] = svmpredict(TeLa, TeFeCo, model);
    
     SVMLabels_M(:,k) = SVMLabels(:);
    
     SVMCoMa = zeros(TaskNumb, TaskNumb);             
     for i = 1 : TaskNumb  
         for j = 1 : TaskNumb
        
             SVMCoMa(i,j) = numel(find(SVMLabels...
                 (1 + (i - 1)*size(TeLa,1)/TaskNumb : i*size(TeLa,1)/TaskNumb) == j));
        
         end    
     end
    
     SVMAccuracy(k) = accuracy(1);
     SVMConf{k} = SVMCoMa;
    
end

%% Quantitative Assessments

SVMAcc = sum(SVMAccuracy(:))/SampNumb;
ConfMat_SVM1 = 0;
    
for w = 1 : SampNumb
    
     ConfMat_SVM1 = ConfMat_SVM1 + SVMConf{w};

end

ConfMat_SVM = round(100*(ConfMat_SVM1/SampNumb)/(numel(TeLa)/TaskNumb));

disp(['SVMAccuracy : ', num2str(SVMAcc)])
disp('SVMConfusionMatrix')
disp(num2str(ConfMat_SVM))









