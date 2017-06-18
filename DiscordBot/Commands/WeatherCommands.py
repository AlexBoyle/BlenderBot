#https://github.com/csparpa/pyowm
import asyncio
import pyowm


class WeatherCommands:
    owm = pyowm.OWM('665d0497ac66c8c8cfd2178807d07f57')
    commandlist = [['+wnz', 'get current weather by zip code'],['+wnp', 'get current weather by name (city,country)']]

    async def run(self, message):
        message = message.content[1:]
        #get current weather
        if message.startswith('wnz '):
            return self.current_weather_z(message[3:])
        if message.startswith('wnp '):
             return self.current_weather_p(message[3:])
        if message == 'help' :
             return self.help()

    def help(self):
        output = "```"
        for entry in self.commandlist:
            output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
        return output + "```"

    def current_weather_z(self, zip, country='us', unit='fahrenheit'):
        zip = zip.strip()
        observation = self.owm.weather_at_zip_code(zip,country)
        w = observation.get_weather()
        temperature = w.get_temperature(unit)
        status = w.get_status()
        out = (
            "```\nThe temperature right now is: **%s**!\n"
            "The status is: **%s**\n"
            "Today's low is **%s** and the high for today is going to be **%s**!\n```"
        )% (temperature['temp'],status,temperature['temp_min'],temperature['temp_max'])
        return out

    def current_weather_p(self, location, unit='fahrenheit'):

        location = location.strip().split(',')
        city,country = location[0],location[1]

        observation = self.owm.weather_at_place('%s,%s' % (city,country))
        w = observation.get_weather()

        temperature = w.get_temperature(unit)
        status = w.get_status()

        out = (
            "```\nThe temperature right now is: **%s**!\n"
            "The status is: **%s**\n"
            "Today's low is **%s** and the high for today is going to be **%s**!\n```"
        ) % (temperature['temp'],status,temperature['temp_min'],temperature['temp_max'])
        return out
