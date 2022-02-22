
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

  
}

// the loop routine runs over and over again forever:
void loop() {
   int data1 = analogRead(A0);
  int data2 = analogRead(A1);
  int data3 = analogRead(A2);
  int data4 = analogRead(A3);
  int data5 = analogRead(A4);
  int data6 = analogRead(A5);
  int data7 = analogRead(A6);
  int data8 = analogRead(A7);
  
  // print out the value you read:
  Serial.print("data1: ");
  Serial.println(data1);
  Serial.print("data2: ");
  Serial.println(data2);
  Serial.print("data3: ");
  Serial.println(data3);
  Serial.print("data4: ");
  Serial.println(data4);
  Serial.print("data5: ");
  Serial.println(data5);
  Serial.print("data6: ");
  Serial.println(data6);
  Serial.print("data7: ");
  Serial.println(data7);
  Serial.print("data8: ");
  Serial.println(data8);
  Serial.print("\n\n");
  delay(1000);        // delay in between reads for stability
}
