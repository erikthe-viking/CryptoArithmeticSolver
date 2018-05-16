# Erik Kirkegaard

# Crypto Arithmetic Solver

import sys
import numpy
from random import randint

class digit():
    # Used to represent each digit of the 3 different input strings
    char = "" #Char that is in the string
    valid_list = [0,0,0,0,0,0,0,0,0] # List of valid assignments using 9
    value = 0# value assigned to the charachter
    
    def __init__(self,x):
        self.char = x
        
    def __repr__(self):
        x = str(self.value)
        return self.char
    
    def set_val(self, num):
        if self.valid_list[num] == 0:
            self.valid_list[num] = 1
            value = num
        
class Adder():
  
    solution = "SUCCESS" # Solution to the problem
    add_1 = "TURING" # Additive 1
    add_2 = "TESTER" # Additive 2
    carry = 0 # Carry Variable
    size = 0 # Size of largest addend
    size_2 = 0 # Size of smalles adend
    max_size = 0
    
    test = []
    a1 = [] # list of digit objects assigned to Additive 1
    a2 = [] # list of digit objects assigned to Additive 2
    sol = []  # list of digit objects assigned to the Solution
    unique_list = [] # list of unique charachters
    unique_sol = []
    num_assigned = [] # List of numbers that are already assigned

    name = ""

    def __init__(self, x):
        self.name = x
    
    def take_user_input(self, input_1, input_2, goal):
        self.solution = goal
        self.add_1 = input_1
        self.add_2 = input_2
      
    def create_lists(self):
        
        for i in range(0,len(self.add_1)): # Breaks the first adder up by chars 
           a = digit(self.add_1[i])
           self.a1.append(a)
               
        for i in range(0,len(self.add_2)): # Breaks the second adder up by chars
           a = digit(self.add_2[i])
           self.a2.append(a)
        for i in range(0,len(self.solution)): #Breaks the solution up by chars
           a = digit(self.solution[i])
           self.sol.append(a)

        if len(self.a2) > len(self.a1):
            self.size = len(self.a2)
            self.size_2 = len(self.a1)
        else:
            self.size = len(self.a1)
            self.size_2 = len(self.a2)

        if len(self.sol) < len(self.a1) or len(self.sol) < len(self.a2):
            return "Not a Valid Answer"

       

      
    def find_unique_chars(self):

        for i in range(0,self.size):

            if i < len(self.a1) and i < len(self.a2):
                if self.a1[i].char == self.a2[i].char:
                    self.unique_list.append(self.a1[i])
                else:
                    x = False
                    a = False
                    for j in range(0, len(self.unique_list)):
                        if self.a1[i].char == self.unique_list[j].char:
                            x = True
                        if self.a2[i].char == self.unique_list[j].char:
                            a = True
                    if x == False and i < len(self.a1):
                        self.unique_list.append(self.a1[i])
                    if a == False and i < len(self.a2):
                        self.unique_list.append(self.a2[i])
        
            elif i > len(self.a1):
                a = False
                for j in range(0, len(self.unique_list)):
                    if self.a2[i].char == self.unique_list[j].char:
                        a = True
                if a == False and i < len(self.a2):
                    self.unique_list.append(self.a2[i])
                    
            elif i > len(self.a2):
                x = False
                for j in range(0, len(self.unique_list)):
                    if self.a1[i].char == self.unique_list[j].char:
                        x = True
                if x == False and i < len(self.a1):
                    self.unique_list.append(self.a1[i])
                    
        for i in range(0,len(self.sol)):
            b = False
            for j in range(0,len(self.unique_sol)):
                if self.sol[i].char == self.unique_sol[j].char:
                        b = True
            if b == False:
                self.unique_sol.append(self.sol[i])
            #    print(self.unique_sol)

        # Checks to make sure that there are no more than 9 unique charachters
        self.test = self.test + self.unique_sol + self.unique_list
      
        counter = 0
        for i in range(0,len(self.unique_sol)):
            for j in range(0,len(self.unique_list)):
                if self.unique_sol[i].char == self.unique_list[j].char:
                    counter = counter + 1
                
        self.max_size = len(self.test) - counter

                    
  
    def assign_values(self):
        
        if self.max_size > 9:
            print("INVALID INPUT number is too large!")
            print()
       
        
        for i in range(0,9):
            if i < len(self.unique_list):
                if self.unique_list[i].value == 0:
                    b = False
                    for j in range(0,len(self.num_assigned)):
                        if i == self.num_assigned[j]:
                            b = True
                    if b == False:
                        if i == 0:
                            count = 1
                        else:
                            count = i
                        self.unique_list[i].value = count
                        self.num_assigned.append(count)
        
        self.Deduct()
        for i in range(0,len(self.a1)):
            for j in range(0,len(self.unique_list)):
                if self.unique_list[j].char == self.a1[i].char:
                    self.a1[i].value = self.unique_list[j].value
                    

        for i in range(0,len(self.a2)):
            for j in range(0,len(self.unique_list)):
                if self.unique_list[j].char == self.a2[i].char:

                    self.a2[i].value = self.unique_list[j].value
         
              
        for i in range(1,self.size):
            if i < len(self.sol):
                if i < len(self.a1) and i < len(self.a2):
                    if (self.a1[len(self.a1)-i].value + self.a2[len(self.a2)-i].value) <= 9:
                        self.sol[len(self.sol)-i].value = self.a1[len(self.a1)-i].value + self.a2[len(self.a2)-i].value + self.carry
                        self.carry = 0
                    else:
                        self.carry = 1
                        self.sol[len(self.sol)-i].value = self.a1[len(self.a1)-i].value + self.a2[len(self.a2)-i].value - 10

                if i > len(self.a1) and i < len(self.a2):
                    print("esketit")
                    if(self.a2[len(self.a2)-i].value) <= 9:
                        self.sol[len(self.sol)-i].value = elf.a2[len(self.a2)-i].value + self.carry
                        self.carry = 0
                    else:
                        self.carry = 1
                        self.sol[len(self.sol)-i].value = self.a2[len(self.a2)-i].value - 10
            
                if i < len(self.a1) and i > len(self.a2):
                    print("hello")
                    if self.a1[len(self.a1)-i].value <= 9:
                        self.sol[len(self.sol)-i].value = self.a1[len(self.a1)-i].value + self.carry
                        self.carry = 0
                    else:
                        self.carry = 1
                        self.sol[len(self.sol)-i].value = self.a1[len(self.a1)-i].value - 10
        
        for i in range(0,len(self.sol)):
            for j in range(1,self.size+1):
                if i < self.size and i < self.size_2:
                 #   if self.a1[len(self.a1)-i]
                    x = 0
                    
    def Deduct(self): # Uses heurstics to make deductions based on position and value

        # Checks to see if a letter at the same index is equal for solution and addends
        if self.a1[len(self.a1)-1].char == self.a2[len(self.a2)-1].char and self.a1[len(self.a1)-1].char == self.sol[len(self.sol)-1].char:
            self.a1[len(self.a1)-1].value = 0
            self.a1[len(self.a2)-1].value = 0
            self.a1[len(self.sol)-1].value = 0
    
            
        # Checks to see if the leading charachter is
        # equal to any other charachter in the addends
        # Sets the leading digit to 1 because there is not a sum of numbers less than 1000 that is superior to 1999
        b = False
        for i in range(0,len(self.a1)):
            if self.a1[i].char == self.sol[0].char:
                b = True   
        for i in range (0,len(self.a2)):
            if self.a2[i].char == self.sol[0].char:
                b = True
        if b == True:
            self.sol[0].value = 1
            
        for i in range(0,len(self.unique_sol)): #Update unique solution with updated values
            if self.unique_sol[i].char == self.sol[0].char:
                self.unique_sol[i].value = self.sol[0].value
                
 
    def run(self): # Runs All functions
        self.create_lists()
        self.find_unique_chars()
        self.assign_values()

        # Prints out Solutions for the problem
        for i in range(0,len(self.a1)):
            print("Addend 1: ",self.a1[i].char, self.a1[i].value)
        print()
        for i in range(0,len(self.a2)):
            print("Addend 2: ",self.a2[i].char, self.a2[i].value)
        print()
        for i in range(0,len(self.sol)):
            print("Solution: ",self.sol[i].char, self.sol[i].value)
       # print(self.sol[2].value)
        
        
def main():
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
    
    x = Adder("Name")
    x.take_user_input(arg1,arg2,arg3)
    x.run()
    

if __name__ == '__main__':
        main()
    
