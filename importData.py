from workLogs import WorkLogs
from helperFunctions import convertStringToData
import csv

def getData(csvFile):
    newData = []
    try:
        with open(csvFile, 'r', encoding='utf-8-sig') as file:  
            next(file)
            reader = csv.reader(file, delimiter = ';')
            for row in reader:
                newData.append(WorkLogs(convertStringToData(row[0]),row[1], row[2]))
    except FileNotFoundError:
        print('Could not open file')
        raise SystemExit
    except:
        print('Invalid file')
        raise SystemExit

    ##--sort data--##
    newData.sort(key = lambda x: x.date, reverse = False)
    ##-------------##
    return newData 

def organiseData(data):
    logsDict = {}
    week = []
    day = []
    listOfYears = []
    currentYear = data[0].date.year
    currentWeek = data[0].weekNumber()
    currentDay = data[0].date.date()

    for log in data:
        if log.weekNumber() == currentWeek:
            if log.date.date() == currentDay:
                day.append(log)
            else:
                currentDay = log.date.date()
                week.append(day)
                day = []
                day.append(log)
        else:
            week.append(day)
            logsDict[currentWeek] = week
            week = []
            day = []
            currentWeek = log.weekNumber()
            if currentWeek == 1 or (currentYear != log.date.year and currentWeek > 1):
                listOfYears.append(logsDict)
                currentYear = log.date.year
                logsDict = {}   
            currentDay = log.date.date()
            day.append(log)

    week.append(day)
    logsDict[currentWeek] = week
    listOfYears.append(logsDict)

    return listOfYears
