from modelscope.msdatasets import MsDataset
from modelscope.metainfo import Trainers
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope.trainers import build_trainer

class Detect:

    # Detect
    def get_data(url):
        object_detect = pipeline(Tasks.image_object_detection,model='damo/cv_tinynas_object-detection_damoyolo-t')
        return object_detect(url)

    # Detect
    def train():
        kwargs = dict(
                    device='cpu',
                    model='damo/cv_tinynas_object-detection_damoyolo-t',
                    batch_size=1,
                    max_epochs=1,
                    num_classes=1, # 自定义数据中的类别数
                    train_image_dir='./datasets/detect/data', # 训练图片路径
                    train_ann='./datasets/detect/trainval.json', # 训练标注文件路径
                    work_dir='./workdirs',
                )
        trainer = build_trainer(name=Trainers.tinynas_damoyolo, default_args=kwargs)
        trainer.train()