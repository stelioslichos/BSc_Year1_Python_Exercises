'''What is the speed of the vehicle in mph?
40
How many hours has it travelled?
3
Hour | Distance Travelled
-----------------------
1 | 40
2 | 80
3 | 120'''


speed = int(input("What is the speed of the vehicle in mph?\n"))
print()
time = int(input("How many hours has it travelled?\n"))
print()
print("Hour | Distance Travelled")
print("-------------------------")

for i in range(1, time + 1):
    distance = speed * i
    print(f"{i}    | {distance}")