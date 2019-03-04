deg = pi/180;

% NAO constants (in mm)
ShoulderOffsetY = 98.00;
ElbowOffsetY = 15.00;
UpperArmLength = 105.00;
LowerArmLength = 55.95;
ShoulderOffsetZ = 100.00;
HandOffsetX = 57.75;
RHandOffsetZ = 12.31;
Stick = 160;

% set some default plot options, base and shadow are not useful for a multi-arm plot
plotopts = {'nobase', 'noshadow'};

rightarm = SerialLink( [
    Revolute('d', 0, 'alpha', -pi/2, 'a', 0, 'modified')
    Revolute('d', 0, 'alpha', pi/2,  'a', 0, 'offset', pi/2, 'modified')
    Revolute('d', -UpperArmLength, 'alpha', -pi/2, 'a', 0, 'modified')
    Revolute('d', 0, 'alpha', pi/2,  'a', 0, 'modified')
    Revolute('d', -HandOffsetX-LowerArmLength, 'alpha', -pi/2,  'a', 0, 'modified')
    ], ...
    'base', transl(0, -ShoulderOffsetY-ElbowOffsetY, ShoulderOffsetZ), ...
    'tool', trotx(pi/2)*trotz(-pi/2)*transl(0, Stick, 0), ...
    'plotopt', plotopts, ...
    'name', 'right arm', 'manufacturer', 'Aldabaran');
