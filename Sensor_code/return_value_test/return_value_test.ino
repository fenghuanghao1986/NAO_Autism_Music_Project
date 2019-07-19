const int selectPins[6] = {7,6,5,4,3,2}; // mux1 S0~7, S1~6, S2~5; mux2 S0~4, S1~3, S2~2
const int zOutput = 5; // Don't know what is this for in our case
const int zInput1 = A1; // Connect common z to A1 for mux1
const int zInput2 = A2; // Connect common z to A2 for mux2

void setup() {
  Serial.begin(9600);   // Initialize the serial port
  // Set up the select pins as outputs:
  for (int i=0; i<6; i++)
  {
    pinMode(selectPins[i], OUTPUT);
    digitalWrite(selectPins[i], HIGH);
  }
  pinMode(zInput1, INPUT);  // Set up z1 as an input for mux1
  pinMode(zInput2, INPUT);  // Set up z2 as an input for mux2
}

void loop() {
  // loop through all 11 pins
  for (byte pin=0; pin<=7; pin++)
  {
    selectMux1Pin(pin);   // Select one at a time from mux1
    // selectMux2Pin(pin);   // Select one at a time from mux2
    int inputValue1 = analogRead(A1);  // read z1
    // int inputValue2 = analogRead(A2)  // read z2
    int hitBar = checkSensor(inputValue1, pin);
    Serial.print(hitBar);
  }
  Serial.println();
  delay(50);

}

// The selectMuxPin function sets the S0, S1, and S2 pins
// accordingly, given a pin from 0-7.
void selectMux1Pin(byte pin)
{
  for (int i=0; i<3; i++)
  {
    if (pin & (1<<i))
      digitalWrite(selectPins[i], HIGH);
    else
      digitalWrite(selectPins[i], LOW);
  }
}

void selectMux2Pin(byte pin)
{
  for (int i=0; i<3; i++)
  {
    if (pin & (1<<i))
      digitalWrite(selectPins[i], HIGH);
    else
      digitalWrite(selectPins[i], LOW);
  }
}

int checkSensor(int inputValue, int pin) {
  if (inputValue > 100) {
    return pin;
  }
  else {
    return 0;
  }
}
