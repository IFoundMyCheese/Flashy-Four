def convertToHexaDecimal(n):
    hexNumber = "" 
    hexadecimalCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    while n != 0:
        r = n%16
        n = int(n/16)
        hexNumber =  hexadecimalCharacters[r] + hexNumber
    if hexNumber == "":
        return "00"
    elif len(hexNumber) == 1:
        return "0" + hexNumber
    else:
        return hexNumber


def getPythonColor(r, g, b):
    rHex = convertToHexaDecimal(r)
    gHex = convertToHexaDecimal(g)
    bHex = convertToHexaDecimal(b)
    pythonColor = "#" + rHex + gHex + bHex
    return pythonColor