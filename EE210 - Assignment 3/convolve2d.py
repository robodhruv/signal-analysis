from numpy.fft import fft2, ifft2


def fftconvolve2d(x, y, mode="full"):
    """
    x and y must be real 2D numpy arrays.

    mode must be "full" or "valid".
    """
    x_shape = np.array(x.shape)
    y_shape = np.array(y.shape)
    z_shape = x_shape + y_shape - 1
    z = ifft2(fft2(x, z_shape) * fft2(y, z_shape)).real

    if mode == "valid":
        # To compute a valid shape, either np.all(x_shape >= y_shape) or
        # np.all(y_shape >= x_shape).
        valid_shape = x_shape - y_shape + 1
        if np.any(valid_shape < 1):
            valid_shape = y_shape - x_shape + 1
            if np.any(valid_shape < 1):
                raise ValueError("empty result for valid shape")
        start = (z_shape - valid_shape) // 2
        end = start + valid_shape
        z = z[start[0]:end[0], start[1]:end[1]]

    return z