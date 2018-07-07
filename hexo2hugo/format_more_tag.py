#!/usr/local/bin/python3

import os
import sys

def parse_sys_args():
    args = sys.argv
    if len(args) != 2:
        print(f'Usage:\n  {args[0]} [path_name]\n')
        sys.exit(1)
    else:
        if os.path.isdir(args[1]):
            return args[1]

def format_more_split(path):
    with open(path, 'r') as mdfile:
        lines = mdfile.readlines()
    has_more = False
    for line in lines:
        if '<!--' in line and 'more' in line:
            index = lines.index(line)
            lines[index] = '<!--more-->\n'
            has_more = True
            break;
    if has_more:
        with open(path, 'w') as mdfile:
            mdfile.writelines(lines)
        print(f'{path} Done!')
    else:
        print(f'{path} has no split string!')

if __name__ == '__main__':
    path = parse_sys_args()
    files = os.listdir(path)
    mdfiles = []
    for f in files:
        if '.md' in f:
            mdfiles.append(os.path.join(path, f))

    print(mdfiles)
    for f in mdfiles:
        format_more_split(f)

