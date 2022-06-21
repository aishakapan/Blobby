#Analyzing user message sentiment

from pysentimiento import create_analyzer

def process_sentiment(message):
    '''Takes a user message as input and outputs
    appropriate response based on the sentiment of message'''
    blob_response = None
    analyzer = create_analyzer(task='sentiment', lang='en')
    print(message)
    results = analyzer.predict(message)
    print(results)
    output = results.output
    print(output)

    if output == 'POS':
        blob_response = 'Yay :D'
    elif output == 'NEG':
        blob_response = 'Aw :('
    else:
        blob_response = 'Oh OK!'

    return blob_response



if __name__ == '__main__':
    print(process_sentiment('well fuck you stupid motherfucking bitch i hate you'))  # Aw :(
    print(process_sentiment('i got dumped')) # Aw :(
    print(process_sentiment('i am very happy today')) # Yay :D
    print(process_sentiment('it is quite normal')) #