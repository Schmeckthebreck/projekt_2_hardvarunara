# Import necessary libraries
import machine, onewire, ds18x20, time, json

# Load configuration from config.json file
with open("config.json",) as file:
    config = json.load(file)

# Get the unique ID of the Pico board
pico_id = machine.unique_id()

# Configure Raspberry Pico pin for temperature sensor
raspberry_pico = machine.Pin(config["pin"])
temp_sensor = ds18x20.DS18X20(onewire.OneWire(raspberry_pico))

# Scan for connected temperature sensors
roms = temp_sensor.scan() 

# Get the interval for temperature readings from the configuration
timer_s = config["interval"]

# Function to convert temperature sensor ID to hexadecimal format
def temp_id_to_hex(rom):
    id_hex = rom.hex()
    return id_hex

# Continuous loop for reading temperature data and printing it
while True:
    # Start temperature conversion on the sensor
    temp_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        # Print Pico's unique ID, sensor ID in hexadecimal, and temperature reading
        print(pico_id.hex(),temp_id_to_hex(rom),temp_sensor.read_temp(rom), end = "")
        print("\n")
    # Wait for the specified interval before taking the next set of readings
    time.sleep(timer_s)



