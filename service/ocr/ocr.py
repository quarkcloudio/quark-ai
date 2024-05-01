from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

class OCR:

    # OCR识别
    def get_image_text(img_url):
        ocr_recognition = pipeline(Tasks.ocr_recognition, model='damo/cv_convnextTiny_ocr-recognition-scene_damo')

        return ocr_recognition(img_url)