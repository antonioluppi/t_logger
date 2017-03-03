float internaltemp;
float externaltemp;
int internalReading;
int internalSensor = 0;
int externalReading;
int externalSensor = 1;
int count = 0;
void setup()
{
  analogReference(INTERNAL);
  Serial.begin(9600);
}

void loop()
{
  internalReading = analogRead(internalSensor);
  externalReading = analogRead(externalSensor);
  internaltemp = internalReading / 9.31;
  externaltemp = externalReading / 9.31;

  Serial.print(count++);
  Serial.print(", \t");
  Serial.print(internaltemp);
  Serial.print(", \t");
  Serial.println(externaltemp);
  delay(100);
}
