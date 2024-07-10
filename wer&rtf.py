import matplotlib.pyplot as plt
import numpy as np

systems = ['DeepSpeech', 'Kaldi', 'PocketSphinx', 'Vosk', 'Julius', 'Coqui STT', 'Wav2Letter++']
wer = [15, 8, 25, 10, 20, 12, 7]
rtf = [0.8, 0.5, 0.1, 0.7, 0.2, 0.6, 0.3]
noise_resilience = [0.6, 0.9, 0.4, 0.7, 0.3, 0.8, 0.85]

x = np.arange(len(systems))
width = 0.25

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(x - width/2, wer, width, label='WER')
ax1.bar(x + width/2, rtf, width, label='RTF')
ax2.plot(x, noise_resilience, color='r', marker='o', label='Noise Resilience')

ax1.set_xlabel('ASR Systems')
ax1.set_ylabel('WER / RTF')
ax2.set_ylabel('Noise Resilience')
ax1.set_xticks(x)
ax1.set_xticklabels(systems)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.title('Comparison of ASR Systems')
plt.show()
