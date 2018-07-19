#! usr/bin/python

# Given

# {
#   "like",
#   "love",
#   "hate",
#   "yes"
# }
# the longest words are ["like", "love", "hate"].

#A dict with only keys is called a set.

#created as a set object
# d = {
#   "like",
#   "love",
#   "hate",
#   "yes"
# }


def find_longest_words(input):
    word_len_dict = {}
    for word in d:
        word_len_dict[word]=len(word)

    longest_word = max(word_len_dict, key = word_len_dict.get)
    longest_word_length= word_len_dict[longest_word]

    #using list comprehension
    longest_words = [k for k,v in word_len_dict.iteritems() if v == longest_word_length]

    # for k,v in word_len_dict.iteritems():
    #     print k,v
    #     if v == longest_word_length:
    #         longest_words.append(k)

    return longest_words

if __name__ == "__main__":
    input =  {"like","love","hate","yes"}
    print find_longest_words(input)
