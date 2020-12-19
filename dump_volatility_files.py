

"""
takes a list of volatility dumpfiles and gets the -Q 
"""
import os

input_filename = "Johnbi.txt"

command = 'volatility --profile=Win7SP1x64 dumpfiles -f destroyed.elf -D dump/ --name file -Q '

with open(input_filename, "r") as in_file:
    input_data = in_file.readlines()

    phoffset = ''
    for line in input_data:
        phoffset = line.split(' ')[0].strip()
        print(f'processing {phoffset}')
        os.system(f'{command}{phoffset}')