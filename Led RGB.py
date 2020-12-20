import RPi.GPIO as GPIO
import time
import random
Vermelho = 18
Verde = 23
Azul = 24

GPIO.setwarnings (False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(Vermelho, GPIO.OUT)
GPIO.setup(Verde, GPIO.OUT)
GPIO.setup(Azul, GPIO.OUT)

pwm_Verm = GPIO.PWM(Vermelho,100)
pwm_Verm.start(0)

pwm_Verde = GPIO.PWM(Verde,100)
pwm_Verde.start(0)

pwm_Azul = GPIO.PWM(Azul,100)
pwm_Azul.start(0)

try:
    while True:
        
       pwm_Verm.ChangeDutyCycle(random.randint(0,100))
       pwm_Verde.ChangeDutyCycle(random.randint(0,100))
       pwm_Azul.ChangeDutyCycle(random.randint(0,100))
       time.sleep(0.2)
       
except KeyboardInterrupt:
    GPIO.cleanup ()
