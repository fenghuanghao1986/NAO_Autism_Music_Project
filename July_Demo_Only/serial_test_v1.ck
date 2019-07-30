

SerialIO cereal;
cereal.open(0, SerialIO.B9600, SerialIO.ASCII);

<<<"start the loop">>>;

SinOsc t[] => dac;

while(true)
{
    <<<"in the loop">>>;
    cereal.onLine() => now;
    cereal.getLine() => string line;
    <<< line >>>;
    Std.atoi(line) => int a;

    [a] @=> int t[];
    
    
    if (t.cap() == 2)
    {
        0.3 => t[1].freq;
        0.3 => t[1].gain;
        0.3 :: second => now;
    }
    else
        continue;

}
