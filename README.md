Phyton would work with or without the arduino IDE displaying bloch sphere the only need to be change is the variable **H_State**
to operate. with arduino first is the mobile hostpot must be at 2.4GHZ and arduino ESP8266 and laptop must be connected in the same mobile hotspot

**line 61 and 62** would have this IP this ip is the IP of the ESP and would need to be change depending of the IP of the ESP
**# Function to send data to ESP32
base = "http://192.168.242.237/"**

the rest of the python  would work instantly 

Arduino code would not run without the python as it rely on the pythons computation
Folder must be downloaded as a whole library named **ESP_MICRO.h** must be inside the folder as this library cannot be downloaded in the IDE
**line 21** would have the code **start("test", "bard1348");** this is the SSID and the password of the mobile hotspot tesst is the SSID while the bard1348 is the password 

