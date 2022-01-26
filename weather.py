# to find the weather

weatherEnd = 1

def weatherToday():
   global trueFeelsLike
   global humidity
   global weather
   
   weatherEnd = 1
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
        print(f"Temperature: {trueTemperature} but it feels like: {trueFeelsLike}")
        print(f"Humidity: {humidity}")
        print(f"Weather Report: {report[0]['description']}")
   else:
            # showing the error message
            print("Error in the HTTP request")

    # tells you what it thinks
def walkGood():
   global point
        
   point = 3
   try:
          if trueFeelsLike < -20:
                print("it's pretty chilly")
                point - 2
          elif trueFeelsLike > 0:
                print("feels like a good temperature for a bike ride")
          else:
                print("feels like a good temperature for a walk")
                point - 1

          if humidity > 30 or humidity < 50:
                print("the humidity isn't very good outdoors")
                point - 1
          else:
                print("good humidity today")
          global weatherEnd
          weatherEnd = 0
          
          
            
   except:
          print("something went wrong try a different place or try typing differently") 
    # decides how the weather is
def pointTally():
        if point == 3:
            print("good weather for a walk right now")
        if point == 2:
          print("it's ok for a walk right now")
        if point == 1:
            print("probably shouldn't go for a walk")
        if point == 0:
          print("don't go on a walk")
def weatherRun():
      
      
      while weatherEnd == 1:
          weatherToday()
          walkGood()
