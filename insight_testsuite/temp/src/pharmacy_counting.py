
from decimal import Decimal
from collections import OrderedDict

class PharmacyData(object):
    def __init__(self):
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

    
    def isRecordValid(self,record):
        '''
        This method validates a record based on the project 
        requirements. 
        For current project, 
        a) Each record must have 5 fields which are 'id,prescriber_last_name,
        prescriber_first_name,drug_name,drug_cost'.
        
        b) id and drug_cost must be positive numbers. 
        
        c) prescriber_last_name,prescriber_first_name,drug_name must 
        be string values.
        
        Input parameter: record is in form of a comma seperated
        values of the fields
        
        Input: A record containing comma seperated fields
        Output: True/False based on validity of the record
        
        '''
        if record is not None: 
            fields = record.split(",")
        if len(fields) is not 5:
            return False
        elif self.isFieldANumber(fields[0]) is False: 
            return False
        elif self.isFieldANumber(fields[4]) is False:
            return False
        elif float(fields[0]) < 0: 
            return False
        elif float(fields[4]) < 0:
            return False
        else:
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
        print("Inside readAndProcessTheInputFile")
        inputFile = None
        print("Inside readAndProcessTheInputFile")
        try:
            inputFile = open(inputFilePath,"r")
        except (OSError, IOError) as exception:
            print("Error:File could not be opened. The exception details are:{}".format(exc))
            return False
        else:
            for line in inputFile:
                #If the record is valid, proceed further
                if self.isRecordValid(line):            
                    fields = line.split(",")
                    
                    #Initialize the precriber's count for a drug
                    uniquePrescribersCount = 1; 
                    
                    #If the drug_name already exists in the dictionary
                    if fields[3] in drugDictionary.keys(): 
                        Values = drugDictionary[fields[3]]
                        
                        #If the prescriber is new for the drug. First name and last name
                        # are not present already for the drug
                        if (fields[1] != Values[0]) or (fields[2] != Values[1]):
                            Values[2] = Values[2] + 1;
                            
                        #Update the total cost of the drug    
                        Values[3] = Decimal(Values[3]) + Decimal(fields[4])
                        
                        #Update the record in the dictionary
                        drugDictionary[fields[3]] = Values
                        
                    # The drug is new to the dictionary   
                    else:
                        drugDictionary[fields[3]] = [fields[1],fields[2],uniquePrescribersCount,Decimal(fields[4])]
                
        finally:
            if inputFile: 
                inputFile.close()


    def extractFieldsFromDictionary(self,drugDictionary):
        for key,values in drugDictionary.items():
            drugDictionary[key] = [values[2],int(values[3])]
        orderedDrugData = OrderedDict(sorted(drugDictionary.items(), key=lambda k: ((k[1][1],k[0])),reverse=True))
        return(orderedDrugData)        
    
    def dictionaryToOutputFile(self,drugDictionary):
        """
        This method saves the drug dictionary 
        into an output file
        """
        with open("output/top_cost_drug.txt", 'w') as file_handler:
            temp_str = "drug_name" + "," + "num_prescriber" + "," + "total_cost\n"
            file_handler.write(temp_str)
            for key,value in drugDictionary.items():
                temp_str = key + "," + str(value[0]) + "," + str(value[1])
                file_handler.write("{}\n".format(temp_str))


def main():
    #print("Number of fields in a record are ",args.num_fields)
    #print("Path for the input file is ", args.inputFile_path)
    #print("Path for the output file is ", args.outputFile_path)
    
    pharmacyDataObject = PharmacyData()
    
    drugDataDictionary = {}
    
    pharmacyDataObject.readAndProcessTheInputFile("input/itcont.txt",drugDataDictionary)
    orderedDrugData = pharmacyDataObject.extractFieldsFromDictionary(drugDataDictionary)
    pharmacyDataObject.dictionaryToOutputFile(orderedDrugData)


if __name__ == "__main__":
    #parser = argparse.ArgumentParser(description='Arguments to MainScript.')
    #parser.add_argument('--page_url', default='https://en.wikipedia.org/wiki/yoga',
    #               help='URL of the first wiki page to start downloading')
    #parser.add_argument('--num_pages', default=10, type=int,
    #               help='Number of Wiki pages to be downloaded')
    #parser.add_argument('--doc_num', default=1, type=int,
    #               help='Wiki doc number to be retieved from SQL database')
    #parser.add_argument('--pattern', default='pattern',
    #               help='Pattern to be searched in the database')
    #parser.add_argument('--num_pages_to_mongodb', default=5, type=int,
    #               help='Pages to be saved to mongodb from SQL db')
    #args = parser.parse_args()	
    main()

