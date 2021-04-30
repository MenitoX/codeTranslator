#Exports
__all__ = ['responseChar', 'codeArray', 'binArray', 'digitArray', '__BIN_BASE__', '__DEC_BASE__','__START_POS__', '__MIN_BASE__', '__MAX_BASE__', '__MAX_N__', '__MIN_N__']

# Response chars array
responseChar = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+?")

# Possible codes array
codeArray = ["bcd", "gry", "ed3", "jsn", "par", "pbt", "ham"]

# Binary numbers array
binArray = ["0", "1"]

# Digits Array
digitArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Binary base as string
__BIN_BASE__ = "2"

# Decimal base as string
__DEC_BASE__ = "10"

# Starting position of an array
__START_POS__ = 0

# Min possible base
__MIN_BASE__ = 1

# Max possible base
__MAX_BASE__ = 64

# Max n
__MAX_N__ = 1000

# Min n
__MIN_N__ = 1