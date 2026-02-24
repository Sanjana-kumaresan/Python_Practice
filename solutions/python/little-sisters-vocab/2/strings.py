def add_prefix_un(word):
    return "un" + word
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = [prefix + word for word in vocab_words[1:]]
    return " :: ".join([prefix] + words)
def remove_suffix_ness(word):
    if word.endswith("iness"):
        return word[:-5] + "y"
    elif word.endswith("ness"):
        return word[:-4]
    return word
def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    words = sentence.split()
    word = words[index].strip(".,!?")
    return word + "en"