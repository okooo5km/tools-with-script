import argparse


class StringsFile:
    def __init__(self, path):
        self.path = path
        self.raw = []
        with open(path) as f:
            lines = f.readlines()
            metadata = {}
            for line in lines:
                line = line[:-1]
                if line == "":
                    continue
                if line.startswith("/*"):
                    metadata = dict()
                    metadata["comment"] = line
                else:
                    line = line.replace('"', "")
                    line = line.replace(";", "")
                    line = line.replace(" ", "")
                    strings = line.split("=")
                    metadata["tag"] = strings[0]
                    metadata["string"] = strings[1]
                    self.raw.append(metadata)

    @property
    def strings(self):
        return [meta["string"] for meta in self.raw]

    @property
    def tags(self):
        return [meta["tag"] for meta in self.raw]
    
    @property
    def comments(self):
        return [meta["comment"] for meta in self.raw]

    def translate(self):
        text = '\n'.join(self.strings)
        self.google_translate("auto", "zh_CN", text)

    @staticmethod
    def google_translate(src_lan, target_lan, text):
        return text

def get_args():
    parser = argparse.ArgumentParser(description="翻译 iOS 和 macOS App 工程的本地化 String 文件的工具")
    parser.add_argument("-f", "--file", help="指定待翻译的文件")
    return parser.parse_args()


def main():
    sf = StringsFile("/Users/5km/Documents/workspace/macOS/InternationalDemo/InternationalDemo/zh-Hans.lproj/Main.strings")
    print('\n'.join(sf.strings))

# https://translate.google.cn/#view=home&op=translate&sl=auto&tl=en&text=喝水

if __name__ == "__main__":
    main()