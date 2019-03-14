class DataTypeError(Exception): pass

# conversion Celsius to Kelvin.
def convertCelsiusToKelvin(temperature):
    if type(temperature) == str:
        raise DataTypeError('Invalid datatype')
    temperature = float(temperature) + 273.15
    return temperature

#conversion Celsius to Fahrenheit.
def convertCelsiusToFahrenheit(temperature):
    if type(temperature) == str:
        raise DataTypeError('Invalid datatype')
    temperature = (float(temperature) * 1.8000) + 32.00
    return temperature

#conversion Fahrenheit to Celsius.
def convertFahrenheitToCelsius(temperature):
    if type(temperature) == str:
        raise DataTypeError('Invalid datatype')
    temperature = (float (temperature) - 32 ) / 1.8
    return temperature

#conversion Fahrenheit to Kelvin.
def convertFahrenheitToKelvin(temperature):
    if type(temperature) == str:
        raise DataTypeError('Invalid datatype')
    temperature = (float(temperature) + 459.67) * 5/9
    return temperature

#conversion Kelvin to Fahrenheit.
def convertKelvinToFahrenheit(temperature):
    if type(temperature) == str:
        raise DataTypeError('Invalid datatype')
    temperature = (float(temperature) * 1.8) - 459.67
    return temperature

#conversion Kelvin to Celsius.
def convertKelvinToCelsius(temperature):
    if type(temperature) == str:
        raise DataTypeError('Invalid datatype')
    temperature = float(temperature) - 273.15
    return temperature