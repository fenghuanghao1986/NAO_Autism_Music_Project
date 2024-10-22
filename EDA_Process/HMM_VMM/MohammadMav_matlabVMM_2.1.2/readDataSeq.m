
function [seqTD, seqASD]=readDataSeq(ds, T, epis)
% [seqTD, seqASD]=readDataSeq(ds, T)


load lisa_data_1_152.mat data
warning OFF
% ds = 10;
% T = 4;
% O = 2^T;  % number of the outcomes

m = 0; n = 0;
    for i =[1:27,30:58]
        
        if data(i).st == 1
            n = n + 1;
%             st1(n) = i;
            tmp  = [data(i).gaze(data(i).epis == epis)]'; tmp(tmp == 120) = 1; tmp(tmp == 0) = 1; tmp(tmp == 40) = 0; tmp(tmp == 80) = 1;
            tmp = tmp(1:ds:end)';
            seqTD{n}.se = signal2phrase(tmp, T, 0);
            seqTD{n}.sn = data(i).sn;
            seqTD{n}.kdx = data(i).kdx;
            
        else
            m = m + 1;
%             st2(m) = i;
            tmp  = [data(i).gaze(data(i).epis == epis)]'; tmp(tmp == 120) = 1;  tmp(tmp == 0) = 1;tmp(tmp == 40) = 0; tmp(tmp == 80) = 1;
            tmp = tmp(1:ds:end)';
            seqASD{m}.se = signal2phrase(tmp, T, 0);
            seqASD{m}.sn = data(i).sn;
            seqASD{m}.kdx = data(i).kdx;
            
            
        end
    end



