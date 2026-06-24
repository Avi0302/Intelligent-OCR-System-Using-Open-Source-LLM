import os
os.environ["FLAGS_use_mkldnn"] = "0"
os.environ["PADDLE_PDX_ENABLE_MKLDNN_BYDEFAULT"] = "0"

from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_angle_cls=True,
    lang='en',
    enable_mkldnn=False
)


def extract_text(image):

    result = ocr.ocr(image)

    extracted_text = []

    for line in result:
        if line:
            for word in line:
                extracted_text.append(word[1][0])

    return "\n".join(extracted_text)