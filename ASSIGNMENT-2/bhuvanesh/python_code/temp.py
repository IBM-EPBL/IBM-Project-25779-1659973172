import random
from time import *
flag=True
while(flag):
    Temp = random.randint(0,50)
    Humi = random.randint(10,50)
    if Temp>45 and Humi<30:
        print("Ambient Temperature =",Temp,"Ambient Humidity =",Humi)
        print("---------------------ALARM ON----------------------")
        flag=False
    else:
        print("Ambient Temperature =",Temp,"Ambient Humidity",Humi)
        sleep(0.5);