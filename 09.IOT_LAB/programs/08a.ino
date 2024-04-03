#include <DHT.h>
DHT dht(8, DHT11);
void setup()
{
    Serial.begin(9600);
    dht.begin();
    Serial.println("Starting DHT test");
    delay(2000);
}
void loop()
{
    float h = dht.readHumidity();
    float t = dht.readTemperature();
    if (isnan(h) || isnan(t))
    {
        Serial.println("Failed to read from DHT sensor!");
    }
    else
    {
        Serial.print("Humidity: ");
        Serial.print(h);
        Serial.print(" %\t");
        Serial.print("Temperature: ");
        Serial.print(t);
        Serial.println(" *C");
    }
    delay(2000);
}
