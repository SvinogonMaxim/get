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
