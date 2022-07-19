from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user_form')
def new_user():
    return render_template('user.html')

@app.route('/list')
def list():
    con = sql.connect("database.db") #database.db파일에 접근.
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from users")

    rows = cur.fetchall()
    return render_template("list.html",rows = rows)


@app.route('/user_info',methods = ['POST', 'GET'])
def user_info():
    if request.method == 'POST':
        try:
            user_email = request.form['user_email']
            user_name = request.form['user_name']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO users (email, name) VALUES (?,?)",(user_email,user_name) )

                msg = "Success"

        except:
            con.rollback()
            msg = "error"

        finally:
            return render_template("result.html",msg = msg)
            con.close()