import torch


class TmpDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


class SuperLoader:
    def __init__(self, original_dataloader):
        self.original_dataloader = original_dataloader

    def filter(self, query):
        return None

    def sample(self, N: int):
        return None
