from datetime import timedelta
from helperFunctions import checkIfInconclusive, checkIfOvertime, checkIfWeekend, presentTime

def dataToFile(data, fileName):
    f = open(fileName, "w")
    for year in data:   
        for weekNo in year:
            workTimeSum = timedelta(days = 0, seconds=0, minutes=0, hours=0)
            dayJob = timedelta(hours = 8*len(year[weekNo])).total_seconds()
        
            for index, dayNo in enumerate(year[weekNo]):
                workTime = dayNo[-1].date - dayNo[0].date
                inconclusive = checkIfInconclusive(dayNo[0].event, dayNo[-1].event)
                state =""
                for element in dayNo:
                    #print(element.gate)
                    if(element.gate == "E/2/KD1/4-8"):
                        state = "critical"
                #print("##") 

                if not (index == len(year[weekNo])-1):
                    f.write(f'Day {dayNo[0].date.date()} Work {workTime}{checkIfWeekend(dayNo[0].date)}{checkIfOvertime(workTime.total_seconds())}{inconclusive}{state}\n')
                else:
                    f.write(f'Day {dayNo[0].date.date()} Work {workTime}{checkIfWeekend(dayNo[0].date)}{checkIfOvertime(workTime.total_seconds())}{inconclusive}{state} ')

                workTimeSum += workTime

            allSeconds = workTimeSum.total_seconds()
            sign = '-' if (allSeconds - dayJob) < 0 else ''
            extraHours = abs(allSeconds - dayJob)

            presentWorkTime = presentTime(allSeconds)
            presentExtraTime = presentTime(extraHours)

            f.write(f'{presentWorkTime[0]:02d}:{presentWorkTime[1]:02d}:{presentWorkTime[2]:02d} {sign}{presentExtraTime[0]:02d}:{presentExtraTime[1]:02d}:{presentExtraTime[2]:02d}\n')

    f.close()
    return   
