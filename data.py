
from flask import request, jsonify, url_for
from flask import Flask, render_template
from flask_cors import CORS
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import pyodbc

key = b"\x1f4\xc0\xf4\x82\xb8\x8e\x88\xe7\xd1'\xdf\x128D\xe5"
iv = b'\xe4BG\xaa\xe7(\xfc6\xe8\xea\x18&H\x1c\xb9>'
account_ID = 0
arr_ID = []
counts = -1
test = "False"
j = 0
arr_data = []
arrdat = []
i = 0

con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Acer\Documents\Coding\Web application project\Password Manager.accdb;'

app = Flask(__name__)

cors = CORS(app)

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/register', methods = ['GET','POST'])
def register():
    return render_template('register.html')


@app.route('/signup', methods = ['GET','POST'])
def signup():
    data =  request.get_json()
    print(data)
    username,email,password = data.split('|')
    print(username)
    print(email)
    print(password)
    

    add(email.upper(),password,username.upper())         

def add(sEmail, sPassword, sUsername ):
    print("hello")
   
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Acer\Documents\Coding\Web application project\Password Manager.accdb;'
    conn = pyodbc.connect(con_string)
        
    print("Connected to database")
    global key, iv
    print(sUsername)
    print(sEmail)
    print(sPassword)
    C1 = AES.new(key, AES.MODE_CBC, iv)
    C2 = AES.new(key, AES.MODE_CBC, iv)
    C3 = AES.new(key, AES.MODE_CBC, iv)
    Cipheremail = C1.encrypt(pad(sEmail.encode(), 16))
    Cipherpassword = C2.encrypt(pad(sPassword.encode(), 16))
    Cipherusername = C3.encrypt(pad(sUsername.encode(), 16))
        
    cursor = conn.cursor()
    cursor.execute('SELECT LAST(Account_ID) FROM Accounts')
    lastID = cursor.fetchone()
    x = lastID[0] + 1
        
    cursor.execute('INSERT INTO Accounts VALUES (?,?,?,?)', (x,Cipherusername , Cipherpassword, Cipheremail))
    print(Cipherusername)
    conn.commit()
    print("value added to the database")
    print(Cipherusername)
    print(Cipheremail)
    print(Cipherpassword)
    return "True"

    

@app.route('/Login', methods = ['GET','POST'])
def Login():
    return render_template("login.html")


@app.route('/login', methods = ['GET','POST'])
def login():
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Acer\Documents\Coding\Web application project\Password Manager.accdb;'
    cdata = b''
    data = b''
    global key, iv, account_ID, test, j
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
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Accounts ')
    result = cursor.fetchall()
    for row in result:
        cdata = row[1]
        C2 = AES.new(key, AES.MODE_CBC, iv)
        plainname = unpad(C2.decrypt(cdata), 16)
        data = row[2]
        C3 = AES.new(key, AES.MODE_CBC, iv)
        plainpass= unpad(C3.decrypt(data),16)
        plainpass = plainpass.replace(b'\x00',b'')
        plainname = plainname.replace(b'\x00',b'')
        passw = plainpass.decode()
        name = plainname.decode()
        if (name == username) and (passw == password):
            account_ID = row[0]
            print(account_ID)
            print("yes")   
            test = "True"

    return test
        
@app.route('/confirm', methods = ['GET','POST'])
def confirm():
    global test
    if request.method == 'GET':
        print(test)
        return test       
        
    
@app.route('/menu', methods = ['GET','POST'])
def menu():
    return render_template('menu.html')


@app.route('/count', methods = ['GET','POST'])
def count():
    if request.method == 'GET':
        global account_ID, arr_ID, arr_data, counts
        conn = pyodbc.connect(con_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Passwords WHERE Account_ID=?",(account_ID))
        result = cursor.fetchall()
        if result:
            for row in result:
                arr_ID.append(row[0])
                arr_data.append(row[1])
                counts = counts + 1
            print(counts)
            return str(counts)
             
        return ""
        

@app.route('/call', methods = ['GET','POST'])
def call():
    global account_ID, arr_ID, arr_data, counts, i
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Acer\Documents\Coding\Web application project\Password Manager.accdb;'
    
    if request.method == 'GET':
        C2 = AES.new(key, AES.MODE_CBC, iv)
        plaindata = unpad(C2.decrypt(arr_data[i]), 16)
        i = i + 1
        k = plaindata.decode()
        return k
             
    return ""

@app.route('/save', methods = ['GET','POST'])
def save(): 

    data = request.get_json()
    newdata = data
    global account_ID, arrdat, i
    arrdat = newdata.split("~") 
    i = len(arrdat) 
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Acer\Documents\Coding\Web application project\Password Manager.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected to database")

    cursor = conn.cursor()
    cursor.execute('DELETE FROM Passwords WHERE Account_ID = ?',account_ID)
    conn.commit()
    print("Data Deleted")
    print(i)
    for j in range(i):
        cursor.execute('SELECT LAST(ID) FROM Passwords')
        lastID = cursor.fetchone()
        x = lastID[0] + 1
        C1 = AES.new(key, AES.MODE_CBC, iv)
        cipherdata = C1.encrypt(pad(arrdat[j].encode(),16))
        cursor.execute('INSERT INTO Passwords VALUES (?,?,?)', (x,cipherdata,account_ID))    
        conn.commit()
    
    return "True"
        
        

if __name__ =="__main__":
    app.run(debug=True)
    url_for('static',filename='static\js\SignUp.js')
    url_for('static',filename='static\js\Login.js')
    url_for('static',filename='static\js\menu.js')
    url_for('static',filename='static\js\index.js')
    url_for('static',filename='static\css\style.css')
    url_for('static',filename='static\images\LOGO(2).jpg')
    url_for('static',filename='static\images\logoo.jpg')
    url_for('static',filename='static\images\Logo2.jpg')
    url_for('static',filename='static\images\services.jpg')
    url_for('static',filename='static\images\contactUs.jpg')
    url_for('static',filename='static\images\instagram.jpg')
    url_for('static',filename='static\images\facebook.jpg')
    url_for('static',filename='static\images\tiktok.jpg')
    url_for('static',filename='static\images\twitter.jpg')

