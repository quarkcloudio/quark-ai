from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

class OCR:

    # OCR识别
    def getImageText():
        ocr_recognition = pipeline(Tasks.ocr_recognition, model='damo/cv_convnextTiny_ocr-recognition-general_damo')

        ### 使用url
        img_url = 'http://duguang-labelling.oss-cn-shanghai.aliyuncs.com/mass_img_tmp_20220922/ocr_recognition.jpg'
        return ocr_recognition(img_url)