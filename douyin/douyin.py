#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
    :author: 5km (十里)
    :url: https://www.smslit.top
    :copyright: © 2018 5km <5km@smslit.cn>
    :license: MIT, see LICENSE for more details.
"""
import os
import imageio
import numpy as np
from PIL import Image

PIC_PATH = 'glasses.jpg'

def convert_douyin_image(pic_path, offset=10):
    '''为普通图片添加红蓝溢出位移效果，抖音app效果
    :param pic_path: 图片路径
    :type pic_path: unicode字符串
    :param offset: 红蓝位移大小，单位像素，默认值是10
    :return r_pic_path: 返回转换图片的路径
    :rtype: unicode字符串
    '''
    if os.path.exists(pic_path):
        pic_name, extension = os.path.splitext(pic_path)
        pic_path_new = pic_name + '_' + str(offset) + extension
        img_data = Image.open(pic_path)
        img_array = np.array(img_data)
        if offset > 0:
            img_r = np.copy(img_array)
            img_gb = np.copy(img_array)
            img_r[:-offset, :-offset, 1:3] = 0
            img_gb[offset:, offset:, 0] = 0
            img_array[:-offset, :-offset, :] = img_r[:-offset, :-offset, :] + img_gb[offset:, offset:, :]
        image = Image.fromarray(img_array)
        image.save(pic_path_new)
        print(f'Saved {pic_path_new}!')
        return pic_path_new

def create_gif(image_list, gif_name):
    '''创建gif图片
    :param image_list: 图片名称列表
    :type image_list: list
    :param gif_name: gif图片路径
    :type gif_name: unicode字符串
    '''
    print(f'\nCreating 「{gif_name}」from {image_list} ...')
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.05)
    print(f'Saved {gif_name}!')


if __name__ == '__main__':
    pic_list = []
    for i in range(0, 11, 2):
        pic_path = convert_douyin_image(PIC_PATH, i)
        if pic_path:
            pic_list.append(pic_path)
    temp_l = list.copy(pic_list)
    temp_l.reverse()
    pic_list = pic_list + temp_l[1:]
    p_name, p_ext = os.path.splitext(PIC_PATH)
    gif_name = PIC_PATH.replace(p_ext, '.gif')
    create_gif(pic_list, gif_name)
    
