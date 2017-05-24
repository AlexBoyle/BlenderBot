#https://github.com/csparpa/pyowm

import pyowm
owm = pyowm.OWM('665d0497ac66c8c8cfd2178807d07f57')

commandlist = [['+wnz', 'get current weather by zip code'],['+wnp', 'get current weather by name (city,country)']]

def run(message):
    #get current weather
    if message.startswith('wnz '):
         return current_weather_z(message[3:])
    if message.startswith('wnp '):
         return current_weather_p(message[3:])
    if message == 'help' :
        return help()

def help():
    output = ""
    for entry in commandlist:
          output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
    return output

def current_weather_z(zip, country='us', unit='fahrenheit'):
    zip = zip.strip()
    observation = owm.weather_at_zip_code(zip,country)
    w = observation.get_weather()
    temperature = w.get_temperature(unit)
    status = w.get_status()
    out = '''
	The temperature right now is: **%s**!
The status is: **%s**
Today's low is **%s** and the high for today is going to be **%s**!
	''' % (temperature['temp'],status,temperature['temp_min'],temperature['temp_max'])
    return out
	
def current_weather_p(location, unit='fahrenheit'):

    location = location.strip().split(',')
    city,country = location[0],location[1]
	
    observation = owm.weather_at_place('%s,%s' % (city,country))
    w = observation.get_weather()
	
    temperature = w.get_temperature(unit)
    status = w.get_status()
    
    out = '''
    The temperature right now is: **%s**!
The status is: **%s**
Today's low is **%s** and the high for today is going to be **%s**!
    ''' % (temperature['temp'],status,temperature['temp_min'],temperature['temp_max'])
    
    return out
