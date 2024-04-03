void setup()
{
    pinMode(8, OUTPUT);
}
void loop()
{
    for (int i = 0; i <= 255; i++)
    {
        analogWrite(8, i);
        delay(100);
    }
    for (int i = 255; i >= 0; i--)
    {
        analogWrite(8, i);
        delay(100);
    }
}