import math
import time

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay} milliseconds is {result}")

if __name__ == "__main__":
    number = int(input())
    delay = int(input())
    delayed_sqrt(number, delay)