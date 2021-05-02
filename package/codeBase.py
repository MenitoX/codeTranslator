from math import ceil
from .models import *
from .decimalBase import decimalToBase, baseToDecimal, checkBase
__all__ = ['numberToBcd', 'bcdToNumber', 'numberToGray', 'grayToNumber', 'numberToExcess', 'excessToNumber', 'bcdBinToNumber', 'numberToJohnson', 'johnsonToNumber', 'numberToParity', 'parityToNumber']


def bcdBinToNumber(binary):  
    nibbles = int(len(binary)/4)
    
    decimalValue = ""
    maxIndex = 3 + 1
    minIndex = 0
    # Iteration for each 4 bit segment
    for i in range(nibbles):
        binaryValue = ""

        # Indexing error resolver
        #if manIndex > 0:
            #minIndex = 0
        
        # We get the nibble segment value
        for i in range(minIndex, maxIndex):
            binaryValue += binary[i]
        
        decimalValue += baseToDecimal(binaryValue, __BIN_BASE__) 
        
        minIndex += 4
        maxIndex += 4
    return decimalValue

def numberToBcd(number, base):
    if base != __DEC_BASE__:
        number = baseToDecimal(number, __BIN_BASE__)
    number = list(number)
    number = [decimalToBase(i , __BIN_BASE__) for i in number]
    
    # This block of code gives us the binary BCD 
    for i in range(len(number)):
       while len(number[i]) < 4:
           number[i] = '0' + number[i]
    
    number = "".join(number)
    
    # dev testing return
    # return number
    
    number = baseToDecimal(number ,__BIN_BASE__)
    return number
       
def bcdToNumber(number):
    # Remember that checkbase returns true when there's an error
    if checkBase(number, __BIN_BASE__):
        number = decimalToBase(number, __BIN_BASE__)
    
    while len(number)%4 != 0:
        number = '0' + number
    number = bcdBinToNumber(number)
    return number

def numberToGray(number, base):
    if base != __BIN_BASE__:
        number = baseToDecimal(number, base)
        number = decimalToBase(number, __BIN_BASE__)
    number = list(number)
    resList = list()
    resList.append(number[__START_POS__])
    for i in range(1, len(number)):
        if int(number[i]) + int(number[i-1]) == 1:
            resList.append("1")
        else:
            resList.append("0")
    resList = "".join(resList)
    return resList

def grayToNumber(number):
    if checkBase(number, __BIN_BASE__):
        number = decimalToBase(number, __BIN_BASE__)
    number = list(number)
    for i in range(1, len(number)):
        if int(number[i]) + int(number[i-1]) == 1:
            number[i] = "1"
        else:
            number[i] = "0"
    number = "".join(number)
    return number

def numberToExcess(number, base):
    if base != __DEC_BASE__:
        number = baseToDecimal(number, __BIN_BASE__)
    number = list(number)
    number = [str(int(i)+3) for i in number]
    number = "".join(number)
    
    
    # Retorno como BCD decimal
    number = numberToBcd(number, __DEC_BASE__)
    number = decimalToBase(number, __BIN_BASE__)
    return number

def excessToNumber(number):
    number = bcdToNumber(number)
    number = [str(int(i)-3) for i in number]
    number = "".join(number)
    number = decimalToBase(number, __BIN_BASE__)
    
    # Retorna binario del numero original del BCD ( o sea pre-añadido el exceso )
    return number

# Johnson , estados == 2*n , menor posible

def lesserPowerOfTwo(number):
    number = int(number)
    # Plus 1 because of state 0
    bits = ceil((number+1)/2)
    power = 0
    c = 0
    while bits > power:
        power = 2 ** c
        c += 1
    return power

def numberToJohnson(number, base):
    if base != __DEC_BASE__:
        number = baseToDecimal(number, __BIN_BASE__)
    
    bits = lesserPowerOfTwo(number)
    returnList = list()
    for i in range(bits):
        returnList.append("0")
    
    index = bits-1
    for i in range(int(number)):
        if index == __START_POS__-1 and returnList[__START_POS__] == "1":
            index = bits-1

        if returnList[index] == "0":
            returnList[index] = "1"
        else:
            returnList[index] = "0"
        index -= 1
    
    returnList = "".join(returnList)
    return returnList
    
def johnsonToNumber(number):
    if checkBase(number, __BIN_BASE__):
        number = decimalToBase(number, __BIN_BASE__)
    
    numberList = list(number)
    ceroCount = 0
    
    for value in numberList:
        if value == "0":
            ceroCount += 1  
    
    if numberList[__START_POS__] == "1":
        number = len(numberList) + ceroCount
    else:
        number = len(numberList) - ceroCount
    number = decimalToBase(number, __BIN_BASE__)
    return number 

def numberToParity(number, base):
    if base != __BIN_BASE__:
        number = decimalToBase(number, __DEC_BASE__)
    oneCount = 0
    number = list(number)
    for i in number:
        if i == "1":
            oneCount += 1
    if oneCount % 2 == 0:
        return "1"
    else:
        return "0"

# It makes no sense, I'll just return the binary from the number
def parityToNumber(number):
    if checkBase(number, __BIN_BASE__):
        number = decimalToBase(number, __BIN_BASE__)
    else:
        number = list(number)
        number.pop(len(number)-1)
    return number



codeFunctions = [["bcd" ,numberToBcd], ["gry", numberToGray],  ["ed3", numberToExcess]]