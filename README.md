import time
import r2r_adc as adc
import adc_plot as ap


mx = 3.18
dt = 0.0001
tm = 3.0

vls = []
tls = []


a = adc.R2R_ADC(mx, dt, False)

try:
    t0 = time.time()

    while time.time() - t0 < tm:
        v = a.get_sc_voltage()
        t = time.time() - t0

        vls.append(v)
        tls.append(t)

    ap.plot_voltage_vs_time(tls, vls, mx)

finally:
    a.deinit()
