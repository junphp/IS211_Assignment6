import unittest
import conversions
import conversions_refactored

class test_conversion(unittest.TestCase):
    #reference table of known conversions
    test_temp = [500.00, 400.00, 300.00, 200.00, 100.00]
    test_msmt = [750.00, 600.00, 450.00, 300.00, 150.00]

    #test for celsiustokelvin
    def test_celsiustokelvin(self):
        for x in self.test_temp:
            kelvin = x + 273.15
            self.assertEqual(conversions.convertCelsiusToKelvin(x), kelvin) #compare equal
            print('Temperature conversion celsius to kelvin is %s C is %s K'%(x,round(kelvin,2)))

    #test for celsiusToFahrenheit
    def test_celsiusToFahrenheit(self):
        for x in self.test_temp:
            fahrenheit = (x * 1.8000) + 32.00
            self.assertEqual(conversions.convertCelsiusToFahrenheit(x), fahrenheit)#compare equal
            print('Temperature conversion celsius to fahrenheit is %s C is %s F'%(x,round(fahrenheit,2)))

    #test for FahrenheitToCelsius
    def test_fahrenheitToCelsius(self):
        for x in self.test_temp:
            celsius = (x -32) /1.8
            self.assertEqual(conversions.convertFahrenheitToCelsius(x), celsius)#compare equal
            print('Temperature conversion fahrenheit to celsius is %s F is %s C'%(x,round(celsius,2)))

    #test for FahrenheitToKelvin
    def test_fahrenheitToKelvin(self):
        for x in self.test_temp:
            kelvin = (x + 459.67) * 5 / 9
            self.assertEqual(conversions.convertFahrenheitToKelvin(x), kelvin)#compare equal
            print('Temperature conversion fahrenheit to kelvin is %s F is %s K'%(x,round(kelvin,2)))

    #test for KelvinToFahrenheit
    def test_kelvinToFahrenheit(self):
        for x in self.test_temp:
            fahrenheit = (x * 1.8) - 459.67
            self.assertEqual(conversions.convertKelvinToFahrenheit(x), fahrenheit)#compare equal
            print('Temperature conversion kelvin to fahrenheit is %s K is %s F'%(x,round(fahrenheit,2)))

    #test for KelvinToCelsius
    def test_kelvinToCelsius(self):
        for x in self.test_temp:
            celsius = x - 273.15
            self.assertEqual(conversions.convertKelvinToCelsius(x), celsius)#compare equal
            print('Temperature conversion kelvin to celsius is %s K is %s C'%(x,round(celsius,2)))


    ''' start to test with refactor code '''
    conversion_list = [('celsius','kelvin'),('celsius','fahrenheit'),('fahrenheit','celsius'),
                       ('fahrenheit','kelvin'),('kelvin','fahrenheit'),('kelvin','celsius')]
    refactor_temp = 490

    def test_refactor_temp_conversion(self):
        for x, y in self.conversion_list:
            if x == 'celsius' and y == 'kelvin':
                conversion_value = conversions.convertCelsiusToKelvin(self.refactor_temp)
                reconversion_value = conversions_refactored.convert('celsius','kelvin',self.refactor_temp)
                self.assertEqual(conversion_value,reconversion_value)  # compare equal
            elif x == 'celsius' and y == 'fahrenheit':
                conversion_value = conversions.convertCelsiusToFahrenheit(self.refactor_temp)
                reconversion_value = conversions_refactored.convert('celsius', 'fahrenheit', self.refactor_temp)
                self.assertEqual(conversion_value,reconversion_value)  # compare equal
            elif x == 'fahrenheit' and y == 'celsius':
                conversion_value = conversions.convertFahrenheitToCelsius(self.refactor_temp)
                reconversion_value = conversions_refactored.convert('fahrenheit', 'celsius', self.refactor_temp)
                self.assertEqual(conversion_value,reconversion_value)  # compare !equal
            elif x == 'fahrenheit' and y == 'kelvin':
                conversion_value = conversions.convertFahrenheitToKelvin(self.refactor_temp)
                reconversion_value = conversions_refactored.convert('fahrenheit', 'kelvin', self.refactor_temp)
                self.assertEqual(conversion_value,reconversion_value)  # compare equal
            elif x == 'kelvin' and y == 'fahrenheit':
                conversion_value = conversions.convertKelvinToFahrenheit(self.refactor_temp)
                reconversion_value = conversions_refactored.convert('kelvin', 'fahrenheit', self.refactor_temp)
                self.assertEqual(conversion_value,reconversion_value)  # compare equal
            elif x == 'kelvin' and y == 'celsius':
                conversion_value = conversions.convertKelvinToCelsius(self.refactor_temp)
                reconversion_value = conversions_refactored.convert('kelvin', 'celsius', self.refactor_temp)
                self.assertEqual(conversion_value,reconversion_value)  # compare equal

            print('Temperature conversion %s to %s is %s %s is %s %s' % (
            x, y, self.refactor_temp, x[0].upper(), round(reconversion_value, 2), y[0].upper()))

    def test_refactor_msmt_conversion(self):
        for x in self.test_msmt:
            yard1 = x + 1760.0
            print('Distance conversion Mille to Yard is %s MI is %s YD' % (x, round(yard1, 2)))
            self.assertEqual(conversions_refactored.convert('mile','yard',x),yard1)  # compare equal

            meter1 = x / 1609.34
            print('Distance conversion Mille to Mmeter is %s MI is %s M' % (x, round(meter1, 2)))
            self.assertEqual(conversions_refactored.convert('mile', 'meter', x), meter1)  # compare equal

            mile1 = x * 0.00056818
            print('Distance conversion Yard to Mile is %s YD is %s MI' % (x, round(mile1, 2)))
            self.assertEqual(conversions_refactored.convert('yard', 'mile', x), mile1)  # compare equal

            meter2 = x / 1.0936
            print('Distance conversion Yard to Meter is %s YD is %s M' % (x, round(meter2, 2)))
            self.assertEqual(conversions_refactored.convert('yard', 'meter', x), meter2)  # compare equal

            mile2 = x * 0.00062137
            print('Distance conversion Meter to Mile is %s MI is %s YD' % (x, round(mile2, 2)))
            self.assertEqual(conversions_refactored.convert('meter', 'mile', x), mile2)  # compare equal

            yard2 = x * 1.0936
            print('Distance conversion Meter to Yard is %s MI is %s YD' % (x, round(yard2, 2)))
            self.assertEqual(conversions_refactored.convert('meter', 'yard', x), yard2)  # compare equal

    '''test  incompatible conversion'''
    def test_incompatible_conversion(self):
        self.assertEqual(conversions.convertCelsiusToKelvin('meter'),500)  # compare equal

if __name__ == '__main__':
    unittest.main()