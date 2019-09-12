from sense_hat import SenseHat
from subprocess import call

sense = SenseHat()

def shutdown():
  # Shutdown the computer.
  call("sudo halt", shell=True)
  
sense.stick.direction_middle = shutdown
  
while True:
  # measure temperature
  tempC = sense.get_temperature()
  tempF = round((tempC * 9/5) + 32)
  message = "T " + str(tempF) + " F"
  print(message)
  sense.show_message(message)
  
  # measure humidity
  humidity = sense.get_humidity()
  humidity = round(humidity)
  message = "H " + str(humidity) + " %"
  print(message)
  sense.show_message(message)
  
  # measure pressure
  pressure_hPa = sense.get_pressure()
  pressure_psi = round(pressure_hPa * 0.0145, 1)
  message = "P " + str(pressure_psi) + " psi" 
  print(message)
  sense.show_message(message)

