#
# DeepLearningCSVLogger
#
# Summary: The aim of this code is to provide deep learning programmers the option of saving all (or some) the parameters used to build different neural networks and the results obtained in
# their datasets. This data storage will enable them to create a database with every model which has been tested and to perform comparison between different constructed models (with different 
# parameters).
#

import csv
import numpy as np

# Create CSV file with the column headers of interest
def createCSVFile(filePath, listOfHeaders):

  with open(filePath, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(listOfHeaders)

  csvfile.close()

def addRowToCSVFile(filePath, newRow):

  with open(filePath, 'a') as csvfile: # 'a' opens the file for appending; any data written to the file is automatically added to the end.
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(newRow)

  csvfile.close()


def readRowFromCSVFile(filePath, rowID):

  csvfile = open(filePath, 'rb')
  spamreader = csv.reader(csvfile, delimiter=',')

  names = spamreader.next()

  for row in spamreader:
    print row[0], rowID
    if float(row[0]) == float(rowID):
      return row[0], row[1], row[2]

  return -1, -1, -1
  




       


