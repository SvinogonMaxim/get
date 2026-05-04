import time 
import mcp3021_driver as mcp 
import adc_plot as ap

a = 5.173
dt = 8.0

adc = mcp.MCP3021(a, False)

u = [] 
t = []

try: 
    t0 = time.perf_counter()

    while time.perf_counter() - t0 < dt:
        x = time.perf_counter() - t0
        y = adc.get_voltage()

        t.append(x)
        u.append(y)

    ap.plot_voltage_vs_time(t, u, a)
    ap.plot_sampling_period_hist(t)
finally: 
    adc.deinit()