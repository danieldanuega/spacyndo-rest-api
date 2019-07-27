# Dependency Parser

To use the API to predict **dependency parser** use this url: `spacy-id.herokuapp.com/tasks/dep`,
then use a body request (JSON) to send your text that will be predicted, like this `"text": "your text here"`.
It will send you a graph of dependency relations as a .svg file. 

# Named Entity Recognition

To use the API to predict **NER** use this url: `spacy-id.herokuapp.com/tasks/ner`,
then use a body request (JSON) to send your text that will be predicted, like this `"text": "your text here"`.
It will send you a JSON array consist of text and entity that are predicted by the model.

