// two oscillators, melody and harmony
SinOsc s => Pan2 mpan => dac;
TriOsc t => dac;

// we will use these to separate notes later
0.5 => float onGain;
0.0 => float offGain;

// declare and initialize our arrays of MIDI note #s
[57,57,64,64,66,66,64,62,62,61,61,59,59,57] @=> int melNotes[];
[61,61,57,61,62,62,61,59,56,57,52,52,68,69] @=> int harmNotes[];

// quarter note and half note durations
0.5 :: second => dur q;
1.0 :: second => dur h;
[q,q,q,q,q,q,h,q,q,q,q,q,q,q,h] @=> dur myDurs[];

// make one more array to hold the words
["Twin", "kle", "twin", "kle", "lit", "tle", "star,",
"how", "I", "won", "der", "what", "you", "are."] @=> string words[];

// loop over all the arrays
for(0 => int i; i < melNotes.cap(); i++)
{
    // print out index, MIDI notes, and words from arrays
    <<< i, melNotes[i], harmNotes[i], words[i] >>>;
    
    // set melody and harmony from arrays
    Std.mtof(harmNotes[i]) => s.freq;
    Std.mtof(melNotes[i]) => t.freq;
    
    // melody has a random pan for each note
    Math.random2f(-1.0, 1.0) => mpan.pan;
    
    // notes are on for 70% of duration from array
    onGain => s.gain => t.gain;
    0.7 * myDurs[i] => now;
    
    // space between notes is 30% of array duration
    offGain => s.gain => t.gain;
    0.3 * myDurs[i] => now;
}
