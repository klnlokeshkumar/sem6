int sensorData;
void setup()
{
    Serial.begin(9600);
    pinMode(9, OUTPUT);
    pinMode(8, INPUT);
}
void loop()
{
    sensorData = digitalRead(8);
    if (sensorData == HIGH)
    {
        digitalWrite(9, HIGH);
        Serial.println("Sensor activated");
        Serial.println("Motion detected");
        delay(50);
    }
    else
    {
        digitalWrite(9, LOW);
        delay(50);
    }
}