// new data type called durations dur

SinOsc s => dac;

220.0 => float twinkle;
// defines note durations for on and off
0.55 :: second => dur onDur;
0.05 :: second => dur offDur;

1 => int onGain;
0 => int offGain;

// play note
twinkle => s.freq;
onGain => s.gain;
onDur => now;

offGain => s.gain;
offDur => now;

// assign next note freq
1.5 *=> twinkle;

// play other note
twinkle => s.freq;
onGain => s.gain;
onDur => now;

offGain => s.gain;
offDur => now;
