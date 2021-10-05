import csv
import matplotlib.pyplot as plt
from tracker import statChecker

partPants = []
cur = []
partPS = []

with open('participants.csv') as partPants:
    partPants = csv.reader(partPants)

    for row in partPants:
        tempP = statChecker(row[0])
        cur.append(float(row[2])-(float(row[1])-tempP[2]))
        partPS.append(tempP[0])

plt.ylim(0,8.5)
plt.title('The Great Manga Race')
plt.xlabel('Participants')
plt.ylabel('Days Read Since Start of Race')
plt.bar(partPS, cur)
# plt.pie(cur, labels = partPS, autopct = '%.1f%%')
plt.show()