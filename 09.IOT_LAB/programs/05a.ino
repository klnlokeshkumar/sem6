#include <servo.h>
Servo s1;
int Servopin = 8;
void setup()
{
    s1.attach(Servopin);
}
void loop()
{
    s1.write(90);
    delay(500);
}
