from importData import getData, organiseData
from saveToFile import dataToFile

newData = getData("data.csv")       
organisedData = organiseData(newData) 
dataToFile(organisedData, "result")

