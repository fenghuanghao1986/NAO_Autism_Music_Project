// Sine Twinkle Music with float variables

SinOsc s => dac;

220.0 => float twinkle;
1.6818 * twinkle => float little;

1 => int onGain;
0 => int offGain;

// play one note
twinkle => s.freq;
onGain => s.gain;
0.3 :: second => now;
offGain => s.gain;
0.3 :: second => now;

1.5 *=> twinkle;

// play onther note of 2nd twinkle
twinkle => s.freq;
onGain => s.gain;
0.3 :: second => now;
offGain => s.gain;
0.3 :: second => now;

// play note of little
little => s.freq;
onGain => s.gain;
0.3 :: second => now;
offGain => s.gain;
0.3 :: second => now;
