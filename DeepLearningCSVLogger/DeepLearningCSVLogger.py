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

def countNumberOfRowsInCSVfile(filePath):
    
  csvfile = open(filePath, 'rb')
  spamreader = csv.reader(csvfile, delimiter=',')
  row_count = len(list(spamreader))-1 # DO NOT COUNT HEADER ROW
  
  return row_count

def saveEpochMetricsToCSV(filePath, training_accuracy, training_loss, validation_accuracy, validation_loss):
    
  numEpochs = len(training_accuracy)
    
  with open(filePath, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    
    # Generate Headers
    listOfHeaders = ['METRIC'] # 'TRAIN ACC', 'TRAIN LOSS', 'VAL ACC', 'VAL LOSS', 'LR']
    row_TrainAcc = ['TRAIN_ACC']
    row_TrainLoss = ['TRAIN_LOSS']
    row_ValAcc = ['VAL_ACC']
    row_ValLoss = ['VAL_LOSS']
    #row_LR = ['LR']
    for i in range(numEpochs):
      listOfHeaders.append('EPOCH_' + str(i+1))
      row_TrainAcc.append(training_accuracy[i])
      row_TrainLoss.append(training_loss[i])
      row_ValAcc.append(validation_accuracy[i])
      row_ValLoss.append(validation_loss[i])
      #row_LR.append(learning_rate[i])
        
    writer.writerow(listOfHeaders)
    writer.writerow(row_TrainAcc)
    writer.writerow(row_TrainLoss)
    writer.writerow(row_ValAcc)
    writer.writerow(row_ValLoss)
    #writer.writerow(row_LR)
    
    csvfile.close()




       


