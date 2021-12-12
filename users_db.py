import smtplib
import sqlite3 as sq
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


with sq.connect("users.db") as connect:
    cursor = connect.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            second_name TEXT,
            patronymic TEXT,
            birthday TEXT,
            user_email
            )""")
    cursor.execute("""INSERT INTO USERS(first_name, second_name, patronymic, birthday, user_email) VALUES
                ('Maria', 'Voitenko', 'Sergeevna', '17 05 1978', 'Mari78@gmail.com'),
                ('Olga', 'Shyshkevich', 'Oleksandrovna', '29 11 1992', 'flower11@gmail.com'),
                ('Konstantin', 'Poletskiy', 'Sergeevich', '01 10 1999', 'Poletskiy_Konstantin@gmail.com'),
                ( 'Anton', 'Korolenko', 'Petrovich', '14 02 2001', 'Antony01@gmail.com'
                )""")
connect.commit()


class User:

    def get_full_name(self):
        with sq.connect('users.db') as con:
            cur = con.cursor()
            for row in cur.execute('SELECT first_name, second_name, patronymic FROM users'):
                print(row[0], row[1], row[2])

    def get_short_name(self):
        with sq.connect('users.db') as con:
            cur = con.cursor()
            for row in cur.execute('SELECT first_name, second_name, patronymic FROM users'):
                print(f'{row[0]} {row[1][0]}. {row[2][0]}.')

    def get_age(self):
        with sq.connect('users.db') as con:
            cur = con.cursor()
            cur.execute('SELECT birthday FROM users')
            print(cur.fetchall())

    def __str__(self):
        return f'Data: {self.get_short_name()}, {self.get_age()}'

    def new_user(self):
        con = sq.connect('users.db')
        cur = con.cursor()
        first_name = input('Enter your first_name: ')
        second_name = input('Enter your second_name: ')
        patronymic = input('Enter your patronymic: ')
        birthday = input('Enter your birthday: ')
        user_email = input('Enter your email: ')
        cur.execute("""INSERT INTO USERS (first_name, second_name, patronymic, birthday, user_email)
                VALUES (?, ?, ?, ?, ?)""", (first_name, second_name, patronymic, birthday, user_email))
        con.commit()
        return user_email

    def send_email(self):
        msg = MIMEMultipart()
        user_email = User.new_user(self)
        server_email = 'server_email@gmail.com'
        server_password = '12345'
        message = 'Dear user, you have been successfully registered.'
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(server_email, server_password)
        server.sendmail(server_email, user_email, msg.as_string())
        server.quit()
    pass

    def search_user(self):
        with sq.connect('users.db') as con:
            cur = con.cursor()
            first_name = input('Enter the first_name: ')
            second_name = input('Enter the second_name: ')
            cur.execute(f"""SELECT first_name FROM "USERS" WHERE first_name ='{first_name}' """)
            result_1 = cur.fetchall()
            cur.execute(f"""SELECT second_name FROM "USERS" WHERE second_name ='{second_name}' """)
            result_2 = cur.fetchall()
            if result_1 and result_2:
                print('This user in the Date Base')
            else:
                print('First_name or second_name are wrong')
                User.search_user(self)


user = User()
user.get_full_name()
user.get_age()
user.__str__()
user.get_short_name()
user.new_user()
user.search_user()
