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

## pharmacy_counting.py
    This script contains the code for solving the given problem. The approach behind 
    solving the problem is as follows:

    1) Two dictionaries are maintained.
    Dictionary 1 -> One for storing the unique number of prescribers and total cost against a drug.
            Key = Drug Name
            Value = [Unique number of prescribers, total cost of the drug]
    Dictionay 2 -> One for maintaining a list of subscribers against each drug
            Key = Drug Name
            Value = List of subscribers by their id
            
            
    2) The input file is read line by line and the values in the dictionaries 
    are updated as follows:
        -> If the drug in new to the dictionary
            a)Initialize the prescribers count to 1 
            b)Store the prescibers count and drug cost against its name
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
                -> Update the count of the prescribers with lentgh of the list against that 
                drug in Dictionary 2.
     3) Sort the Dictionary 1 after all the entries are available in the dictionary
     4) Store the dictionary to the output file.
     
## Unit Testing



