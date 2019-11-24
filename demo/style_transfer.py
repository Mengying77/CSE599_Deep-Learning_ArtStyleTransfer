"""
Style Transfer
"""

import os
import base64

def transfer(input_image_name, style):
    """
    Load model and perform style transfer on input image
    :param input_image_name: filename of an input image
    :param style: a style name before '-' in image filename
    :return: output_image
    """

    input_image = open('../images/input/' + input_image_name)

    # style_image = ...

    # transfer style

    # save output_image in output
    # output_image = ...

    output_image = '../images/style/' + 'Gogh-StarryNight.jpg' # temp
    encoded__output_image = base64.b64encode(open(output_image, 'rb').read())

    return encoded__output_image