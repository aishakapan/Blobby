#Analyzing user message sentiment

from pysentimiento import create_analyzer

analyzer = create_analyzer(task="sentiment", lang="en")

results = analyzer.predict("I have seen a pretty flower")
print(dict(results['output']))
