// sound chain: white noise to pan2 to dac
Noise n => Pan2 p => dac;

// noise can sound quite loud
0.2 => n.gain;

// infinite loop
while (true)
{
    // oscillate pan between 1.0 and -10.
    Math.sin(now/second) => p.pan;
    // do it pretty often, to make it smooth
    ms => now;
}