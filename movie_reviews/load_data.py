def load_base_training():
    file = open('/data/kaggle/movie_reviews/data/train.tsv')

    # One dict for phrase length (in words)
    train_dicts = []
    for _ in range(53):  # Longest phrase contains 53 words
        train_dicts.append({})
    
    # Ignore heading
    file.next()

    #print file.next().strip().split('\t')
    for l in file:
        phraseid, sentenceid, phrase, sentiment = l.strip().split('\t')
        phrase = phrase.lower()
        words = phrase.split(' ')
        train_dicts[len(words)][phrase] = sentiment

    return train_dicts


def load_base_test():
    testfile = open('/data/kaggle/movie_reviews/data/test.tsv') 

    test_lines = []

    # Ignore Heading
    testfile.next()

    for l in testfile:
        phraseid, sentenceid, phrase = l.strip().split('\t')
        test_lines.append((phraseid, phrase.lower()))

    return test_lines



def lookup_dict(train_dicts, phrase):
    num_words = len(phrase.split(' '))

    if num_words > 52:
        return None

    #print "Looking for phrase: " + phrase + " -- Returning: " + str(train_dicts[num_words].get(phrase))
    return train_dicts[num_words].get(phrase)


def write_submission(array):
    filename = '/data/kaggle/movie_reviews/data/submission.csv'
    print "Writing output to filename: " + filename
 
    outputfile = open(filename, 'w') 
    outputfile.write("PhraseId,Sentiment\n")

    for el in array:
        outputfile.write(str(el[0]) + "," + str(el[1]) + "\n")

    outputfile.close() 
     

def calculate_most_frequent(train_dicts):
    most_frequent = []

    for i in range(len(train_dicts)):
        distrib_sentiments = [0]*6

        for item in train_dicts[i]:
            distrib_sentiments[int(train_dicts[i][item])] += 1
            distrib_sentiments[5] += 1
        print "Looking at phrase size: " + str(i) + ", total phrases: " + str(distrib_sentiments[5]) + " -->" + \
              str([round(float(x)/max(distrib_sentiments[5],1), 2) for x in distrib_sentiments[0:5]])
        most_frequent.append(max( (v, i) for i, v in enumerate(distrib_sentiments[0:5]) )[1])
    
    most_frequent = most_frequent + [2,]*100  # Autocomplete with 2s
    return most_frequent


