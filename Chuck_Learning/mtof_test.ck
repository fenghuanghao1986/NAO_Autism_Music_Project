TriOsc t => dac;
0.4 => t.gain;

for( 0 => int i; i < 127; i++)
{
    Std.mtof(i) => float Hz;
    <<< i, Hz >>>;
    Hz => t.freq;
    200::ms => now;

}