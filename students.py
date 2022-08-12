from flask import redirect, render_template, request, Blueprint
from classes import Student, StudentDatabase
import random

students = Blueprint("students", __name__, static_folder="static", template_folder="templates")

userdataFILE = "C:\\Users\\Tushar Ray\\OneDrive\\Desktop\\PythonFiles\\FlaskFiles\\dataOfUser.txt"
studentData = "C:\\Projects\\flaskSite\\studentList.csv"


@students.route("/")
def students_default():
    return render_template("studentsDirectory.html")


@students.route("/createstudents")
def studentcreate():
    return render_template("createnewstudent.html")


@students.route("/createstudentredirect", methods = ["POST"])
def studentcreateredirect():
    fname = request.form["firstname"]
    lname = request.form["lastname"]
    gender_type = request.form["gender"]
    location = request.form["address"]
    study = request.form["major"]

    id_list = random.sample(range(1, 10), 7)
    id_number = str(id_list[0]) + str(id_list[1]) + str(id_list[2]) + str(id_list[3]) + str(id_list[4]) + str(id_list[5]) + str(id_list[6])

    newStudent = Student(fname, lname, gender_type, location, study, id_number)

    studentFile = StudentDatabase(studentData)

    students = studentFile.readStudents()

    found = False

    for student in students:
        if newStudent.getFirstName() == student.getFirstName() and newStudent.getLastName() == student.getLastName() and newStudent.getGender() == student.getGender() and newStudent.getAddress() == student.getAddress() and newStudent.getMajor() == student.getMajor():
            found = True
            break

    if not found:
        students.append(newStudent)
        studentFile.writeStudents(students)

    return redirect("/students/studenttable")


@students.route("/studenttable", methods=["GET"])
def student_table():

    studentFile = StudentDatabase(studentData)
    allStudents = studentFile.readStudents()

    return render_template("studenttable.html", studentlist = allStudents)


@students.route("/deletestudent")
def delete_student():
    formfirstname = request.args.get("firstname")
    formlastname = request.args.get("lastname")
    formgender = request.args.get("gender")
    formaddress = request.args.get("address")
    formfield = request.args.get("major")
    formID = request.args.get("id")

    studentToBeDeleted = Student(formfirstname, formlastname, formgender, formaddress, formfield, formID)

    return render_template("deletestudentsure.html", htmlstudentinfo = studentToBeDeleted)


@students.route("/deletestudentredirect", methods=["POST"])
def delete_student_redirect():
    response = request.form["yesOrNo"].strip()
    if response == "yes":
        formID = request.form["id"].strip()

        newList = []
        dbstudent = StudentDatabase(studentData)
        students = dbstudent.readStudents()

        for student in students:

            if student.getID() == formID:
                continue

            newList.append(student)

        dbstudent.writeStudents(newList)

    else:
        return redirect("/students/studenttable")

    return redirect("/students/studenttable")


@students.route("/updatestudent")
def update_student():

    formfirstname = request.args.get("firstname").strip()
    formlastname = request.args.get("lastname").strip()
    formgender = request.args.get("gender").strip()
    formaddress = request.args.get("address").strip()
    formmajor = request.args.get("major").strip()
    formID = request.args.get("id").strip()

    singleStudent = Student(formfirstname, formlastname, formgender, formaddress, formmajor, formID)

    return render_template("updatestudent.html", htmlstudentinfo = singleStudent)


@students.route("/updatestudentredirect", methods=["POST"])
def update_student_redirect():
    formfirstname = request.form["firstname"].strip()
    formlastname = request.form["lastname"].strip()
    formgender = request.form["gender"].strip()
    formaddress = request.form["address"].strip()
    formmajor = request.form["major"].strip()
    formID = request.form["id"].strip()

    studentUpdated = Student(formfirstname, formlastname, formgender, formaddress, formmajor, formID)

    dbstudent = StudentDatabase(studentData)
    students = dbstudent.readStudents()

    for student in students:

        if student.getID() == formID:

            student.setFirstName(studentUpdated.getFirstName())
            student.setLastName((studentUpdated.getLastName()))
            student.setGender((studentUpdated.getGender()))
            student.setAddress((studentUpdated.getAddress()))
            student.setMajor((studentUpdated.getMajor()))
            break

    dbstudent.writeStudents(students)

    return redirect("/students/studenttable")
