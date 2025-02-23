#!/usr/bin/env python3
'''Lab 3 Example: Get free disk space'''

#Author ID:113561229

import subprocess

def free_space():
    # Launch the command to get free disk space
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE, 
                         shell=True)
    
    
    output, error = p.communicate()

    if error:
        return f'Error: {error.decode("utf-8").strip()}'

    # Decode the output and strip newline characters
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
