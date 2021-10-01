from pyodbc import connect
import auth

conn = connect('Driver={ODBC Driver 17 for SQL Server};'
               f'Server=tcp:{auth.SQLserver_name}.database.windows.net,1433;'
               f'Database={auth.SQLdatabase_name};'
               f'Uid={SQLdatabase_uid};'
               f'Pwd={SQLdatabase_upw};'
               'Encrypt=yes;'
               'TrustServerCertificate=no;'
               'Connection Timeout=30;')

with conn.cursor() as cursor:
    cursor.execute("select * from WeatherStation where temperature < temperature_alarmpoint")
    rows = cursor.fetchall()

for i, row in enumerate(rows):
    print(f"Row {i}: {row}")
