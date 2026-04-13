and GPIO.input(down):
            num = 255
            print(num, dec2bin(num))
            time.sleep(sleep_time)

        elif GPIO.input(up):
            num = num + 1
            if num > 255:
                num = 0
            print(num, dec2bin(num))
            time.sleep(sleep_time)

        elif GPIO.input(down):
            num = num - 1
            if num < 0:
                num = 0
            print(num, dec2bin(num))
            time.sleep(sleep_time)
