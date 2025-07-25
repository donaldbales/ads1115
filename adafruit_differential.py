
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import adafruit_ads1x15.ads1x15 as X15

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus, address 0x049 (73)
ads = ADS.ADS1115(i2c, 1, 128, address=73)

ads.mode = X15.Mode.CONTINUOUS

# Create single-ended input on channel 0
#chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format('raw', 'v'))

while True:
    print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    time.sleep(0.5)

