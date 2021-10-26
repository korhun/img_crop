import os
from tkinter import filedialog
from tkinter import *
from typing import AnyStr, Tuple
import cv2
import yaml

end_txt = "                   \r"


def select_dir():
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory()


def enumerate_files(dir_path, recursive=False):
    for root, sub_dirs, files in os.walk(dir_path):
        for name1 in files:
            yield path_join(root, name1)
        if not recursive:
            break


def path_join(a: AnyStr, *paths: AnyStr) -> AnyStr:
    return os.path.join(a, *paths).replace("/", os.path.sep)


def get_file_name_extension(file_full_name) -> Tuple[AnyStr, AnyStr, AnyStr]:
    dir_name1, file_name = os.path.split(file_full_name)
    name1, extension1 = os.path.splitext(file_name)
    return dir_name1, name1, extension1


def get_margins(fn):
    with open(fn, "r") as stream:
        try:
            values = yaml.safe_load(stream)
            return values.get('top', 0.0378), values.get('left', 0), values.get('right', 0), values.get('bottom', 0)
        except:
            return 0.0378, 0, 0, 0


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_fn = path_join(current_dir, "config.yml")
    top, left, right, bottom = get_margins(config_fn)

    dir_name = select_dir()
    target_dir_name0 = path_join(dir_name, "_cropped")

    if top > 0:
        target_dir_name0 += "_top_" + str(top).replace(",", ".")
    if left > 0:
        target_dir_name0 += "_left_" + str(left).replace(",", ".")
    if right > 0:
        target_dir_name0 += "_right_" + str(right).replace(",", ".")
    if bottom > 0:
        target_dir_name0 += "_bottom_" + str(bottom).replace(",", ".")

    target_dir_name = target_dir_name0
    i = 0
    while os.path.isdir(target_dir_name):
        i += 1
        target_dir_name = target_dir_name0 + " (" + str(i) + ")"
    os.makedirs(target_dir_name)

    i = 0
    for fn in enumerate_files(dir_name):
        try:
            i += 1
            print("{} - {}".format(i, fn), end=end_txt)
            dir_name, name, extension = get_file_name_extension(fn)

            img = cv2.imread(fn)
            height, width = img.shape[0], img.shape[1]

            top_y = height * top if top > 0 else 0
            bottom_y = height - height * bottom if bottom > 0 else height
            left_x = width * left if left > 0 else 0
            right_x = width - width * right if right > 0 else width

            img_cropped = img[int(top_y):int(bottom_y), int(left_x):int(right_x)]

            new_fn = path_join(target_dir_name, name + ".png")
            cv2.imwrite(new_fn, img_cropped)

            print(new_fn)
        except:  # no image
            pass

    print("finished")
