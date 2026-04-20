import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, pin, freq, vmax, verbose=False): 
        self.pin = pin 
        self.freq = freq 
        self.vmax = vmax 
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT, initial=0)

        self.pwm = GPIO.PWM(self.pin, self.freq)
        self.pwm.start(0)

    def deinit(self):
        self.pwm.ChangeDutyCycle(0)
        self.pwm.stop()
        GPIO.cleanup()

    def set_voltage(self, v):
        if not (0.0 <= v <= self.vmax):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.vmax:.2f} В)")
            self.pwm.ChangeDutyCycle(0)
            return

        duty = v / self.vmax * 100
        self.pwm.ChangeDutyCycle(duty)

        if self.verbose:
            print(f"Коэффициент заполнения: {duty:.2f}\n")
if __name__ == "__main__": 
    dac = PWM_DAC(12, 500, 3.290, True)

    try:
        while True:
            try:
                v = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(v)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    except KeyboardInterrupt:
        pass

    finally:
        dac.deinit()