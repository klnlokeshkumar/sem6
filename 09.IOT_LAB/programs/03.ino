int c;
void setup()
{
    Serial.begin(9600);
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
    pinMode(10, OUTPUT);
}
void loop()
{
    for (c = 1; c <= 3; c++)
    {
        if (c == 1)
        {
            digitalWrite(8, 1);
            digitalWrite(9, 0);
            digitalWrite(10, 0);
        }
        else if (c == 2)
        {
            digitalWrite(8, 0);
            digitalWrite(9, 1);
            digitalWrite(10, 0);
        }
        else
        {
            digitalWrite(8, 0);
            digitalWrite(9, 0);
            digitalWrite(10, 1);
        }
        delay(1000);
        Serial.println(c);
    }
}