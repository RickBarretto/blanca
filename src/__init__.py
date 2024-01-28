from .import classifier
from .import decoder

def load(content: str) -> dict:
    return decoder.decode(classifier.classify(content))