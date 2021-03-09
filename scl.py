import pandas as pd
import csv
from colorama import init,Fore

data = pd.read_json('contacts.json')

i=0
j=0

id = []
contacts = []

file = open('traces.csv','w') 

writer = csv.writer(file)
writer.writerow(['Ticket ID', 'Ticket Trace'])
for i in range(len(data)):
  trace = []
  trace.append(data.loc[i]['Id'])
  id.append(data.loc[i]['Id'])
  contacts.append(data.loc[i]['Contacts'])
  for j in range(len(data)):
      if(i == j):
        pass
      else:
        # print(i,j)
        if((data.loc[i]['Email'] == '' and data.loc[j]['Email'] == '') or (data.loc[i]['Phone'] == '' and data.loc[j]['Phone'] == '')):
          pass
        else:
          if(data.loc[i]['Email'] != data.loc[j]['Email']) or (data.loc[i]['Phone'] != data.loc[j]['Phone']):
            print(Fore.GREEN + '[',i,j,'] ' + Fore.YELLOW + data.loc[i]['Email'] + ' '+ data.loc[i]['Phone'] +' -> ' + data.loc[j]['Email'] + ' '+ data.loc[j]['Phone'] + '[No Duplicate Found]')
          if((data.loc[i]['Email'] == data.loc[j]['Email']) or (data.loc[i]['Phone'] == data.loc[j]['Phone'])):
            print(Fore.RED + '[',i,j,'] ' + Fore.YELLOW + data.loc[i]['Email'] + ' '+ data.loc[i]['Phone'] +' -> ' + data.loc[j]['Email'] + ' '+ data.loc[j]['Phone']+ '[Duplicate Found]')
            contacts[i] += data.loc[j]['Contacts']
            trace.append(data.loc[j]['Id'])
          
  trace.sort()
  trace = "-".join(map(str, trace))
  writer.writerow([id[i], str(trace) + ',' + str(contacts[i])])
file.close()