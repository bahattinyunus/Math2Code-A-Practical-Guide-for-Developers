import numpy as np

def cosine_similarity(v1, v2):
    """
    İki vektör arasındaki açının kosinüsü.
    Benzerlik = (A . B) / (||A|| * ||B||)
    1'e yakınsa benzer, 0 ise dik (alakasız), -1 ise zıt.
    """
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    
    if norm_v1 == 0 or norm_v2 == 0:
        return 0
        
    return dot_product / (norm_v1 * norm_v2)

class MovieRecommender:
    def __init__(self):
        # Film Özellikleri: [Aksiyon, Komedi, Dram, Bilim Kurgu]
        self.movies = {
            "Matrix": np.array([0.9, 0.1, 0.2, 0.9]),
            "Hangover": np.array([0.1, 0.9, 0.1, 0.0]),
            "Godfather": np.array([0.3, 0.1, 0.9, 0.0]),
            "Inception": np.array([0.8, 0.2, 0.4, 0.9]),
            "Avengers": np.array([0.9, 0.4, 0.1, 0.6])
        }
        
    def recommend(self, user_profile, top_k=2):
        print(f"Kullanıcı Profili: {user_profile}")
        scores = []
        
        for name, features in self.movies.items():
            sim = cosine_similarity(user_profile, features)
            scores.append((name, sim))
            
        # Skorlara göre sırala (Büyükten küçüğe)
        scores.sort(key=lambda x: x[1], reverse=True)
        
        return scores[:top_k]

if __name__ == "__main__":
    recsys = MovieRecommender()
    
    # Kullanıcı: Aksiyon ve Bilim Kurgu seviyor
    user_alice = np.array([0.8, 0.1, 0.1, 0.8]) 
    
    print("Alice için Öneriler:")
    for movie, score in recsys.recommend(user_alice):
        print(f"- {movie}: {score:.4f}")
        
    # Kullanıcı: Komedi seviyor
    user_bob = np.array([0.1, 0.9, 0.1, 0.0])
    
    print("\nBob için Öneriler:")
    for movie, score in recsys.recommend(user_bob):
        print(f"- {movie}: {score:.4f}")
