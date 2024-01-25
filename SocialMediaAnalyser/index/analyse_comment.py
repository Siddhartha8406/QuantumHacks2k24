from collections import Counter
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class CommentAnalyser:
    def __init__(self) -> None:
        self.tokenized_word = []
        self.final_words = []
        self.emotion_list = []

        self.neg = 0
        self.neu = 0
        self.pos = 0


    def lower_words(self):
        lower_case = self.text.lower()
        self.final_text = lower_case.translate(str.maketrans('','',string.punctuation))

    def tokenize(self ):
        self.tokenized_word = word_tokenize(self.final_text)
        for word in self.tokenized_word:
            if word not in stopwords.words('english'):
                self.final_words.append(word)

    def get_emotion_list(self):
        with open('/Users/siddharthareddy/QuantamHacks2k24/SocialMediaAnalyser/index/emotions.txt','r') as file:
            for line in file:
                clear_line = line.replace("\n", '').replace(',','').replace("'",'').strip()
                word, emotion = clear_line.split(':')

                if word in self.final_words:
                    self.emotion_list.append(emotion)

    def sentiment_analyze(self):
        analyser = SentimentIntensityAnalyzer().polarity_scores(self.final_text)
        if analyser['neg'] > analyser['pos']:
            self.neg += 1
        elif analyser['pos'] > analyser['neg']:
            self.pos += 1
        else:
            self.neu += 1

    def analyze(self, text):
        length = len(text)
        for x in text:
            self.text = x
            self.lower_words()
            self.tokenize()
            self.get_emotion_list()
            self.sentiment_analyze()


        return [self.neg, self.neu, self.pos]

if __name__ == "__main__":
    a = CommentAnalyser()
    print(a.analyze(["Really Helpful",  "This is the error "]))