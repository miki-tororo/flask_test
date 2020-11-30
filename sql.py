import psycopg2

print(1)

 
import psycopg2


# connect postgreSQL
users = 'postgres'
dbnames = 'flask'
passwords = 'postgres'
#host、port are not need on local

conn = psycopg2.connect(" user=" + users +" dbname=" + dbnames +" password=" + passwords)

# excexute sql
cur = conn.cursor()
cur.execute('SELECT * FROM Test;')
results = cur.fetchall()

#output result
print(results)
for i in results:
    print(i)
    for j in i:
        print(j)

cur.close()
conn.close()
