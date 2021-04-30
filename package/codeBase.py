from math import ceil
from .models import *
from .decimalBase import decimalToBase, baseToDecimal, checkBase
__all__ = ['numberToBcd', 'bcdToNumber']


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
        
        minIndex -= 4
        maxIndex -= 4
        
    return decimalValue

def numberToBcd(number, base):
    if base != __DEC_BASE__:
        number = baseToDecimal(number, base)
    number = list(str(number))
    number = [str(decimalToBase(i , __BIN_BASE__)) for i in number]
    for i in range(len(number)):
        while len(number[i]) < 4:
            number[i] = '0' + number[i]
    number = "".join(number)
    return number
    

def bcdToNumber(number, base):
    # Bases 2 or 10
    if base != __BIN_BASE__:
        number = str(decimalToBase(number, __BIN_BASE__))
    while len(number)%4 != 0:
        number = '0' + number
    number = binaryToBcd(number)
    return number

