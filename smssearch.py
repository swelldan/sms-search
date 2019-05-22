import sqlite3

searchInput = input("What would you like to search? \n")

connection = sqlite3.connect("sms.db")
cursor = connection.cursor()
cursor.execute("select message.text "
               "from message where text like '%" + searchInput + "%' "
               "order by date desc;")
results = cursor.fetchall()
for r in results:
    print(r)
cursor.close()
connection.close()
