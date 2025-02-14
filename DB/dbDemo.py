import mysql.connector

#host, DBName, user, password
conn = mysql.connector.connect(host='localhost',
                               database='PythonAutomation',
                               user='root',
                               password='jfreyes_25',
                               auth_plugin='mysql_native_password')

print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
row = cursor.fetchall()

#print records
print(row)