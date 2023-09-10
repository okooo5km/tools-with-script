# hexo2hugo

此脚本主要是转换markdown文章中头信息的格式，方便将hexo文章向hugo迁移，毕竟hugo是个神速渲染的静态博客工具。

详情参考：[hexo博客迁移到hugo](https://blog.5km.studio/2018/07/07/hexo2hugo/)

## 使用

主要修改 `dir_path` 为存储文章的目录，就可以批处理文章中的头信息，这里实现的非常粗糙，可能会遇到各种问题，主要关注头信息中的以下信息：

- tags
- categories
- date
- 去除layout和author

也可以单独使用函数 `format_md_file`，其中第二个参数是是否更改名称，若修改文件名称，是以文件名最前面以年月日开头的，比如`2018-05-02-test.md`，局限性大一些，可以自行修改函数；若不修改就是替换源文件。


