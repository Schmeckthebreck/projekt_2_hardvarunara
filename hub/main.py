# Import necessary libraries
import paho.mqtt.client as mqtt
import serial
import json
import time
import struct

# Load configuration from config.json file
with open("hub/config.json",) as file:
    config = json.load(file)

# Create a MQTT client and register a callback for connect events
client = mqtt.Client()
# Connect to a broker
client.connect(config["broker"], port=1883, keepalive=60)
# Start a background loop that handles all broker communication
client.loop_start()
# Continuous loop for reading serial data and publishing it to MQTT broker
while True:
    
    # Open a serial connection on COM6 port with a baud rate of 19200
    with serial.Serial('COM6', 19200, timeout=1) as ser:
        # Read a line from the serial port
        line = ser.readline()
        decoded_line = line.decode("utf-8")
        
    # Check if the received line is not empty 
    if len(line) > 0:
        # Split the decoded line into individual components
        list_ = decoded_line.split()
        pico_id = list_[0]
        temp_id = list_[1] 
        temp = list_[2]
        
        # Convert temperature to float, multiply by 1000, and convert to integer
        float_temp = float(temp)
        int_temp = int(float_temp) *1000
        
        # Get the current timestamp
        time_ = int(time.time()) 
        
        # Pack timestamp and temperature as binary data
        packed = struct.pack(">Ii", time_, int_temp)
        
        # Construct MQTT topic based on configuration settings and received data
        topic = config["topic"]
        name = config["name"] 
        topic_ = f"{topic}/{name}/{pico_id}/{temp_id}"
        
        # Print the constructed MQTT topic for debugging purposes
        print(topic_) 
        
        # Publish the packed data to the MQTT broker with specified topic and QoS level
        msg = client.publish(topic_, payload=packed, qos=1)
    else:
        # Continue to the next iteration if no data is received
        continue
