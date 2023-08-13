from machine import TouchPad, Pin
import time
from phone.simcom import A7672S
gsm=A7672S()


capacitiveValue = 500
threshold = 150 # Threshold to be adjusted
touch_pin = TouchPad(Pin(4))

print((touch_pin.read()))

# print("\nESP32 Touch Demo")
# while True: # Infinite loop
#   capacitiveValue = touch_pin.read()
#   if capacitiveValue < threshold:
#     print("Fil touché")
#     time.sleep_ms(500)
#     gsm.Call.dial(9865116823)