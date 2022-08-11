#!/usr/bin/python3

count = 0

with open('dracula.txt', 'r') as fo:
    with open('vampytimes.txt', 'w') as nfo:
        for line in fo:
            if 'vampire' in line.lower():
                print(line)
                count += 1
                nfo.write(line)
print(count)
