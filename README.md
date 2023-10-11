projekt_2_hardvarunara

Description:
This project is a temperature monitoring solution utilizing Raspberry Pi Pico and DS18B20 one-wire sensor. 
The system is designed to measure temperature regularly from one or more sensors, report the temperature 
over UART(standard output connection to the USB port), receive temperature readings over UART, and further 
transmit the readings through MQTT.

BOM:
Raspberry Pi Pico
USB cable for Raspberry Pi Pico
DS18B20 one-wire digital sensor.
Breadboard and wires.

Connections:
1.	Connect the DS18B20 sensor to the Raspberry Pi Pico according to the specifications provided for the DS18B20 sensor.
2.	Connect Raspberry Pi Pico to the computer using a USB cable.

Software setup:
1. Ensure the comuter is connected to the raspberry Pi pico.
2. Open the path to the sensor folder through the terminal (PowerShell).
3. Transfer the contents of the sensor folder to the Raspberry Pi pico:
mpremote cp temp.py :
mpremote cp config.json :

5. Run the program on the raspberry pi pico:
Mpremote

7. Import temp.py.
8. Close the terminal.
9. Change the COM port to which your Pico is connected to in main.py, and modify where the message should be sent in the config file.
10. Run main.py to send the temperature readings.
