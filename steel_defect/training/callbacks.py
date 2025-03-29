import numpy as np

class EarlyStopping:
    def __init__(self, patience=5, min_delta=0):
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.best_loss = np.inf
        
    def __call__(self, val_loss):
        if val_loss < self.best_loss - self.min_delta:
            self.best_loss = val_loss
            self.counter = 0
        else:
            self.counter += 1
            if self.counter >= self.patience:
                return True
        return False

class ModelCheckpoint:
    def __init__(self, filepath, monitor='val_loss'):
        self.filepath = filepath
        self.monitor = monitor
        self.best_score = None
        
    def __call__(self, score, model):
        if self.best_score is None or score < self.best_score:
            self.best_score = score
            torch.save(model.state_dict(), self.filepath)
            return True
        return False