def hash_join(table_a, table_b, key_a, key_b):
    """
    Basit bir Hash Join algoritması implementasyonu.
    Set ve Dictionary yapılarını kullanır.
    """
    print(f"Joining Table A ({len(table_a)} rows) and Table B ({len(table_b)} rows)...")
    
    # Hash Phase: Build a hash map from the smaller table (usually)
    # Burada basitlik adına Table B'yi hash map'e çevirelim.
    hash_map = {}
    
    for row in table_b:
        key_val = row[key_b]
        if key_val not in hash_map:
            hash_map[key_val] = []
        hash_map[key_val].append(row)
        
    # Probe Phase: Scan Table A and look up in hash map
    result = []
    
    for row_a in table_a:
        key_val = row_a[key_a]
        if key_val in hash_map:
            # Match found
            matches = hash_map[key_val]
            for row_b in matches:
                # Merge rows representing the join
                merged_row = {**row_a, **row_b} 
                # Not: Key collision durumunda ikinci tablo ezer, 
                # gerçek bir DB'de column alias gerekir.
                result.append(merged_row)
                
    return result

if __name__ == "__main__":
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]
    
    orders = [
        {"order_id": 101, "user_id": 1, "product": "Laptop"},
        {"order_id": 102, "user_id": 1, "product": "Mouse"},
        {"order_id": 103, "user_id": 2, "product": "Monitor"}
    ]
    
    joined_data = hash_join(users, orders, "id", "user_id")
    
    print("\n--- SONUÇLAR (INNER JOIN) ---")
    for row in joined_data:
        print(row)
