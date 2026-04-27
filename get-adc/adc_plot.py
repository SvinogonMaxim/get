import matplotlib.pyplot as plt

def plot_voltage_vs_time(t, v, mx): 
    plt.figure(figsize=(10, 6)) 
    plt.plot(t, v)

    plt.title("График зависимости напряжения на входе АЦП от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")

    plt.xlim(0, max(t))
    plt.ylim(0, mx + 0.05)

    plt.grid(True)
    plt.show()
def plot_sampling_period_hist(t): 
    dt = []

    for i in range(1, len(t)):
        dt.append(t[i] - t[i - 1])

    plt.figure(figsize=(10, 6))
    plt.hist(dt)

    plt.title("Распределение периодов дискретизации измерений\nпо времени на одно измерение")
    plt.xlabel("Период измерения, с")
    plt.ylabel("Количество измерений")

    plt.xlim(0, 0.06)

    plt.grid(True)
    plt.show()