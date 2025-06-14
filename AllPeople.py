import os
from Main import makeDotToDot

for i, personpicture in enumerate(os.listdir('testimages/people')):
    print(f'{i}: {personpicture} to be made')

startFrom = int(input("Image To Start From: "))
for i, personpicture in enumerate(os.listdir('testimages/people')):
    if i >= startFrom:
        print(f'Making dot to dot of: {personpicture}')
        makeDotToDot('testimages/people/' + personpicture)
