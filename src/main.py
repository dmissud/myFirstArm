import time

from adafruit_motor import servo
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

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}') # Press Ctrl+F8 to toggle the breakpoint.


# function init
def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])

# function pcaScenario
def pca_scenario(numero_de_servo,angle_arrivee):
    """Scenario to test servo"""
    print(f'freq, {pca.servo[numero_de_servo]._pwm_out.frequency}')
    print(f'minuty, {pca.servo[numero_de_servo]._min_duty}')
    print(f'range, {pca.servo[numero_de_servo]._duty_range}')
    print(f'range, {pca.servo[numero_de_servo].angle}')
    angle_depart=int(pca.servo[numero_de_servo].angle)
    time.sleep(2)
    while angle_depart!=angle_arrivee:
        if angle_arrivee>angle_depart:
            angle_depart=angle_depart+1
            pca.servo[numero_de_servo].angle = angle_depart
        else:
            angle_depart=angle_depart-1
            pca.servo[numero_de_servo].angle = angle_depart
        time.sleep(0.05)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    init()
    pca_scenario(0,90)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
