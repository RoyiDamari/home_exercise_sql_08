import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="admin",
    password="admin",
    port="5559"
)

cursor = connection.cursor()

select_query = "select * from sp_get_author_wrote_most_books();"
cursor.execute(select_query)

rows = cursor.fetchall()
print(rows)

select_query1 = "select * from sp_average_books_for_author();"
cursor.execute(select_query1)

rows1 = cursor.fetchall()
print(rows1)

select_query2 = "select * from sp_books_statistics();"
cursor.execute(select_query2)

rows2 = cursor.fetchall()
print(rows2)

insert_query = """insert into books (title, release_date, price, author_id)
values (%s, %s, %s, %s) returning id;
"""
insert_values = ('Misery', '1987-06-08 20:21:00', 59.50, 6)
cursor.execute(insert_query, insert_values)
new_id = cursor.fetchone()[0]
print('new_id', new_id)

connection.commit()

cursor.close()
connection.close()