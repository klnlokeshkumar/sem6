#include <Stepper.h>
int motorspeed = 5;
Stepper mystepper(2048, 2, 4, 3, 5);
void setup()
{
    mystepper.setSpeed(motorspeed);
}
void loop()
{
    mystepper.step(512);
    delay(2000);
    mystepper.step(-1024);
    delay(2000);
}
