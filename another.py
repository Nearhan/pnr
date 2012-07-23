import os, datetime

directory = str(datetime.date.today())

print directory

wiki_file = open('wiki_file', 'w')
wiki_file.write('h1. Daily Pnrs')
wiki_file.write('\r')
wiki_file.write('\r')
wiki_file.write('\r')

def add_to_wiki(wiki):
    global wiki_file
    title = 'h3. {0} + Pnrs'.format(wiki)
    wiki_file.write(title)
    wii_file.write('\n')

    file_open = open('wiki', 'rb')
    for line in file_open.readlines():


for x in os.listdir(directory):
    add_to_wiki(x)
