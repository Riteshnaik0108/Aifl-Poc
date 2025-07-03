import torch 
import torch.nn as nn 
import numpy as np 
import random 
import string 
 
# Character vocabulary and encoding 
all_chars = string.ascii_lowercase + string.digits  # 'a-z0-9' 
char_to_idx = {ch: i for i, ch in enumerate(all_chars)} 
vocab_size = len(all_chars) 
 
def encode_string(s): 
    return torch.tensor([char_to_idx[c] for c in s], dtype=torch.long) 
 
def generate_string_data(n_samples=1000, seq_len=6): 
    X = [] 
    y = [] 
    for _ in range(n_samples): 
        if random.random() > 0.5: 
            # Repeating pattern 
            repeat_unit_len = random.choice([1, 2, 3]) 
            unit = ''.join(random.choices(all_chars, k=repeat_unit_len)) 
            repeated = (unit * (seq_len // repeat_unit_len + 1))[:seq_len] 
            X.append(encode_string(repeated)) 
            y.append(1) 
        else: 
            # Random non-repeating string 
            rand_str = ''.join(random.choices(all_chars, k=seq_len)) 
            X.append(encode_string(rand_str)) 
            y.append(0) 
    X = torch.stack(X) 
    y = torch.tensor(y, dtype=torch.float32).unsqueeze(1) 
    return X, y 
 
# Define model 
class PatternDetector(nn.Module): 
    def __init__(self, vocab_size, embed_dim, seq_len): 
        super(PatternDetector, self).__init__() 
        self.embedding = nn.Embedding(vocab_size, embed_dim) 
        self.fc1 = nn.Linear(embed_dim * seq_len, 64) 
        self.relu = nn.ReLU() 
        self.fc2 = nn.Linear(64, 1) 
 
    def forward(self, x): 
        x = self.embedding(x)  # (batch, seq_len, embed_dim) 
        x = x.view(x.size(0), -1)  # flatten 
        x = self.relu(self.fc1(x)) 
        x = self.fc2(x)  # no sigmoid here 
        return x 
 
# Parameters 
SEQ_LEN = 6 
embed_dim = 10 
X, y = generate_string_data(seq_len=SEQ_LEN) 
model = PatternDetector(vocab_size, embed_dim, SEQ_LEN) 
 
# Loss and optimizer 
criterion = nn.BCEWithLogitsLoss() 
optimizer = torch.optim.Adam(model.parameters(), lr=0.01) 
 
# Training loop 
for epoch in range(100): 
    model.train() 
    output = model(X) 
    loss = criterion(output, y) 
    optimizer.zero_grad() 
    loss.backward() 
    optimizer.step() 
    if (epoch + 1) % 10 == 0: 
        predictions = torch.sigmoid(output) 
        acc = ((predictions > 0.5).float() == y).float().mean() 
        print(f"Epoch [{epoch+1}/100] Loss: {loss.item():.4f} | Accuracy: {acc.item():.4f}") 
 
# Prediction function 
def predict_string_pattern(s): 
    s = s.lower() 
    if len(s) != SEQ_LEN or any(c not in char_to_idx for c in s): 
        print(f"Input must be alphanumeric string of length {SEQ_LEN}") 
        return 
    input_tensor = encode_string(s).unsqueeze(0) 
    with torch.no_grad(): 
        model.eval() 
        logits = model(input_tensor) 
        pred = torch.sigmoid(logits) 
        print(f"Input: {s}") 
        print("Pattern Detected" if pred.item() > 0.5 else "Pattern Not Detected") 
 
# Interactive loop 
while True: 
    user_input = input(f"\nEnter an alphanumeric string of length {SEQ_LEN} (or type 'exit'): ").strip() 
    if user_input.lower() == "exit": 
        break 
    predict_string_pattern(user_input)
