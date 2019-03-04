clear all
mdlNAO_RA; % Create the kinematic chain
R = SerialLink(rightarm);
% R.plot([0*deg, 0*deg, 0*deg, -0*deg, 0])
T = R.fkine([-2*deg, -28*deg, 0, 0, 0])  % Strarting position (Max distance)
In = R.ikine(T,'mask', [1 1 1 0 0 0]) % Calculate the x,y,z of starting position

matrix = zeros(200,6);  % Initilize a matrix for saving the results

y_offset = -90:1:90;  % Set offset in the y-axis. +-90mm of the starting point 

y_start = T.t(2);
counter = 1;
for i = 1:60             % Set offset in the x-axis. -60mm of the starting point 
    T.t(1) = T.t(1) - 1; % Then we calculate the inverse kinematics for these
    T.t(2) = y_start;    % x,y positions and we save them 
    for j = 1:180
    
    In = R.ikine(T,'mask', [1 1 1 0 0 0]);
    
    matrix(counter,1) =  T.t(1); % We save x coordinate
    matrix(counter,2) =  T.t(2); % We save y coordinate
    
    matrix(counter,3) =  In(1); % We save motors' angles
    matrix(counter,4) =  In(2);
    matrix(counter,5) =  In(3);
    matrix(counter,6) =  In(4);
    

    T.t(2) = y_start + y_offset(j);
    counter = counter + 1;
    
    end
end