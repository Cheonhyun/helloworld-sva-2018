int RVal= 3;
int GVal= 5;
int BVal= 6;
int buttonState = 0;
int buttonR = 1;
int buttonG = 2;
int buttonB = 4;
int ledR = 9;
int ledG = 10;
int ledB = 11;
int buttonstate = 0;
int a = 2000; //this sets how long the stays one color for
int ledcolor = 0;
int lightON = 0;
int val1 = 0;
int val2 = 0;
int val3 = 0;
int pushed = 0;


//Number of LEDs
const int numberLeds=3;
//Pins for each LED
int led[numberLeds] = {9,10, 11};
//State of each LED
int ledState[numberLeds];



//Number of buttons
const int numberButtons=3;

//Set the pins used for each button
int button[numberButtons] = {1,2,4};

//Start state of the LEDs off (HIGH=off when INPUT_PULLUP used)
//No need for pullup/down resistors
int lastButtonState[numberButtons];

//Bools used for when buttons currently pressed (used for long press detection)
bool buttonActive[numberButtons];

//Debounce timer for each button
unsigned long lastDebounceTime[numberButtons];


//Set the debounce delay
int debounceDelay=25;
//Set the time required for a long press
int longPressDelay=500;


void setup() {
  // put your setup code here, to run once:
  buttonSetup();
  pinMode (button[numberButtons], INPUT_PULLUP);
  ledSetup();
  pinMode (led[numberLeds], OUTPUT);
  Serial.begin(9600);
  pinMode (RVal, OUTPUT);
  pinMode (GVal, OUTPUT);
  pinMode (BVal, OUTPUT);
  pinMode (buttonR, INPUT_PULLUP);
  pinMode (buttonG, INPUT_PULLUP);
  pinMode (buttonB, INPUT_PULLUP);

  pinMode (ledR, OUTPUT);
  pinMode (ledG, OUTPUT);
  pinMode (ledB, OUTPUT);
  loop1();
  pinMode (RVal, OUTPUT);
  loop1();
  pinMode (GVal, OUTPUT);
  loop1();
  pinMode (BVal, OUTPUT);
  
  

}

void loop() {

  
  
    
  // put your main code here, to run repeatedly: 
  
  //Loop through each button and get the state
  //0=not pressed
  //1=short press
  //2=long press
  //You could also loop through, set veriables for each button
  //then act on each buttons state seperately
  
  for (int x=0; x<numberButtons; x++)
  {
    int state=buttonHandler(x);

    if ( state== 1)
    {
      ledState[x]=!ledState[x];
      digitalWrite(led[x], ledState[x]);
    }

    if (state == 2)
    {
      ledState[2]=!ledState[2];
      digitalWrite(led[2], ledState[2]);
    }
  }
  
   
}
  






int buttonHandler(int number)
{
  //Handle presses for each button
  int reading = digitalRead(button[number]);

  //Check if button state has changed since last check
  if (reading != lastButtonState[number])
  {
    if (reading==HIGH && !buttonActive[number])
    {
      lastButtonState[number] = reading;
      
      //Return 0 (not pressed)
      return 0;
    }
    
    //if reading is high (open)
    if (reading==HIGH && buttonActive[number])
    {
      if (millis() - lastDebounceTime[number] > debounceDelay)
      {
        lastButtonState[number] = reading;

        buttonActive[number]=true;

        //Return 1 (short press)
        return 1;
      }

      lastButtonState[number] = reading;

      buttonActive[number]=false;
      
      //Return 0 (not pressed)
      return 0;
    }
    
    //if reading is low (closed)
    else if (reading==LOW)
    {
      if (!buttonActive[number])
      {
        //Start debounce timer
        lastDebounceTime[number]=millis();
        
        lastButtonState[number] = reading;

        buttonActive[number]=true;

        //Return 0 (not pressed)
        return 0;
      }
      //Return 0 (not pressed)
      return 0;
    }
  }

  //Check if reading still high (open)
  if (reading==HIGH)
  {
    lastButtonState[number] = reading;
    buttonActive[number]=false;

    //Return 0 (not pressed)
    return 0;
  }

  
  if (reading==LOW)
  {
    //Check if button pressed for long enough to register as long press
    if (millis() - lastDebounceTime[number] > longPressDelay && buttonActive[number])
    {
      lastButtonState[number] = reading;

      buttonActive[number]=false;

      //Return 2 (long press)
      return 2;
    }
    else
      //Return 0 (not pressed)
      return 0;
  }
}






void ledSetup()
{
  for (int x=0; x<numberLeds; x++)
  {
    pinMode(led[x], OUTPUT);
    ledState[x]=LOW;
  }
}






void buttonSetup()
{
  for (int x=0; x<numberButtons; x++)
  {
    lastButtonState[x]=HIGH;
    buttonActive[x]=false;
    lastDebounceTime[x]=0;
   // buttonState[x]=HIGH;
    pinMode(button[x], INPUT_PULLUP);
    
  }
}



void loop1(void) {
 {
  val1 = digitalRead(buttonR);
  val2 = digitalRead(buttonG);
  val3 = digitalRead(buttonB);
  
  if(val1 == HIGH && lightON == LOW){
    pushed = 1 - pushed;
 
  }
  lightON = val1;
  if(pushed == HIGH){
    Serial.println("Light ON");
    digitalWrite(ledR, LOW);
  }
  else{
    Serial.println("Light OFF");
    digitalWrite(ledR, HIGH);
  }
   
   
  if(val2 == HIGH && lightON == LOW){
    pushed = 1 - pushed;
    
  }
  
  lightON = val2;
  if(pushed == HIGH){
    Serial.println("Light ON");
    digitalWrite(ledG, LOW);
  }
  else{
    Serial.println("Light OFF");
    digitalWrite(ledG, HIGH);
  }
   
  if(val3 == HIGH && lightON == LOW){
    pushed = 1 - pushed;
    
  }
  lightON = val3;
  if(pushed == HIGH){
    Serial.println("Light ON");
    digitalWrite(ledB, LOW);
  }
  else{
    Serial.println("Light OFF");
    digitalWrite(ledB, HIGH);
  }
  
}
int ledcolor = random(4); //this randomly selects a number between 0 and 6

switch (ledcolor) {



case 1: //if ledcolor equals 3 then the led will turn yellow
analogWrite(RVal, 160);
digitalWrite(GVal, HIGH);
delay(a);
analogWrite(RVal, 0);
digitalWrite(GVal, LOW);
break;

 
case 2: //if ledcolor equals 4 then the led will turn cyan
analogWrite(RVal, 168);
digitalWrite(BVal, HIGH);
delay(a);
analogWrite(RVal, 0);
digitalWrite(BVal, LOW);
break;
case 3: //if ledcolor equals 5 then the led will turn magenta
digitalWrite(GVal, HIGH);
digitalWrite(BVal, HIGH);
delay(a);
digitalWrite(GVal, LOW);
digitalWrite(BVal, LOW);
break;
}

}
