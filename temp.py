import RPi.GPIO as GPIO
import time
import commands
 
def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000
    # Uncomment the next line if you want the temp in Fahrenheit
    #return float(1.8*cpu_temp)+32
 
def get_gpu_temp():
    gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
    return  float(gpu_temp)
    # Uncomment the next line if you want the temp in Fahrenheit
    # return float(1.8* gpu_temp)+32
 
def main():
	fan_pin = 24
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(fan_pin,GPIO.OUT)
	while True:
		#print "CPU temp: ", str(get_cpu_temp())
		#print "GPU temp: ", str(get_gpu_temp())
		if int(get_cpu_temp()) > 41:
			GPIO.output(fan_pin,True)
		elif int(get_cpu_temp()) < 37:
			GPIO.output(fan_pin,False)
		time.sleep(10)
if __name__ == '__main__':
    main()
