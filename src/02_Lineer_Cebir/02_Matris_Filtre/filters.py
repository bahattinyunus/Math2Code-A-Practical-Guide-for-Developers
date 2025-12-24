import numpy as np
import matplotlib.pyplot as plt

def create_sample_image():
    # 10x10 'luk basit bir gri tonlamalı resim (0-255)
    # Satranç tahtası deseni
    img = np.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            if (i+j) % 2 == 0:
                img[i, j] = 255
    return img

def apply_blur(image):
    """
    3x3 Mean Filter (Blur) uygular.
    Her piksel, çevresindeki 9 kareli pencerenin ortalaması olur.
    """
    rows, cols = image.shape
    output = np.zeros((rows, cols))
    
    # Padding eklemedigimiz icin kenarlari atlariz
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            # 3x3 pencereyi al
            window = image[i-1:i+2, j-1:j+2]
            output[i, j] = np.mean(window)
            
    return output

if __name__ == "__main__":
    print("--- Matris Filtreleme Demo (Blur) ---")
    
    original = create_sample_image()
    blurred = apply_blur(original)
    
    print("Orijinal Resim (Matrisin bir kısmı):")
    print(original[:5, :5])
    
    print("\nBulanıklaştırılmış Resim (Değerler yumuşadı):")
    print(blurred[:5, :5])
    
    try:
        # Eger matplotlib kuruluysa goster
        plt.subplot(1, 2, 1)
        plt.title("Original")
        plt.imshow(original, cmap='gray')
        
        plt.subplot(1, 2, 2)
        plt.title("Blurred")
        plt.imshow(blurred, cmap='gray')
        
        # plt.show() # Can blocks execution in some envs
        print("Görselleştirme hazır (kodda plt.show() kapalı.")
    except ImportError:
        pass
