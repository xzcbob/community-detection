import gc
import random

dataset = 'youtube'

if __name__ == '__main__':
    graphFile = open('graph/com-'+dataset+'.ungraph.txt')
    #graphFile = open('graph/email-Eu-core.txt')
    graphDict = {}
    #comFlie = open('ground-truth/com-'+dataset+'.all.cmty.txt')
    comFlie = open('ground-truth/com-'+dataset+'.top5000.cmty.txt')
    #comFlie = open('ground-truth/email-Eu-core-department-labels.txt')

    comDict = {}
    '''
    for topline in open('ground-truth/email-Eu-core-department-labels.txt'):
        [a,b] = topline.split()
        comDict[a] = b
    '''
    comLine = comFlie.readline()
    while comLine:
        temp = comLine.split()
        if len(temp) >= 3:
            for i in temp:
                if i not in comDict:
                    comDict[i] = 1

        comLine = comFlie.readline()
    
    for x in range(5):
        graphLine = graphFile.readline()
    
    subgraphtext = open('subgraph/'+dataset+'.subgraph.txt','w')
    #subgraphtext = open('subgraph/'+dataset+'.subgraph2.txt','w')
    #subgraphtext = open('subgraph/email2.txt','w')
    
    
    while graphLine:
        [a,b] = graphLine.split()
        if a in comDict and b in comDict:
            subgraphtext.writelines(a+'\t'+b+'\n')
        graphLine = graphFile.readline()
    
    '''
    graphLine = graphFile.readline()
    while graphLine:
        [a,b] = graphLine.split()
        if a in comDict and b in comDict:
            subgraphtext.writelines(a+' '+b+' ')
        graphLine = graphFile.readline()
    '''

    '''
    while graphLine:
        [a,b] = graphLine.split()
        if a in comDict and b in comDict:
            if a in graphDict:
                graphDict[a].append(b)
            else:
                graphDict[a] = [b]

            if b in graphDict:
                graphDict[b].append(a)
            else:
                graphDict[b] = [a]
        graphLine = graphFile.readline()

    
    随机生成图  效果较差
    nodenum = 0
    quene = []
    for i in range(5):
        quene.append(random.choice(list(graphDict)))
    subgraph = {}
    subgraphtext = open('subgraph/'+dataset+'.subgraph.txt','w')
    while nodenum < subgraphsize and quene != []:
        temp = quene.pop(0)
        for x in graphDict[temp]:
            if not(temp in subgraph and x in subgraph[temp] or x in subgraph and temp in subgraph[x]):
                subgraphtext.writelines(temp+'\t'+x+'\n')
                quene.append(x)
                nodenum += 1
                if temp in subgraph:
                    subgraph[temp].append(x)
                else:
                    subgraph[temp] = [x]
    '''

