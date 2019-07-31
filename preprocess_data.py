import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer 


def preprocess_word(word):
    # Remove punctuation
    word = word.strip('\'"?!,.():;')
    # Convert more than 2 letter repetitions to 2 letter
    # funnnnny --> funny
    word = re.sub(r'(.)\1+', r'\1\1', word)
    # Remove - & '
    word = re.sub(r'(-|\')', '', word)
    return word


def is_valid_word(word):
    # Check if word begins with an alphabet
    return (re.search(r'^[a-zA-Z][a-z0-9A-Z\._]*$', word) is not None)


def handle_emojis(tweet):
    # Smile -- :), : ), :-), (:, ( :, (-:, :')
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\))', 'good', tweet)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', 'good', tweet)
    # Love -- <3, :*
    tweet = re.sub(r'(<3|:\*)', 'good', tweet)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;)', 'good', tweet)
    # Sad -- :-(, : (, :(, ):, )-:
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:)', 'bad', tweet)
    # Cry -- :,(, :'(, :"(
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', 'bad', tweet)
    return tweet

def preprocess_tweet(tweet):
    processed_tweet = []
    # Convert to lower case
    tweet = tweet.lower()
    # Replaces URLs with the word URL
    tweet = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', " ", tweet)
    # Replace @handle with the word USER_MENTION
    tweet = re.sub(r'@[\S]+', " ", tweet)
    # Replaces #hashtag with hashtag
    tweet = re.sub(r'#(\S+)', r' \1 ', tweet)
    #Remove $tags and replace with $tag
    tweet = re.sub(r'\$(\S+)', r' \1 ', tweet)
    tweet = re.sub(r'\(' , "" , tweet)
    tweet = re.sub(r'\)' , "" , tweet)
    # Remove RT (retweet)
    tweet = re.sub(r'\brt\b', '', tweet)
    # Replace 2+ dots with space
    tweet = re.sub(r'\.{2,}', " ", tweet)
    tweet = tweet.strip(' "\'')
    tweet.lstrip('\...')
    tweet.rstrip('\...')
    tweet.lstrip('\"')
    tweet.rstrip('\"')
    tweet.lstrip('\!')
    tweet.rstrip('\!')
    tweet.lstrip('\@')
    tweet.rstrip('\@')
    tweet.lstrip('\#')
    tweet.rstrip('\#')
    tweet.lstrip('\$')
    tweet.rstrip('\$')
    tweet.lstrip('\%')
    tweet.rstrip('\%')
    tweet.lstrip('\?')
    tweet.rstrip('\?')
    tweet.lstrip('\^')
    tweet.rstrip('\^')
    tweet.lstrip('\&')
    tweet.rstrip('\&')
    tweet.lstrip('\*')
    tweet.rstrip('\*')
    tweet.lstrip('\(')
    tweet.rstrip('\)')
    tweet.lstrip('\<')
    tweet.rstrip('\>')
    tweet.lstrip('\:')
    tweet.rstrip('\:')
    tweet.lstrip('\;')
    tweet.rstrip('\;')
    
    # Strip space, " and ' from tweet
    tweet = tweet.strip(' "\'')
    # Replace emojis with either EMO_POS or EMO_NEG
    tweet = handle_emojis(tweet)
    # Replace multiple spaces with a single space
    #tweet = re.sub(r'\s+', ' ', tweet)
    words = tweet.split()
    #Removing Stop words
    new_stopwords = set(stopwords.words('english'))
    #stop_words = set(stopwords.words('english')) 
    words = [w for w in words if w not in new_stopwords] 
    for word in words:
        word = preprocess_word(word)
        '''if is_valid_word(word):
            if True:
                word = str(porter_stemmer.stem(word))
                word = lemmatizer.lemmatize(word)'''
        processed_tweet.append(word)
    #print(processed_tweet)
    return ' '.join(processed_tweet)

if __name__ == '__main__':
    lemmatizer = WordNetLemmatizer() 
    porter_stemmer = PorterStemmer()
    print("Doneeeeeeeee!!!!!!!!!!!!!1")