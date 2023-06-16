import insightface


class Recognize:
    def __init__(self):
        # app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CUDAExecutionProvider'])
        self.handler = insightface.model_zoo.get_model('buffalo_l')
        self.handler.prepare(ctx_id=0)


    def get_feature(self, imageFace):
        print("aaa")
        feature = self.handler.get_feat(imageFace)
        return feature
