% Music EDA classification (SVM, MKL, single sensor)

% Fs = 32;
% scales = [1:100];
% DesiredFrequency=scal2frq(scales,'cmor1.5-2',1/32)
% 
% fw = DesiredFrequency/2;
% scales = Fs ./ fw

% all 33 same files results after time correction, since the video recoding
% system not sync the time properly, so move 1 min up than before, q sensor
% always sync the real time
% the following results are from Surface computer

% 1vs2
% SVMAccuracy : 51.5152
% SVMConfusionMatrix
% 52  48
% 48  52

% 1vs3
% SVMAccuracy : 53.0303
% SVMConfusionMatrix
% 55  45
% 48  52

% 2vs3
% SVMAccuracy : 57.5758
% SVMConfusionMatrix
% 76  24
% 61  39

% 1vs2vs3 c = 0.1
% SVMAccuracy : 36.3636
% SVMConfusionMatrix
% 48  33  18
% 45  33  21
% 33  39  27

% 1vs2vs3 c = 10
% SVMAccuracy : 30.303
% SVMConfusionMatrix
% 39  27  33
% 45  18  36
% 27  39  33


%% Clean
clc;
clear all;
close all;

%% Make Dataset

disp('Loading Data ...')
downSamp = 100;

% C = 0.1; % for 2 different tasks
% C = 10; % for 3 different tasks

task_1 = load('vec_warm');
task_1 = task_1.output;
task_2 = load('vec_inter');
task_2 = task_2.output;
task_3 = load('vec_game');
task_3 = task_3.output;

% 2 tasks
% DataSet = { downsample(task_2', downSamp)', ...
%             downsample(task_3', downSamp)'};
% 3 tasks
DataSet = { downsample(task_1', downSamp)', ...
            downsample(task_2', downSamp)', ...
            downsample(task_3', downSamp)'};
       
SampNumb = 33;
% TaskNumb = 2;
TaskNumb = 3;

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
     minLe = min(TrSaLe(:));
     maxLe = max(TrSaLe(:));
     
     TrSaLe = (TrSaLe - minLe)/(maxLe - minLe);
     TeSaLe = (TeSaLe - minLe)/(maxLe - minLe); 
     PCAratio = 0.05;
     [TrFeLe, TeFeLe] = CorrectPCA(TrSaLe, TeSaLe, PCAratio);
    
%%  SVM
    
     TrFeCo = TrFeLe;    
     TeFeCo = TeFeLe; 
     % C = 0.1 for 2 tasks
%      [model] = svmtrain(TrLa, TrFeCo, '-s 0 -c 0.1 -t 0 ');
     % C = 10 for 3 tasks C = 0.1 gives better result
     [model] = svmtrain(TrLa, TrFeCo, '-s 0 -c 10 -t 0 ');

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

