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


    def lower_words(self):
        lower_case = self.text.lower()
        self.final_text = lower_case.translate(str.maketrans('','',string.punctuation))

    def tokenize(self ):
        self.tokenized_word = word_tokenize(self.final_text)
        for word in self.tokenized_word:
            # print(f"Word: {word}")
            if word not in stopwords.words('english'):
                self.final_words.append(word)

    def get_emotion_list(self):
        with open('emotions.txt','r') as file:
            for line in file:
                clear_line = line.replace("\n", '').replace(',','').replace("'",'').strip()
                word, emotion = clear_line.split(':')

                if word in self.final_words:
                    self.emotion_list.append(emotion)

    def sentiment_analyze(self):
        analyser = SentimentIntensityAnalyzer().polarity_scores(self.final_text)
        analyze_results = {'neg': analyser["neg"]*100, "pos": analyser["pos"]*100, 'neu': analyser['neu']*100}
        print(analyze_results)

    def analyze(self, text):
        self.text = text
        self.lower_words()
        self.tokenize()
        self.get_emotion_list()
        self.sentiment_analyze()


if __name__ == "__main__":
    cls = CommentAnalyser()
    text = open('read.txt', encoding='utf-8').read()
    text = text.split('\n')
    for x in text:
        cls.analyze(x)
