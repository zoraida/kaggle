import load_data

train_dicts = load_data.load_base_training()
most_freq = load_data.calculate_most_frequent(train_dicts)

test_array = load_data.load_base_test()

test_prediction = []

found = 0
missing = 0

for phraseid, phrase in test_array:
    sentiment = load_data.lookup_dict(train_dicts, phrase)
    #print phraseid, phrase
    if sentiment:                            # If found
        test_prediction.append((phraseid, sentiment))
        print (phraseid, sentiment)
        found += 1
    else:                                    # If not found
        num_words = len(phrase.split(' '))
        test_prediction.append((phraseid, str(most_freq[num_words])))
        print (phraseid, str(most_freq[num_words]))
        missing += 1

print "Found: " + str(found)
print "Missing (predicted): " + str(missing)

load_data.write_submission(test_prediction) 

#print train_dicts[1]
