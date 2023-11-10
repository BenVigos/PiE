char reset1;

void setup() {
  Serial.begin(9600); //begin serial port
  pinMode(2, OUTPUT);
}

void loop() {
  delay(500);
  Serial.println("Give number");
  while (Serial.available() <= 0)
      //Serial.flush();
  {}
  //Serial.read();
  int val = Serial.parseInt();
  
  digitalWrite(2, HIGH);
  delay(val*1000);
  digitalWrite(2,LOW);


}
