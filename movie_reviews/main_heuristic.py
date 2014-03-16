import load_data
import nltk

train_set = load_data.load_base_training()
test_set = load_data.load_base_test()

classifier = nltk.NaiveBayesClassifier.train(train_set)

test_features_set = [i['features'] for i in test_set]
#print nltk.classify.accuracy(classifier, test_features_set)

test_prediction = []

for i in test_set:
    guess = classifier.classify(i['features'])
    test_prediction.append((i['phraseid'], guess))
    print (i['phraseid'], guess)

#print train_dicts[1]
load_data.write_submission(test_prediction)
