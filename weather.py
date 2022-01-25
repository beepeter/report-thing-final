# to find the weather
def weatherToday():
    global trueFeelsLike
    global humidity
    global weather
    city = input("""what city are you in
""")
    # importing requests and json
    import requests, json
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    # City Name CITY = "Hyderabad"
    # API key API_KEY = "Your API Key"
    # upadting the URL
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5faffc8d3f14f722eb3f73c2519cf247"
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        feelsLike = main['feels_like']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        trueTemperature = temperature - 273
        trueFeelsLike = feelsLike - 273
        print(
            f"Temperature: {trueTemperature} but it feels like: {trueFeelsLike}"
        )
        print(f"Humidity: {humidity}")
        print(f"Weather Report: {report[0]['description']}")
    else:
        # showing the error message
        print("Error in the HTTP request")


def walkGood():
    if trueFeelsLike < -20:
        print("it's pretty chilly")
    elif trueFeelsLike > 0:
        print("feels like a good temperature for a bike ride")
    else:
        print("feels like a good temperature for a walk")

    if humidity > 30 or humidity < 50:
        print("the humidity isn't very good outdoors")
    else:
        print("good humidity today")
