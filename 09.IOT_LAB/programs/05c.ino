#include <servo.h>
Servo s1;
int Servopin = 8;
void setup()
{
    s1.attach(Servopin);
}
void loop()
{
    for (int i = 180; i >= 0; i -= 45)
    {
        s1.write(i);
        delay(500);
    }
}
