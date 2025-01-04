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
def pca_scenario():
    """Scenario to test servo"""
    for i in range(2):
        for j in range(MIN_ANG[i],MAX_ANG[i],1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.1)
        for j in range(MAX_ANG[i],MIN_ANG[i],-1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.1)
        pca.servo[i].angle=None #disable channel
        time.sleep(0.5)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    init()
    GPIO.output(22, GPIO.HIGH)
    pca_scenario()
    GPIO.output(22, GPIO.LOW)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
