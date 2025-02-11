# The Music Box - Remote-Controlled Musical Device

## Overview

The Music Box is a remote-controlled device that plays random musical notes using a Pico-Sensor kit and Python. The project integrates hardware components, including a buzzer, LED, and RGB lights, to create an engaging and interactive musical experience.

## Features

- Remote-controlled musical note generation
- LED and RGB light synchronization with music
- Play/Pause functionality for user control
- Randomized note playback for variety
- Wireless interaction using a Pico microcontroller

## Hardware & Materials

- Raspberry Pi Pico
- IR Remote Control
- Buzzer
- RGB LED Strip
- Standard LED
- Resistors and Wiring
- Power Supply

## Software Dependencies

Ensure you have the following Python libraries installed:

```bash
pip install machine utime neopixel
```

## Implementation Steps

1. Turn on the device using the remote's Play/Pause button.
2. The red LED indicates the device's status: ON (active) or OFF (paused).
3. Each button press plays a random note via the buzzer and triggers an RGB light show.
4. The red LED turns on and off in sync with playback.

## Code Snippet (Example)

```python
from machine import Pin, PWM
from utime import sleep
import random

buzzer = PWM(Pin(12))
tones = {"C4": 262, "D4": 294, "E4": 330, "F4": 349, "G4": 392, "A4": 440, "B4": 494}

def play_note():
    note = random.choice(list(tones.values()))
    buzzer.freq(note)
    buzzer.duty_u16(30000)
    sleep(0.5)
    buzzer.duty_u16(0)

while True:
    play_note()
    sleep(1)
```

## Testing

- **Signal Transmission:** Verified that button presses successfully transmit signals to the Pico microcontroller.
- **Play/Pause Functionality:** Ensured accurate toggling of the device.
- **LED & RGB Response:** Checked synchronization with remote button presses.

## Future Improvements

- Add a feature to allow users to assign specific musical notes to remote buttons.
- Implement a setting mode for user-defined sound effects.

## Conclusion

The Music Box successfully combines hardware and software to create an interactive musical experience. The integration of the Pico-Sensor kit with Python demonstrates the seamless interaction between embedded systems and software programming.
