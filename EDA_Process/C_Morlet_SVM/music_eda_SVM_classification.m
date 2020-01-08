% Music EDA classification (SVM, MKL, single sensor)

% Fs = 32;
% scales = [1:100];
% DesiredFrequency=scal2frq(scales,'cmor1.5-2',1/32)
% 
% fw = DesiredFrequency/2;
% scales = Fs ./ fw


clc;
clear all;
close all;

%% Make Dataset

disp('Loading Data ...')
downSamp = 100;

% C = 0.1; % for 2 different tasks

task_1 = load()