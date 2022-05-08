from sqlite3 import *

conn = connect("new_database.db")
cursor = conn.cursor()

try:
    query = '''CREATE TABLE students (
        student_name TEXT, 
        avg_score INT,
        class TEXT,
        parents_name TEXT
        )'''
    cursor.execute(query)
except:
    print("Table students already created")

query2 = '''INSERT INTO students 
            (student_name, avg_score, class, parents_name) 
            VALUES 
            ('Панасюк Євгенія', 11, '6А', 'Панасюк Володимир')'''
cursor.execute(query2)



query5 = '''SELECT * FROM students WHERE class = '7А' '''
cursor.execute(query5)
data = cursor.fetchall()
print(data)
for row in data:
    print("Имя: " + row[0])
    print("Средний бал: " + str(row[1]))
    print("Класс: " + row[2])
    print("Имя родителя: " + row[3])
    print("---------------------------------------")
conn.commit()

