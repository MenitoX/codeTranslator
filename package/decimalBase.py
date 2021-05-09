from .models import responseChar, __START_POS__, __DEC_BASE__, __BIN_BASE__, __MIN_BASE__, __MAX_BASE__, __MIN_N__, __MAX_N__, codeArray, codeNamesArray
import package.codeBase as CB

#Exports
__all__ = ['baseToDecimal', 'decimalToBase', 'errorCheck', 'checkBase', 'resolveBases', 'parseOutput']

# Convertion of int array to responseChar array values, receives int array
def joinString(numberList, base = None):
    
    numberList = [responseChar[i] for i in numberList]
    numberList = "".join(numberList)
    return numberList

# Convertion from 1-64/code base to decimal, receives string number and original base
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
        for i,j in CB.codeFunctionsCtoN:
            if base == i:
                return j(number, __DEC_BASE__)
        
# Convertion to decimal bases 1-64, receives string number and ending base
def decimalToBase(number, base):
    retList = list()
    number = int(number)
    base = int(base)
    if base == 1:
        return number * "1"
    elif number == 0:
        return "0"
    elif number == "":
        return ""

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
        # Modificar para checkear codigos
        numberDecimal = int(baseToDecimal(number, base))
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
        if checkBase(number, __BIN_BASE__):
            return True
    return False

def resolveBases(number, base, conversionBase):
    # d d
    # d c
    # c d
    # c c
    if base.isdigit() and conversionBase.isdigit():
        number = baseToDecimal(number, base)
        number = decimalToBase(number, conversionBase)
    elif base.isdigit() and not conversionBase.isdigit():
        number = baseToDecimal(number, base)
        number = decimalToBase(number, __BIN_BASE__)
        for i,j in CB.codeFunctionsNtoC:
            if i == conversionBase:
                number = j(number)
    elif not base.isdigit() and conversionBase.isdigit():
        number = baseToDecimal(number, base)
        number = decimalToBase(number, conversionBase)
    else:
        number = baseToDecimal(number, base)
        number = decimalToBase(number, __BIN_BASE__)
        for i,j in CB.codeFunctionsNtoC:
            if i == conversionBase:
                number = j(number)
    return number

def parseOutput(number, baseOutput):
    if baseOutput in codeArray:
        index = codeArray.index(baseOutput)
        baseOutput = "Codigo " + codeNamesArray[index] + ": "
    else:
        baseOutput = "Base " + baseOutput + ": "
    print(baseOutput, number)

