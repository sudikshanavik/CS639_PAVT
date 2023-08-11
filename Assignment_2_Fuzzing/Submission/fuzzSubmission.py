from kast import kachuaAST
import sys
from z3 import *
sys.path.insert(0, "KachuaCore/interfaces/")
from interfaces.fuzzerInterface import *
sys.path.insert(0, '../KachuaCore/')
import random
from random import randint
from kast.kachuaAST import *
# Each input is of this type.
#class InputObject():
#    def __init__(self, data):
#        self.id = str(uuid.uuid4())
#        self.data = data
#        # Flag to check if ever picked
#        # for mutation or not.
#        self.pickedOnce = False
        
class CustomCoverageMetric(CoverageMetricBase):
    # Statements covered is used for
    # coverage information.
    def __init__(self):
        super().__init__()

    # TODO : Implement this
    def compareCoverage(self, curr_metric, total_metric):
        for i in curr_metric:
            if i not in total_metric:
                 return True
                 
        # must compare curr_metric and total_metric
        # True if Improved Coverage else False
        return False

    # TODO : Implement this
    def updateTotalCoverage(self, curr_metric, total_metric):
        for i in curr_metric:
            if i not in total_metric:
               total_metric.append(i)
        # Compute the total_metric coverage and return it (list)
        # this changes if new coverage is seen for a
        # given input.
        return total_metric
       
y=1000
class CustomMutator(MutatorBase):
    def __init__(self):
        pass

    # TODO : Implement this
    def mutate(self, input_data, coverageInfo, irList):
        # Mutate the input data and return it
        # coverageInfo is of type CoverageMetricBase
        # Don't mutate coverageInfo
        # irList : List of IR Statments (Don't Modify)
        # input_data.data -> type dict() with {key : variable(str), value : int}
        # must return input_data after mutation.
        #for i in irList:
        #    if(isinstance(i[0],kachuaAST.ConditionCommand)):
          #       print(type(i[0].cond) )
                # if type(i[0].cond)==BoolFalse :
                 #  print(i[0].cond.rexpr)
        
        for i in input_data.data.keys():
        
             if(input_data.data[i]==0):
                 input_data.data[i]=input_data.data[i]+1
            
             input_data.data[i]=1/input_data.data[i]+random.randrange(-y,y)
       
        return input_data


# Reuse code and imports from
# earlier submissions (if any)."'
