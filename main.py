# Course: CS 30
# Period: 2
# Date created: 28/12/21
# Date last modified: 24/01/22
# Name: Petros Gane
# Description: A project to find out if the weather is ok for outdoors activity

import weather
import timecheck

weatherEnd = 1

currentTime = timecheck.timeFind()
currentTime.findTime()

weather.weatherRun()
weather.pointTally()