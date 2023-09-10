import os
from glob import glob

root_dir = "./"  # Replace with your directory path

def replace_in_file(file_path, old_str, new_str):
    with open(file_path, 'r+') as f:
        content = f.read()
        f.seek(0)
        f.write(content.replace(old_str, new_str))

for filename in glob(root_dir + '/**/*.md', recursive=True):
    replace_in_file(filename, "www.smslit.top", "blog.5km.studio")

