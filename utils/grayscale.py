def grayscale(value):
    scale = " .'`^,:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    if value>255:
        return scale[-1]
    else:
        return scale[round((value/255)*len(scale))]
