 # A project to find out if the weather is ok for outdoors activity

import weather
import timecheck

currentTime = timecheck.timeFind()
currentTime.findTime()
weather.weatherToday()
weather.walkGood()