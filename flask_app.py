from flask import Flask, render_template
from flask import request, url_for
from flask_cors import CORS
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import pyodbc
import os
import mysql.connector

key = b"\x1f4\xc0\xf4\x82\xb8\x8e\x88\xe7\xd1'\xdf\x128D\xe5"
iv = b'\xe4BG\xaa\xe7(\xfc6\xe8\xea\x18&H\x1c\xb9>'
account_ID = 0
arr_ID = []
editDats = []
counts = -1
test = "False"
j = 0
arr_data = []  # stores the encrypted data from the password table
arrdat = []  # stores the password data from the password manager website
i = 0
counting = -1
tempaccount_ID = []
newdats = []

con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Yaseen\Documents\ARPANET\ARPANET\Password Manager.accdb;'
connecter = mysql.connector.connect(host='Yaseen.mysql.pythonanywhere-services.com',
                                    database='Yaseen$Password_Manager',
                                    user='Yaseen',
                                    password='Yasu0178264746+')
res = "None"
app = Flask(__name__)

cors = CORS(app)
# Makes sure the application will open up on the index html page


@app.route('/')
def index():
    global account_ID, arr_ID, arr_data, counts, i, counting, editDats, con_string, connecter
    arr_data.clear()
    arr_ID.clear()
    counting = -1
    editDats.clear()
    i = 0
    counts = 0
    account_ID = 0
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Yaseen\Documents\ARPANET\ARPANET\Password Manager.accdb;'
    connecter = mysql.connector.connect(host='Yaseen.mysql.pythonanywhere-services.com',
                                    database='Yaseen$Password_Manager',
                                    user='Yaseen',
                                    password='Yasu0178264746+')
    return render_template('index.html')
# Makes sure the application will open up on the index html page


# Creates a link for the register html to be called from
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
# Creates a link for the register html to be called from

# receives sign up data from the sign up html page and adds it to the database


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    global key, iv, con_string, res, connecter
    if request.method == 'POST':
        res = "None"
        conn = pyodbc.connect(con_string)

        cursor = connecter.cursor()
        cursor.execute('SELECT * FROM Accounts')

        result = cursor.fetchall()
        data = request.get_json()
        sUsername, sEmail, sPassword = data.split('|')

        for row in result:
            if(row[0] != None):
                cdata = row[1]
                # decrypting the data from the database
                C2 = AES.new(key, AES.MODE_CBC, iv)
                plainname = unpad(C2.decrypt(cdata), 16)

                mail = row[3]
                C4 = AES.new(key, AES.MODE_CBC, iv)
                plainmail = unpad(C4.decrypt(mail), 16)

        # decrypting the data from the database
        # When an encrypted text is decrypted between every letter \x00 can be found which results

        # in not being able to confirm whether or not the password and username are correct
                plainname = plainname.replace(b'\x00', b'')
                plainmail = plainmail.replace(b'\x00', b'')
        # so I am using replace to remove \x00 from the byte data
                name = plainname.decode()
                email = plainmail.decode()
                if (sUsername.upper() == name):
                    res = "Name"
                elif(email == sEmail.upper()):
                    res = "Mail"

        if res == "None":
            add(sEmail.upper(), sPassword, sUsername.upper())

        return res

    if request.method == 'GET':
        print(res)
        return res
# receives sign up data from the sign up html page and adds it to the database

# used to add the provided sign up data to the database


def add(sEmail, sPassword, sUsername):
    print("Hello")
    global key, iv, con_string, connecter
    conn = pyodbc.connect(con_string)
    # encrypting the provided data
    C1 = AES.new(key, AES.MODE_CBC, iv)
    C2 = AES.new(key, AES.MODE_CBC, iv)
    C3 = AES.new(key, AES.MODE_CBC, iv)
    Cipheremail = C1.encrypt(pad(sEmail.encode(), 16))
    Cipherpassword = C2.encrypt(pad(sPassword.encode(), 16))
    Cipherusername = C3.encrypt(pad(sUsername.encode(), 16))
    # encrypting the provided data

    cursor = connecter.cursor()
    cursor.execute('SELECT * FROM Accounts ORDER BY Account_ID DESC LIMIT 1;')
    last = cursor.fetchone()
    x = last[0] + 1

    cursor.execute('INSERT INTO Accounts VALUES (%s,%s,%s,%s)',
                   (x, Cipherusername, Cipherpassword, Cipheremail))
    print(Cipherusername)
    connecter.commit()
    print("value added to the database")

