#include <SoftwareSerial.h>
SoftwareSerial EEBlue(10, 11);
void setup()
{
    Serial.begin(9600);
    EEBlue.begin(9600);
    Serial.println("Bluetooth is ready");
}
void loop()
{
    if (EEBlue.available())
    {
        Serial.write(EEBlue.read());
    }
    if (Serial.available())
    {
        EEBlue.write(Serial.read());
    }
}
