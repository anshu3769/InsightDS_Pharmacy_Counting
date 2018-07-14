#!/bin/bash

#This script runs the python script which reads the input file and implement the desired features and store the result
#in the output file

touch ./output/top_cost_drug.txt 
python ./src/pharmacy_counting.py ./input/itcont.txt ./output/top_cost_drug.txt
