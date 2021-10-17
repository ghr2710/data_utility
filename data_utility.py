#1 usr/bin/env python3

import csv

def read(file):
    save_data = []
    with open(file, "r", newline = "") as data:
        reader = csv.reader(data)
        for read in reader:
            save_data.append(read)
            
    return save_data

def write(save_data, file):
    with open(file, "w", newline = "") as data:
        writer = csv.writer(data)
        writer.writerows(save_data)


if __name__ == "__main__":
    main()

    










    
