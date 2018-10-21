# -*- coding: utf-8 -*-
"""
    :author: 5km (十里)
    :url: https://www.smslit.top
    :copyright: © 2018 5km <5km@smslit.cn>
    :license: MIT, see LICENSE for more details.
"""
import os
import math
from PIL import Image


def get_binary_image(filename):
    '''得到二值化图片数据'''
    img = Image.open(filename).convert("P")
    # his = img.histogram()
    # his_10 = [(j, k) for j,k in sorted(enumerate(his), key=lambda x:x[1], reverse = True)[:10]]
    # print(his_10)
    
    threshold = [220, 227]
    binary_img = Image.new("P", img.size, 255)

    for x in range(img.size[1]):
        for y in range(img.size[0]):
            pix = img.getpixel((y,x))
            if pix in threshold:
                # these are the numbers to get
                binary_img.putpixel((y,x), 0)

    return binary_img


def save_binary_image(img_path, png=False):
    '''保存二值化图片'''
    bimg = get_binary_image(img_path)
    if png:
        bimg_path = 'b_code.png'
    else:
        bimg_path = 'b_' + img_path
    bimg.save(bimg_path)
    
    return bimg_path


def slice_image(bimg):
    '''通过传入的二值化图片数据进行纵向切图，得到每个字符的分割图，并返回图片数量'''
    letters = []
    foundletter = False
    letter_start = 0
    letter_end = 0
    for x in range(bimg.size[0]):
        pixelist = [bimg.getpixel((x, y)) for y in range(bimg.size[1])]
        has_p = 0 in pixelist
        if foundletter == False and has_p == True:
            foundletter = True
            letter_start = x
        if foundletter == True and has_p == False:
            foundletter = False
            letter_end = x
            letters.append((letter_start, letter_end))
    
    for letter in letters:
        img = bimg.crop((letter[0], 0, letter[1], bimg.size[1]))
        yield img


class VectorCompare:
    '''向量空间类'''
    def magnitude(self, concordance):
        '''计算矢量大小'''
        total = 0
        for count in concordance.values():
            total += count ** 2
        return math.sqrt(total)

    def relation(self, concordance1, concordance2):
        '''计算矢量之间的 cos 值'''
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2.keys():
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


def build_vector(img):
    '''将图片转换为矢量'''
    vector = {}
    count = 0
    for i in img.getdata():
        vector[count] = i
        count += 1
    return vector


def load_iconset(iconset, dir_path='./iconset'):
    '''加载训练集数据'''
    imageset = []
    for letter in iconset:
        letter_dir = os.path.join(dir_path, letter)
        for img in os.listdir(letter_dir):
            temp = []
            if '.gif' in img:
                img_path = os.path.join(letter_dir, img)
                letter_image = Image.open(img_path)
                temp.append(build_vector(letter_image))
                imageset.append({letter: temp})
    
    return imageset


def guess_image_by(imageset, bimg):
    '''根据样本数据识别'''
    guess = []
    v = VectorCompare()

    for img in slice_image(bimg):
        for image in imageset:
            for x, y in image.items():
                if len(y) != 0:
                    guess.append(( v.relation(y[0],build_vector(img)), x))
        guess.sort(reverse=True)
        yield guess[0]


def image_to_string(filename):
    bimg = get_binary_image(filename)
    iconset = [
        '0', '1', '2', '3','4', '5', '6', '7', '8', '9',
        '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
        't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    imageset = load_iconset(iconset)
    s = ''
    for guess_tuple in guess_image_by(imageset, bimg):
        s += guess_tuple[1]
    return s

    
if __name__ == '__main__':
    print(image_to_string('code.gif'))