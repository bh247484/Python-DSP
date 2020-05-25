import matplotlib.pyplot as plt
import matplotlib.style as style
import dsp_resources.mysignals as sig

style.use('ggplot')
style.use('dark_background')
fig, plt_arr = plt.subplots(3, sharex=True)
fig.suptitle('Multiplot')

plt_arr[0].plot(sig.InputSignal_1kHz_15kHz, color="magenta")
plt_arr[0].set_title('Subplot Uno', color="magenta")

plt_arr[1].plot(sig.InputSignal_1kHz_15kHz, color="yellow")
plt_arr[1].set_title('Subplot Dos', color="yellow")

plt_arr[2].plot(sig.InputSignal_1kHz_15kHz, color="red")
plt_arr[2].set_title('Subplot Tres', color="red")

plt.show()
