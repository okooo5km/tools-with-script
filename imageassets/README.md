# imageassets

一个生成苹果平台图标文件的工具，可以转换指定图片或者指定目录下的 png 图片为标准尺寸的图片集，默认生成三种尺寸的文件：

- 18x18 px
- 36x36 px
- 54x54 px

**注：**

- 当前以命令行工具的形式使用，还未添加生成指定尺寸的命令参数支持
- 原始图片尽量大

## 使用方法

```shell
python3 imageassets/imageassets.py --help
usage: imageassets.py [-h] path

一款生成图片集的小工具

positional arguments:
  path        指定图片的目录或者图片文件

optional arguments:
  -h, --help  show this help message and exit
```

## 更新计划清单

- [ ] 指定生成图片的基本尺寸，单位：像素
- [ ] 指定生成图片的基本尺寸的最大倍数，比如指定为 2，就会生成一张基本尺寸的图片和一张 2 倍于基本尺寸的图片
- [ ] 指定输出目录