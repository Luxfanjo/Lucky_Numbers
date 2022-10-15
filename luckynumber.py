
import random
import datetime

x = datetime.datetime.now()
i = 0

if x.strftime("%A")=="Monday":
    hpyCls = list(range(31))
    random.shuffle(hpyCls)
    print(f'{x.strftime("%d")} szczęśliwy numerek to: {hpyCls[i]}')
    i += 1
elif x.strftime("%A")=="Tuesday":
    hpyCls = list(range(31))
    random.shuffle(hpyCls)
    print(f'{x.strftime("%d")} szczęśliwy numerek to: {hpyCls[i]}')
    i += 1
elif x.strftime("%A")=="Wednesday":
    hpyCls = list(range(31))
    random.shuffle(hpyCls)
    print(f'{x.strftime("%d")} szczęśliwy numerek to: {hpyCls[i]}')
    i += 1
elif x.strftime("%A")=="Thurdsday":
    hpyCls = list(range(31))
    random.shuffle(hpyCls)
    print(f'{x.strftime("%d")} szczęśliwy numerek to: {hpyCls[i]}')
    i += 1
elif x.strftime("%A")=="Friday":
    hpyCls = list(range(31))
    random.shuffle(hpyCls)
    print(f'{x.strftime("%d")} szczęśliwy numerek to: {hpyCls[i]}')
    i += 1
elif x.strftime("%A")=="Saturday":
    print(f'{x.strftime("%x")} Dzisiejszy dzień jest dniem wolnym')
    
elif x.strftime("%A")=="Sunday":
    print(f'{x.strftime("%x")} Dzisiejszy dzień jest dniem wolnym')

