int pinoTilt = 8;
 
void setup()
{
  Serial.begin(9600);
  pinMode(pinoTilt, INPUT);
}
 
void loop()
{

  if(digitalRead(pinoTilt) == HIGH)//identificar se houve vibração
  {
    Serial.print("1");
  } 
  else
  {
    Serial.print("0");
  }
}