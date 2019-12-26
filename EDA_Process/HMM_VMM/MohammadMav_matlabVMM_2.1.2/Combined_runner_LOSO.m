% A simple hands-on tutorial
% Browse the code to get the basics of how-to utilize this VMM tool

clear all

global T

verbose = 0;
m = 0;

for T = 1:8;
    m = m + 1;
    n = 0;
    for ds = 16;
        n = n + 1;
        epis = 1; % FF = 1, SF = 2, RE = 3;
        [seqTD, seqASD]=readDataSeq(ds, T, epis);
        
        createParams;
        
        % use AB with size = 5
        disp('---------------------------------------------------');
        if (verbose == 1), disp('working with AB={A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P }'); end
        disp('---------------------------------------------------');
        s = 3;
        % 3. run each of the VMM algorithms
        if (verbose == 1), disp(sprintf('Working with %s', 'PPMC' )); end
        %     disp('--------')
        jVmmASD_full = vmm_createNew(map(ab, seqASD),  ALGS{s}, paramsASD);
        jVmmTD_full = vmm_createNew(map(ab, seqTD),  ALGS{s}, paramsTD);
        
        % test TD sequences versus two models: model_1: TD_LOSO; model_2:
        % ASD_full
        for i = 1:length(seqTD)
            jVmmTD_LOSO = vmm_createLOSO(map(ab, seqTD),  ALGS{s}, i,  paramsTD);
            logLikTD(i,1) = vmm_logEval(jVmmTD_LOSO,mapS(ab, seqTD{i}.se));
            logLikTD(i,2) = vmm_logEval(jVmmASD_full,mapS(ab, seqTD{i}.se));
            if (verbose == 1) ,   disp([ logLikTD(i,1), logLikTD(i,2), logLikTD(i,1) - logLikTD(i,2)]); end
            clear jVmmTD_LOSO
            
        end
        disp(sprintf('epis= %d, T= %d ds= %d \n' , epis, T, ds));
        disp(sprintf('TD = %f', sum(logLikTD(:,1) > logLikTD(:,2))/length(seqTD)*100))
        resultsTD(m,n) = sum(logLikTD(:,1) > logLikTD(:,2))/length(seqTD)*100;
        
        for i = 1:length(seqASD)
            jVmmASD_LOSO = vmm_createLOSO(map(ab, seqASD),  ALGS{s}, i,  paramsASD);
            logLikASD(i,1) = vmm_logEval(jVmmASD_LOSO,mapS(ab, seqASD{i}.se));
            logLikASD(i,2) = vmm_logEval(jVmmTD_full,mapS(ab, seqASD{i}.se));
            if (verbose == 1), disp([ logLikASD(i,1), logLikASD(i,2), logLikASD(i,1) - logLikASD(i,2)]); end
            clear jVmmASD_LOSO
        end
        resultsASD(m,n) = sum(logLikASD(:,1) > logLikASD(:,2))/length(seqASD)*100;
        disp(sprintf('ASD= %f', sum(logLikASD(:,1) > logLikASD(:,2))/length(seqASD)*100))
        
        %for i = 1:length(seqASDF)
        %  jVmmASD_LOSO = vmm_createLOSO(map(ab, seqASD),  ALGS{s}, i,  paramsASD);
        %  logLikASDF(i,1) = vmm_logEval(jVmmTD_full,mapS(ab, seqASDF{i}.se));
        %  logLikASDF(i,2) = vmm_logEval(jVmmASD_full,mapS(ab, seqASDF{i}.se));
        %  disp([ logLikASDF(i,1), logLikASDF(i,2), logLikASDF(i,1) - logLikASDF(i,2)]);
        %  clear jVmmASD_LOSO
        %end
        %  disp(sprintf('ASDF= %f' , sum(logLikASDF(:,1) > logLikASDF(:,2))/length(seqASDF)*100))
        
    end
end