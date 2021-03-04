# 社区发现机器学习代码（Community detection based on machine learning）

## 目前代码已包括：

* DBSCAN
* K-Means
* Optics

图嵌入（Graph embedding）后的 amazon 数据集 node2vec(64) 数据已经放在了 emb 文件夹下，可以直接跳过实验步骤 1-3

代码基于斯坦福数据集（Stanford Large Network Dataset Collection），数据下载：http://snap.stanford.edu/data/。

机器学习部分代码需要使用 sklearn 所以先安装

pip3 install sklearn

实验步骤：

1.将图数据放在 graph 文件夹下，将 top 5,000 社区数据放在 ground-truth 文件夹下。

2.对于不同的数据集，修改并运行 generate_subgraph.py 中的代码，生成过滤后的子图。

3.使用两种图嵌入方法 word2vec node2vec 。

	word2vec 运行 gengrate_word2vec_emb.py。
	node2vec 指令如下：

	node2vec

	python2 src/main.py --input subgraph/youtube.subgraph.txt --output emb/node2vec128/youtube.subgraph.emb --dimensions 128
	python2 src/main.py --input subgraph/youtube.subgraph.txt --output emb/node2vec64/youtube.subgraph.emb --dimensions 64


4.运行 dbscan.py 以验证结果。如有兴趣也可以运行 k-means.py 和 optics.py。
