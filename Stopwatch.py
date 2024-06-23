import time

mytime = int(input("enter seconds\n"))

for i in range(mytime,0,-1):
    seconds = i % 60
    minutes = int(i/60)%60
    hours = int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end='\r')
    time.sleep(1)
print("it's time up")    
    
