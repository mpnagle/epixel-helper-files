import json
import csv
import sys

if (len(sys.argv) < 2):
  print "json2csv needs a filename to run, i.e. 'python json2csv.py experiments.json'"

filename = sys.argv[1] #i.e. experiments.json
outputname = filename.split(".")[0] + ".csv"

file = open(filename)  
data = file.read()

dataByLine = data.split("\n")

file.close()


resultsArray = []
theFirstLine = [dataByLine[0],dataByLine[1]]


x = 0 

for line in dataByLine:

  #hackety way to avoide the newline that split produces at the end
  if len(line) < 4:
    continue
  
  lineJSON = json.loads(line)

  underscoreID = lineJSON['_id']


  photoURL = lineJSON['photoURL']
  userBarcode = lineJSON['userBarcode']
  dateCreated = lineJSON['dateCreated']
  coloniesCount = lineJSON['coloniesCountAtThisTime']
  colonyData = lineJSON['colonyData']


  header = [underscoreID,photoURL,userBarcode,dateCreated,coloniesCount]

  valuesArray = []
  
  
  resultsArrayByExperiment = []
  
  for colony in colonyData:

    IsValid = colony["IsValid"]
    X = colony["X"]
    Y = colony["Y"]
    ROI = colony["ROI"]
    N_in_clust = colony["N_in_clust"]
    Area = colony["Area"]
    Radius = colony["Radius"]
    Hue = colony["Hue"]
    Saturation = colony["Saturation"]
    Rmean = colony["Rmean"]
    Gmean = colony["Gmean"]
    Bmean = colony["Bmean"]
    Rsd = colony["Rsd"]
    Gsd = colony["Gsd"]
    Bsd = colony["Bsd"]
    ColorName = colony["ColorName"]
    NumberOfColoniesThisColor = colony["NumberOfColoniesThisColor"]
    Rarity = colony["Rarity"]
    colonyValues = [IsValid,X,Y,ROI,N_in_clust,Area,Radius,Hue,Saturation,Rmean,Gmean,Bmean,Rsd,Gsd,Bsd,ColorName,NumberOfColoniesThisColor,Rarity]

    row = header + colonyValues


    resultsArrayByExperiment.append(row)
  
  resultsArray.append(resultsArrayByExperiment)

csvHeader = ["_id","photoUrl","userBarcode","dateCreated","coloniesCountAtThisTime","IsValid","X","Y","ROI","N_in_clust","Area","Radius","Hue","Saturation","Rmean","Gmean","Bmean","Rsd","Gsd","Bsd","ColorName","NumberOfColoniesThisColor","Rarity"]

with open(outputname, 'wb') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter=',',
                         quotechar='"', quoting=csv.QUOTE_MINIMAL)
  csvwriter.writerow(csvHeader)
  for resultsArrayRow in resultsArray:
    for row in resultsArrayRow:
      csvwriter.writerow(row)


      
