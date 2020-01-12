% Music EDA classification (SVM, MKL, single sensor)

% Fs = 32;
% scales = [1:100];
% DesiredFrequency=scal2frq(scales,'cmor1.5-2',1/32)
% 
% fw = DesiredFrequency/2;
% scales = Fs ./ fw

%% SVM - Linear Kernal
% the following results are from Lab computer

% 1vs2
% SVMAccuracy : 51.5152
% SVMConfusionMatrix
% 27  73
% 24  76
% for c = 100
% SVMAccuracy : 60.6061
% SVMConfusionMatrix
% 52  48
% 30  70

% 1vs3
% SVMAccuracy : 46.9697
% SVMConfusionMatrix
% 58  42
% 64  36

% 2vs3
% SVMAccuracy : 56.0606
% SVMConfusionMatrix
% 79  21
% 67  33
% for c = 1000
% SVMAccuracy : 71.2121
% SVMConfusionMatrix
% 79  21
% 36  64

% 1vs2vs3 c = 0.1
% SVMAccuracy : 36.3636
% SVMConfusionMatrix
% 12  67  21
% 18  64  18
%  9  58  33

% 1vs2vs3 c = 10
% SVMAccuracy : 37.3737
% SVMConfusionMatrix
% 42  36  21
% 39  42  18
% 39  33  27

%% SVM - Polynomial Kernal

% c = 0.1 1vs2
% SVMAccuracy : 57.5758
% MKLAccuracy : 43.9394
% SVMConfusionMatrix
% 21  79
%  6  94
% MKLConfusionMatrix
% 36  64
% 48  52

% c = 100 1vs3
% SVMAccuracy : 60.6061
% MKLAccuracy : 50
% SVMConfusionMatrix
% 58  42
% 36  64
% MKLConfusionMatrix
% 45  55
% 45  55

% c = 1 2vs3
% SVMAccuracy : 60.6061
% MKLAccuracy : 57.5758
% SVMConfusionMatrix
% 94   6
% 73  27
% MKLConfusionMatrix
% 67  33
% 52  48

% c = 1 1vs2vs3
% SVMAccuracy : 40.404
% MKLAccuracy : 42.4242
% SVMConfusionMatrix
% 12  76  12
% 12  85   3
%  9  67  24
% MKLConfusionMatrix
% 24  55  21
% 21  58  21
%  9  45  45

%% SVM - RBF Kernal

% c = 0.1 1vs2
% SVMAccuracy : 53.0303
% MKLAccuracy : 43.9394
% SVMConfusionMatrix
% 39  61
% 33  67
% MKLConfusionMatrix
% 36  64
% 48  52

% c = 100 1vs3
% SVMAccuracy : 56.0606
% MKLAccuracy : 50
% SVMConfusionMatrix
% 55  45
% 42  58
% MKLConfusionMatrix
% 45  55
% 45  55

% c = 0.1 2vs3
% SVMAccuracy : 60.6061
% MKLAccuracy : 57.5758
% SVMConfusionMatrix
% 61  39
% 39  61
% MKLConfusionMatrix
% 67  33
% 52  48

% c = 1000 1vs2vs3
% SVMAccuracy : 39.3939
% MKLAccuracy : 42.4242
% SVMConfusionMatrix
% 33  42  24
% 39  39  21
% 36  18  45
% MKLConfusionMatrix
% 24  55  21
% 21  58  21
%  9  45  45

%% Clean
clc;
clear all;
close all;

%% Make Dataset

disp('Loading Data ...')
downSamp = 100;

% C = 0.1; % for 2 different tasks
% C = 10; % for 3 different tasks

task_1 = load('vec_warm0');
task_1 = task_1.output;
task_2 = load('vec_inter0');
task_2 = task_2.output;
task_3 = load('vec_game0');
task_3 = task_3.output;

