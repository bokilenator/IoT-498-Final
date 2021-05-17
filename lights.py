import time
from rpi_ws281x import *
from gpiozero import LED
led = LED(19)
led.off()

# LED strip configuration:
LED_COUNT       = 12      # Number of LED pixels.
LED_GPIO_R      = 12      # GPIO pin connected to the pixels (18 uses PWM!).
LED_GPIO_G      = 13      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 5     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL_18    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_CHANNEL    = 1       # set to '1' for GPIOs 13, 19, 41, 45 or 53



# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def lightSlippers():
    strip_r = Adafruit_NeoPixel(LED_COUNT, LED_GPIO_R, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL_18)
    strip_r.begin()
    colorWipe(strip_r, Color(255, 0, 0))  # Red wipe
    colorWipe(strip_r, Color(0,0,0), 10)

def lightSneakers():
    strip_g = Adafruit_NeoPixel(LED_COUNT, LED_GPIO_G, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip_g.begin()
    colorWipe(strip_g, Color(0, 255, 0))  # Green wipe
    colorWipe(strip_g, Color(0,0,0), 10)

def lightSnowBoots():
    led1 = LED(17)
    led2 = LED(27)
    ledCycle(led1, led2)

def lightRainBoots():
    led1 = LED(16)
    led2 = LED(21)
    ledCycle(led1, led2)


def ledCycle(led1, led2):
    for i in range(5):
        led1.on()
        led2.on()
        time.sleep(.5)
        led1.off()
        led2.off()
        time.sleep(.2)