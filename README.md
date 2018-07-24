# Pharmacy_Counting

## Directory Structure of the repository

    |-README.md
    |-run.sh
    |-src
        |-pharmacy-counting.py
    |-input
        |-itcont.txt
    |-output
        |-top_cost_drug.txt
    |-insight_testsuite
        |-run_tests.sh
        |-tests
            |-test_1
                |-input
                    |-itcont.txt
                |-output
                    |-top_cost_drug.txt
            |-test_2
                |-input
                    |-itcont.txt 
                |-output
                    |-top_cost_drug.txt
                    
                
## The format of the input file (itcont.txt) is:

    id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
    1000000001,Smith,James,AMBIEN,100
    1000000002,Garcia,Maria,AMBIEN,200
    1000000003,Johnson,James,CHLORPROMAZINE,1000
    1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
    1000000005,Smith,David,BENZTROPINE MESYLATE,1500


## The format for the output file (top_cost_drug.txt) is:
     drug_name,num_prescriber,total_cost
    CHLORPROMAZINE,2,3000
    BENZTROPINE MESYLATE,1,1500
    AMBIEN,2,300

## Problem Statement
Read the contents of the input file and generate a list of all drugs, the total number of UNIQUE individuals 
who prescribed the medication, and the total drug cost,listed in descending order based on the total drug 
cost and if there is a tie, drug name.

## Approach to solve the problem
    This script contains the code for solving the given problem. The approach behind 
    solving the problem is as follows:

    1) Two dictionaries are maintained.
    Dictionary 1 -> for storing the unique number of prescribers and total cost against a drug.
            Key = Drug Name
            Value = [Unique number of prescribers, total cost of the drug]
    Dictionay 2 -> for maintaining a list of prescribers against each drug
            Key = Drug Name
            Value = List of subscribers by their id
            
    2) The input file is read line by line and the values in the dictionaries 
    are updated as follows:
        -> If the record is valid (validity checks like number of fields in the record 
           are correct, drug cost and id are numbers not strings, last name, first name, drug
           names are strings etc)
            -> If the drug in new to the dictionary
                a)Initialize the prescribers count to 1 
                b)Store the prescribers count and drug cost against its name
                in Dictionary 1
                c) Store the prescribers id against the drug name in Dictionary 2.
                
           Point to be noted = First name and last name of two prescribers can be 
                same but the id must be unique.
            
            -> If the drug already exists
                a)Check if the prescribers id is present in the list of ids against that 
                drug name in Dictionary 2.
                    -> If present, do nothing
                    -> If not present, add the id to the list of prescribers in Dictionary 2
                    -> Update the cost of the drug in Dictionary 1
                    -> Update the count of the prescribers with length of the list against that 
                    drug in Dictionary 2.
     3) Sort the Dictionary 1 after all the entries are available in the dictionary
     4) Store the dictionary to the output file.
     
## Running instructions
     1. Copy the input file in the input/ directory. The format for the input file has been specified above.
     2. Run the run.sh script with path to input file and output file as its arguments. There are two commands
        in the script - 
         touch ./output/top_cost_drug.txt 
         python ./src/pharmacy_counting.py ./input/itcont.txt ./output/top_cost_drug.txt
     where top_cost_drug.txt is the name of the output file and input/itcont.txt is the name of the input
     file. Replace these names with the names of your output and input file names.
          
            Troubleshooting
                a) If the user does not have permission to execute the script.
                    Execute the command "chmod 755 run.sh" to give the user permission to execute the script.
     3. The script will execute the pharmacy_counting.py script. An output file will be generated
      at the path specified in the arguments to the run.sh script.
     
## Test Cases identified and tested
        1) Check for the path of input and output files given to the run.sh script as parameters
           If any of the path does not exist, the program exits.
            TESTED
        2) Enter less/more number of fields in any record than specified for the problem
           (number of fields is 5 for current problem). That record will not be counted as valid data.
            TESTED
        3) Use a non-numeric value as drug_cost. That record will not be counted as valid data.
            TESTED
        4) Use a non-numeric value as prescribers id. That record will not be counted as valid data.
            TESTED
        5) Use negative values for drug_cost and/or prescribers id. The record will not be counted as
            valid data.
            TESTED
            
## Test cases that can be further added if more information is provided 
        1) First name and last name of the prescribers must be string ( if its a condition)
        2) If the drug name is correct. It can be checked against a correct drug name list.
   
        Duplicate records can be removed first. It will require to read the data and store in a dictionary
        New data will be checked against existing data in the dictionary. This dictionary will be further 
        used for producing the final output file.



