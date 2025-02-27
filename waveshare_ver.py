from machine import Pin, PWM, I2C
from ir_rx.nec import NEC_16
import random
from utime import sleep, sleep_ms
from neopixel import NeoPixel
import time


remote_Key = {
    0x45: 'CHANNEL1',0x09: 'EQ',0x1c: '5',
    0x46: 'CHANNEL2',0x16: '0',0x5a: '6',
    0x47: 'CHANNEL3',0x19: '100',0x42: '7',
    0x44: 'PREV',    0x0d: '200',0x52: '8',
    0x40: 'NEXT',    0x0c: '1',  
    0x43: 'PLAY.PAUSE',0x18: '2',
    0x07: 'VOL1',    0x5e: '3',
    0x15: 'VOL2',    0x08: '4',
    0x4a: '9'        }

tones = { "B0": 31,"C1": 33,"CS1": 35,"D1": 37,"DS1": 39,"E1": 41,"F1": 44,"FS1": 46,"G1": 49,
"GS1": 52,"A1": 55,"AS1": 58,"B1": 62,"C2": 65,"CS2": 69,"D2": 73,"DS2": 78,"E2": 82,
"F2": 87,"FS2": 93,"G2": 98,"GS2": 104,"A2": 110,"AS2": 117,"B2": 123,"C3": 131,"CS3": 139,
"D3": 147,"DS3": 156,"E3": 165,"F3": 175,"FS3": 185,"G3": 196,"GS3": 208,"A3": 220,"AS3": 233,
"B3": 247,"C4": 262,"CS4": 277,"D4": 294,"DS4": 311,"E4": 330,"F4": 349,"FS4": 370,"G4": 392,
"GS4": 415,"A4": 440,"AS4": 466,"B4": 494,"C5": 523,"CS5": 554,"D5": 587,"DS5": 622,"E5": 659,
"F5": 698,"FS5": 740,"G5": 784,"GS5": 831,"A5": 880,"AS5": 932,"B5": 988,"C6": 1047,"CS6": 1109,
"D6": 1175,"DS6": 1245,"E6": 1319,"F6": 1397,"FS6": 1480,"G6": 1568,"GS6": 1661,"A6": 1760,
"AS6": 1865,"B6": 1976,"C7": 2093,"CS7": 2217,"D7": 2349,"DS7": 2489,"E7": 2637,"F7": 2794,
"FS7": 2960,"G7": 3136,"GS7": 3322,"A7": 3520,"AS7": 3729,"B7": 3951,"C8": 4186,"CS8": 4435,
"D8": 4699,"DS8": 4978
        }

song = ["B0", "C1", "CS1", "D1", "DS1", "E1", "F1", "FS1", "G1", "GS1", "A1", "AS1", "B1", "C2", "CS2", "D2", "E2", "F2", "GS2", "AS2",
        "C3", "D3", "E3", "FS3", "GS3", "A3", "C4", "CS4", "D4", "DS4", "E4", "F4", "G4", "GS4", "AS4", "B4", "CS5", "D5", "E5", "FS5",
        "G5", "A5", "B5", "CS6", "DS6", "E6", "FS6", "G6", "A6", "B6", "C7", "CS7", "D7", "DS7", "F7", "G7", "GS7", "AS7", "B7", "CS8", "DS8"]

def callback(data,addr,ctrl):
    global ir_data
    global ir_addr

    if(data>0):
        ir_data=data
        ir_addr=addr
       
        if ir_data==0x43:
            if led.value()==True:
                print("Pause")
                led.value(0)
            else:
                print("Play")
                led.value(1)
            
           
    
        if  led.value()==True:
            led.value(0)
            rand = getRadnom(0,len(song)-1)
            songs = song[rand]
            tone = tones[songs]
            print("rand:",rand,"song",songs,"Tone",tone)
            playTone(tone,tone)
           
    
        else:
            print("power is off")
        
        ir_data=0
        print('data {:02x}'.format(data))
        


def playTone(frequency,duty):
   
    buzzer.duty_u16(duty)
    buzzer.freq(frequency)
    PlayRGB(True)
    sleep(0.1)
    buzzer.duty_u16(0)
    
    


def getRadnom(i, m):
    random_number = random.randint(i, m)
    return random_number


    
led = Pin(10,Pin.OUT)

rgb_led_num =   22
rgb_led_pin =   Pin(rgb_led_num, Pin.OUT)
rgb_led     =   NeoPixel(rgb_led_pin, 1) 


board_led = Pin('LED', Pin.OUT)
buzzer = PWM(Pin(12))
ir = NEC_16(Pin(15,Pin.IN),callback)
ir_data=0
ir_addr=0


def PlayRGB(play):
    max_lum=100
    red=0
    green=0
    blue=0
    while play:
        for i in range(0,max_lum):
            red=i
            blue=max_lum-i
            rgb_led[0]=(red,green,blue)
            rgb_led.write()
            time.sleep_ms(2)
        for i in range(0,max_lum):
            green=i
            red=max_lum-i
            rgb_led[0]=(red,green,blue)
            rgb_led.write()
            time.sleep_ms(2)
        for i in range(0,max_lum):
            blue=i
            green=max_lum-i
            rgb_led[0]=(red,green,blue)
            rgb_led.write()
            time.sleep_ms(2)
            play=False
        led.value(1)
        break
