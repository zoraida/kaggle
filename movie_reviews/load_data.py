def load_base_training():
    """
        Returns an array of ({att1:?, att2:?, ..., attN:?}, sentiment_value)
    """
    file = open('/Users/zoraida/Analytics/rotten-tomatoes/data/train.tsv')

    train_lines = []

    # Ignore heading
    file.next()

    for l in file:
        phraseid, sentenceid, phrase, sentiment = l.split('\t')
        train_lines.append((build_features(phrase), sentiment))

    return train_lines


def load_base_test():
    """
        Returns an array of {features:{att1:?, att2:?, ..., attN:?}, phrase_id:?}
    """
    testfile = open('/Users/zoraida/Analytics/rotten-tomatoes/data/test.tsv')

    test_lines = []

    # Ignore Heading
    testfile.next()

    for l in testfile:
        phraseid, sentenceid, phrase = l.split('\t')
        test_lines.append({'features': build_features(phrase), 'phraseid': phraseid})

    return test_lines


def build_features(phrase):
    return {'nwords': len(phrase.strip().split(' '))}


def write_submission(array):
    filename = '/Users/zoraida/Analytics/rotten-tomatoes/data/submission.csv'
    print "Writing output to filename: " + filename

    outputfile = open(filename, 'w')
    outputfile.write("PhraseId,Sentiment\n")

    for el in array:
        outputfile.write(str(el[0]) + "," + str(el[1]))

    outputfile.close()
