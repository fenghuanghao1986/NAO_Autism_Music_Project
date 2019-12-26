% A simple hands-on tutorial
% Browse the code to get the basics of how-to utilize this VMM tool
clc
clear all
close all hidden

global T

verbose = 0;
m = 0;
k =18; % smoothing factor
delay = 0; %starting point delay in coding

PathData = 'C:\Documents and Settings\Vision\My Documents\Dave\Gaze Project\MohammadMavadati\MiamiProjectGaze\Saved';
mkdir(PathData);
SavingFile = ['\Part_TD_ASD_VMM_Classifications_ProbSeq_ImageFormat']
for T = 4;
    m = m + 1;
    n = 0;
    for ds = 18;
        n = n + 1;
        epis = 1; % FF = 1, SF = 2, RE = 3;
        [seqTD, seqASD]=readDataSeqKdx(ds, T, epis, k, delay);
        
        createParams;
        
        % use AB with size = 5
        disp('---------------------------------------------------');
        if (verbose == 1), disp('working with AB ={A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P }'); end
        disp('---------------------------------------------------');
        s = 3;
        % 3. run each of the VMM algorithms
        %%the name of the VMM algorithm; one of the followings: {'LZms', 'LZ78', 'PPMC', 'DCTW', 'BinaryCTW', 'PST'}
        if (verbose == 1), disp(sprintf('Working with %s', 'PPMC' )); end
        %     disp('--------')
        
        jVmmTD_full = vmm_createNew(map(ab, seqTD),  ALGS{s}, paramsTD);
        jVmmASD_full = vmm_createNew(map(ab, seqASD),  ALGS{s}, paramsASD);
        

% 
% TD_VMM_Results =  Prob_TransitionVMM(jVmmTD_full, ab, T);
% ASD_VMM_Results =  Prob_TransitionVMM(jVmmASD_full, ab, T);

numStages=2%specifies the number of stages we want to caclulate the probability of each seq.

SavingFile = [SavingFile 'T' num2str(T) '_NumStage' num2str(numStages)]

[TD_VMM_Results,TD_P0_Symb] =  Prob_TransitionVMM_V2(jVmmTD_full, ab, T, seqTD,numStages);
P0_Symb = TD_P0_Symb;
VMM_Prob = TD_VMM_Results;

% [TD_mat_Image,TD_Tot_Prob,TD_Tot_Symb ] = Funct_Plot_ProbAllSeq_V1(P0_Symb,VMM_Prob,T, numStages,'TD');
% save ([PathData, SavingFile], 'TD_mat_Image', 'TD_Tot_Prob' ,'TD_Tot_Symb');
% clear 'TD_mat_Image' 'TD_Tot_Prob' 'TD_Tot_Symb'
[TD_Tot_Prob,TD_Tot_Symb ] = Funct_Plot_ProbAllSeq_V1_WithoutMat(P0_Symb,VMM_Prob,T, numStages,'TD')
save ([PathData, SavingFile '_NoMatMatrix'],'TD_Tot_Prob' ,'TD_Tot_Symb');
clear 'TD_Tot_Prob' 'TD_Tot_Symb'


close all hidden
[ASD_VMM_Results ,ASD_P0_Symb]=  Prob_TransitionVMM_V2(jVmmASD_full, ab, T, seqASD,numStages);
P0_Symb = ASD_P0_Symb;
VMM_Prob = ASD_VMM_Results;
[ASD_mat_Image,ASD_Tot_Prob,ASD_Tot_Symb ] = Funct_Plot_ProbAllSeq_V1(P0_Symb,VMM_Prob,T, numStages,'ASD');

save ([PathData, SavingFile], 'ASD_mat_Image', 'ASD_Tot_Prob','ASD_Tot_Symb','-append');
clear 'TD_mat_Image' 'TD_Tot_Prob' 'TD_Tot_Symb'

    end
end
clear all
T=4; 
numStages=2%specifies the number of stages we want to caclulate the probability of each seq.
%%run this cript to get the result of TD and ASD entropy and other related
%%informations
Funct_EntropySeqEyeGaze

