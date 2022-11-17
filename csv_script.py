import os, glob
import csv

with open('writeups.csv', 'w', encoding='UTF8') as f:

    path = './writeups_dataset'
    
    # Use this header if you're using data_creation_three_col
    #header = ['Writeup_name', 'Category', 'Text', 'Overview', 'Analysis', 'Attack_execution']
    
    # Use this header if you're using data_creation_one_col
    header = ['Writeup_name', 'Category', 'Text', 'Label']
    
    
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)


    def data_creation_three_col(writeup_name, category, text, tag):
        data = ''
        if(tag == "Overview" or tag == "overview"):
            data = [writeup_name.replace(path, '').replace('/', '').replace('.txt', ''), 'web', text, 1, 0, 0]
        if(tag == "Analysis" or tag == "analysis"):
            data = [writeup_name.replace(path, '').replace('/', '').replace('.txt', ''), 'web', text, 0, 1, 0]
        if(tag == "Attack Execution" or tag == "AttackExecution" or tag == "attack execution"):
            data = [writeup_name.replace(path, '').replace('/', '').replace('.txt', ''), 'web', text, 0, 0, 1]
        writer.writerow(data)
        
    def data_creation_one_col(writeup_name, category, text, tag):
        data = ''
        if(tag == "Overview" or tag == "overview"):
            data = [writeup_name.replace(path, '').replace('/', '').replace('.txt', ''), 'web', text,'overview']
        if(tag == "Analysis" or tag == "analysis"):
            data = [writeup_name.replace(path, '').replace('/', '').replace('.txt', ''), 'web', text, 'analysis']
        if(tag == "Attack Execution" or tag == "AttackExecution" or tag == "attack execution"):
            data = [writeup_name.replace(path, '').replace('/', '').replace('.txt', ''), 'web', text, 'attack_execution']
        writer.writerow(data)



    # Iterate over all txt files in the directory
    for filename in glob.glob(os.path.join(path, '*.txt')):
        #print(filename)
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            lines_list = []
            for line in f:
                if(line != '\n' and not line.isspace()):
                    lines_list.append(line)
                
            text = ""
            tag = ""
            
            for line in lines_list:
                # Tag line
                if(line[0] == '#'):
                    if(len(text) != 0):
                        data_creation_one_col(filename, 'web', text, tag)
                        text = ''
                    string = ''.join(line)
                    tag = string.replace('# ', '').replace('#', '').replace(' ', '').replace('\n', '')
                # Not Tag line
                else:
                    new_line = ''.join(line)
                    text = text + new_line
                if(len(lines_list) -1 == lines_list.index(line)):
                    data_creation_one_col(filename, 'web', text, tag)