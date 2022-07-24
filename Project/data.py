
import mysql.connector
myconn=mysql.connector.connect(host="localhost",user="root",passwd="aarti",)

mycursor= myconn.cursor()

mycursor.execute("CREATE DATABASE myaarti")
#print(mycursor)
data=mycursor.fetchone()
print("connection established to: ",data)
myconn.close()
