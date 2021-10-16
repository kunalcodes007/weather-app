import pyowm


owm=pyowm.OWM('988bfbfa6eacb160409177665db40dd1')

place=owm.weather_at_place('New Delhi')

weather=place.get_weather()

temp=weather.get_temperature('celsius')

for key,value in temp.items():

print(key,value)