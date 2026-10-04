import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def plot_data(data_list, num_analog, num_digital):
    fig, axes = plt.subplots(num_analog + num_digital, 1, figsize=(10, 8))

    def animate(i):
        for ax in axes:
            ax.clear()

        if data_list:
            x = list(range(len(data_list)))
            analog_values = [d[0] for d in data_list]
            digital_values = [d[1] for d in data_list]

            for i in range(num_analog):
                ax = axes[i]
                ax.plot(x, [vals[i] for vals in analog_values], label=f'Analog {i+1}', color='r')
                ax.set_xlabel('Data Point')
                ax.set_ylabel('Value')
                ax.legend(loc='upper right')
                ax.set_title(f'Analog Sensor {i+1} Data')

            for i in range(num_digital):
                ax = axes[num_analog + i]
                ax.plot(x, [vals[i] for vals in digital_values], label=f'Digital {i+1}', color='g')
                ax.set_xlabel('Data Point')
                ax.set_ylabel('Value')
                ax.legend(loc='upper right')
                ax.set_title(f'Digital Sensor {i+1} Data')

    ani = FuncAnimation(fig, animate, interval=1000)
    plt.tight_layout()
    plt.show()
