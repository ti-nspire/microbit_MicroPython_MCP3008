from microbit import *
class MCP3008:
    def __init__(self, CSpin=pin16):
        self.CS = CSpin.write_digital
        self.CS(1)

        self.mosi = [bytearray([1, (1<<7)|(ch<<4), 0]) for ch in range(8)]
        self.miso = bytearray([0, 0, 0])

    def read(self, CH):
        self.CH = CH

        self.CS(0)
        spi.write_readinto(self.mosi[CH], self.miso)
        self.CS(1)
        return (self.miso[1]<<8 | self.miso[2]) & 1023

##############
# how to use #
##############
if __name__ == "__main__":
    # Initialize the microbit.spi module.
    # You can also specify any of the following options:
    # baudrate=1000000, bits=8, mode=0, sclk=pin13, mosi=pin15, and miso=pin14
    spi.init()

    # Instantiate the MCP3008 class with !CS assigned to pin16.
    adc = MCP3008(CSpin=pin16)

    while True:
        # Get 10-bit data by converting the voltage applied to the channel 0 of MCP3008.
        ADdata = adc.read(CH=0)
        volt   = ADdata * 3.23/1024.0

        print("AD %d, %.2f(V)" % (ADdata, volt))
        sleep(1000)
