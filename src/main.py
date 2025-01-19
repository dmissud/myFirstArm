import time
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO

#Constants
nbPCAServo=16
#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]
#Objects pca=ServoKit(channels=16, address=40)
pca = ServoKit(channels=16)
# Configuration des broches GPIO
GPIO.setmode(GPIO.BCM)  # Utiliser le numéro de broche du processeur Broadcom
GPIO.setup(22, GPIO.OUT)  # Définir la broche GPIO 22 comme une sortie

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}') # Press Ctrl+F8 to toggle the breakpoint.


# function init
def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])

# function pcaScenario
def pca_scenario(nb):
    """Scenario to test servo"""
    print(f'freq, {pca.servo[nb]._pwm_out.frequency}')
    print(f'minduty, {pca.servo[nb]._min_duty}')
    print(f'range, {pca.servo[nb]._duty_range}')
    pca.servo[nb].angle = 90
    time.sleep(3)
    pca.servo[nb].angle = 45
    time.sleep(3)
    pca.servo[nb].angle = 0
    time.sleep(3)
    pca.servo[nb].angle = 45
    time.sleep(3)
    pca.servo[nb].angle = 90
    time.sleep(3)
    pca.servo[nb].angle = 135
    time.sleep(3)
    pca.servo[nb].angle = 180
    time.sleep(3)
    pca.servo[nb].angle = 135
    time.sleep(3)
    pca.servo[nb].angle = 90
    time.sleep(3)
    pca.servo[nb].angle=None #disable channel
    time.sleep(0.5)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    init()
    GPIO.output(22, GPIO.HIGH)
    pca_scenario(0)
    GPIO.output(22, GPIO.LOW)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
