#Analyzing user message sentiment

from pysentimiento import create_analyzer

def process_sentiment():
    analyzer = create_analyzer(task='sentiment', lang='en')
    results = analyzer.predict('I have seen a pretty flower')
    output = str(results)
    return output[22:25]

def blob_talk():
    blob_sentiment = process_sentiment()
    blob_response = None
    if blob_sentiment == 'POS':
        blob_response = 'Yay :D'
    elif blob_sentiment == 'NEG':
        blob_response = 'Aw :('
    else:
        blob_response = 'Oh OK!'

    return blob_response




