int i;
void setup()
{
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
    pinMode(10, OUTPUT);
}
void loop()
{
    for (int i = 0; i <= 255; i++)
    {
        for (int i = 0; i <= 255; i++)
        {
            for (int i = 0; i <= 255; i++)
            {
                RGB(i, j, k);
                delay(100);
            }
        }
    }
}
void RGB(int R, int G, int B)
{
    analogWrite(8, R);
    analogWrite(9, G);
    analogWrite(10, B);
}
