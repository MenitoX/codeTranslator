from math import ceil
from package.models import *
import package.decimalBase as DB

__all__ = ['codeFunctionsCtoN', 'codeFunctionsNtoC']

######### UTILITIES ###########################

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

def redundantCuantity(dataBits):
    cuantity = 0
    for i,j in dataBits:
        i = DB.baseToDecimal(i, __BIN_BASE__)
        if str(i) == str(lesserPowerOfTwo(i)):
            cuantity += 1
    print(cuantity)
    return cuantity

def decimalToBinWithCeros(number, maxLen):
    number = DB.decimalToBase(number, __BIN_BASE__)
    while len(number) < maxLen:
        number = '0' + number
    return number

############### Number To Code ################

def numberToBcd(number):
    # number en BIN
    number = DB.baseToDecimal(number, __BIN_BASE__)
    number = list(number)
    number = [DB.decimalToBase(i , __BIN_BASE__) for i in number]
    
    # This block of code gives us the binary BCD 
    for i in range(len(number)):
       while len(number[i]) < 4:
           number[i] = '0' + number[i]
    number = "".join(number)
    number = str(int(number))
    return number
       
def numberToGray(number):
    # CHECKEAR SI FUNCA PARA 1 BIT Y 2 BITS
    # number en Bin
    number = list(number)
    resList = list()
    resList.append(number[__START_POS__])
    for i in range(1, len(number)):
        if int(number[i]) + int(number[i-1]) == 1:
            resList.append("1")
        else:
            resList.append("0")
    resList = "".join(resList)
    resList = str(int(resList))
    return resList

def numberToExcess(number):
    number = DB.baseToDecimal(number, __BIN_BASE__)
    number = list(number)
    number = [str(int(i)+3) for i in number]
    number = "".join(number)
    
    
    # Retorno como BCD
    number = numberToBcd(DB.decimalToBase(number, __BIN_BASE__))
    return number

def numberToJohnson(number):
    # number en BIN
    number = DB.baseToDecimal(number, __BIN_BASE__)
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
    
def numberToParity(number):
    # number en BIN

    oneCount = 0
    number = list(number)
    for i in number:
        if i == "1":
            oneCount += 1
    if oneCount % 2 == 0:
        return "1"
    else:
        return "0"

def numberToPentabit(number):
    # number en BIN
    if (len(number)%5 != 0):
        return '0'
    else:
        return '1'

def numberToHamming(number):
    error = -1
    while error != 0:
        number = list(number)
        maxLenBin =  len(DB.decimalToBase(len(number), __BIN_BASE__))
        number = list(enumerate(number))
        number = [[decimalToBinWithCeros(i+1, maxLenBin), j] for i,j in number]
        redundantC = redundantCuantity(number)
        pos = maxLenBin-1
        error = list()
        for i in range(redundantC):
            bit = ""
            c = 0
            for i,j in number:
                if i[pos] == "1":
                    if j == "1":
                        c += 1
            bit = c * "1"
            if (int(numberToParity(bit))):
                error.append("0")
            else:
                error.append("1")
            pos -= 1
        
        error.reverse()
        error = "".join(error)
        error = DB.baseToDecimal(error, __BIN_BASE__)
        error = int(error)
        errorValue = number[error-1][1]
        if error > 0:
            if(int(errorValue)):
                number[error-1][1] = '0'
            else:
                number[error-1][1] = '1'
        number = [j for i,j in number]
        number = "".join(number)
    return number

########### Code To Number ##################

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
        
        decimalValue += DB.baseToDecimal(binaryValue, __BIN_BASE__) 
        
        minIndex += 4
        maxIndex += 4
    return decimalValue

def bcdToNumber(number, base):
    # Remember that checkbase returns true when there's an error
    # number es bin BCD
    
    while len(number)%4 != 0:
        number = '0' + number
    number = bcdBinToNumber(number)
    number = DB.decimalToBase(number, base)
    return number
                 
def grayToNumber(number, base):
    # number == BIN posicion 
    number = list(number)
    for i in range(1, len(number)):
        if int(number[i]) + int(number[i-1]) == 1:
            number[i] = "1"
        else:
            number[i] = "0"
    number = "".join(number)
    # number esta en BIN aqui
    number = DB.baseToDecimal(number, __BIN_BASE__)
    number = DB.decimalToBase(number, base)
    return number
    
def excessToNumber(number, base):
    # number is BIN bcd
    number = bcdBinToNumber(number)
    number = [str(int(i)-3) for i in number]
    number = "".join(number)
    number = DB.decimalToBase(number, base)
    
    # Retorna en base del numero original del BCD ( o sea pre-añadido el exceso )
    return number

def johnsonToNumber(number, base):
    # number en BIN
    
    numberList = list(number)
    ceroCount = 0
    
    for value in numberList:
        if value == "0":
            ceroCount += 1  
    
    if numberList[__START_POS__] == "1":
        number = len(numberList) + ceroCount
    else:
        number = len(numberList) - ceroCount
    number = DB.decimalToBase(number, base)
    return number 

def parityToNumber(number, base):
    # number en BIN
    number = DB.baseToDecimal(number, __BIN_BASE__)
    number = DB.decimalToBase(number, base)
    return number

def pentabitToNumber(number, base):
    # number en BIN
    number = DB.baseToDecimal(number, __BIN_BASE__)
    number = DB.decimalToBase(number, base)
    return number

def hammmingToNumber(number, base):
    #number is BIN
    c = 0
    power = 2**c
    number = list(number)
    while power < len(number):
        number[power-1] = ""
        c += 1
        power = 2**c
    number = "".join(number)
    number = DB.baseToDecimal(number, __BIN_BASE__)
    number = DB.decimalToBase(number, base)
    return number

codeFunctionsNtoC = [["bcd" ,numberToBcd], ["gry", numberToGray],  ["ed3", numberToExcess], ["jsn", numberToJohnson], ["par", numberToParity], ["pbt", numberToPentabit], ["ham", numberToHamming]]

codeFunctionsCtoN = [["bcd" ,bcdToNumber], ["gry", grayToNumber],  ["ed3", excessToNumber], ["jsn", johnsonToNumber], ["par", parityToNumber], ["pbt", pentabitToNumber], ["ham", hammmingToNumber]]

