Hid myHid;                  // (1) Makes a new Hid.

// message to convey data from Hid device
HidMsg msg;                 // (2) Makes a Hid message holder.

// device number: which keyboard to open
1 => int device;            // (3) Opens Hid on keyboard device.

// open keyboard; or exit if fail to open
if( !myHid.openKeyboard( device ) )
{                           // (4) Error if it can't be opened.
    <<< "Can't open this device!! ", "Sorry." >>>;  
    me.exit();              // (5) Exit, because nothing more can be done.
}

<<< "keyboard '" + myHid.name() + "' ready", "" >>>;

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

SinOsc chord[3];               // (1) Three oscillators for a chord

for (0 => int i; i < chord.cap(); i++)
{
    // connect each element of our array to dac
    chord[i] => dac;           // (2) Connects them all to the dac...

    // adjust gain so we don't overload
    1.0/chord.cap() => chord[i].gain; // (3) ...and sets their gains so you don't overload.
}

fun void playChord(int root, string quality, dur howLong)
{
    // set root of chord
    Std.mtof(root) => chord[0].freq;        // (4) Root of chord.

    // set fifth of chord
    Std.mtof(root+7) => chord[2].freq;      // (5) Fifth of chord.

    // third sets quality, major or minor
    if (quality == "major")
    {
        Std.mtof(root+4) => chord[1].freq;  // (6) Major chord.
    }
    else if (quality == "minor") {
        Std.mtof(root+3) => chord[1].freq;  // (7) Minor chord.
    }
    else
    {
        <<< "You must specify major or minor!!" >>>;
    }
    howLong => now;
}

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
        //playChord(xylo[pos], "major", T)
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
