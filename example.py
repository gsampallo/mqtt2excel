from MQTT2Excel import MQTT2Excel

m2e = MQTT2Excel("broker.hivemq.com","demo1.xls")

m2e.setRecordsNumber(50)

# If you have more topics you just need to add another line with the name of the topic
m2e.addTopics("NIVELGAS")

m2e.start()