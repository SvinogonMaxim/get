import matplotlib.pyplot as plt


def plot_voltage_vs_time(t, v, mx):
    plt.figure(figsize=(10, 6))
    plt.plot(t, v)

    plt.title("График зависимости напряжения на входе АЦП от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")

    plt.xlim(0, max(t))
    plt.ylim(0, mx)

    plt.grid(True)
    plt.show()
