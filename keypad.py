#include <Keypad.h>

const int row_num = 4;
const int col_num = 4;

long int current_time = 0;
long int prev_time = 0;
int threshold = 4000;       //  threshold of 2000 ms or 2 seconds
char keypressed = '\0';
int score = 0;

char keys[row_num][col_num] = {
  {'1' , '2' , '3' , 'A'},
  {'4' , '5' , '6' , 'B'},
  {'7' , '8' , '9' , 'C'},
  {'*' , '0' , '#' , 'D'}
};

byte row_pins[] = {19,18,5,17};
byte col_pins[] = {16,4,2,15};

//  making keypad object
Keypad k = Keypad(makeKeymap(keys), row_pins, col_pins, row_num, col_num );

void setup(){
  Serial.begin(115200);
}

void loop(){

  //  picking a random element from 2D array
  byte random_row = random(1,5);
  byte random_column = random(1,5);
  char random_element = keys[random_row-1][random_column-1];

  //  Creating hints
  String hint1 = "Row : " + String(random_row);
  String hint2 = "Column : " + String(random_column);
  byte random_hint = random(1,3);  //  possible values : 1 or 2

  //  picking up a hint
  if (random_hint  ==  1)Serial.println(hint1 + "\t" + hint2);
  else Serial.println(hint2 + "\t" + hint1);



  //  GAME LOOP
  while (true){

    //  looking for a key pressed
    char key = k.getKey();

    //  if valid key is pressed, keypressed will get that key, otherwise, \0
    if (key){
      keypressed = key;
    }



    //  starting timer
    current_time = millis();




    //  checking results and breaking this loop in threshold seconds
    if (current_time - prev_time  ==  threshold){

      //  checking results
      if (keypressed  ==  random_element){
        score++;
        if (score > 6){
          Serial.println("You WON!");
          while(1);
        }
        Serial.println("Correct guess, score : " + String(score));
        threshold = threshold - 500;
        if (threshold < 500)threshold = 500;
      }

      else{
        Serial.println("You LOSE!");
        while(1);
      }

      //  updating prev_time
      prev_time = current_time;
      break;
    }
  }
}