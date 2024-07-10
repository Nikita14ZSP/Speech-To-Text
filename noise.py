import matplotlib.pyplot as plt

noise_levels = [0, 10, 20, 30, 40, 50]
kaldi_performance = [8, 10, 12, 15, 18, 20]
deepspeech_performance = [15, 18, 22, 26, 30, 35]
wav2letter_performance = [7, 9, 12, 15, 19, 23]

plt.figure(figsize=(10, 6))
plt.plot(noise_levels, kaldi_performance, label='Kaldi', marker='o')
plt.plot(noise_levels, deepspeech_performance, label='DeepSpeech', marker='o')
plt.plot(noise_levels, wav2letter_performance, label='Wav2Letter++', marker='o')

plt.xlabel('Noise Level (dB)')
plt.ylabel('WER')
plt.title('Performance Over Different Noise Levels')
plt.legend()
plt.grid(True)
plt.show()
