from package.decimalBase import *
from package.codeBase import *

def main():
    # Input
     #data = input("Input your data: ")
    
    # Input parsing
    # data = data.split(" ")
    # number = data[0]
    # startingBase = data[1]
    # endingBase = data[2]
    
    #print(bcdToNumber(str(numberToBcd("00010111", "2")), "2"))
    
    #if errorCheck(number, startingBase, endingBase):
        #print("Invalid input")
        #return
    
    
    print(numberToParity("11101111", "2"))
    #print(johnsonToNumber(numberToJohnson("3", 10)))
    #print(excessToNumber(numberToExcess("23", "10")))
    #print(bcdToNumber("1010110"))
    #print(grayToNumber("1100001010", "2"))
    #print(numberToBcd("85", "10"))
    #print(bcdToNumber("17"))
    #print(baseToDecimal("10111", "2"))
    #print(decimalToBase("23", "2"))

    return



# main Init
if __name__ == '__main__':
    main()