DataSet0 = { 
            downsample(task_1', downSamp)', ...
            downsample(task_2', downSamp)', ...
            downsample(task_3', downSamp)', ...
            };
         
task_1 = load('vec_warm1');
task_1 = task_1.output;
task_2 = load('vec_inter1');
task_2 = task_2.output;
task_3 = load('vec_game1');
task_3 = task_3.output;

DataSet1 = { 
            downsample(task_1', downSamp)', ...
            downsample(task_2', downSamp)', ...
            downsample(task_3', downSamp)', ...
            };
       
SampNumb = 17;
% TaskNumb = 2; 
TaskNumb = 3;

%% Kfold & PCA & Classification

disp('Kfold & PCA & Classification ...')

SVMAccuracy = zeros(1, SampNumb);
SVMConf = cell(1,SampNumb); 

MKLAccuracy = zeros(1, SampNumb);
MKLConf = cell(1,SampNumb);

SVMLabels_M = zeros(TaskNumb,SampNumb);
MKLLabels_M = zeros(TaskNumb,SampNumb);

for k = 1 : SampNumb         
    
     TrSaLe = [];
     TeSaLe = [];
     TrSaRi = [];
     TeSaRi = [];
    
     for i = 1 : numel(DataSet0)
    
         TempMemLe = DataSet0{i};
         TempMemRi = DataSet1{i};
        
         if isempty(TempMemLe)
             continue
         else
            
            [TrainLe, TestLe] = Kfold(TempMemLe, SampNumb, SampNumb, k); 
            [TrainRi, TestRi] = Kfold(TempMemRi, SampNumb, SampNumb, k); 
    
            TrSaLe = [TrSaLe; TrainLe];
            TeSaLe = [TeSaLe; TestLe]; 
            TrSaRi = [TrSaRi; TrainRi];
            TeSaRi = [TeSaRi; TestRi];
            
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
     
     % Normalize the Dataset (Right) and PCA
     minRi = min(TrSaRi(:));
     maxRi = max(TrSaRi(:));
     
     TrSaRi = (TrSaRi - minRi)/(maxRi - minRi);
     TeSaRi = (TeSaRi - minRi)/(maxRi - minRi); 
     PCAratio = 0.05;
     [TrFeRi, TeFeRi] = CorrectPCA(TrSaRi, TeSaRi, PCAratio);
    
%%  SVM
    
     TrFeCo = cat(2,TrFeLe, TrFeRi);    
     TeFeCo = cat(2,TeFeLe, TeFeRi);
     
%    "-t kernel_type : set type of kernel function (default 2)\n"
% 	"	0 -- linear: u'*v\n"
% 	"	1 -- polynomial: (gamma*u'*v + coef0)^degree\n"
% 	"	2 -- radial basis function: exp(-gamma*|u-v|^2)\n"
% 	"	3 -- sigmoid: tanh(gamma*u'*v + coef0)\n"
% 	"	4 -- precomputed kernel (kernel values in training_set_file)\n"
%   "-c cost : set the parameter C of C-SVC, epsilon-SVR, and nu-SVR (default 1)\n"
     % C = 0.1 for 2 tasks in general 1 gives better results from surface
     
     if numel(DataSet1) == 2
         [model] = svmtrain(TrLa, TrFeCo, '-s 0 -c 0.01 -t 0 ');
     else
         [model] = svmtrain(TrLa, TrFeCo, '-s 0 -c 0.01 -t 0 ');
     end

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
     
%% MKL
% I am using half of the sample (17 samples out of 33 total samples) as 
% left and another half for right, then use them as trainng set and test 
% set, we will see what will happen

     if numel(DataSet1) == 2
         [MKLLabels,~,~] = LpMKL_MW_2f(TrFeLe, TrFeRi, TrLa, TeFeLe, TeFeRi, 10, TaskNumb, 2); 
     else
         [MKLLabels,~,~] = LpMKL_MW_2f(TrFeLe, TrFeRi, TrLa, TeFeLe, TeFeRi, 10, TaskNumb, 2);
     end
         
     MKLLabels_M(:,k) = MKLLabels(:);
    
     MKLCoMa = zeros(TaskNumb, TaskNumb);  
     for i = 1 : TaskNumb  
         for j = 1 : TaskNumb
        
             MKLCoMa(i,j) = numel(find(MKLLabels...
                (1 + (i - 1)*size(TeLa,1)/TaskNumb : i*size(TeLa,1)/TaskNumb) == j));
        
         end    
     end
              
     MKLAccuracy(k) = 100*numel(find((MKLLabels - TeLa) == 0))/numel(TeLa);
     MKLConf{k} = MKLCoMa;
    
end

%% Quantitative Assessments

SVMAcc = sum(SVMAccuracy(:))/SampNumb;
MKLAcc = sum(MKLAccuracy(:))/SampNumb;

ConfMat_SVM1 = 0;
ConfMat_MKL1 = 0;
    
for w = 1 : SampNumb
    
     ConfMat_SVM1 = ConfMat_SVM1 + SVMConf{w};
     ConfMat_MKL1 = ConfMat_MKL1 + MKLConf{w};

end

ConfMat_SVM = round(100*(ConfMat_SVM1/SampNumb)/(numel(TeLa)/TaskNumb));
ConfMat_MKL = round(100*(ConfMat_MKL1/SampNumb)/(numel(TeLa)/TaskNumb));

disp(['SVMAccuracy : ', num2str(SVMAcc)])
disp(['MKLAccuracy : ', num2str(MKLAcc)])
disp('SVMConfusionMatrix')
disp(num2str(ConfMat_SVM))
disp('MKLConfusionMatrix')
disp(num2str(ConfMat_MKL))

