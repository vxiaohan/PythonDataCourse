import sqlite3 as lite
import pandas

with lite.connect('test.sqlite') as con:
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print(data)

employee = [{'name': 'Mary', 'age': 23, 'gender': 'F'}, {'name': 'John', 'age': 33, 'gender': 'M'}]
df = pandas.DataFrame(employee)

with lite.connect('test.sqlite') as con:
    df.to_sql('employee', con=con, if_exists='replace', index = None)
