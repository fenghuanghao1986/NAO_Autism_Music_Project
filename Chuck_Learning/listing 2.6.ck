// panning example
SinOsc s => Pan2 p => dac;

// initialize pan position
-1.0 => float panPosition;

// loop to vary panning
while (panPosition < 1.0){
    panPosition => p.pan;
    <<< panPosition >>>;
    panPosition + 0.01 => panPosition;
    10 :: ms => now;
}

