# coding=gbk

import os
import os.path
import shutil
import time

src_root = r"F:\src"
dst_root = r"F:\back"

def is_invalid(path):
    return os.path.splitext(path)[1] not in set(['.jpg', '.mp4'])

def is_repeat(file, file_set):
    return file in file_set


def tidy_pic(src_root, dst_root):
    src_root = src_root.rstrip("\\")
    dst_root = dst_root.rstrip("\\")
    files = set()

    # 先将目标目录下的文件全部添加到集合，避免重运行此脚本时报错
    for dirpath, dirnames, filenames in os.walk(dst_root):
        for file in filenames:
            files.add(file)

    for dirpath, dirnames, filenames in os.walk(src_root):
        for file in filenames:
            if is_invalid(file) or is_repeat(file, files):
                continue

            files.add(file)

            fullpath = os.path.join(dirpath, file)
            mtime = time.localtime(os.stat(fullpath).st_mtime)
            tmp = dst_root + "\\" + str(mtime.tm_year) + "_" + str(mtime.tm_mon)

            if not os.path.exists(tmp):
                os.makedirs(tmp)

            shutil.move(fullpath, tmp)


if __name__ == "__main__":
    tidy_pic(src_root, dst_root)
