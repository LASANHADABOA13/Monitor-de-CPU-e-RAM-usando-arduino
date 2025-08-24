#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  Serial.begin(9600);
  

  lcd.begin(16, 2);
  
  lcd.setCursor(0, 0);
  lcd.print("CPU:      RAM:");
  lcd.setCursor(0, 1);
  lcd.print("           %");
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    int c_index = data.indexOf('C');
    int r_index = data.indexOf('R');
    int comma_index = data.indexOf(',');

    if (c_index >= 0 && r_index >= 0 && comma_index > c_index) {
      String cpuValue = data.substring(c_index + 1, comma_index);
      String ramValue = data.substring(r_index + 1);
      
      lcd.setCursor(4, 1);
      lcd.print("   ");
      lcd.setCursor(4, 1);
      lcd.print(cpuValue + "%");

      lcd.setCursor(12, 1);
      lcd.print("   ");
      lcd.setCursor(12, 1);
      lcd.print(ramValue);
    }
  }
}