# used to add the provided sign up data to the database


# Creates a link for the login html to be called from
@app.route('/Login', methods=['GET', 'POST'])
def Login():
    return render_template("login.html")
# Creates a link for the login html to be called from

# used to confirm the login details


@app.route('/login', methods=['GET', 'POST'])
def login():
    cdata = b''
    data = b''
    global key, iv, account_ID, test, j, arr_ID, arr_data, counts, i, counting, con_string, connecter
    arr_data.clear()
    arr_ID.clear()
    counting = -1
    editDats.clear()
    i = 0
    counts = 0
    data = request.get_json()
    new = data
    if j == 0:
        j = j + 1
    else:
        account_ID = 0
        test = "False"
    username = new.split('|')[0].upper()
    password = new.split('|')[1]
    conn = pyodbc.connect(con_string)
    cursor = connecter.cursor()
    cursor.execute('SELECT * FROM Accounts;')
    result = cursor.fetchall()
    for row in result:
        cdata = row[1]
        # decrypting the data from the database
        C2 = AES.new(key, AES.MODE_CBC, iv)
        plainname = unpad(C2.decrypt(cdata), 16)
        data = row[2]
        C3 = AES.new(key, AES.MODE_CBC, iv)
        plainpass = unpad(C3.decrypt(data), 16)

        mail = row[3]
        C4 = AES.new(key, AES.MODE_CBC, iv)
        plainmail = unpad(C4.decrypt(mail), 16)

        # decrypting the data from the database
        # When an encrypted text is decrypted between every letter \x00 can be found which results
        plainpass = plainpass.replace(b'\x00', b'')
        # in not being able to confirm whether or not the password and username are correct
        plainname = plainname.replace(b'\x00', b'')
        plainmail = plainmail.replace(b'\x00', b'')
        # so I am using replace to remove \x00 from the byte data
        passw = plainpass.decode()
        name = plainname.decode()
        print(name)
        email = plainmail.decode()
        print(email)
        if ((name == username) or (username == email)) and (passw == password):
            account_ID = row[0]
            test = "True"

    print(test)
    return test
# used to confirm the login details

# Creates a second link for the GET method in javascript to return whether or not the password and username is correct


@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    global test
    if request.method == 'GET':
        print(test)
        return test
# Creates a second link for the GET method in javascript to return whether or not the password and username is correct


# Creates a link for the menu html to be called from
@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html')
# Creates a link for the menu html to be called from

# counts the number of passwords that have the same account_ID as the previously provided accout_ID


@app.route('/count', methods=['GET', 'POST'])
def count():

    if request.method == 'GET':
        global account_ID, arr_ID, arr_data, counts, j, i, counting, editDats, con_string, connecter, tempaccount_ID
        i = 0
        arr_data.clear()
        arr_ID.clear()
        counting = -1
        tempaccount_ID.clear()
        tempaccount_ID.append(account_ID)
        editDats.clear()
        conn = pyodbc.connect(con_string)
        cursor = connecter.cursor()
        cursor.execute(
            'SELECT * FROM Passwords WHERE Account_ID = %s;', (tempaccount_ID))

        result = cursor.fetchall()
        if result:
            for row in result:
                arr_ID.append(row[0])
                arr_data.append(row[1])
                counts = counts + 1
            print(counts)
        cursor.close
        return str(counts)

        return "False"
# counts the number of passwords that have the same account_ID as the previously provided accout_ID

# calls the passwords that are related to the correct account_ID


@app.route('/call', methods=['GET', 'POST'])
def call():
    global account_ID, arr_ID, arr_data, counts, i, counting, con_string, connecter

    if request.method == 'GET':
        # This ensures that the program does not go past the arrays limit
        # This ensures that the program does not go past the arrays limit
        # decrypting the data from the databas
        if(i < len(arr_data)):
            C2 = AES.new(key, AES.MODE_CBC, iv)
            plaindata = unpad(C2.decrypt(arr_data[i]), 16)
            # decrypting the data from the database
            k = plaindata.decode() + "~" + str(arr_ID[i])
            i = i + 1
            print(k)
            return k
        return "False"

