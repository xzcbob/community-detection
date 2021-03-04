import word2vec

word2vec.word2vec('subgraph/amazon.subgraph2.txt','emb/word2vec64/amazon.subgraph.emb',size=64,binary=0,verbose=True)
word2vec.word2vec('subgraph/youtube.subgraph2.txt','emb/word2vec64/youtube.subgraph.emb',size=64,binary=0,verbose=True)
word2vec.word2vec('subgraph/dblp.subgraph2.txt','emb/word2vec64/dblp.subgraph.emb',size=64,binary=0,verbose=True)
word2vec.word2vec('subgraph/email2.txt','emb/word2vec64/email.emb',size=64,binary=0,verbose=True)

word2vec.word2vec('subgraph/amazon.subgraph2.txt','emb/word2vec128/amazon.subgraph.emb',size=128,binary=0,verbose=True)
word2vec.word2vec('subgraph/youtube.subgraph2.txt','emb/word2vec128/youtube.subgraph.emb',size=128,binary=0,verbose=True)
word2vec.word2vec('subgraph/dblp.subgraph2.txt','emb/word2vec128/dblp.subgraph.emb',size=128,binary=0,verbose=True)
word2vec.word2vec('subgraph/email2.txt','emb/word2vec128/email.emb',size=128,binary=0,verbose=True)