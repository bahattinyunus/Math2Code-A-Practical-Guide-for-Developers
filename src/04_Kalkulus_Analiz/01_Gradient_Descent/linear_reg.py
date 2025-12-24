import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(x, y, learning_rate=0.01, epochs=1000):
    """
    y = m*x + c doğrusu için m ve c parametrelerini optimize eder.
    Cost Function: MSE (Mean Squared Error)
    """
    n = len(x)
    m = 0
    c = 0
    history = []
    
    for i in range(epochs):
        y_pred = m * x + c
        
        # Cost (sadece takip etmek icin)
        cost = (1/n) * sum((y_pred - y)**2)
        history.append(cost)
        
        # Gradientlerin Hesaplanması (Türev)
        # dJ/dm = (2/n) * sum(x * (y_pred - y))
        # dJ/dc = (2/n) * sum(y_pred - y)
        
        dm = (2/n) * sum(x * (y_pred - y))
        dc = (2/n) * sum(y_pred - y)
        
        # Güncelleme
        m = m - learning_rate * dm
        c = c - learning_rate * dc
        
        if i % 100 == 0:
            print(f"Epoch {i}: Cost {cost:.4f}, m {m:.4f}, c {c:.4f}")
            
    return m, c, history

if __name__ == "__main__":
    print("--- Gradient Descent Engine ---")
    
    # Basit veri seti (Lineer ilişki)
    X = np.array([1, 2, 3, 4, 5])
    # y = 2x + 1 civarında gürültülü veri
    y = np.array([3, 5, 7, 9, 11]) + np.random.normal(0, 0.1, 5)
    
    m_opt, c_opt, cost_history = gradient_descent(X, y)
    
    print(f"\nOptimization Complete:")
    print(f"Best m: {m_opt}")
    print(f"Best c: {c_opt}")
    
    # Tahmin
    print(f"Prediction for x=6 (Expected ~13): {m_opt * 6 + c_opt:.2f}")
    
    try:
        plt.plot(cost_history)
        plt.title("Cost Function over Epochs")
        plt.xlabel("Epoch")
        plt.ylabel("MSE")
        # plt.show()
    except ImportError:
        pass
