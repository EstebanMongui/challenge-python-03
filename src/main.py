# Resolve the problem!!

import re

def run():
    # Start coding here  
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        pattern = re.compile(r'[a-z]')
        for line in f:
            match = pattern.findall(line)
        print (''.join(match))

if __name__ == '__main__':
    run()


