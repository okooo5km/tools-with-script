import os
from PIL import Image


class MessageImage:
    """ MessageImage 类
        初始化加载图片或者手动打开图片，将隐写信息写入图片，也可以解析图片中的隐写信息
    Attributes:
        image: 打开图片的 Image 类型对象
        pkghead: 写入图片隐写信息的头标记，可以初始化时赋值
    """

    def __init__(self, imgpath, pkghead=None):
        if imgpath:
            self.open(imgpath)
        else:
            self.image = None
        if pkghead:
            self.pkghead = pkghead
        else:
            self.pkghead = 0x5555AAAA

    def sethead(self, pkghead):
        if pkghead:
            self.pkghead = pkghead

    def open(self, imgpath):
        try:
            self.image = Image.open(imgpath).convert('RGBA')
            self.imgpath = imgpath
        except:
            self.image = None

    def encode(self, info, save=True, show=False):
        if self.image is None:
            print('图片为空，请调用实例的 open 方法打开一张图片！')
            return False
        pkgbytes = self.__pack(info)
        self.__putdata(pkgbytes)
        if save:
            pathlist = os.path.splitext(self.imgpath)
            newpath = pathlist[0] + '_code' + pathlist[1]
            print(newpath, end=' ')
            self.image.save(newpath)
        if show:
            self.image.show()
        return True

    def decode(self):
        if self.image is None:
            print('图片为空，请调用实例的 open 方法打开一张图片！')
            return None        
        return self.__unpack()

    def freespace(self):
        """
        查看图片存储隐藏数据的可用空间，单位 byte
        """
        if self.image is None:
            print('图片为空，请调用实例的 open 方法打开一张图片！')
            return 0
        size = self.image.size
        return int(size[0] * size[1] / 2)

    def __even(self, image):
        """
        将图片中像素数据的 RGBA 值偶数化，即清零
        """
        pixels = list(image.getdata())
        evenpixels = [(r>>1<<1,g>>1<<1,b>>1<<1,t>>1<<1) for [r,g,b,t] in pixels]
        return evenpixels

    def __pack(self, info):
        """
        打包数据，转换为待写入图片的字节数据组，并返回
        """
        tagbytes = self.pkghead.to_bytes(4, 'little')
        databytes = bytearray(info, 'utf8')
        lengthbytes = len(databytes).to_bytes(4, 'little')
        pkgbytes = tagbytes + lengthbytes + databytes
        return pkgbytes

    def __putdata(self, pkgbytes):
        evenpixels = self.__even(self.image)
        freespace = self.freespace()
        if len(pkgbytes) > freespace:  # 超出全部数据空间， 抛出异常
            raise Exception("错误: 不能载入超过 " + freespace + " 字节的数据到图片中。")
        for index, byte in enumerate(pkgbytes):
            _index = 2 * index
            evenpixels[_index] = tuple([v + (((byte & 0x0F) >> i) & 0x01)  for i, v in enumerate(evenpixels[_index])])
            _index += 1
            evenpixels[_index] = tuple([v + (((byte >> 4) >> i) & 0x01)  for i, v in enumerate(evenpixels[_index])])
        newimg = Image.new(self.image.mode, self.image.size)
        newimg.putdata(evenpixels)
        self.image = newimg

    def __getdata(self, start, stop):
        start = (start - 1) if start % 2 else start
        pixels = list(self.image.getdata())
        pkgbytes = bytearray()
        for i in range(start, stop):
            (r, g, b, a) = tuple([v & 0x01 for v in pixels[2 * i]])
            v = r | (g << 1) | (b << 2) | (a << 3)
            (r, g, b, a) = tuple([v & 0x01 for v in pixels[2 * i + 1]])
            v |= (r << 4) | (g << 5) | (b << 6) | (a << 7)
            pkgbytes.append(v.to_bytes(4, 'little')[0])
        return pkgbytes  

    def __unpack(self):
        pkgbytes = self.__getdata(0, 8)
        pkghead = int.from_bytes(pkgbytes[0:4], 'little')
        if pkghead == self.pkghead:
            length = int.from_bytes(pkgbytes[4:8], 'little')
            pkgbytes = self.__getdata(8, 8 + length)
            info = str(pkgbytes, encoding='utf8')
            return info
        else:
            return None


if __name__ == '__main__':
    mi = MessageImage('demo.png')
    mi.encode('你好，世界！hello, world!')
    mi.open('demo_code.png')
    print(mi.decode())