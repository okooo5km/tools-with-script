# -*- coding: utf-8 -*-
"""
    :author: 5km (十里)
    :url: https://www.smslit.top
    :copyright: © 2018 5km <5km@smslit.cn>
    :license: MIT, see LICENSE for more details.
"""
import markdown
import os.path as op
from bs4 import BeautifulSoup


class Markdown2Html:
    def __init__(self, cssfile=None):
        '''
        初始化 Markdown2Html 类，可传入特定 css 文件作为样式
        '''
        self.headTag = '<head><meta charset="utf-8" /></head>'
        if cssfile:
            self.setStyle(cssfile)

    def setStyle(self, cssfile=None):
        '''
        设置样式表文件
        '''
        if cssfile is None:
            self.headTag = '<head><meta charset="utf-8" /></head>'
        else:
            with open(cssfile, 'r') as f:
                css = f.read()
                self.headTag = self.headTag[:-7] \
                    + f'<style  type="text/css">{css}</style>' \
                    + self.headTag[-7:]

    def convert(self, infile, outfile=None, prettify=False):
        '''
        转换文件
        '''
        if not op.isfile(infile):
            print('请输入正确的 markdown 文件路径！')
            return

        if outfile is None:
            outfile = op.splitext(infile)[0] + '.html'

        with open(infile, 'r', encoding='utf8') as f:
            markdownText = f.read()

        rawhtml = self.headTag + markdown.markdown(
            markdownText, output_format='html5', extensions=['extra'])

        if prettify:
            prettyHtml = BeautifulSoup(rawhtml, 'html5lib').prettify()
            with open(outfile, 'w', encoding='utf8') as f:
                f.write(prettyHtml)
        else:
            with open(outfile, 'w', encoding='utf8') as f:
                f.write(rawhtml)


if __name__ == '__main__':
    m2h = Markdown2Html('github.css')
    m2h.convert('./README.md', './README.html')
