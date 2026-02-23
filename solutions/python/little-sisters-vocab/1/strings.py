"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string
    with the prefix followed by the words with prefix prepended,
    separated by ' :: '.
    """
    prefix = vocab_words[0]
    words = [prefix + word for word in vocab_words[1:]]
    return " :: ".join([prefix] + words)


def remove_suffix_ness(word):
    """Remove the suffix 'ness' from the word while keeping spelling in mind."""
    if word.endswith("iness"):
        # heaviness -> heavy
        return word[:-5] + "y"
    elif word.endswith("ness"):
        # sadness -> sad
        return word[:-4]
    return word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    words = sentence.split()
    word = words[index].strip(".,!?")
    return word + "en"