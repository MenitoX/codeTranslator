from .models import responseChar, __START_POS__, __DEC_BASE__, __MIN_BASE__, __MAX_BASE__, __MIN_N__, __MAX_N__

#Exports
__all__ = ['joinString', 'baseToDecimal', 'decimalToBase', 'errorCheck', 'checkBase']

# Convertion of int array to responseChar array values, receives int array
def joinString(numberList):
    numberList = [responseChar[i] for i in numberList]
    numberList = "".join(numberList)
    return numberList

# Convertion from 1-64 base to decimal, receives string number and original base
def baseToDecimal(number, base):
    numberList = list(number)
    base = int(base)
    digits = len(numberList) - 1
    
    returnNumber = 0
    for i in numberList:
        returnNumber += responseChar.index(i)* (base**digits)
        digits -= 1
    return returnNumber

# Convertion to decimal bases 1-64, receives string number and ending base
def decimalToBase(number, base):
    retList = list()
    number = int(number)
    base = int(base)
    while number != 0:
        remainder = number % base  
        number = int(number / base)    
        retList.insert(__START_POS__, remainder)
    retNumber = joinString(retList)
    return retNumber

# Error check for decimal type only inputs
def errorCheck(number, base, endingBase):
    if base != __DEC_BASE__:
        numberDecimal = baseToDecimal(number, base)
    else:
        numberDecimal = int(number)
    
    baseInt = int(base)
    endingBase = int(endingBase)
    if baseInt < __MIN_BASE__ or baseInt > __MAX_BASE__:
        error = True
        print("Invalid starting Base")
    elif endingBase < __MIN_BASE__ or endingBase > __MAX_BASE__:
        error = True
        print("Invalid ending Base")
    elif checkBase(number, base):
        error = True
        print("Number not in Base")
    elif numberDecimal < __MIN_N__ or numberDecimal > __MAX_N__:
        error = True
        print("Too big!")
    else:
        error = False
    return error

# Error check for decimal type only bases, receives int number and base, True if error in base
def checkBase(number, base):
    compareList = list()
    for i in range(int(base)):
        compareList.append(responseChar[i])
    numberList = list(number)
    for i in numberList:
        if i not in compareList:
            return True
    return False