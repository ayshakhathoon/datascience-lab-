import nltk
token="THE BIG CAT ATE THE LITTLE MOUSE WHO WAS AFTER THE FRESH CHEESE"
new_token=nltk.wordpunct_tokenize(token)
print(new_token)
new_tag=nltk.pos_tag(new_token)
print(new_tag)
grammer= "NP: {<DT>?<JJ>*<NN>} "
chunkParser=nltk.RegexpParser(grammer)
chunked=chunkParser.parse(new_tag)
print(chunked)
chunked.draw()