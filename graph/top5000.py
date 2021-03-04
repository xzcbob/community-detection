dataset = 'amazon'

if __name__ == '__main__':
    f = open('/home/xzc/学习/实验/Community detection/S1910W0692许张弛/node2vec-master/graph/com-'+dataset+'top5000.ungraph.txt','w')
    toplist = {}
    newfile = ''

    for topline in open('/home/xzc/学习/实验/Community detection/S1910W0692许张弛/node2vec-master/graph/com-'+dataset+'.top5000.cmty.txt'):
        temp = topline.split()
        for x in temp:
            if x not in toplist:
                toplist[x] = 1

    for graphline in open('/home/xzc/学习/实验/Community detection/S1910W0692许张弛/node2vec-master/graph/com-'+dataset+'.ungraph.txt'):
        temp = graphline.split()
        for x in temp:
            if x in toplist:
                f.writelines(graphline)
    
    