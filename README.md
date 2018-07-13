# Pharmacy_Counting

## Directory Structure of the repository

README.md 

run.sh
src

    pharmacy-counting.py

input

    itcont.txt

output

    top_cost_drug.txt

insight_testsuite

    run_tests.sh
        tests
            test_1
                input
                    itcont.txt
                output
                    top_cost_drug.txt
            test_2
                input
                    itcont.txt
                output
                    top_cost_drug.txt
                
The format of the input file (itcont.txt) is:

### id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500


The format for the output file (top_cost_drug.txt) is:
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300

### Problem Statement
Read the contents of the input file and generate a list of all drugs, the total number of UNIQUE individuals 
who prescribed the medication, and the total drug cost,listed in descending order based on the total drug 
cost and if there is a tie, drug name.

### pharmacy_counting.py
This script contains the code for solving the given problem. The script is well commented to understand the code. 



