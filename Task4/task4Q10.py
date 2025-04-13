#Q10)

import math

def round_up_down(number):
    rounded_up = math.ceil(number)
    rounded_down = math.floor(number)
    print("Original number:", number)
    print("Rounded up (ceil):", rounded_up)
    print("Rounded down (floor):", rounded_down)

round_up_down(4.3)
