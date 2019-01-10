# textGO

textGO 是利用百度 AI 免费的 OCR 服务进行图片中文字识别的工具。

详情参考：[python 实现命令行工具 textGO]()

## 使用方法

1. 参考 [只要10分钟 快速掌握文字识别](http://ai.baidu.com/forum/topic/show/867951) 获取自己的 api_key 和 secret_key，编辑文件 `config.json` 将这两个 key 配置到相应位置。

2. 调用命令查看帮助，按照帮助使用即可：

    ```Shell
    $ python3 ./textGO/textGO.py -h

    usage: textGO.py [-h] [-c CONFIG] img

    OCR 识别图片中的文字

    positional arguments:
      img                   指定要识别的图片

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            指定配置文件
    ```
