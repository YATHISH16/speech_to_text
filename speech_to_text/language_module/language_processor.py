from language_module.grammar_corrector import correct_grammar
from language_module.punctuation import add_punctuation
from language_module.formatter import format_text


def process_text(text):

    text = format_text(text)

    print("Language Processing Complete")

    return text