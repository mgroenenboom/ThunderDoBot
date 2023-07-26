from profanity_filter import ProfanityFilter
import spacy



def find_bad_words(text):
    nlp = spacy.load('en_core_web_sm')
    profanity_filter = ProfanityFilter(nlps={'en':nlp})
    nlp.add_pipe(profanity_filter.spacy_component, last=True)

    doc = nlp(text)

    return doc._.is_profane
