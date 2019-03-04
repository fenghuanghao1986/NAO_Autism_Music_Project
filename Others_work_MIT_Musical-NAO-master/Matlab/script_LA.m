clear all
mdlNAO_LA;
R = SerialLink(leftarm);
% R.plot([0*deg, 0*deg, 0*deg, -0*deg, 0])
T = R.fkine([-2*deg, 28*deg, 0, 0, 0])
In = R.ikine(T,'mask', [1 1 1 0 0 0])

matrix = zeros(200,6);

y_offset = -90:1:90;

y_start = T.t(2);
counter = 1;
for i = 1:60
    T.t(1) = T.t(1) - 1;
    T.t(2) = y_start;
    for j = 1:180
    
    
    In = R.ikine(T,'mask', [1 1 1 0 0 0]);
    matrix(counter,1) =  T.t(1);
    matrix(counter,2) =  T.t(2);

    matrix(counter,3) =  In(1);
    matrix(counter,4) =  In(2);
    matrix(counter,5) =  In(3);
    matrix(counter,6) =  In(4);
%     matrix(counter,7) =  In(5);
    

    T.t(2) = y_start + y_offset(j);
    counter = counter + 1;
    
    end
end