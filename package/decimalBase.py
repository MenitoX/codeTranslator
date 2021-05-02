from .models import responseChar, __START_POS__, __DEC_BASE__, __BIN_BASE__, __MIN_BASE__, __MAX_BASE__, __MIN_N__, __MAX_N__, codeArray

#Exports
__all__ = ['joinString', 'baseToDecimal', 'decimalToBase', 'errorCheck', 'checkBase']

# Convertion of int array to responseChar array values, receives int array
def joinString(numberList):
    numberList = [responseChar[i] for i in numberList]
    numberList = "".join(numberList)
    return numberList

# Convertion from 1-64 base to decimal, receives string number and original base
def baseToDecimal(number, base):
    if base.isdigit():
        numberList = list(number)
        base = int(base)
        digits = len(numberList) - 1
        
        returnNumber = 0
        for i in numberList:
            returnNumber += responseChar.index(i)* (base**digits)
            digits -= 1
        return str(returnNumber)
    else:
        return

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

# Error check for inputs
def errorCheck(number, base, endingBase):
    error = False

    if base != __DEC_BASE__:
        numberDecimal = baseToDecimal(number, base)
    else:
        numberDecimal = int(number)
    
    if base.isdigit():
        baseInt = int(base)
        if baseInt < __MIN_BASE__ or baseInt > __MAX_BASE__:
            error = True
            print("Invalid numeric starting Base")
    else:
        if base not in codeArray:
            error = True
            print("Invalid base not a code")
    
    if endingBase.isdigit():
        endingBase = int(endingBase)
        if endingBase < __MIN_BASE__ or endingBase > __MAX_BASE__:
            error = True
            print("Invalid ending Base")
    else:
        if endingBase not in codeArray:
            error = True
            print("Invalid base not a code")
    
    if checkBase(number, base):
        error = True
        print("Number not in Base")
    
    elif numberDecimal < __MIN_N__ or numberDecimal > __MAX_N__:
        error = True
        print("Too big!")
    
    
    return error

# Error check for bases, receives string number and base, True if error in base
def checkBase(number, base):
    if base.isdigit():
        compareList = list()
        for i in range(int(base)):
            compareList.append(responseChar[i])
        numberList = list(number)
        for i in numberList:
            if i not in compareList:
                return True
    else:
        if number[__START_POS__] == '0':
            return checkBase(number, __BIN_BASE__)
        else:
            return checkBase(number, __DEC_BASE__)
    return False

