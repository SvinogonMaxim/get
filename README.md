import r2r_dac as r2r
import time

d = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, False)

try:
    d.set_number(255)
    time.sleep(30)
finally:
    d.deinit()
