from flask import Flask,render_template,request,url_for,jsonify,json
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import MEDIUMTEXT

app = Flask(__name__)

# creade db variable using SQLAlchemy:::
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:MyNewPass@localhost/courses'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure mysql database connection:::
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'MyNewPass'
# app.config['MYSQL_DB'] = 'courses'

# mysql = MySQL(app)

# define table :::
class Course(db.Model):
    __tablename__ = 'course_list'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(50))
    tech = db.Column(db.String(50))
    duration = db.Column(db.String(30))
    price = db.Column(db.Float)

@app.route('/')
def index():
    courses = Course.query.all()
    courseList = []
    for course in courses:
        courseDict = {}
        courseDict["id"] = course.id
        courseDict["title"] = course.title
        courseDict["tech"] = course.tech
        courseDict["duration"] = course.duration
        courseDict["price"] = course.price
        courseList.append(courseDict)
    return render_template('/index.html',data = courseList)

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        details = request.form
        name = details['name']
        email = details['email']
        print(name,email)
        # cur = mysql.connection.cursor()
        # cur.execute('INSERT INTO User(name,email) VALUES (%s,%s)',(name,email))
        # mysql.connection.commit()
        # cur.close()
        # return 'sucess'
    return render_template('signup.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about/',methods=['POST','GET'])
def about():
    cur = mysql.connection.cursor()
    cur.execute('select title from course_list')
    title_list = cur.fetchall()
    cur.close()

    if 'title' in request.form:
        title = request.form['title']
        tech = request.form['tech']
        duration = request.form['duration']
        price = request.form['price']
        print(title,tech,duration,price)

    elif 'module_no' in request.form:
        module_no = request.form['module_no']
        module = request.form['module']
        topics = request.form['topics']
        course = request.form['course']
        print(module_no,module,topics,course)

    return render_template('about.html',titles = title_list)

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
    price = format(data2[4],'.2f')
    cur.execute(f'select * from course_{id}_modules')
    data3 = cur.fetchall()
    data3_list = list()
    for x in data3:
        # print(my_id)
        temp_data = list(x)
        data3_list.append(temp_data[:2])
    data4 = dict(data3_list)
    data5 = list(data4.keys())
    data6 = list(data4.values())
    data10 = {}
    for key in data5:
        cur.execute(f'select topics from course_{my_id}_modules where module_no = {key}')
        data7 = cur.fetchall()
        data8 = list(data7)
        data9 = []
        for e in data8:
            data9.append(e[0])
            data10[data4[key]] = data9
    print(data10)
    cur.close()
    return render_template('/product_description.html',data2 =  data2,data4 = data4,data10 = data10,price = price)

@app.route('/update',methods=['POST','GET'])
def update():
    # fetch form data:::
    if request.method == 'POST':
        form_data = request.form
        title = form_data['title']
        tech = form_data['tech']
        duration = form_data['duration']
        price = form_data['price']
        # create mysql cursor:::
        cur = mysql.connection.cursor()
        
        # execute query::
        cur.execute('INSERT INTO courses.course_list (title,tech,duration,price) values (%s,%s,%s,%s)',(title,tech,duration,price))
        # make changes sql query::::
        mysql.connection.commit()

        cur.execute('SELECT COUNT(*) as ROW_COUNT FROM course_list')
        count = cur.fetchone()
        
        cur.execute(f'CREATE TABLE course_{count[0]}_modules (module_no int,module varchar(30),id int primary key auto_increment,topics varchar(100))')
        mysql.connection.commit()
        # close cursor::::
        cur.close()
        # return success:::
        return f'{count[0]} no Course created Successfully! '
    return render_template('/course_CRUD.html')

@app.route('/mockTest')
def mockTest():
    cur = mysql.connection.cursor()
    cur.execute('SELECT questions,topics from study.interview_questions order by rand() limit 8')
    data = list(cur.fetchall())
    cur.close()
    ques = list()
    topics =list()
    for i in data:
        ques.append(i[0])
        topics.append(i[1])
    return render_template('/mockTest.html', ques = ques, topics = topics)

@app.route('/submited')
def submission():
    return render_template('/submited.html')

@app.route('/course_details/<int:id>/<string:module>')
def module(id,module):
    cur = mysql.connection.cursor()
    cur.execute(f'select * from courses.course_{id}_modules where module = "{module}"')
    data = cur.fetchall()
    cur.close()
    return render_template('/course_content.html',data = data ,module = module)

@app.route('/user/<int:id>')
def user_details(id):
    cur = mysql.connection.cursor()
    # write your user fetch sql code with cur at below:::
    cur.close()
    return render_template('/user_account.html',id = id)

@app.route('/user/<int:id>/profile')
def userProfile(id):
    cur = mysql.connection.cursor()
    # write your user fetch sql code with cur at below:::
    cur.close()
    return render_template('/userProfile.html',id = id)


@app.route('/test')
def test():
    return render_template('/test.html')
    
if __name__ == '__main__':
    app.run(debug=True)