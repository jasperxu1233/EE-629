import serial
import time
import MySQLdb as mdb

arduino = serial.Serial("/dev/ttyACM0") // make sure you write correct serial
arduino.baudrate=9600
data = arduino.readline()
time.sleep(2)
data = arduino.readline()
pieces =data.split("\t")
temperature = pieces[0]
humidity = pieces[1]
con = mdb.connect('localhost','root','password','database_name');
with con:
  cursor =con.cursor()
  cursor.execute("INSERT INTO table_name VALUES('',%s,%s)",(temperature    ,humidity))
  con.commit()
  cursor.close()
