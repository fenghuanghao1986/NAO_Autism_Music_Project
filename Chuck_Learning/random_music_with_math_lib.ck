SqrOsc s => dac;

for (0 => int i; i < 16; i++)
{
    Math.random2(48, 72) => int myNote;
    Math.random2f(0.05, 0.9) => float myGain;
    <<< myNote, myGain >>>;
    Std.mtof(myNote) => s.freq;
    myGain => s.gain;
    0.2 :: second => now;
}
