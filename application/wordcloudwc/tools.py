import pandas as pd

def dicfromfile(path):
    text_dict = {}
    with open(path, encoding='utf8') as f:
        for line in f:
            cell = line.split(' ')
            text_dict[str(cell[0])] = int(cell[1])
    return text_dict

def dicfromcsv(path):
    text_dict = {}
    data = pd.read_csv(path, sep=',', header=None).values
    for line in data:
        text_dict[str(line[0])] = int(line[1])

    return text_dict

def dicfromexcel(path):
    text_dict = {}
    data = pd.read_excel(path, header=None).values
    for line in data:
        text_dict[str(line[0])] = int(line[1])

    return text_dict

if __name__ == '__main__':
    # print(dicfromcsv('./4chinese/wcinput.csv'))
    print(dicfromexcel('4chinese/data/wcinput.xlsx'))