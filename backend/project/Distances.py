import numpy as np


class Distances:
    @staticmethod
    def cosine_similarity(a, b):
        dot_product = np.dot(a, b.T)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b, axis=1)
        return dot_product / (norm_a * norm_b)

    @staticmethod
    def normalize_embeddings(embeddings):
        # Tính độ dài của mỗi vector nhúng
        norms = np.linalg.norm(embeddings, axis=1)

        # Chia mỗi vector nhúng cho độ dài của nó
        normalized_embeddings = embeddings / norms[:, np.newaxis]

        return normalized_embeddings

    def compare_face_with_euclidean(self, face_embedding, database_embeddings):
        # Chuẩn hóa face_embedding và database_embeddings
        # face_embedding = self.normalize_embeddings(face_embedding)
        # database_embeddings = self.normalize_embeddings(database_embeddings)
        # print(face_embedding.shape,database_embeddings.shape)

        # Tính khoảng cách Euclidean giữa face_embedding và mỗi vector nhúng trong database_embeddings
        # distances = np.linalg.norm(database_embeddings - face_embedding, axis=1)
        ls_ins=[]
        for face in database_embeddings:
            face_embedding=self.normalize_embeddings(face_embedding)
            face=self.normalize_embeddings(face)

            instance=np.linalg.norm(face-face_embedding)
            ls_ins.append(instance)
        return ls_ins

    def classic(self, face_embedding, database_vectors, type_distances):
        if type_distances == "cosine":
            similarities = self.cosine_similarity(face_embedding, database_vectors)
        if type_distances == "euclidean":
            similarities = self.compare_face_with_euclidean(face_embedding, database_vectors)
        return similarities