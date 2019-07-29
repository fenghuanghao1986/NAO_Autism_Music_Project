// Listing 10.2 Keyboard organ controlled by Hid event
// Hid object
Hid hi;                  // (1) Makes a new Hid object...

// message to convey data from Hid device
HidMsg msg;              // (2) ...and Hid message holder.

// device number: which keyboard to open
0 => int device;         // (3) Keyboard device number.

// open keyboard; or exit if fail to open
if( !hi.openKeyboard( device ) ) me.exit();  // (4) Opens it, exits if failed.

// print a message!           // (5) Prints message if success.
<<< "keyboard '" + hi.name() + "' ready", "" >>>;

// sound chain for Hid keyboard controlled organ
BeeThree organ1 => dac; // (6) Organ UGen through reverb to dac.
BeeThree organ2 => JCRev r => dac;

1 => int change;

// infinite event loop
while( true )
{
    // wait for event
    hi => now;                    // (7) Waits for keyboard event.
    // get message
    <<< hi >>>;

    if( hi.recv( msg ) )       // (8) loops over all messages (keys pressed).
    {

        if (change == 1)
        {
            
            // button (key) down, play a Note
            if( msg.isButtonDown() )
            {                         // (9) If keyDown, set frequency from keycode...
                // take ascii value of button, convert to freq
                
                Std.mtof( msg.ascii ) => organ1.freq;
                <<< "key DOWN:", msg.ascii >>>;
                // sound the note
                .2 => organ1.noteOn;    // (10) ... and play a note.
            }
            
            else // button up, noteOff
            {
                // deactivate the note
                0 => organ1.noteOff;   // (11) End the note on keyUp.
            }
        }
        else
        {
            if( msg.isButtonDown() )
            {                         // (9) If keyDown, set frequency from keycode...
                // take ascii value of button, convert to freq
                
                Std.mtof( msg.ascii ) => organ2.freq;
                <<< "key DOWN:", msg.ascii >>>;
                // sound the note
                .3 => organ2.noteOn;    // (10) ... and play a note.
                
            }
            else // button up, noteOff
            {
                // deactivate the note
                0 => organ2.noteOff;   // (11) End the note on keyUp.
            }
        
        }
        <<< change >>>;
        <<< msg.ascii >>>;
        <<< "done1" >>>;
        
        if ((msg.ascii == 0) && (change == 0) && (msg.isButtonDown())) 
        {
            1 => change;
        }
        else if ((msg.ascii == 0) && (change == 1) && (msg.isButtonDown()))
        {
            0 => change;
        }
        
        
        <<< change >>>;
        <<< msg.ascii >>>;
        <<< "done2" >>>;
    }
    
}


