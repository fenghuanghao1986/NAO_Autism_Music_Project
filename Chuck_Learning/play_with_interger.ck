SinOsc s => dac;
220 => int myPitch;

1 => int onGain;
0 => int offGain;

// play one note
myPitch => s.freq;
onGain => s.gain;
0.3 :: second => now;

offGain => s.gain;
0.3 :: second => now;

2 *=> myPitch;

// play another note, with a higer pitch
myPitch => s.freq;
onGain => s.gain;
0.3 :: second => now;

offGain => s.gain;
0.3 :: second => now;