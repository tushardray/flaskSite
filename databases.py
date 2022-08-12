from flask import Flask, url_for, redirect, render_template, request, Blueprint, current_app
from flask_bootstrap import Bootstrap
import mysql.connector
from classes import Match

databases = Blueprint("databases", __name__, static_folder="static", template_folder="templates")

connector = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Test1234*",
    database="footballgames"
)


@databases.route("/footballmatches")
def footballMatches():
    cursor = connector.cursor()
    cursor.execute("SELECT * FROM matches ORDER BY datePlayed DESC LIMIT 50")

    newList = []

    for record in cursor:
        matchObject = Match(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9])
        newList.append(matchObject)

    cursor2 = connector.cursor()
    cursor2.execute("SELECT COUNT(*) FROM matches")

    for record in cursor2:
        totalNum = record[0]

    cursor.close()
    cursor2.close()

    connector.commit()

    return render_template("footballTable.html", datalist=newList, totalTableLength=totalNum)


@databases.route("/expandedfootballtable", methods=["POST"])
def expandedTable():
    newList = []

    cursorCounter = connector.cursor()
    cursorCounter.execute("SELECT count(*) FROM matches")
    for record in cursorCounter:
        totalNum = record[0]
        print(totalNum)

    showVal = request.form["showVals"]

    if showVal == "showAll":
        cursorFull = connector.cursor()
        cursorFull.execute("SELECT * FROM matches ORDER BY datePlayed DESC")

        for record in cursorFull:
            extraMatchObjects = Match(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                      record[7], record[8], record[9])
            newList.append(extraMatchObjects)

        cursorFull.close()

    elif showVal == "showHalf":

        half = int(totalNum / 2)

        cursorHalf = connector.cursor()
        cursorHalf.execute("SELECT * FROM matches ORDER BY datePlayed DESC LIMIT " + str(half))

        for record in cursorHalf:
            halfMatchObjects = Match(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                      record[7], record[8], record[9])
            newList.append(halfMatchObjects)

        cursorHalf.close()

    elif 0 < int(showVal) < int(totalNum):
            cursorCustom = connector.cursor()
            cursorCustom.execute("SELECT * FROM matches ORDER BY datePlayed DESC LIMIT " + showVal)

            for record in cursorCustom:
                extraMatchObjects = Match(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                          record[7], record[8], record[9])
                newList.append(extraMatchObjects)

            cursorCustom.close()

    else:
        print("ELSE IN ACTION. EMERGENCY")
        pass

    connector.commit()

    return render_template("expandedTable.html", datalist=newList, totalTableLength=totalNum)


@databases.route("/footballmatchesdelete")
def deleteMatch():

    formID = request.args.get("id")
    formDate = request.args.get("date")
    formHomeTeam = request.args.get("hometeam")
    formAwayTeam = request.args.get("awayteam")
    formHomeScore = request.args.get("homescore")
    formAwayScore = request.args.get("awayscore")
    formTournament = request.args.get("tournament")
    formCity = request.args.get("city")
    formCountry = request.args.get("country")
    formNeutrality = request.args.get("neutrality")

    matchObject = Match(formID, formDate, formHomeTeam, formAwayTeam, formHomeScore, formAwayScore, formTournament, formCity, formCountry, formNeutrality)

    return render_template("footballDeleteMatch.html", record = matchObject)


@databases.route("/deletematchredirect", methods=["POST"])
def deleteMatchRedirect():

    formID = request.form["id"].strip()
    cursor = connector.cursor()
    deleteQuery = "DELETE FROM matches WHERE id=" + str(formID)
    cursor.execute(deleteQuery)
    cursor.close()
    connector.commit()

    return redirect("/databases/footballmatches")


@databases.route("/footballmatchesedit")
def editMatches():

    formID = request.args.get("id")
    formDate = request.args.get("date")
    formHomeTeam = request.args.get("homeTeam")
    formAwayTeam = request.args.get("awayTeam")
    formHomeScore = request.args.get("homeScore")
    formAwayScore = request.args.get("awayScore")
    formTournament = request.args.get("tournament")
    formCity = request.args.get("city")
    formCountry = request.args.get("country")
    formNeutrality = request.args.get("neutrality")

    matchObject = Match(formID, formDate, formHomeTeam, formAwayTeam, formHomeScore, formAwayScore, formTournament, formCity, formCountry, formNeutrality)

    return render_template("footballEditMatch.html", matchInfo=matchObject)


@databases.route("/footballmatchesupdateredirect", methods=["POST"])
def editMatchesRedirect():

    cursor = connector.cursor()

    newDate = request.form["date"]
    newHomeTeam = request.form["homeTeam"].strip()
    newAwayTeam = request.form["awayTeam"].strip()
    newHomeScore = request.form["homeScore"]
    newAwayScore = request.form["awayScore"]
    newTournament = request.form["tournament"].strip()
    newCity = request.form["city"].strip()
    newCountry = request.form["country"].strip()
    newNeutrality = request.form["neutral"].strip()
    ID = request.form["id"]

    editQuery = '''\
            UPDATE matches SET datePlayed="{newDate}", home_team="{newHomeTeam}", 
            away_team="{newAwayTeam}", home_score={newHomeScore}, away_score={newAwayScore},
            tournament="{newTournament}", city="{newCity}", country="{newCountry}", 
            neutral="{newNeutrality}" where id={ID}
            '''.format(newDate=newDate, newHomeTeam=newHomeTeam, newAwayTeam=newAwayTeam,
                       newHomeScore=newHomeScore, newAwayScore=newAwayScore, newTournament=newTournament,
                       newCity=newCity, newCountry=newCountry, newNeutrality=newNeutrality, ID=ID)

    print(editQuery)

    cursor.execute(editQuery)

    cursor.close()

    connector.commit()

    return redirect("/databases/footballmatches")
