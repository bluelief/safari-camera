# Copyright (c) 2018 Bluelief.
# Licensed under the MIT License.

from pyzbar.pyzbar import decode

from bottle import route, run, HTTPResponse, post, request

# Use for decode pictures
import cv2
import base64
import numpy as np
from PIL import Image
from io import BytesIO


def readb64(base64_string):
    sbuf = BytesIO()
    sbuf.write(base64.b64decode(base64_string))
    pimg = Image.open(sbuf)

    return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)


def contrast(image, a):
    lut = [ np.uint8(255.0 / (1 + np.exp(-a * (i - 128.) / 255.))) for i in range(256)]
    result_image = np.array( [ lut[value] for value in image.flat], dtype=np.uint8 )
    result_image = result_image.reshape(image.shape)

    return result_image


def convert_image_to_code(image):
    print('\n-------------- Debug screen --------------')

    image_glay = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_convert = contrast(image_glay, 6)
    #cv2.imwrite("image.png", image)
    result = decode(image_convert)

    return result


@post("/")
def http_header():
    image = readb64(request.params['image'])
    result = convert_image_to_code(image)
    print(result)

    if result:
        result = result[0]
        body = {"status": "OK", "type": result.type, "code": str(result.data, 'utf-8')}
    else:
        body = {"status": "NG"}
    r = HTTPResponse(status=200, body=body)
    r.set_header("Content-Type", "application/json")

    return r


run(host='localhost', port=8080, debug=True, reloader=True)
