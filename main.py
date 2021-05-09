from package.decimalBase import *
from package.codeBase import *

def main():
    # Input
    data = input("Input your data: ")
    
    # Input parsing
    data = data.split(" ")
    number = data[0]
    startingBase = data[1]
    endingBase = data[2]
    
    # Error checking
    if errorCheck(number, startingBase, endingBase):
        print("Invalid input")
        return
    
    # Resolve
    result = resolveBases(number, startingBase, endingBase)
    
    # Output
    parseOutput(result, endingBase)



# main Init
if __name__ == '__main__':
    main()

