import random
import math

def calculate_stats(data):
    """
    Basit istatistik hesaplayıcı:
    - Mean (Ortalama)
    - Variance (Varyans)
    - Std Dev (Standart Sapma)
    """
    n = len(data)
    if n == 0:
        return 0, 0, 0
    
    mean = sum(data) / n
    
    variance = sum([(x - mean) ** 2 for x in data]) / n
    std_dev = math.sqrt(variance)
    
    return mean, variance, std_dev

if __name__ == "__main__":
    print("--- Server Latency Dashboard ---")
    
    # 100 tane rastgele latency verisi (ms)
    # 5 tanesi spike olsun (anomali)
    latencies = [random.normalvariate(50, 5) for _ in range(95)]
    latencies.extend([200, 210, 190, 500, 250]) # Anomaliler
    
    mean, var, std = calculate_stats(latencies)
    
    print(f"Total Requests: {len(latencies)}")
    print(f"Mean Latency: {mean:.2f} ms")
    print(f"Standard Deviation: {std:.2f} ms")
    
    # Anomali Tespiti: Veri > Mean + 3 * StdDev
    threshold = mean + 3 * std
    print(f"\nAnomaly Threshold (3-Sigma): {threshold:.2f} ms")
    
    anomalies = [x for x in latencies if x > threshold]
    print(f"Detected Anomalies ({len(anomalies)}): {anomalies}")
