from collections import Counter
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
final_text = lower_case.translate(str.maketrans('','',string.punctuation))


tokenized_word = word_tokenize(final_text)

final_words = []

for word in tokenized_word:
    if word not in stopwords.words('english'):
        final_words.append(word)

# print(final_words)
emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        # print(f"Word:{word} Emotion:{emotion}")

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
# print(w)


def sentiment_analyze(sentiment_text):
    analyser = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(analyser)
    # neg = analyser['neg']
    # pos = analyser['pos']
    # if pos == neg:
    #     print('Neutral')
    # elif neg > pos :
    #     print("Negative!")
    # elif pos > neg:
    #     print("Positive!")

    print(analyser["neg"]*100)

sentiment_analyze(final_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show