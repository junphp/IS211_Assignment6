'''
refactory method
'''
class ConversionNotPossible(Exception): pass

def convert(fromUnit, toUnit, value):
    fromUnit = str(fromUnit).lower()
    toUnit = str(toUnit).lower()
    okToTemp = False
    okToMsmt = False
    temp = ['celsius', 'kelvin', 'fahrenheit']
    msmt = ['mile', 'yard', 'meter']

    if fromUnit in temp:
        okToTemp = True
    elif fromUnit in msmt:
        okToMsmt = True

    if okToTemp:
        if fromUnit == 'celsius' and toUnit == 'kelvin':
            result = value + 273.15
        elif fromUnit == 'celsius' and toUnit == 'fahrenheit':
            result = (value * 9 / 5) + 32
        elif fromUnit == 'fahrenheit' and toUnit == 'celsius':
            result = (value - 32) / 1.8
        elif fromUnit == 'fahrenheit' and toUnit == 'kelvin':
            result = (value + 459.67) * 5 / 9
        elif fromUnit == 'kelvin' and toUnit == 'fahrenheit':
            result = value * 9/5 - 459.67
        elif fromUnit == 'kelvin' and toUnit ==  'celsius':
            result = value - 273.15

    elif okToMsmt:

        if fromUnit == 'mile' and toUnit == 'yard':
            result = value + 1760.0
        elif fromUnit == 'mile' and toUnit == 'meter':
            result = value / 1609.34
        elif fromUnit == 'yard' and toUnit == 'mile':
            result = value * 0.00056818
        elif fromUnit == 'yard' and toUnit == 'meter':
            result = value / 1.0936
        elif fromUnit == 'meter' and toUnit == 'mile':
            result = value * 0.00062137
        elif fromUnit == 'meter' and toUnit == 'yard':
            result = value * 1.0936
    if okToTemp == False and okToMsmt == False :
        raise ConversionNotPossible('Invalid conversion value')
    else:
        return result
'''
    try:
        if okToTemp == True or okToMsmt == True:
            return result
    except:
        raise ConversionNotPossible('Invalid conversion value')
'''

