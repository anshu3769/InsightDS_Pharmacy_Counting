
#This program takes an input file with fields -id,prescriber_last_name,
#prescriber_first_name,drug_name,drug_cost  and return the drugs list with 
#the number of their unique prescribers and total cost on those drugs in an 
#output file.  

import argparse
import sys
import os

from decimal import Decimal
from collections import OrderedDict

class PharmacyData(object):
    def __init__(self):
        self.numberOfFieldsInARecord = 0
        self.id_index = 0
        self.prescribers_last_name_index = 0
        self.prescribers_first_name_index = 0
        self.drug_name_index = 0
        self.drug_cost_index = 0
        
        pass
    
    def isFieldANumber(self,x):
        '''
        This method checks if a given string is
        a number or not. e.g. for isFieldANumber('1234.67')
        will return true, while isFieldANumber('abc')
        will return false.
        
        Input: a string named x
        Output: True/False indicating the string is a number or not
        '''
        try:
            float(x)
            return True
        except ValueError:
            return False

    def setVariablesForTheDataSet(self):
        '''
        This method sets the variables required 
        for this problem. These variables are:
        a)Number of fields in a record
            -> Currently, a valid record contains 5 fields namely
               id, prescriber_last_name, prescriber_first_name, drug_name, drug_cost
        b) Location of the fields in a record
        These variables will be required while reading the input file.
        In future, if some new fields are added in a record or index of any field changes,
        single change in this method will update the values in all the methods
        where these variables are used.
        '''
        self.numberOfFieldsInARecord = 5
        self.id_index = 0
        self.prescribers_last_name_index = 1
        self.prescribers_first_name_index = 2
        self.drug_name_index = 3
        self.drug_cost_index = 4
       
    
    def isRecordValid(self,record):
        '''
        This method validates a record based on the project 
        requirements. 
        For current project,
        a) Each record must have number of fields equal to 
         numberOfFieldsInARecord
        
        b) id and drug_cost must be positive numbers. 
        
        c) prescriber_last_name,prescriber_first_name,drug_name must 
        be string values.
        
        Input: A record containing comma seperated fields
        Output: True/False based on validity of the record
        
        '''
        if record is None:
            print("Exit isRecordValid method -->")
            return False
        else: 
            fields = record.split(",")
            if len(fields) is not self.numberOfFieldsInARecord:
                return False
            if self.isFieldANumber(fields[self.id_index]) is False: 
                return False
            if self.isFieldANumber(fields[self.drug_cost_index]) is False:
                return False
            if float(fields[self.id_index]) < 0: 
                return False
            if float(fields[self.drug_cost_index]) < 0:
                return False
        return True
        
        
    def readAndProcessTheInputFile(self,inputFilePath,drugDictionary):
        '''
        This method reads the input file, extracts the records 
        line by line and stores them in a dictionary after the 
        processing. 
        The drug_name acts as the key. The values for a
        key is a list of prescriber_last_name,prescriber_first_name,
        count of the unique prescribers and total cost of the drug.
        
        The prescriber's last and first name are kept in dictionary 
        to count the unique prescribers for that drug. These two fields
        will be removed in further processing.
        
        Input: inputFilePath is the path with filename in it
                drugDictionary is for storing the intermediate
                result
        Output: drugDictionary with intermdediate results       
        '''
        print("<--Enter readAndProcessTheInputFile method")
        inputFile = None
        try:
            inputFile = open(inputFilePath,"r")
        except (OSError, IOError) as exception:
            print("Error:File could not be opened. The exception details are:{}".format(exc))
            print("Exit readAndProcessTheInputFile method-->")
            return False
        else:
            for line in inputFile:
                #If the record is valid, proceed further
                if self.isRecordValid(line):            
                    fields = line.split(",")
                    
                    #Initialize the precriber's count for a drug
                    uniquePrescribersCount = 1; 
                    
                    #If the drug_name already exists in the dictionary
                    if fields[self.drug_name_index] in drugDictionary.keys():
  			key = fields[self.drug_name_index] 
                        Values = drugDictionary[fields[self.drug_name_index]]
                        
                        #If the prescriber is new for the drug. First name and last name
                        # are not present already for the drug
                        if (fields[self.prescribers_last_name_index] != Values[0]) or (fields[self.prescribers_first_name_index] != Values[1]):
                            Values[2] = Values[2] + 1;
                            
                        #Update the total cost of the drug    
                        Values[3] = Decimal(Values[3]) + Decimal(fields[self.drug_cost_index])
                        
                        #Update the record in the dictionary
                        drugDictionary[key] = Values
                        
                    # The drug is new to the dictionary   
                    else:
                        drugDictionary[fields[self.drug_name_index]] = [fields[self.prescribers_last_name_index],fields[self.prescribers_first_name_index],uniquePrescribersCount,Decimal(fields[self.drug_cost_index])]
                
        finally:
            if inputFile: 
                inputFile.close()
		print("Exit readAndProcessTheInputFile method-->")


    def extractFieldsFromDictionary(self,drugDictionary):
	'''
	This method refines the dictionary to contain
	only the required fields and sorts the dictionary
	based on total cost of the drugs in descending order first
	and if their is a tie, then drug name is used.
	'''

        print("<--Enter extractFieldsFromDictionary  method")
        orderedDrugDictionary = {}
        for key,values in drugDictionary.items():
            drugDictionary[key] = [values[2],int(values[3])]
        orderedDrugDictionary = OrderedDict(sorted(drugDictionary.items(), key=lambda k: ((k[1][1],k[0])),reverse=True))
        print("Exit extractFieldsFromDictionary  method-->")
        return(orderedDrugDictionary)        
    
    def dictionaryToOutputFile(self,drugDictionary,outputFilePath):
        '''
        This method saves the drug dictionary 
        into an output file
        '''
        print("<--Enter dictionaryToOutputFile  method")
        with open(outputFilePath, 'w') as file_handler:
            temp_str = "drug_name" + "," + "num_prescriber" + "," + "total_cost\n"
            file_handler.write(temp_str)
            for key,value in drugDictionary.items():
                temp_str = key + "," + str(value[0]) + "," + str(value[1])
                file_handler.write("{}\n".format(temp_str))
        print("Exit dictionaryToOutputFile  method-->")


def main():

    #Check if the input and output file paths exist 
    inputFilePath = sys.argv[1]
    outputFilePath = sys.argv[2]

    if os.path.exists(inputFilePath):
        print("Input file path exists. Program continues")
    else:
        print("Input file path does not exist on the system. Program exits")
        return None

    
    if os.path.exists(outputFilePath):
        print("Output file path exists. Program continues")
    else:
        print("Output file path does not exist on the system. Program exits")
        return None
    
    #Create an object of the PharmacyData class
    pharmacyDataObject = PharmacyData()
    
    #Initialize the variables of the object
    pharmacyDataObject.setVariablesForTheDataSet()

    #Initialize empty drug dictionary.     
    drugDataDictionary = {}
    
    # Process the input file and store the result in the output file.
    pharmacyDataObject.readAndProcessTheInputFile(inputFilePath,drugDataDictionary)
    orderedDrugDataDictionary = pharmacyDataObject.extractFieldsFromDictionary(drugDataDictionary)
    pharmacyDataObject.dictionaryToOutputFile(orderedDrugDataDictionary,outputFilePath)


if __name__ == "__main__":
    main()

