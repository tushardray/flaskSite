class Student:

    def __init__(self, firstname, lastname, gender, address, major, idnum):
        self.__firstname = firstname.strip()
        self.__lastname = lastname.strip()
        self.__gender = gender.strip()
        self.__address = address.strip()
        self.__major = major.strip()
        self.__idnum = idnum.strip()

        # GET CLASSES

    def getFirstName(self):
        return self.__firstname

    def getLastName(self):
        return self.__lastname

    def getGender(self):
        return self.__gender

    def getAddress(self):
        return self.__address

    def getMajor(self):
        return self.__major

    def getID(self):
        return self.__idnum

        # SET CLASSES

    def setFirstName(self, updatedFirstName):
        self.__firstname = updatedFirstName

    def setLastName(self, updatedLastName):
        self.__lastname = updatedLastName

    def setGender(self, updatedGender):
        self.__gender = updatedGender

    def setAddress(self, updatedAddress):
        self.__address = updatedAddress

    def setMajor(self, updatedMajor):
        self.__major = updatedMajor

    # DON'T PUT A SET ID - I DON'T WANT THAT VALUE TO CHANGE.

    def __str__(self):
        return self.__firstname + self.__lastname + self.__gender + self.__address + self.__major + self.__idnum










class StudentDatabase:

    def __init__(self, filename):
        self.csvfile = filename

    def readStudents(self):

        students = []
        with open(self.csvfile, "r") as file:
            fileLines = file.readlines()

            for line in fileLines:
                stripped_line = line.strip()
                if len(stripped_line) == 0:
                    continue
                singlePerson = stripped_line.split(",")
                studentObj = Student(singlePerson[0], singlePerson[1], singlePerson[2], singlePerson[3], singlePerson[4], singlePerson[5])
                students.append(studentObj)

        return students

    def writeStudents(self, studentsList):

        separator = ","
        listOfStrings = []

        with open(self.csvfile, "w") as file:
            for student in studentsList:
                studentString = separator.join(
                    [student.getFirstName(), student.getLastName(), student.getGender(), student.getAddress(),
                     student.getMajor(), student.getID()]
                )

                listOfStrings.append(studentString)
            fullStudents = "\n".join(listOfStrings) + "\n"
            file.write(fullStudents)




















class Match:
    def __init__(self, id, datePlayed, home_team, away_team, home_score, away_score, tournament, city, country, neutral):
        self.__id = id
        self.__datePlayed = datePlayed
        self.__home_team = home_team
        self.__away_team = away_team
        self.__home_score = home_score
        self.__away_score = away_score
        self.__tournament = tournament
        self.__city = city
        self.__country = country
        self.__neutral = neutral

    def getID(self):
        return self.__id

    def getDate(self):
        return self.__datePlayed

    def getHomeTeam(self):
        return self.__home_team

    def getAwayTeam(self):
        return self.__away_team

    def getHomeScore(self):
        return self.__home_score

    def getAwayScore(self):
        return self.__away_score

    def getTournament(self):
        return self.__tournament

    def getCity(self):
        return self.__city

    def getCountry(self):
        return self.__country

    def getNeutral(self):
        return self.__neutral