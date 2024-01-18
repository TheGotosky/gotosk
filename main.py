import time
t = 0
while True:
    t +=1
    time.sleep(1)
    print(f'{t} секунд')
    if t == 60:
        print("минута!!")
        break