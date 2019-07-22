// 2-part random music with panning
// two oscillators, melody and harmony

SinOsc s => Pan2 mpan => dac;
TriOsc t => dac;

// we will use these to separate notes later
0.5 => t.gain;
0.5 => float onGain;
0.0 => float offGain;

72 => int melodyNote;

while(true)
{
    // set melody pitch womwhat randomly, with limits
    Math.random2(-3, 3) +=> melodyNote;
    
    if(melodyNote < 60)
    {
        60 => melodyNote;
    }
    if(melodyNote > 84)
    {
        84 => melodyNote;
    }
    
    Std.mtof(melodyNote) => s.freq;
    
    // melody has a random pan for each note
    Math.random2f(-1.0, 1.0) => mpan.pan;
    
    // on a dice roll, change harmony note
    if(Math.random2(1, 6) == 1)
    {
        Std.mtof(melodyNote - 12) => t.freq;
    }
    
    // pick one of three random durations
    Math.random2(1, 3) * 0.2 => float myDur;
    
    // note on time is 80% of duration
    onGain => s.gain;
    (myDur * 0.8) :: second => now;
    
    // space between notes is 20% of array duration
    offGain => s.gain;
    (myDur * 0.2) :: second => now;
}

