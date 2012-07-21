import os, sys, csv, datetime, random 


class CsvConverter(object):
    '''An object that takes all csv files in a directory
    and parses it into a confluence wiki style'''

    def __init__(self):
        '''Sets up init variables '''
        self.new_dir = self.make_dir()
        self.today, self.tomorrow = self.create_date_string()
        self.important_values = (1, 5, 6, 7, 8, 9, 10, 13)
        self.files = self.gather_files()

    def gather_files(self):
        '''gathers all files in the directory'''
        return [files for files in os.listdir('.') if files.count('.csv')]

    def convert_files(self):
        '''Main function that loops through each file and converts them'''
        for csv in self.files:
            self.convert_single_file(csv)


    def convert_single_file(self, csv_file):
        '''Converts a single file, this function starts a loop'''
        fixed_data = list()
        raw_data = self.read_file(csv_file) 
        self.parse_file(fixed_data, raw_data) 
        self.write_new_file(fixed_data, csv_file)
        print 'Finish converting {0}'.format(csv_file)

    
    def read_file(self, csv_file):
        '''reads csv file, and gathers raw data '''
        f_read = open(csv_file, 'rU')
        data = [line for line in csv.reader(f_read)]
        f_read.close()
        return data
        

    def parse_file(self, fixed_data, raw_data): 
        '''fucntion that parses raw data into fixed data '''
        check = ''
        for x in raw_data:
            if x[0] == 'PNR_ID':
                result = [x[i] for i in self.important_values]
                fixed_data.append(result)    
                continue
            if x[9] == self.today or x[9] == self.tomorrow:  
                if not x[0] == check:
                    result = [x[i] for i in self.important_values]
                    fixed_data.append(result)    
                    check = x[0]
                else:
                    continue
            else:
                continue


    def write_new_file(self, fixed_data, csv_file):
        '''writes the new file into a directory'''        
        new_file_name = csv_file.replace('.csv', '').upper()
        new_file = open(os.path.join(self.new_dir, new_file_name), 'w')

        
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



    def make_dir(self):
        today = str(datetime.date.today())
        if not os.path.exists(today):
            os.makedirs(today)
        return today



    def format_date_string(self, date):
        a = date.strftime('%d, %b').upper()
        b = a.replace(',', '').replace(' ', '')
        return b

    def create_date_string(self):
        #Create Date String
        today = datetime.date.today()
        tomorrow = today  + datetime.timedelta(days=1)
        today_format = self.format_date_string(today)
        tomorrow_format = self.format_date_string(tomorrow)
        return today_format, tomorrow_format

if __name__ == "__main__":
    Csv_Converter = CsvConverter()
    Csv_Converter.convert_files()

