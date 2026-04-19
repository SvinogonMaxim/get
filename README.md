import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, pins, vmax, verbose=False):
        self.pins = pins
        self.vmax = vmax
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pins, GPIO.OUT, initial=0)

    def deinit(self):
        GPIO.output(self.pins, 0)
        GPIO.cleanup()

    def set_number(self, n):
        if not (0 <= n <= 255):
            print("Число выходит за диапазон ЦАП (0 - 255)")
            GPIO.output(self.pins, 0)
            return

        code = [int(x) for x in bin(n)[2:].zfill(8)]
        GPIO.output(self.pins, code)

        if self.verbose:
            print(f"Число на вход ЦАП: {n}, биты: {code}\n")

    def set_voltage(self, v):
        if not (0.0 <= v <= self.vmax):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.vmax:.2f} В)")
            GPIO.output(self.pins, 0)
            return

        n = int(v / self.vmax * 255)
        self.set_number(n)


if __name__ == "__main__":
    dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

    try:
        while True:
            try:
                v = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(v)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