# calls the passwords that are related to the correct account_ID

# saves the passwords to the database


@app.route('/save', methods=['GET', 'POST'])
def save():
    upload = False
    if request.method == 'POST':
        upload = True
        data = request.get_json()
        newdata = data
        global account_ID, arrdat, i, arr_data, counts, counting, con_string, connecter
        arrdat = newdata.split("~")
        conn = pyodbc.connect(con_string)

        cursor = connecter.cursor()

        # encrypting data to be added to the database
        C1 = AES.new(key, AES.MODE_CBC, iv)
        cipherdata = C1.encrypt(pad(arrdat[1].encode(), 16))
        # encrypting data to be added to the database
        cursor.execute('UPDATE Passwords SET Encrypted_data = %s WHERE ID = %s;',
                       (cipherdata, arrdat[0]))
        connecter.commit()
        arr_data.clear()  # I had to add this block of code and it results in the person having to press the call button twice when calling
        # their passwords (because I figured this out so late I was not able to change this glitch)
        counts = 0
        # from the javascript end,but I can't remove it because it protects the other passwords from being displayed
        # which was an issue before I added this code
        return "True"

    if((request.method == 'GET') and not(upload)):
        return "True"
    # saves the passwords to the database


@app.route('/adddat', methods=['GET', 'POST'])
def addat():
    return render_template('add.html')


@app.route('/ed', methods=['GET', 'POST'])
def ed():
    return render_template('edit.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    global counting, editDats
    if request.method == 'POST':
        data = request.get_json()
        newdats = data
        editDats.append(newdats)
        return "True"

    if request.method == 'GET':
        line = editDats[0]+"|" + editDats[1] + \
            "|" + editDats[2] + "|" + editDats[3]
        return line


@app.route('/addd', methods=['GET', 'POST'])
def addd():
    upload = False
    if request.method == 'POST':
        data = request.get_json()
        newdats = data
        global account_ID, arrdat, i, arr_data, counts, con_string, connecter
        conn = pyodbc.connect(con_string)

        cursor = connecter.cursor()
        cursor.execute('SELECT * FROM Passwords ORDER BY ID DESC LIMIT 1;')
        last = cursor.fetchone()
        x = last[0] + 1

        C1 = AES.new(key, AES.MODE_CBC, iv)
        cipherdata = C1.encrypt(pad(newdats.encode(), 16))
        # encrypting data to be added to the database
        cursor.execute('INSERT INTO Passwords VALUES (%s,%s,%s)',
                       (x, cipherdata, account_ID))
        connecter.commit()
        upload = True
        return "True"

    if((request.method == 'GET') and not(upload)):
        return "True"
    return "False"


delete = False


@app.route('/delete', methods=['GET', 'POST'])
def deleted():
    global delete, con_string, connecter, newdats
    if request.method == 'POST':
        delete = True
        data = request.get_json()
        newdats.clear()
        newdats.append(data)

        conn = pyodbc.connect(con_string)
        cursor = connecter.cursor()

        cursor.execute('DELETE FROM Passwords WHERE ID = %s;', (newdats))
        connecter.commit()
        print(newdats)
        return "True"

    if (request.method == 'GET') and (delete):
        delete = False
        return "True"
    return "False"


# links the required files for the app
if __name__ == "__main__":
    app.run(debug=True)
    url_for('static', filename='static\js\SignUp.js')
    url_for('static', filename='static\js\Login.js')
    url_for('static', filename='static\js\menu.js')
    url_for('static', filename='static\js\index.js')
    url_for('static', filename='static\css\style.css')
    url_for('static', filename='static\images\LOGO (2).jpg')
    url_for('static', filename='static\images\logoo.jpg')
    url_for('static', filename='static\images\Logo2.jpg')
    url_for('static', filename='static\images\services.jpg')
    url_for('static', filename='static\images\contactUs.jpg')
    url_for('static', filename='static\images\instagram.jpg')
    url_for('static', filename='static\images\facebook.jpg')
    url_for('static', filename='static\images\tiktok.jpg')
    url_for('static', filename='static\images\twitter.jpg')
# links the required files for the app
