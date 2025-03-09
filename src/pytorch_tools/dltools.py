class SuperLoader():
    def __init__(self, original_dataloader):
        self.original_dataloader = original_dataloader

    def filter(self, query):
        return None

    def sample(self, N:int):
        return None
