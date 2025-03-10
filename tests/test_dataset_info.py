from pytorch_tools.dstools import get_ds_typing, get_ds_shape
import torch
import numpy as np


class SampleDS(torch.utils.data.Dataset):
    def __init__(self):
        self.data_dict = [
            {"data": np.zeros(3), "label": 0},
            {"data": np.zeros(3), "label": 0},
            {"data": np.zeros(3), "label": 1},
        ]

    def __len__(self):
        return len(self.data_dict)

    def __getitem__(self, idx):
        return self.data_dict[idx]


def test_ds_iter_typing():
    sample_ds = SampleDS()
    resp = get_ds_typing(sample_ds)
    print(resp)


def test_ds_iter_shape():
    sample_ds = SampleDS()
    resp = get_ds_shape(sample_ds)
    print(resp)
