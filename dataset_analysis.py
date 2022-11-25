from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from PIL import Image


def print_data(data):
    """
    Parameters
    ----------
    data : dict
    """
    for k, v in data.items():
        print("%s:\t%s" % (k, v))
    #print("Min width: %i" % data['min_width'])
    #print("Max width: %i" % data['max_width'])
    #print("Min height: %i" % data['min_height'])
    #print("Max height: %i" % data['max_height'])


def main(path):
    """
    Parameters
    ----------
    path : str
        Path where to look for image files.
    """
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

    # Filter files by extension
    onlyfiles = [f for f in onlyfiles if f.endswith('.jpg')]  #.png
    #print(onlyfiles)

    train_shapes = []
    data = {}
    data['images_count'] = len(onlyfiles)
    data['min_width'] = 10**100  # No image will be bigger than that
    data['max_width'] = 0
    data['min_height'] = 10**100  # No image will be bigger than that
    data['max_height'] = 0

    for filename in onlyfiles:
        #print(filename)
        im = Image.open('D:\\research_work\data\VHR_segmentation_data\\NWPU VHR-10 dataset\\positive image set\\' + filename)
        width, height = im.size
        train_shapes.append([width, height])
        #data[filename] = im.size
        data['min_width'] = min(width, data['min_width'])
        data['max_width'] = max(width, data['max_width'])
        data['min_height'] = min(height, data['min_height'])
        data['max_height'] = max(height, data['max_height'])

    print_data(data)
    #print(data)

    #df_train = pd.DataFrame({'Shapes': train_shapes})
    #train_counts = df_train['Shapes'].value_counts()

    # print("Training Image Shapes:")
    # for i in range(len(train_counts)):
    # print("Shape %s counts: %d" % (train_counts.index[i], train_counts.values[i]))

    # for i in range(len(train_counts)):
    # print(train_counts.index[i])

    # print(type(train_shapes))
    tr_shapes = np.array(train_shapes)
    # print(type(tr_shapes))
    # print(tr_shapes[0])
    # print(tr_shapes[1])
    # print(tr_shapes[2])

    only_widths = np.sort(tr_shapes[:, 0])
    only_heights = np.sort(tr_shapes[:, 1])
    widths_heights = np.sort(tr_shapes[:, [0, 1]])

    print("mean of all widths/heights")
    print(np.mean(only_widths))
    print(np.mean(only_heights))
    #print(np.mean(widths_heights, axis=0))
    me_w, me_h = np.mean(widths_heights, axis=0)

    print(" greater & less  than mean for widths & height respectively")
    print("------widths-----")
    print("Greater than mean:",len([1 for i in only_widths if i > me_w]))
    print("Lesser than mean:",len([1 for i in only_widths if i < me_w]))
    print("------heights-----")
    print("Greater than mean:",len([1 for i in only_heights if i > me_h]))
    print("Lesser than mean:",len([1 for i in only_heights if i < me_h]))

    print("--------------------")

    print("median of all widths/heights")
    print(np.median(widths_heights, axis=0))
    md_w, md_h = np.median(widths_heights, axis=0)

    print("greater & less  than median for widths & height respectively")
    print("------widths-----")
    print("Greater than mean:",len([1 for i in only_widths if i > md_w]))
    print("Lesser than mean:",len([1 for i in only_widths if i < md_w]))
    print("------heights-----")
    print("Greater than mean:",len([1 for i in only_heights if i > md_h]))
    print("Lesser than mean:", len([1 for i in only_heights if i < md_h]))

    print("--------------------")

    plt.hist(only_widths)
    plt.show()

    plt.hist(only_heights)
    plt.show()



if __name__ == '__main__':
    #change format of image .jpg or .png to be indexed in main()
    #main(path='D:\\research_work\data\DOTA-v1.0_object_detection\\train\images\\')
    main(path='D:\\research_work\data\VHR_segmentation_data\\NWPU VHR-10 dataset\\positive image set\\')