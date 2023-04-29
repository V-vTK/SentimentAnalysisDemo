from nltk.sentiment.vader import SentimentIntensityAnalyzer
# Requires pip install nltk and nltk data:
# https://www.nltk.org/data.html

# Built with the help of
# https://www.nltk.org/howto/sentiment.html

def sentiment_analysis(sentence) -> str:
    '''
    Analyzes the sentiment of a sentence.
    return str: the original sentence along with the analysis
    '''
    result_string = ""

    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)

    result = "positive" if ss["compound"] >= 0 else "negative"
    result_string += (f"'{sentence}': Sentiment was {result} --> ")
    result_string += (f" analysis was: ")
    result_string += (f" {ss} ")

    return result_string



if __name__ == "__main__":

    sentences_list = ["Yoda is the best character in star wars", "Vader is evil", "I am not sure about Boba Fett"]
    for sentence in sentences_list:
        print(sentiment_analysis(sentence))
