import sys
import random

def get_data_from_chunk(chunk):
    values = []
    for line in chunk:
        splitted = line.split(";")
        bodypart = splitted[0]
        value = float(splitted[1])
        person = (int)(splitted[2].replace("p",""))
        values.append(value)
    return (person,values)

def load(path,shuffle=True,equalize=True,chunksize=16):
    inputs = []
    targets = []
    data_map = {}
    with open(path,"r") as infile:
        lines = infile.readlines()
        for i in range(0, len(lines), chunksize):
            chunk = lines[i:i + chunksize]
            data = get_data_from_chunk(chunk)
            if data[0] in data_map:
                data_map[data[0]].append(data[1])
            else:
                data_map[data[0]] = [data[1]]

    min_len = sys.maxint
    if equalize:
        for key in data_map:
            min_len = min(min_len,len(data_map[key]))

    for key in data_map:
        data_map[key] = data_map[key][:min_len]
        for item in data_map[key]:
            inputs.append(item)
            targets.append(key)

    if shuffle:
        zipped = list(zip(inputs,targets))
        random.shuffle(zipped)
        inputs,targets = zip(*zipped)

    inputs = list(inputs)
    targets = list(targets)
    return (inputs,targets)