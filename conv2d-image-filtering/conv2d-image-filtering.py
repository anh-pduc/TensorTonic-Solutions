import numpy as np
def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    """
    image = np.asarray(image, dtype = float)
    kernel = np.asarray(kernel, dtype=float)
    p = padding
    image_pad = np.pad(image, pad_width = p, mode = 'constant', constant_values = 0)
    k = kernel.shape[0]
    h, w = image.shape
    h_out = (h + 2*p - k)//stride + 1
    w_out = (w + 2*p - k)//stride + 1
    lst = []
    for i in range(h_out):
        for j in range(w_out):
            l = np.sum(image_pad[i*stride:i*stride+k,j*stride:j*stride+k] * kernel)
            lst.append(l)
    # n = int(len(lst)**0.5)
    return np.array(lst).reshape(h_out,w_out).tolist()
    
    pass