import insightface
from core import config


class GetFeature:
    def __init__(self):
        self.handler = insightface.model_zoo.get_model(config.DETECTION_MODEL)
        self.handler.prepare(ctx_id=0)

    def get_feature(self, image_face):
        feature = self.handler.get_feat(image_face)
        return feature[0]
