SerialIO.list() @=> string list[];

for(int i; i < list.cap(); i++)
{
    chout <= i <= ": " <= list[i] <= IO.newline();
}

// parse first argument as device number
0 => int device;

if(me.args()) {
    me.arg(0) => Std.atoi => device;
}

if(device >= list.cap())
{
    cherr <= "serial device #" <= device <= " not available\n";
    me.exit(); 
}

SerialIO cereal;
if(!cereal.open(device, SerialIO.B9600, SerialIO.ASCII))
{
	chout <= "unable to open serial device '" <= list[device] <= "'\n";
	me.exit();
}

// Set up the music generators
// synchronize to period

.3::second => dur T;
T - (now % T) => now;
SinOsc s => NRev n => Echo e => dac;

.1 => n.mix;
.2 => e.mix;

0 => int cnt;

[60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77] @=> int xylo[];
<<<"start the loop">>>;

while(true)
{
    <<<"in the loop">>>;
    cereal.onLine() => now;
    cereal.getLine() => string line;
    <<< "line get!" >>>;
    
    if (cnt == 0) 
    {
        1 => cnt;
        
    }
    else if(cnt == 1)
    {
        0 => cnt;
        continue;
    }

    if(line$Object != null) {
        <<< "in the if" >>>;
        chout <= "read line: " <= line <= IO.newline();
        
        StringTokenizer tok;
        tok.set(line);
        Std.atoi(line) => int pos;
        chout <= "pos: " <= pos <= IO.newline();   
        Std.mtof(xylo[pos]) => float f;
        chout <= "Freq: " <= f <= IO.newline();
        s.freq(f); // Change sin wave frequency 
        .3 => s.gain;
        0 => s.phase;
        if( Math.randomf() > .25 ) .25::T => now;
        else .3::T => now;
           
    }
    <<< "out if" >>>;
    .0 => s.gain;
    0.0 :: second => now;
    chout <= "play done" <= IO.newline(); 
   
}
