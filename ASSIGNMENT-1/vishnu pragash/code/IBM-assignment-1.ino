const int led1=6,led2=5,led3=4;
const int pir=2,tilt=12,buzzer=3,r=11,g=10,b=9;
const int temp=A0;  
int carry,i,j,k;
void setup()
{
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(led3,OUTPUT);
  pinMode(buzzer,OUTPUT);
  pinMode(pir,INPUT);
  pinMode(tilt,INPUT);
  pinMode(r,OUTPUT);
  pinMode(g,OUTPUT);
  pinMode(b,OUTPUT);
  Serial.begin(9600);
}
void loop()
{
  carry=digitalRead(tilt);
  i=digitalRead(pir);
  j=analogRead(temp);
  delay(500);
  if((carry==1)&&(i!=HIGH))
  {
    digitalWrite(led1,HIGH);
    delay(500);
    digitalWrite(led2,HIGH);
    delay(500);
    digitalWrite(led3,HIGH);
    delay(500);
    digitalWrite(led1,LOW);
    delay(500);
    digitalWrite(led2,LOW);
    delay(500);
    digitalWrite(led3,LOW);
    delay(500);
  }
  else if(i!=HIGH)
  {
    digitalWrite(led3,HIGH);
    delay(500);
    digitalWrite(led2,HIGH);
    delay(500);
    digitalWrite(led1,HIGH);
    delay(500);
    digitalWrite(led3,LOW);
    delay(500);
    digitalWrite(led2,LOW);
    delay(500);
    digitalWrite(led1,LOW);
    delay(500);
  }
 
  if(i==HIGH)
  {
    digitalWrite(led1,HIGH);
    digitalWrite(led2,HIGH);
    digitalWrite(led3,HIGH);
    tone(buzzer,1200,500);
    digitalWrite(led1,LOW);
    digitalWrite(led2,LOW);
    digitalWrite(led3,LOW);
  }
  if(j<100)
  {
  analogWrite(r,255);
  analogWrite(g,0);
  analogWrite(b,0);
  delay(100);
  analogWrite(r,0);
  analogWrite(g,255);
  analogWrite(b,0);
    delay(100);
  analogWrite(r,0);
  analogWrite(g,0);
  analogWrite(b,255);
    delay(100);
  analogWrite(r,255);
  analogWrite(g,0);
  analogWrite(b,255);
    delay(100);
  analogWrite(r,255);
  analogWrite(g,255);
  analogWrite(b,0);
    delay(100);
  analogWrite(r,0);
  analogWrite(g,255);
  analogWrite(b,255);
    delay(100);
  analogWrite(r,255);
  analogWrite(g,255);
  analogWrite(b,255);
  }else{
  analogWrite(r,0);
  analogWrite(g,0);
  analogWrite(b,0);
  
  }
  
}