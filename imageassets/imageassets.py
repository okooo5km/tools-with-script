import os
import argparse

from PIL import Image


def get_args():
    """获取命令行参数

    Returns:
        [type] -- 参数类
    """
    parser = argparse.ArgumentParser(description="一款生成图片集的小工具")
    parser.add_argument('path', help="指定图片的目录或者图片文件")
    return parser.parse_args()


def img_resize(infile, basesize=(18, 18), maxtimes=3):
    """针对指定图片生成指定尺寸图片

    Arguments:
        infile {string} -- 图片的路径

    Keyword Arguments:
        basesize {tuple} -- 最小尺寸 (default: {(18, 18)})
        maxtimes {int} -- 生成图片尺寸的最大倍数 (default: {3})
    """
    if not os.path.exists(infile):
        print(f"{infile} 不存在!")
        return
    if not os.path.isfile(infile):
        print(f"{infile} 不是文件!")
        return
    if not infile.endswith(".png"):
        print(f"{infile} 不是 PNG 图片!")
        return
    infile = os.path.abspath(infile)
    dir_path = os.path.dirname(infile)
    filename = infile.split("/")[-1]
    outdir = os.path.join(dir_path, "assets")
    if not os.path.exists(outdir):
        os.mkdir(outdir)
        print(f"创建输出目录 {outdir}")
    img = Image.open(infile)
    for i in range(1, maxtimes + 1):
        size = tuple([x * i for x in basesize])
        target_img = img.resize(size, Image.ANTIALIAS)
        outfile = ""
        if i == 1:
            outfile = os.path.join(outdir, filename)
        else:
            name = filename.replace(".", f"@{i}x.")
            outfile = os.path.join(outdir, name)
        target_img.save(outfile)
        print(f"{outfile}{size} 已保存！")


def imgs_resize(from_path):
    """扫描指定路径，转换路径下的图片

    Arguments:
        from_path {string} -- 图片所在目录
    """
    if not os.path.isdir(from_path):
        print(f"{from_path} 不是目录！")
        return
    for path in os.listdir(from_path):
        if os.path.isdir(path):
            continue
        if not path.endswith(".png"):
            continue
        img_resize(path)


def main():
    args = get_args()
    if not os.path.exists(args.path):
        print("请指定有效路径！")
        exit(0)
    if os.path.isdir(args.path):
        imgs_resize(args.path)
    else:
        img_resize(args.path)


if __name__ == "__main__":
    main()
