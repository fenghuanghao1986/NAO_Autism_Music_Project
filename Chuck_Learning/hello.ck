<<< "Hello, World!" >>>;
SinOsc s => dac;
1.0 => s.gain;
220 => s.freq;
0.3 :: second => now;

0.0 => s.gain;
0.3 :: second => now;

1.0 => s.gain;
0.3 :: second => now;

// play two more notes
330 => s.freq;
0.3 => s.gain;
0.3 :: second => now;

0.0 => s.gain;
0.3 :: second => now;

0.3 => s.gain;
0.3 :: second => now;

0.0 => s.gain;
0.3 :: second => now;

