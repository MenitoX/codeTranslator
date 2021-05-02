from .models import *
from .decimalBase import decimalToBase, baseToDecimal, checkBase
__all__ = ['numberToBcd', 'bcdToNumber', 'numberToGray', 'grayToNumber', 'numberToExcess', 'excessToNumber']


def binaryToBcd(binary):  
    nibbles = ceil(len(binary)/4)
    
    decimalValue = ""
    maxIndex = len(binary)
    minIndex = maxIndex - 4
    # Iteration for each 4 bit segment
    for i in range(nibbles):
        binaryValue = ""

        # Indexing error resolver
        if minIndex < 0:
            minIndex = 0
        
        # We get the nibble segment value
        for i in range(minIndex, maxIndex):
            binaryValue += binary[i]
        
        decimalValue = str(baseToDecimal(binaryValue, __BIN_BASE__)) + decimalValue
        
        maxIndex += 4
    return decimalValue

def numberToBcd(number, base):
    if base != __DEC_BASE__:
        number = baseToDecimal(number, base)
    number = list(str(number))
    number = [str(decimalToBase(i , __BIN_BASE__)) for i in number]
    
    # This block of code gives us the binary BCD 
    for i in range(len(number)):
       while len(number[i]) < 4:
           number[i] = '0' + number[i]
    
    number = "".join(number)
    # SUPONGO HACER ESTO PQ SINO NO TIENE SENTIDO ESTA WEEAAAAA
    return number
       
def bcdToNumber(number):
    # Remember that checkbase returns true when there's an error
    if checkBase(number, __BIN_BASE__):
        number = decimalToBase(number, __BIN_BASE__)
    
    while len(number)%4 != 0:
        number = '0' + number
    number = binaryToBcd(number)
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
        number = baseToDecimal(number, base)
    number = list(number)
    number = [str(int(i)+3) for i in number]
    number = "".join(number)
    
    # Retorno como base 2
    #number = decimalToBase(number, __BIN_BASE__)
    
    # Retorno como BCD
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


codeFunctions = [["bcd" ,numberToBcd], ["gry", numberToGray],  ["ed3", numberToExcess]]