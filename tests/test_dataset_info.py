def test_ds_info():
    from pytorch_tools.dstools import get_ds_info
    import torch
    import numpy as np

    class SampleDS(torch.utils.data.Dataset):
        def __init__(self):
            self.data_dict = [
                    {"data":np.zeros(3),
                     "label":0},
                    {"data":np.zeros(3),
                     "label":0},
                    {"data":np.zeros(3),
                     "label":1}
                    ]

        def __len__(self):
            return len(self.data_dict)

        def __getitem__(self, idx):
            return self.data_dict[idx]

    sample_ds = SampleDS()
    resp = get_ds_info(sample_ds)

