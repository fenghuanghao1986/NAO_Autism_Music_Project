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
.5::second => dur T;
T - (now % T) => now;

//SinOsc s => JCRev r => dac;
SinOsc s => NRev n => Echo e => dac;
//SinOsc s => Chorus c => dac;
//SinOsc s => Echo e => dac;
//.05 => s.gain;
//.1 => r.mix;
.1 => n.mix;
//.1 => c.mix;
.2 => e.mix;

[60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77] @=> int xylo[];

while(true)
{
    cereal.onLine() => now;
    cereal.getLine() => string line;

    if(line$Object != null) {
        chout <= "read line: " <= line <= IO.newline();
        
        StringTokenizer tok;
        tok.set(line);
        Std.atoi(line) => int pos;
        chout <= "pos: " <= pos <= IO.newline();
        
        Std.mtof(xylo[pos]) => float f;
        chout <= "Freq: " <= f <= IO.newline();
        s.freq(f); // Change sin wave frequency 
        //.05 => s.gain;
        .3 => s.gain;
        0 => s.phase;

        // advance time
        // note: Math.randomf() returns value between 0 and 1
        if( Math.randomf() > .25 ) .25::T => now;
        else .5::T => now;
           
    }
    
    .01 => s.gain;
    .0 => s.gain;
    0.0 :: second => now;
    chout <= "play done" <= IO.newline();
}
