VOCAB = {
    1: "hello",
    2: "world",
    3: "speech",
    4: "text"
}

def tokens_to_text(tokens):

    words = []

    for token in tokens:
        words.append(VOCAB.get(token, "<unk>"))

    return " ".join(words)