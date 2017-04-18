import MySQLdb

conn = MySQLdb.connect(
    host = '192.168.5.242',
    port = 3306,
    user = 'ichunqiu',
    passwd = 'toortoor',
    db = 'ichunqiu',
)

cus = conn.cursor()

sql = 'select version()'

cus.execute(sql)

print(cus.fetchone())

cus.close()
conn.close()