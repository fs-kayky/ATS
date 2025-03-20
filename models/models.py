class Job:
    def __init__(self, title: str):
        self.title = title
        self.requirements = {}
        self.candidates = []