import json
import random

from flask import Flask, render_template, request, url_for, jsonify, json
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.dialects.mysql import MEDIUMTEXT

app = Flask(__name__)

# creade db variable using SQLAlchemy:::
# engine = create_engine('mysql+mysqlconnector://root:MyNewPass@localhost/courses')
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+mysqlconnector://root:PassWord123@localhost/courses"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# define table :::
class Course(db.Model):
    __tablename__ = "course_list"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    tech = db.Column(db.String(50))
    duration = db.Column(db.String(30))
    price = db.Column(db.Float)

    def Cousrse_list(self):
        return [self.id, self.title, self.tech, self.duration]


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(50))


@app.route("/")
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
    return render_template("/index.html", data=courseList)


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        details = request.form
        name = details["name"]
        email = details["email"]
        newUser = User(name=name, email=email)

        try:
            db.session.add(newUser)
            db.session.commit()

            query1 = text("set @num := 0")
            query2 = text("update user set id = @num := (@num+1)")
            db.session.execute(query1)
            db.session.execute(query2)
            db.session.commit()
            return f"sucessfully added new user", 201
        except Exception as e:
            db.session.rollback()
            return f"An error occurred : {str(e)}", 500

    return render_template("signup.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about/", methods=["POST", "GET"])
def about():
    return render_template("about.html")


@app.route("/signin")
def singin():
    if request.method == "POST":
        login_details = request.form
        email = login_details["email"]
        password = login_details["passwd"]
        # 1. if email match in database user list
        # 2. match paswword (hash type) also
        # 3. then redirect to index page or account page
        # 4. else redirect to singin html w/ flash message of
        # return redirect('/')
        # else:
    return render_template("/signin.html")


@app.route("/dashboard")
def dashboard():
    return render_template("/dashboard_admin.html")


@app.route("/course_details/<int:id>")
def course_details(id):
    course_bio = Course.query.filter_by(id=f"{id}").first()

    query2 = text(f"select distinct module_no,module from course_{id}_modules")
    data = db.session.execute(query2)
    modules = data.fetchall()

    query3 = text(f"select module,id,topics from course_{id}_modules")
    data2 = db.session.execute(query3)
    topics = data2.fetchall()

    db.session.commit()

    return render_template(
        "/product_description.html", course=course_bio, modules=modules, topics=topics
    )


@app.route("/update", methods=["POST", "GET"])
def update():
    # fetch form data:::
    if request.method == 'POST':
        title = request.form['title']
        tech = request.form['tech']
        duration = request.form['duration']
        price = request.form['price']
        print(title,tech,duration,price)
        return render_template('/course_CRUD.html')
    else:
        return render_template('/course_CRUD.html')


@app.route("/mockTest")
def mockTest():
    query = text(
        "select question,option_1,option_2,option_3,option_4 from study.general_knowledge order by rand() limit 5"
    )
    data = db.session.execute(query)
    ques_set = data.fetchall()

    db.session.commit()

    with open("test.json", "r") as f:
        data = json.load(f)
    temp_list = []

    for i in range(5):
        random_number = random.randint(1, 6)
        temp_list.append(random_number)

    ques_id_list = list(set(temp_list[:2]))

    Q_set = []
    for k in ques_id_list:
        for l in range(len(data)):
            if data[l]["id"] == k:
                Q_set.append(data[l]['Q'])
    
    Q_set = enumerate(Q_set)
    print(Q_set)
    return render_template("/mockTest.html", ques=Q_set)


@app.route("/submit")
def submission():
    return render_template("/submited.html")


@app.route("/course_details/<int:id>/<string:module>")
def module(id, module):

    query1 = text(
        f"select id,topics from course_{id}_modules where module like '{module}'"
    )
    data = db.session.execute(query1)
    topics = data.fetchall()

    return render_template("/course_content.html", module=module, topics=topics)


@app.route("/user/<int:id>")
def user_details(id):
    cur = mysql.connection.cursor()
    # write your user fetch sql code with cur at below:::
    cur.close()
    return render_template("/user_account.html", id=id)


@app.route("/user/<int:id>/profile")
def userProfile(id):
    cur = mysql.connection.cursor()
    # write your user fetch sql code with cur at below:::
    cur.close()
    return render_template("/userProfile.html", id=id)


@app.route("/test")
def test():
    return render_template("/test.html")

@app.route("/buy")
def buy_page():
    return render_template("/buy_page.html")


if __name__ == "__main__":
    app.run(debug=True)
