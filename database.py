import mysql.connector as sql
import pwinput as pw

myconnection = sql.connect(host = '127.0.0.1', user = 'root', password = 'Temitayo28', database = 'mybank2_db')
mycursor = myconnection.cursor()
myconnection.autocommit = True

# mycursor.execute('CREATE DATABASE mybank2_db')
# mycursor.execute('SHOW DATABASES')
# print(mycursor)
# for db in mycursor:
#    print(db)

# mycursor.execute(
#     'CREATE TABLE customer_table(id INT(4) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(25), email VARCHAR(25) UNIQUE, account_no VARCHAR(11) UNIQUE, account_bal FLOAT(10), date_created DATETIME DEFAULT CURRENT_TIMESTAMP)'
# )

# mycursor.execute('SHOW TABLES')
# for tables in mycursor:
#     print(tables)

# mycursor.execute('ALTER TABLE customer_table CHANGE id customer_id INT(4) AUTO_INCREMENT')
# mycursor.execute('ALTER TABLE customer_table ADD password VARCHAR(25)')


# fullname = input('Fullname: ')
# email = input('Email: ')
# account_no = input('Account No: ')
# account_bal = float(input('Balance: '))
# password = input('Password: ')

# query = 'INSERT INTO customer_table(fullname, email, account_no, account_bal, password) VALUES(%s, %s, %s, %s, %s)'

# values = (fullname, email, account_no, account_bal, password)

# mycursor.execute(query, values)
# print(mycursor.rowcount, 'customer added successfully')
# myconnection.commit()

import pwinput as pw

# mycursor.execute('SELECT fullname, account_no, account_bal FROM customer_table')
# details = mycursor.fetchall() #fetchone(no tuple, just list, unlike fetchall, which has listed tuples)
# print(details)

# mycursor.execute('SELECT fullname, account_no, account_bal FROM customer_table WHERE email = "sismary@gmail.com" AND password = "1234"')
# details = mycursor.fetchall() #fetchone
# print(details)

# def signin():
#     global account_bal
#     global email
#     email = input('Email: ').strip()
#     password = pw.pwinput()

#     query = 'SELECT fullname, account_no, account_bal FROM customer_table WHERE email = %s AND password = %s'
#     value = (email, password)
#     mycursor.execute(query, value)
#     details = mycursor.fetchone()
#     account_bal = details[2]
#     print(details)

#     if details == None:
#         print('Incorrect Password or Email')
#     else:
#         print('Login successful')
#         deposit()

# def deposit():
#     amount = float(input('Amount: '))
#     new_bal = account_bal + amount

#     query = 'UPDATE customer_table SET account_bal = %s WHERE email = %s'
#     values = (new_bal, email)

#     mycursor.execute(query, values)
#     print('Deposit successful. Your deposit is now,', new_bal)

# signin()

query = ('DELETE FROM customer_table WHERE customer_id = %s')
value = (1,)
# mycursor.execute(query, value)


# mycursor.execute('DROP TABLE customer_table')
mycursor.execute('DROP DATABASE mybank2_db')

# print(mycursor.rowcount, 'customer deleted successfully')

# value = ('email')
# print(type(value))