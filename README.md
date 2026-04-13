cd ~/Repositories
git clone git@github.com:SvinogonMaxim/get.git
cp -r ~/Repositories/get/get-led ~/Repositories/get-led-backup
ls ~/Repositories
mv ~/Repositories/get ~/Repositories/get_broken
mkdir -p ~/Repositories/get/get-led
cp -r ~/Repositories/get-led-backup/* ~/Repositories/get/get-led/
cd ~/Repositories/get
git status
git add get-led/pwm-led.py
git commit -m "Add PWM LED script"
git push
import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
gp.setup(leds, gp.OUT)
gp.output(leds, 0)
l_time = 0.2
while True:
    for led in leds:
        gp.output(led, 1)
        time.sleep(l_time)
        gp.output(led, 0)
    
    for led in reversed(leds):
        gp.output(led, 1)
        time.sleep(l_time)
        gp.output(led, 0)
    
