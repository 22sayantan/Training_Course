from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure mysql database connection:::
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'MyNewPass'
app.config['MYSQL_DB'] = 'courses'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from course_list')
    data = cur.fetchall()
    cur.close()
    return render_template('/index.html',data= data)

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        details = request.form
        name = details['name']
        email = details['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO User(name,email) VALUES (%s,%s)',(name,email))
        mysql.connection.commit()
        cur.close()
        return 'sucess'
    return render_template('signup.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signin')
def singin():
    if request.method == 'POST':
        login_details = request.form
        email = login_details['email']
        password = login_details['passwd']
        cur =mysql.connection.cursor()
        if (cur.execute(f"select * from User where email = '{email}'")):
            mysql.connection.cursor()
            cur.close()
            return redirect('/contact')
        else:
            return render_template('/signin.html')

@app.route('/dashboard')
def dashboard():
    return render_template('/dashboard.html')

@app.route('/course_details/<int:id>')
def course_details(id):
    my_id = id
    cur = mysql.connection.cursor()
    cur.execute(f'select * from course_list where id = {id}')
    data2 = cur.fetchone()
    cur.execute(f'select * from course_{id}_modules')
    data3 = cur.fetchall()
    data3_list = list()
    for x in data3:
        # print(my_id)
        temp_data = list(x)
        data3_list.append(temp_data[:2])
    data4 = dict(data3_list)
    # print(data4)
    data5 = list(data4.keys())
    data6 = list(data4.values())
    print(data5,data6)
    data10 = {}
    for key in data5:
        # print(key)
        # print(data4[key])
        cur.execute(f'select topics from course_{my_id}_modules where module_no = {key}')
        data7 = cur.fetchall()
        data8 = list(data7)
        data9 = []
        for e in data8:
            # print(e)
            data9.append(e[0])
            data10[data4[key]] = data9
    # print(data9)
    # data5 = list()
    # for key in data4.keys():
    #     data5.append([key,data4[key]])
    cur.close()
    return render_template('/product_description.html',data2 =  data2,data4 = data4,data10 = data10)

@app.route('/update')
def update():
    return render_template('/course_CRUD.html')

if __name__ == '__main__':
    app.run(debug=True)