# I'm use to JavaScript which initially I wrote up a code example which would've worked in JS
# but not in python which afterwards I had to change to fit the functionality of the lang being used.
# to answer the question, yes it would've been easier to write this in JS compared to Python as I'm use to the syntax of JS



# Functional Programming is a helpful paradigm when solving this problem as if we were sorting thorugh more private information
# the functions would've helped mas the data being sorted through rather than displaying it globally

##                  Object Oriented Programming
# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing 
# an Object Oriented solution according to the following criteria.
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)
  
    def boost(self):
        self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)
  
    def flame_jet(self,other):
        other.condition = "trashed"


print(AnakinsPod)
print(SebulbasPod)