#Completing a fuzzing loop:

#We are to implement a custom mutation operator along with a coverage metric operator (this operator will determines if there is a change/improvement in coverage metric when a turtle program is executed with mutated inputs.) for the fuzzer loop in `fuzzSubmission.py` file.

#Mainly 3 functions are to be implemented:

    • def compareCoverage
    • def mutate
    • def updateTotalCoverage


compareCoverage:
Takes in two arguments: curr_metric and total_metric
If  there comes any PC in curr_metric that is not in total_metric, return TRUE(Extra coverage gained and updateTotalCoverage will be called), else return FALSE

updateTotalCoverage:
Append any new statement covered in total_metric.

mutate:
Mutating the seed input in order to gain coverage by generating random values using randrange function.


#Installations:

sudo apt-get install graphviz graphviz-dev
pip install pygraphviz
pip install numpy
pip install networkx
pip install z3

#Running the program:
cd KachuaCore

./kachua.py -t 100 --fuzz TestCase/TestCase1.tl -d '{":x": 5, ":y": 100}'
