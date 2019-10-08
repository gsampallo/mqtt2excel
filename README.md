# MQTT2Excel

MQTT2Excel it is a Python library that connects to an mqtt server and subscribes to one or more themes. Save the published data in a spreadsheet.

## Installation

You will need:

- Python
- xlwt: pip install xlwt
- paho.mqtt: pip install paho.mqtt

## How to use

Read example/example.py to know how its work. 

If you work with ESP8266 or ESP32, you will find a file named demo.ino is just an example that connect to a public mqtt broker a publish the read of the analog value to fill the spreadsheet.

Also you can read the article in the blog: https://www.gsampallo.com/blog/2019/10/08/mqtt-a-excel/

