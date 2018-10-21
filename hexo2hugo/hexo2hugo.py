#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
    :author: 5km (十里)
    :url: https://www.smslit.top
    :copyright: © 2018 5km <5km@smslit.cn>
    :license: MIT, see LICENSE for more details.
"""
import os

DIR_PATH = '.'

def format_md_file(md_file, if_new_path=True):
    ''' 按照hugo头信息格式格式化md文件头
    :param md_file: md文件
    :type md_file: unicode字符串
    '''
    print(f'format {md_file} ...')
    if if_new_path:
        path_s = list(os.path.split(md_file))
        new_dir = os.path.join(path_s[0], 'converted')
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        new_path = os.path.join(new_dir, path_s[1][11:])
        print(new_path)
    with open(md_file, 'r') as f:
        lines = f.readlines()
    head_begin = False
    lines2 = lines.copy()
    old_head = ''
    new_head = ''
    for line in lines:
        lines2.pop(0)
        old_head += line
        if not head_begin:
            if '---' in line:
                head_begin = True
        else:
            if '---' in line:
                new_head += line            
                break
            else:
                if 'layout:' in line: 
                    line = ''
                elif 'author:' in line:
                    line = ''
                elif 'tags:' in line:
                    tag_line = line[:-1].split(':')
                    if (not '[' in line) and (tag_line[1].strip() != ''):
                        tags = f'[{tag_line[1]}]'
                        line = tag_line[0] + ': ' + tags + '\n'
                elif 'categories:' in line:
                    tag_line = line[:-1].split(':')
                    if (not '[' in line) and (tag_line[1].strip() != ''):
                        tags = f'[{tag_line[1]}]'
                        line = tag_line[0] + ': ' + tags + '\n'
                elif 'date:' in line:
                    date_time = line[:-1].replace('date:', '').strip()
                    if not '+08:00' in date_time:
                        if '+0800' in date_time:
                            date_time = date_time.replace('+0800', '+08:00')
                            line = f'date: {date_time}\n'
                        else:
                            line = f'date: {date_time} +08:00\n'
        new_head += line            
    print(old_head, '\n\t|\n\tv\n', new_head)
    lines2.insert(0, new_head)
    with open(new_path if if_new_path else md_file, 'w') as f:
        f.writelines(lines2)
    print('Done!\n')


if __name__ == '__main__':
    dir_path = os.path.join(os.path.expanduser('~'), 'Downloads/post')
    for path in os.listdir(dir_path):
        file_path = os.path.join(dir_path, path)
        if os.path.isfile(file_path):
            if '.md' in file_path:
                format_md_file(file_path)
