const int selectPins1[3] = {5,6,7}; // mux1 S0~5, S1~6, S2~7 
const int selectPins2[3] = {2,3,4}; // mux2 S0~2, S1~3, S2~4
const int zOutput = 5; // Don't know what is this for in our case
const int zInput1 = A1; // Connect common z to A1 for mux1
const int zInput2 = A2; // Connect common z to A2 for mux2

void setup() {
  Serial.begin(9600);   // Initialize the serial port
  // Set up the select pins as outputs:
  for (int i=0; i<3; i++)
  {
    pinMode(selectPins1[i], OUTPUT);
    pinMode(selectPins2[i], OUTPUT);
    digitalWrite(selectPins1[i], HIGH);
    digitalWrite(selectPins2[i], HIGH);
  }
  pinMode(zInput1, INPUT);  // Set up z1 as an input for mux1
  //pinMode(zInput2, INPUT);  // Set up z2 as an input for mux2
}

void loop() {
  // loop through all 11 pins
  for (byte pin=0; pin<=7; pin++)
  {
    selectMuxPin1(pin);   // Select one at a time from mux1
    int inputValue1 = analogRead(A1);  // read z1
    int hitBar1 = checkSensor(inputValue1, pin);

    //Serial.print(String(hitBar1));
  }
   for (byte pin=0; pin<=7; pin++)
  {
    selectMuxPin2(pin);   // Select one at a time from mux2
    int inputValue2 = analogRead(A2);  // read z2
    int hitBar2 = checkSensor(inputValue2, pin+7);

    // Serial.print(hitBar1);
    //Serial.print(String(hitBar2));

  }
  //Serial.println();
  //delay(300);
}

// The selectMuxPin function sets the S0, S1, and S2 pins
// accordingly, given a pin from 0-7.
void selectMuxPin1(byte pin)
{
  for (int i=0; i<3; i++)
  {
    if (pin & (1<<i))
      digitalWrite(selectPins1[i], HIGH);
    else
      digitalWrite(selectPins1[i], LOW);
  }
}

void selectMuxPin2(byte pin)
{
  for (int i=0; i<3; i++)
  {
    if (pin & (1<<i))
      digitalWrite(selectPins2[i], HIGH);
    else
      digitalWrite(selectPins2[i], LOW);
  }
}

int checkSensor(int inputValue, int pin) {
  if (inputValue > 1013) {
    Serial.print(String(pin));
    Serial.println();
    Serial.print(String(pin));
    Serial.println();
    delay(300);
    return pin;
  }
  else {

    return 0;
  }
}
