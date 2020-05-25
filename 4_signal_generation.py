import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style

# Signal sampling rate = 20,000Hz

style.use('ggplot')

pi = np.pi

t = np.linspace(0, 1.0, 2001)

sig_5Hz = np.sin((2*pi)*5*t)
sig_250Hz = np.sin((pi)*250*t)

sig_summed = sig_5Hz + sig_250Hz

fig, arr = plt.subplots(3, sharex=True)
fig.suptitle("All Tree")

arr[0].plot(sig_5Hz)
arr[0].set_title("5 Hz")

arr[1].plot(sig_250Hz)
arr[1].set_title("250 Hz")

arr[2].plot(sig_summed)
arr[2].set_title("Summed")

plt.show()
