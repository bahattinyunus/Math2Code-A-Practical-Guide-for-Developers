import math
from collections import defaultdict

class NaiveBayesClassifier:
    def __init__(self):
        self.log_priors = {}
        self.log_likelihoods = defaultdict(dict)
        self.vocab = set()
        self.classes = set()

    def train(self, documents, labels):
        # 1. Calculate Priors P(Class)
        n_docs = len(documents)
        self.classes = set(labels)
        class_counts = defaultdict(int)
        
        for label in labels:
            class_counts[label] += 1
            
        for c in self.classes:
            self.log_priors[c] = math.log(class_counts[c] / n_docs)
            
        # 2. Count words per class
        term_counts = defaultdict(lambda: defaultdict(int))
        class_total_terms = defaultdict(int)
        
        for doc, label in zip(documents, labels):
            for term in doc.split():
                self.vocab.add(term)
                term_counts[label][term] += 1
                class_total_terms[label] += 1
                
        # 3. Calculate Likelihoods P(Word | Class) with Laplace Smoothing
        vocab_size = len(self.vocab)
        for c in self.classes:
            for term in self.vocab:
                numerator = term_counts[c][term] + 1
                denominator = class_total_terms[c] + vocab_size
                self.log_likelihoods[c][term] = math.log(numerator / denominator)

    def predict(self, document):
        best_class = None
        max_prob = -float('inf')
        
        for c in self.classes:
            # log P(C | D) ~ log P(C) + sum(log P(W | C))
            prob = self.log_priors[c]
            for term in document.split():
                if term in self.vocab:
                    prob += self.log_likelihoods[c][term]
            
            if prob > max_prob:
                max_prob = prob
                best_class = c
                
        return best_class

if __name__ == "__main__":
    train_docs = [
        "free money now",
        "win lottery prize",
        "meeting at noon",
        "project deadline today"
    ]
    train_labels = ["spam", "spam", "work", "work"]
    
    classifier = NaiveBayesClassifier()
    classifier.train(train_docs, train_labels)
    
    test_docs = [
        "free prize waiting",
        "meeting schedule update"
    ]
    
    print("--- Naive Bayes Spam Filter ---")
    for doc in test_docs:
        print(f"Doc: '{doc}' -> Pred: {classifier.predict(doc)}")
