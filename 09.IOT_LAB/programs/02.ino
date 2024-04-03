void setup()
{
    pinMode(8, OUTPUT);
    pinMode(10, OUTPUT);
}
void loop()
{
    digitalWrite(8, 1);
    digitalWrite(10, 1);
    delay(1000);
    digitalWrite(8, 0);
    digitalWrite(10, 0);
    delay(1000);
}
