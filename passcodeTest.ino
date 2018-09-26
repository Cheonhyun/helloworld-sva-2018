#define NOTE_A6 1760
#define NOTE_B5 988
#define NOTE_C7 2093

//define pins
const int redButton = 11;
const int blueButton = 12;
const int greenButton = 10;
const int redLed = 9;
const int greenLed = 8;
const int buzzer = 7;

int toneLength = 2;
int correctTones[] = {988, 1760};
int incorrectTones[] = {208, 196};
int code[] = {1,2,3,2}; //this is the code that we set for our lock
int userEntered[4];     //empty array to store the values entered by the user
int buttonCheck;        //counter to store number of times buttons have been pressed

void setup() {

  Serial.begin(9600);   // set up the serial monitor
  Serial.println("Please enter a code to unlock the safe.");
  Serial.println();
  // ENABLE PULL UPS ON INPUTS
  pinMode(redButton, INPUT_PULLUP);
  pinMode(blueButton, INPUT_PULLUP);
  pinMode(greenButton, INPUT_PULLUP);

  //SET UP OUTPUTS
  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);

  pinMode(buzzer, OUTPUT);

  //leave red LED on always to denote "locked" status
  digitalWrite(redLed, HIGH);

}

void loop() {
  // put your main code here, to run repeatedly:

  if (digitalRead(redButton) == LOW){ //if redButton is pressed
    tone(buzzer, NOTE_C7, 100);
    checkEntered(1);                  //call checkEntered and pass it a 1    
    delay(250);                       //wait, needed for correct functioning, otherwise
                                      //buttons are deemed to be pressed more than once
    
  }
  else if (digitalRead(blueButton) == LOW){ //if blueButton is pressed
    tone(buzzer, NOTE_B5, 100);
    checkEntered(2);                  //call checkEntered and pass it a 2    
    delay(250); //wait
    
  }
  else if (digitalRead(greenButton) == LOW){ //if greenButton is pressed
    tone(buzzer, NOTE_A6, 100);
    checkEntered(3);                 //call checkEntered1 and pass it a 3    
    delay(250);                      //wait
    
  }
}
//this function resets the board through software.
void(* resetFunc) (void) = 0;        // declare reset fuction at address 0

//receives input from the user, checks if an index is 0 i.e. empty
//if empty, sets that index to the user input, stores the index and increments check
void checkEntered(int button) {
  int i;
  int index = -1;                   //-1 if array is full
  for (i = 0; i< 4; i++) {
    //Serial.print("size of userEntered is "); Serial.println(sizeof(userEntered));
    if (userEntered[i] == 0) {      //if index is empty 
      userEntered[i] = button;      //store the pressed button in that index
      index = i;                    //store the index
      buttonCheck++;                //increment pressed button count
      Serial.print(i); Serial.print(": "); Serial.println(userEntered[i]);
      break;                        //exit the loop
    }
  }

  //if 4 buttons have been pushed..
  if (buttonCheck == 4) {
    compareCode();              //proceed to checking the entered code with the actual code
  }
  
  
}

//compares entered code to actual code
void compareCode() {
  int i;
  
  if (userEntered[0] == code[0] && userEntered[1] == code[1] && 
      userEntered[2] == code[2] && userEntered[3] == code[3]) { //if correct
    digitalWrite(redLed, LOW);      //turn red LED off
    digitalWrite(greenLed, HIGH);   //turn green LED on
    Serial.println("Code is correct. Safe unlocked.");
    Serial.println();
    for (i = 0; i < toneLength; i++) { //loop to emit two short beeps denoting 
                                       //code is correct
      tone(buzzer, correctTones[i]);
      delay(100);
    }
    noTone(buzzer);               //turn buzzer off
    delay(1500);                  //display green LED for 1.5 s 
    digitalWrite(greenLed, LOW);  //and turn off
    Serial.println("Relocking safe now.");
    delay(100);
    resetFunc();
  }
  
  //if any of the entered numbers don't match
  else if (userEntered[0] != code[0] || userEntered[1] != code[1] || 
          userEntered[2] != code[2] || userEntered[3] != code[3]) {
    Serial.println("Entered code is wrong. Please try again.");
    for (i = 0; i < toneLength; i++) { //loop to emit two short beeps denoting 
                                       //code is incorrect
      tone(buzzer, incorrectTones[i]);
      delay(100);
    }
    //tone(buzzer, NOTE_B5, 500);      //emit tone to denote incorrectness

    delay(300);
    resetFunc();
    
  }
}
