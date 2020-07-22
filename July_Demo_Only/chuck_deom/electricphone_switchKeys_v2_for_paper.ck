// connect to the serial port 
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
// setup 2 instrument and differnt sound effect to them
BeeThree s => NRev n => Echo e => dac;
Mandolin ss => NRev ee => dac;

.1 => n.mix;
.2 => e.mix;
.2 => ee.mix;

0 => int change;
0 => int cnt;
0 => int select;

<<<"Starting with minor lower key">>>;
// assign different frequencies to two xylophone arrays
[60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77] @=> int xylo1[];
[48, 50, 51, 53, 55, 56, 58, 60, 62, 63, 65] @=> int xylo2[];

while(true)
{
    // wait for event
    cereal.onLine() => now;
    cereal.getLine() => string line;
    // instrument selection
    if (select == 0) 
    {
        1 => select;
    }
    else if(select == 1)
    {
        0 => select;
        continue;
    }
    if(change == 1) 
    {
        if (line$Object != null) 
        {
            chout <= "read line: " <= line <= IO.newline();          
            StringTokenizer tok;
            tok.set(line);
            Std.atoi(line) => int pos;
            chout <= "pos: " <= pos <= IO.newline();   
            //playChord(xylo[pos], "major", T)
            Std.mtof(xylo1[pos]) => float f;
            chout <= "Freq: " <= f <= IO.newline();
            s.freq(f); // Change sin wave frequency 
            .5 => s.noteOn;
            // advance time
            // note: Math.randomf() returns value between 0 and 1
            if( Math.randomf() > .25 ) .25::T => now;
            else .5::T => now;
            if (pos == 10 && cnt == 1) 
            {
                0 => change;
                0 => cnt;
                <<< "Play lower key minor next round" >>>;
            }
            else
            {
                1 => change;
                1 => cnt;
            }                   
        }            
            .02 => s.noteOn;
            .0 => s.noteOff;
            0.0 :: second => now;
            chout <= "play done" <= IO.newline();
    }   
    else 
    {
        if (line$Object != null) 
        {
            chout <= "read line: " <= line <= IO.newline();
            StringTokenizer tok;
            tok.set(line);
            Std.atoi(line) => int pos;
            chout <= "pos: " <= pos <= IO.newline();   
            Std.mtof(xylo2[pos]) => float f;
            chout <= "Freq: " <= f <= IO.newline();
            ss.freq(f); // Change sin wave frequency 
            .5 => ss.noteOn;
            // advance time
            // note: Math.randomf() returns value between 0 and 1
            if( Math.randomf() > .25 ) .25::T => now;
            else .5::T => now;
            if (pos == 10 && cnt == 1) 
            {
                1 => change;
                0 => cnt;
                <<< "Play higher key major next round" >>>;
            }
            else
            {
                0 => change;
                1 => cnt;
            }                   
        }            
            .1 => ss.noteOn;
            .0 => ss.noteOff;
            0.05 :: second => now;
            chout <= "play done" <= IO.newline(); 
    }
   
}
