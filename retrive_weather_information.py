import requests

api_key = None
with open("API_KEY.txt") as api:
   api_key = api.read().strip("\n")

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name: ")

complete_url = "{}appid={}&q={}".format(base_url, api_key, city_name)

response = requests.get(complete_url)

output = response.json()

if output["cod"] != "404":
    main_output = output["main"]

    cur_temp = main_output["temp"] - 273.15
    cur_pres = main_output["pressure"]
    cur_hum = main_output["humidity"]
    weather_info = output["weather"]
    weather_description = weather_info[0]["description"]

    print(" Temperature (in celcius unit) = {:.2f}".format(cur_temp))
    print(" Atmosphere Pressure in (hPa unit) = %s" % str(cur_pres))
    print(" Humidity in percentage = %s" % str(cur_hum))
    print(" Description = %s" % str(weather_description))

else:
    print("City not found")
