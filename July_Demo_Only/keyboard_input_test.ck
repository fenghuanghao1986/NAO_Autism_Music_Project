SinOsc chord[3] => Echo e =>  SqrOsc note => dac;               // (1) Three oscillators for a chord

for (0 => int i; i < chord.cap(); i++)
{
    // connect each element of our array to dac
    //chord[i] => dac;           // (2) Connects them all to the dac...

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

Hid myHid;                  // (1) Makes a new Hid.

// message to convey data from Hid device
HidMsg msg;                 // (2) Makes a Hid message holder.

// device number: which keyboard to open
0 => int device;            // (3) Opens Hid on keyboard device.

// open keyboard; or exit if fail to open
if( !myHid.openKeyboard( device ) )
{                           // (4) Error if it can't be opened.
    <<< "Can't open this device!! ", "Sorry." >>>;  
    me.exit();              // (5) Exit, because nothing more can be done.
}

// print status of open keyboard Hid
                            // (6) If success, print happy message.
<<< "keyboard '" + myHid.name() + "' ready", "" >>>;

// Testing the keyboard Hid
// Impulse keyboard "clicker"sdfdwertt
//Impulse imp => dac;         // (7) "Clicker" to hear key strokes.

// infinite event loop
while( true )               // (8) Infinite loop. 
{
    // wait for event
    myHid => now;           // (9) Wait here for a Hid event.

    // get message(s)
    while( myHid.recv( msg ) )
    {                             // (10) Loop over all messages.
        // Process only key (button) down events
        if( change == 1 ) 
        {                         // (11) If keydown...
            // print ascii value and make a click
            <<< "key DOWN:", msg.ascii >>>; // (12) ...then print which key...
            playChord(msg.ascii, "minor", second/10);
            
            .2 => e.mix;

        }
        else // key (button) up
        {
            <<< "key DOWN:", msg.ascii >>>;
            //Chord(msg.ascii, "minor", second/10);
            // do nothing for now // (14) Do nothing on key
            Std.mtof(msg.ascii) => note.freq;
            .2 => note.gain;

        }
        
    }
}
