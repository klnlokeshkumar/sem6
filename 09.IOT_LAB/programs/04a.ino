string color = “ ”;
void setup()
{
    Serial.begin(9600);
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
    pinMode(10, OUTPUT);
}
void loop()
{
    color = Serial.readString();
    color.trim();
    if (color = ‘green’ || color = ‘GREEN’)
    {
        rgb(0, 255, 0);
    }
    if (color = ‘red’ || color = ‘RED’)
    {
        rgb(255, 0, 0);
    }
    if (color = ‘blue’ || color = ‘BLUE’)
    {
        rgb(0, 0, 255);
    }
    if (color = ‘yellow’ || color = ‘YELLOW’)
    {
        rgb(255, 0, 255);
    }
    if (color = ‘cyan’ || color = ‘CYAN’)
    {
        rgb(0, 255, 255);
    }
    if (color = ‘magenta’ || color = ‘MAGENTA’)
    {
        rgb(255, 255, 0);
    }
    if (color = ‘purple’ || color = ‘PURPLE’)
    {
        rgb(128, 128, 0);
    }
    if (color = ‘navyblue’ || color = ‘NAVYBLUE’)
    {
        rgb(0, 128, 0);
    }
    if (color = ‘brown’ || color = ‘BROWN’)
    {
        rgb(165, 42, 42);
    }
    if (color = ‘sage’ || color = ‘SAGE’)
    {
        rgb(178, 136, 172);
    }
}
void rgb(int x, int y, int z)
{
    analogWrite(8, x);
    analogWrite(9, y);
    analogWrite(10, z);
}