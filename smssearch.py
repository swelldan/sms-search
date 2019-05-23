import sqlite3
from operator import itemgetter

searchInput = input("What would you like to search? \n")

connection = sqlite3.connect("sms.db")
cursor = connection.cursor()
cursor.execute("select message.handle_id, message.text, handle.id "
               "from message, handle "
               "where message.text like '%" + searchInput + "%' and handle.ROWID = message.handle_id "
               "order by date desc;")
results = cursor.fetchall()
counter = 0;
for r in results:
    print(str(counter) + ". " + str(r))
    counter+=1
cursor.close()
connection.close()

print('\n There were ' + str(len(results)) + ' results for "' + searchInput + '".\n')

handleId = [lis[0] for lis in results]
messageText =  [lis[1] for lis in results]
contactNum = [lis[2] for lis in results]

chooseResult = input("Which result number would you like to display? \n")
print (results[int(chooseResult)])
