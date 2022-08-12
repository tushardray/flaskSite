from flask import Flask, url_for, redirect, render_template, request
from students import students
from about import about
from databases import databases
from flask_bootstrap import Bootstrap


flaskProgram = "C:\\Users\\Tushar Ray\\OneDrive\\Desktop\\PythonFiles\\FlaskFiles\\flaskProgram.txt"
userdataFILE = "C:\\Users\\Tushar Ray\\OneDrive\\Desktop\\PythonFiles\\FlaskFiles\\dataOfUser.txt"
studentData = "C:\\Users\\Tushar Ray\\environment1\\Scripts\\studentList.csv"

# Next: Optimize website for smaller screens
# After? Betting / predictions / logins / put table in window within site

app = Flask(__name__)
Bootstrap(app)

app.register_blueprint(students, url_prefix="/students") # Whatever goes in url_prefix is the first route in the url.
app.register_blueprint(about, url_prefix="/about")
app.register_blueprint(databases, url_prefix="/databases")

@app.route("/")
def home_page():
    return render_template("homepage.html")

# @app.route("/file")
# def flask_file():
#     return str(file_finder(flaskProgram))

# def file_finder(filename):
#     with open(filename, "r") as file:
#         contents = file.readlines()
#     return contents

# @app.route("/query")
# def firstquery():
#     formname = request.args.get("firstname") # The string is the key and value is provided in the url, then stored in the args variable
#     formage = request.args.get("age")
#     return render_template("extendedlink.html", name=formname, age=formage)

# To change port, run: flask run --port=(port number)



if __name__ == '__main__':
    app.run()