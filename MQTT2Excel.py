import xlwt
import time
import paho.mqtt.client as mqtt
import sys

class MQTT2Excel:

    def __init__(self,mqtt_server,filename):
        self.mqtt_server = mqtt_server
        self.filename = filename
        self.topics = []
        self.number = 10
        self.records = 0

        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet("Data from MQTT",cell_overwrite_ok=True)
        self.ws.write(0, 0, "Data from MQTT")
        self.columns = ["Date Time"]        

        self.fila = 1
        
    def addTopics(self,topic):
        self.topics.append(topic)

    def setRecordsNumber(self,number):
        self.number = number

    def on_connect(self,client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        for topic in self.topics:
            print("Suscribe to "+topic)
            client.subscribe(topic)

    def on_message(self,client, userdata, msg):
        print(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())+" "+msg.topic+" "+str(msg.payload))

        self.ws.write(self.fila, 0, time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()))
        
        topic = str(msg.topic)
        idx_topic = self.topics.index(topic)
        self.ws.write(self.fila, (idx_topic+1), str(msg.payload))
        self.records = self.records + 1
        self.fila = self.fila + 1

        if(self.records == self.number):        
            self.wb.save(self.filename)
            sys.exit("Complete "+str(self.number)+" the records")
        
    
    def start(self):
        self.ws.write(0, 0, "Date Time")
        c = 1
        for topic in self.topics:
            self.ws.write(0, c, topic)
            c = c + 1

        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        client.connect(self.mqtt_server, 1883, 60)
        client.loop_forever()



