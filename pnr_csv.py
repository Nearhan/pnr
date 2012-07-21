## Script to convert CVS and write to a file!

import sys
import csv
import datetime
import os
import random


today = str(datetime.date.today())
f_read = open(sys.argv[1], 'rU')

erica_joke = ['Doctor Who', 'Germany Darkness', 'Smelly Cheese']
random.shuffle(erica_joke) 
joke = 'Erica Loves %s'% (erica_joke.pop())
print joke
#make a new directory for the date 
if not os.path.exists(today):
    os.makedirs(today)

#read from csv
data = [x for x in csv.reader(f_read)]
f_read.close()


#fix up data 
fixed_data = list()
important_values = (1, 5, 6, 7, 8, 9, 10, 13)


#Create Date String
def create_date_string():
    today = datetime.date.today()
    tomorrow = today  + datetime.timedelta(days=1)
    today_format = format_date_string(today)
    tomorrow_format = format_date_string(tomorrow)
    return today_format, tomorrow_format


def format_date_string(date):
    a = date.strftime('%d, %b').upper()
    b = a.replace(',', '').replace(' ', '')
    return b



#Remove duplicate entries and check for today's or tomororows date

current_date, tomorrows_date = create_date_string()

check = ''
for x in data:
    if x[0] == 'PNR_ID':
        result = [x[i] for i in important_values]
        fixed_data.append(result)    
        continue
    if x[9] == current_date or x[9] == tomorrows_date:  
        if not x[0] == check:
            result = [x[i] for i in important_values]
            fixed_data.append(result)    
            check = x[0]
        else:
            continue
    else:
        continue


#Create new File name based on date
string = str(sys.argv[1])
new_file_name =today+'/'+ string 
new_file =open(new_file_name, 'w')

#Write to the new file
for x in range(len(fixed_data)):
    for y in range(len(fixed_data[x])):
        if x == 0:
            if y == 6:
                replaced_string = fixed_data[x][y].replace('Passengers', 'Passengers : LastName/FirstName')
                new_file.write('||'+replaced_string+'||')
            else:
                new_file.write('||'+fixed_data[x][y]+'||')
        elif y == 0:
            new_file.write('|'+fixed_data[x][y]+'|') 
        elif y == 6: 
            strip_new_line = fixed_data[x][y].replace('\n', '  ')
            passenger_string = strip_new_line.replace('.01', ' ')
            new_file.write(passenger_string +'|') 
        else:
            new_file.write(fixed_data[x][y]+ '|')
    new_file.write('\n')

#Close File stream
new_file.close()
