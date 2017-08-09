Basics of NLP and basics of NLTK

#NLP Pipeline

1. The first steps of breaking down a sentence is tokenization. This is simple splitting of words (It may be different for chinese etc). Tokenization
is followed by stemming of the tokens to get more relevant tokens and remove ones which do not matter. 

2. Part of Speech tagging assigns each word with a speech tag. How this is being done is still not clear, I think some form of Markov Model is 
used but I am not clear what. 

3. 3rd step is the Named Entity Recognition problem. I think this is the relevant problem. Here a token is classified or the entire sequence is
classified. 

4. Relation Extraction - I have not looked at this
