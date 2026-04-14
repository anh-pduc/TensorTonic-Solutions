import numpy as np
def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    img_array = np.array(image).flatten()
    his = np.zeros(256)
    for i in range(256):
        for j in range(len(img_array)):
            if img_array[j] == i:
                his[i] += 1
    return his.tolist()