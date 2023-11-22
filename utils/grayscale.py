def grayscale(value):
    scale = ".'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@"
    scale+=scale[::-2]
    return scale[value%len(scale)]

