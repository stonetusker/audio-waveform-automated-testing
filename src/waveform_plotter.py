import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def plot_waveform(file_path):
    sample_rate, data = wavfile.read(file_path)

    if data.ndim == 2:
        data = data[:, 0]  # Use first channel for stereo

    num_samples = len(data)
    duration = num_samples / sample_rate
    time = np.linspace(0, duration, num_samples)

    plt.figure(figsize=(12, 4))
    plt.plot(time, data)
    plt.xlabel('Time [seconds]')
    plt.ylabel('Amplitude')
    plt.title('Audio Waveform')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
