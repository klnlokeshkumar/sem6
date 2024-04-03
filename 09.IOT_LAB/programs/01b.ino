void setup()
{
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
}
void loop()
{
    digitalWrite(8, 1);
    digitalWrite(9, 0);
    delay(1000);
    digitalWrite(8, 0);
    digitalWrite(9, 1);
    delay(1000);
}
