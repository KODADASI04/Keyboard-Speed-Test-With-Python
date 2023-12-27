class Competitor:
    def __init__(self,name = ""):
        self.name  = name
        self.written_words = []
        self.total_score = 0
        self.total_written_char = 0
        self.wrong_written_char = 0
        self.wrong_writtens = []