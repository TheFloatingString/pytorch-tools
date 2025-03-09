def iter_typing(data_dict):
    return_dict = {}
    for key_ in data_dict:
        value_ = data_dict[key_]
        if isinstance(value_, dict):
            inner_dict = iter_typing(value_)
            return_dict[key_] = inner_dict
        else:
            return_dict[key_] = type(value_)
    return return_dict


def iter_shape(data_dict):
    return_dict = {}
    for key_ in data_dict:
        value_ = data_dict[key_]
        if isinstance(value_, dict):
            inner_dict = iter_shape(value_)
            return_dict[key_] = inner_dict
        elif hasattr(value_, "shape"):
            return_dict[key_] = value_.shape
        else:
            return_dict[key_] = None
    return return_dict


def get_ds_typing(ds, idx=0):
    return_dict = {"length": len(ds), "typing": iter_typing(ds[idx])}
    return return_dict


def get_ds_shape(ds, idx=0):
    return_dict = {"length": len(ds), "shape": iter_shape(ds[idx])}
    return return_dict
