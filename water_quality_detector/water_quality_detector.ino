// /********************************************************************/
// TEMPERATURE SENSOR
// #include <OneWire.h>
// #include <DallasTemperature.h>
// /********************************************************************/
// // Data wire is plugged into pin 2 on the Arduino
// #define ONE_WIRE_BUS 2
// /********************************************************************/
// // Setup a oneWire instance to communicate with any OneWire devices
// // (not just Maxim/Dallas temperature ICs)
// OneWire oneWire(ONE_WIRE_BUS);
// /********************************************************************/
// // Pass our oneWire reference to Dallas Temperature.
// DallasTemperature sensors(&oneWire);
// /********************************************************************/
// void setup(void) {
//   // start serial port
//   Serial.begin(9600);
//   Serial.println("Dallas Temperature IC Control Library Demo");
//   // Start up the library
//   sensors.begin();
// }
// void loop(void) {
//   // call sensors.requestTemperatures() to issue a global temperature
//   // request to all devices on the bus
//   /********************************************************************/
//   Serial.print(" Requesting temperatures...");
//   sensors.requestTemperatures();  // Send the command to get temperature readings
//   Serial.println("DONE");
//   /********************************************************************/
//   Serial.print("Temperature is: ");
//   Serial.print(sensors.getTempCByIndex(0));  // Why "byIndex"?
//   int y1 = analogRead(sensors.getTempCByIndex(0));
//   Serial.println(y1);
//   // You can have more than one DS18B20 on the same bus.
//   // 0 refers to the first IC on the wire
//   delay(1000);
// }

// First we include the libraries

/********************************************************************/
//TURBIDITY SENSOR!!!
/********************************************************************/
// void setup() {
//   // initialize serial communication at 9600 bits per second:
//   Serial.begin(9600);
// }

// // the loop routine runs over and over again forever:
// void loop() {
//   // read the input on analog pin 0:
//   // print out the value you read:
//   float volt;
//   float ntu;
//   volt = ((float)analogRead(A0)/1023 *5);
//   ntu = -1120.4*square(volt)+5742.3*volt-4353.8;
//   Serial.println(ntu);
//   delay(100);        // delay in between reads for stability
// }
// float round_to_dp( float in_value, int decimal_place )
// {
//   float multiplier = powf( 10.0f, decimal_place );
//   in_value = roundf( in_value * multiplier ) / multiplier;
//   return in_value;
// }

//DISSOLVED SOLIDS DOESNT WORK, JUST GIVES 0
// Original source code: https://wiki.keyestudio.com/KS0429_keyestudio_TDS_Meter_V1.0#Test_Code
// Project details: https://RandomNerdTutorials.com/arduino-tds-water-quality-sensor/

// #define TdsSensorPin A0
// #define VREF 5.0              // analog reference voltage(Volt) of the ADC
// #define SCOUNT  30            // sum of sample point

// int analogBuffer[SCOUNT];     // store the analog value in the array, read from ADC
// int analogBufferTemp[SCOUNT];
// int analogBufferIndex = 0;
// int copyIndex = 0;

// float averageVoltage = 0.0;
// float tdsValue = 0.0;
// float temperature = 16.0;       // current temperature for compensation

// // median filtering algorithm
// int getMedianNum(int bArray[], int iFilterLen){
//   int bTab[iFilterLen];
//   for (byte i = 0; i<iFilterLen; i++)
//   bTab[i] = bArray[i];
//   int i, j, bTemp;
//   for (j = 0; j < iFilterLen - 1; j++) {
//     for (i = 0; i < iFilterLen - j - 1; i++) {
//       if (bTab[i] > bTab[i + 1]) {
//         bTemp = bTab[i];
//         bTab[i] = bTab[i + 1];
//         bTab[i + 1] = bTemp;
//       }
//     }
//   }
//   if ((iFilterLen & 1) > 0){
//     bTemp = bTab[(iFilterLen - 1) / 2];
//   }
//   else {
//     bTemp = (bTab[iFilterLen / 2] + bTab[iFilterLen / 2 - 1]) / 2;
//   }
//   return bTemp;
// }

// void setup(){
//   Serial.begin(115200);
//   pinMode(TdsSensorPin,INPUT);
// }

// void loop(){
//   static unsigned long analogSampleTimepoint = millis();
//   if(millis()-analogSampleTimepoint > 40U){     //every 40 milliseconds,read the analog value from the ADC
//     analogSampleTimepoint = millis();
//     analogBuffer[analogBufferIndex] = analogRead(TdsSensorPin);    //read the analog value and store into the buffer
//     analogBufferIndex++;
//     if(analogBufferIndex == SCOUNT){
//       analogBufferIndex = 0;
//     }
//   }

//   static unsigned long printTimepoint = millis();
//   if(millis()-printTimepoint > 800U){
//     printTimepoint = millis();
//     for(copyIndex=0; copyIndex<SCOUNT; copyIndex++){
//       analogBufferTemp[copyIndex] = analogBuffer[copyIndex];

//       // read the analog value more stable by the median filtering algorithm, and convert to voltage value
//       averageVoltage = getMedianNum(analogBufferTemp,SCOUNT) * (float)VREF / 1024.0;

//       //temperature compensation formula: fFinalResult(25^C) = fFinalResult(current)/(1.0+0.02*(fTP-25.0));
//       float compensationCoefficient = 1.0+0.02*(temperature-25.0);
//       //temperature compensation
//       float compensationVoltage=averageVoltage/compensationCoefficient;

//       //convert voltage value to tds value
//       tdsValue=(133.42*compensationVoltage*compensationVoltage*compensationVoltage - 255.86*compensationVoltage*compensationVoltage + 857.39*compensationVoltage)*0.5;

//       //Serial.print("voltage:");
//       //Serial.print(averageVoltage,2);
//       //Serial.print("V   ");
//       Serial.print("TDS Value:");
//       Serial.print(tdsValue,0);
//       Serial.println("ppm");
//     }
//   }
// }

//PH SENSOR
#include <Wire.h>

float calibration_value = 21.34 + 8.5;
int phval = 0;
unsigned long int avgval;
int buffer_arr[10], temp;
void setup() {
  Serial.begin(9600);
  delay(2000);
}
void loop() {
  for (int i = 0; i < 10; i++) {
    buffer_arr[i] = analogRead(A0);
    delay(30);
  }
  for (int i = 0; i < 9; i++) {
    for (int j = i + 1; j < 10; j++) {
      if (buffer_arr[i] > buffer_arr[j]) {
        temp = buffer_arr[i];
        buffer_arr[i] = buffer_arr[j];
        buffer_arr[j] = temp;
      }
    }
  }
  avgval = 0;
  for (int i = 2; i < 8; i++)
    avgval += buffer_arr[i];
  float volt = (float)avgval * 5.0 / 1024 / 6;
  float ph_act = -5.70 * volt + calibration_value;
  Serial.println(ph_act);
  delay(1000);
}