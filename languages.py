import matplotlib.pyplot as plt

languages = ['English', 'Spanish', 'German', 'French', 'Chinese', 'Japanese', 'Others']
support = [70, 50, 45, 40, 35, 30, 30]

plt.figure(figsize=(8, 8))
plt.pie(support, labels=languages, autopct='%1.1f%%', startangle=140)
plt.title('Language Support Across ASR Systems')
plt.show()
