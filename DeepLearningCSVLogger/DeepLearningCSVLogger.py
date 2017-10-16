#
# DeepLearningCSVLogger
#
# Summary: The aim of this code is to provide deep learning programmers the option of saving all (or some) the parameters used to build different neural networks and the results obtained in
# their datasets. This data storage will enable them to create a database with every model which has been tested and to perform comparison between different constructed models (with different 
# parameters).
#

import csv
import numpy as np
import sys
sys.path.insert(0, '/path/to/application/app/folder')


# Create CSV file with the column headers of interest
def createCSVFile(filePath, listOfHeaders):

  with open(filePath, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(listOfHeaders)

def addRowToCSVFile(path, newRow):

  csvfile = open(path, 'rb')
  spamreader = csv.reader(csvfile, delimiter=',')

  # row count
  data = list(spamreader)
  row_count = len(data)
  print row_count
       


