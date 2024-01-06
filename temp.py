import  serial
import time

arudino_port = 'COM9'
baud_rate = 9600

arduino = serial.Serial(arudino_port, baud_rate, timeout=1)
time.sleep(2)

num_iterations = 1
for _ in range(num_iterations):
    user_input = input("Enter input for Arduino: ")
    arduino.write(user_input.encode())
    time.sleep(0.1)

while True:
    arudino_output = arduino.readline().decode().rstrip()
    print(f"Arduino Output: {arudino_output}")