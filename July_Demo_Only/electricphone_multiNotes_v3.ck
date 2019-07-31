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

SinOsc notes[2];               // (1) Three oscillators for a chord

for (0 => int i; i < notes.cap(); i++)
{
    // connect each element of our array to dac
    notes[i] => dac;           // (2) Connects them all to the dac...

    // adjust gain so we don't overload
    .6/notes.cap() => notes[i].gain; // (3) ...and sets their gains so you don't overload.
}

fun void playNotes(int note1, int note2, dur howLong)
{
    // set root of chord
    Std.mtof(note1) => notes[0].freq;        // (4) Root of chord.

    // set fifth of chord
    Std.mtof(note2) => notes[1].freq;      // (5) Fifth of chord.


    howLong => now;
}

.3::second => dur T;
T - (now % T) => now;

//.1 => n.mix;
//.2 => e.mix;

0 => int cnt;

[0,60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 0,0,0,0] @=> int xylo[];
<<<"start the loop">>>;

while(true)
{
    <<<"in the loop">>>;
    cereal.onInts(16) => now;
    cereal.getInts() @=> int line[];
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
    [0,0] @=> int note[];
    0 => int k;
    
    if(line$Object != null) {
        <<< "in the if" >>>;
        //chout <= "read line: " <= line <= IO.newline();
        
        //StringTokenizer tok;
        //tok.set(line);
        for (int j; j < line.cap(); j++)
        {
            if (j == 15 && line[j] == 0)
            {
                0 => note[k];
            }
            break;
            
            if(line[j] == 1)
            {
                xylo[j] => note[k];
                k+1 => k;
                continue;
            }
            else
                continue;
        }
 
        playNotes(note[0], note[1], T);
           
        if( Math.randomf() > .25 ) .25::T => now;
        else .3::T => now;
           
    }
    <<< "out if" >>>;

    chout <= "play done" <= IO.newline(); 
   
}
