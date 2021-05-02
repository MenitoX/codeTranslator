from math import ceil
from .models import *
from .decimalBase import decimalToBase, baseToDecimal, checkBase
__all__ = ['numberToBcd', 'bcdToNumber', 'numberToGray']


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

# Esta wea de Bcd no puede estar peor explicada porque directamente no funciona
# porque el ejemplo está mal por la cresta supuestamente es pasar de binario a dec y de ese
# dec a BCD cada digito, pero el ejemplo hace algo nada que ver,  WNNN COMO NO PUEDEN DAR BIEN INSTRUCCIONES DE ALGO QUE YO MISMO
# ENCONTRÉ EN 5 MINUTOS DE GOOGLEAR PO LOCO WTF SAQUENME DE LATINOAMERICA CTM
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
    #return baseToDecimal(number ,__BIN_BASE__)
    

def bcdToNumber(number, base):
    # Bases 2 or 10
    if base != __BIN_BASE__:
        number = str(decimalToBase(number, __BIN_BASE__))
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