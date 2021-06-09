from datetime import datetime, timedelta

def convertStringToData(stringData):
    dtString = stringData.strip()
    dtObject = datetime.strptime(dtString, "%Y-%m-%d %H:%M:%S")
    return dtObject

def presentTime(seconds):
    hours = int(seconds/3600)
    minutes = int((seconds - hours*3600)/60)
    seconds = int(seconds - hours*3600 - minutes*60)
    return [hours, minutes, seconds]

def checkIfOvertime(time):
    minV = timedelta(hours = 6).total_seconds()
    maxV = timedelta(hours = 9).total_seconds()

    if time > maxV:
        return " ot"
    elif time < minV:
        return " ut"
    else:    
        return ""
    
def checkIfInconclusive(firstEvent, lastEvent):
    return "" if ("entry" in firstEvent) and ("exit" in lastEvent) else " i"

def checkIfCritical(event):
    return "E/2/KD1/4-8" if event == "E/2/KD1/4-8" else ""


def checkIfWeekend(day):
    return " w" if day.isoweekday() > 5 else ""

