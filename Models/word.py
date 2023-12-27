class Word:
    def __init__(self,word):
        self.word = word
        self.word_char_count = len(self.word)
        self.wrongchar_count = 0
        self.wrongwritten = False
    
    def calculate_score(self,written_word):
        self.written_char_count = len(written_word)
        
        if(self.word_char_count < self.written_char_count):
            self.wrongchar_count += len(written_word) - len(self.word)
            
        for index,char in enumerate(self.word):
            try:
                if(written_word[index] != char):
                    self.wrongchar_count += 1
            except IndexError:
                self.wrongchar_count += 1

        if(self.wrongchar_count > 0):
            self.wrongwritten = True
            
        self.score =  self.word_char_count - self.wrongchar_count