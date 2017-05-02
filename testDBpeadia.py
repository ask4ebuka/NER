import spotlight
def dbpedia(text):
    annotations = spotlight.annotate('http://model.dbpedia-spotlight.org/en/annotate',
                                      text,
                                     confidence=0.0, support=20)
    return (annotations)
