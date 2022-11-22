import wiotp.sdk.device
import time
from geopy.geocoders import Nominatim
import random

myConfig = {
 "identity": {
 "orgId": "zal46w",
 "typeId": "NodeMCU",
 "deviceId":"12345"},
 "auth": {
 "token": "1234567890"
 }
}
id= [0]
geoloc=Nominatim(user_agent="geoapiExercises")

def init():
 lat, long = "9.914470", "78.143418"
 lat1, long1 = "9.9933491", "78.127579"
 lat2, long2 = "9.917916", "78.123496"
 location = geoloc.reverse(lat + "," + long)
 addr = location.raw['address']
 suburb = addr.get('suburb', '')
 city = addr.get('city', '')
 mydata = {'p': {'suburb1': suburb+", "+city, 'suburb2': "Tepakulam, "+city, 'suburb3': "KK Nagar, "+city,'g_lat1':lat,'g_long1':long,'g_lat2':lat1,'g_long2':long1,'g_lat3':lat2,'g_long3':long2}}
 client.publishEvent(eventId="status", msgFormat="json", data=mydata, qos=0, onPublish=None)

def dumpster_1():
 lat, long = "9.914470", "78.143418"
 location = geoloc.reverse(lat + "," + long)
 addr = location.raw['address']
 suburb = addr.get('suburb', '')
 city = addr.get('city', '')
 level = random.randint(1,100)
 weight = random.randint(1,1000)
 mydata = {'d': {'Level1': level, 'Weight1': weight, 'Lat1': lat, 'Long1': long,'d_dump1':4}}
 if (level > 50 and weight > 500):
  mydata = {
   'd': {'dump1': dumpid, 'Level1': level, 'Weight1': weight, 'Lat1': lat, 'Long1': long, 'd_dump1':1,'Suburb1': suburb, 'City1': city}}
  client.publishEvent(eventId="status", msgFormat="json", data=mydata, qos=0, onPublish=None)
  print("pick")
  time.sleep(2)
 else:
  client.publishEvent(eventId="status", msgFormat="json", data=mydata, qos=0, onPublish=None)
  print("dump ", dumpid)
 print("Published data Successfully: %s", mydata)

def dumpster_2():
 lat, long = "9.9933491", "78.127579"
 location = geoloc.reverse(lat + "," + long)
 addr = location.raw['address']
 suburb = "Tepakulam"
 city = addr.get('city', '')
 level = random.randint(1,100)
 weight = random.randint(1,1000)
 mydata = {'d': {'Level2': level, 'Weight2': weight, 'Lat2': lat, 'Long2': long,'d_dump2':4}}
 if (level > 50 and weight > 500):
  mydata = {
   'd': {'dump2': dumpid, 'Level2': level, 'Weight2': weight, 'Lat2': lat, 'Long2': long,'d_dump2':2,'Suburb2': suburb, 'City2': city}}
  client.publishEvent(eventId="status", msgFormat="json", data=mydata, qos=0, onPublish=None)
  print("pick")
  time.sleep(2)
 else:
  client.publishEvent(eventId="status", msgFormat="json", data=mydata, qos=0, onPublish=None)
  print("dump ", dumpid)
 print("Published data Successfully: %s", mydata)

def dumpster_3():
 lat, long = "9.917916", "78.123496"
 location = geoloc.reverse(lat + "," + long)
 addr = location.raw['address']
 suburb = "KK Nagar"
 city = addr.get('city', '')
 level = random.randint(1,100)
 weight = random.randint(1,1000)
 mydata = {'d': {'Level3': level, 'Weight3': weight, 'Lat3': lat, 'Long3': long,'d_dump3':4}}
 if (level > 50 and weight > 500):
  mydata = {
   'd': {'dump3': dumpid, 'Level3': level, 'Weight3': weight, 'Lat3': lat, 'Long3': long,'d_dump3':3,'Suburb3': suburb, 'City3': city}}
  client.publishEvent(eventId="status", msgFormat="json", data=mydata, qos=0, onPublish=None)
  print("pick")
  time.sleep(2)
 else:
  client.publishEvent(eventId="status", msgFormat="json", data=mydata, qos=0, onPublish=None)
  print("dump ", dumpid)
 print("Published data Successfully: %s", mydata)


def myCommandCallback(cmd):
 print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
 m=cmd.data['command']
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
while True:
 dumpid = random.randint(1,3)
 init()
 if dumpid == 1:
  dumpster_1()
 elif dumpid == 2:
  dumpster_2()
 elif dumpid==3:
  dumpster_3()

 mydata = {'d': {'d_dump1': 4}}
 client.publishEvent(eventId="status", msgFormat="json", data=mydata, qos=0, onPublish=None)

 client.commandCallback = myCommandCallback
 time.sleep(2)
client.disconnect()
