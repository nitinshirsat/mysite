import psycopg2


conn_object = psycopg2.connect(host="192.168.56.105",
                               port="5432",
                               database="testDB",
                               user="certcapture",
                               password="certcapture")
conn_object.set_isolation_level(0)
cur = conn_object.cursor()


fh = open("/data/test.csv", mode='r')

query = "COPY student(rollno, name)\
                FROM STDIN\
                WITH (\
                  FORMAT CSV,\
                  DELIMITER '|',\
                  HEADER true,\
                  NULL ''\
                );"

cur.copy_expert(query,fh)

sql = "select name from student"
result_set = cur.execute(sql).fetchall()
if result_set is not None :
    print result_set


cur.close()
conn_object.close()


