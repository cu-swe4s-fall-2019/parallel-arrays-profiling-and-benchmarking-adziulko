import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt




def boxplot(L, groups, group_col_name, gene_name, boxplot_name):


    X = []
    for l in L:
        A = X.append(l)

    num_ticks = [ i for i in range(1, len(groups)+2) ]

    fig = plt.figure(figsize=(10,3), dpi=300)
    ax = fig.add_subplot(1,1,1)
    ax.boxplot(X)
    plt.xticks(num_ticks, groups, rotation='vertical')
    plt.title(gene_name)
    plt.xlabel(group_col_name)
    plt.ylabel('gene read #')
    plt.savefig(boxplot_name, bbox_inches='tight')



def histogram(L, out_file_name):

    out_file = out_file_name
    D = []

    for l in sys.stdin:
        A = l.rstrip().split()
        D.append(float(A[0]))
        D.append(float(A[1]))

    width=3
    height=3

    fig = plt.figure(figsize=(width,height),dpi=300)
    ax = fig.add_subplot(1,1,1)
    ax.hist(D)
    plt.savefig(out_file,bbox_inches='tight')


def combo(L, out_file_name):

    out_file = out_file_name
    X = []
    Y = []
    D = []

    for l in sys.stdin:
        A = l.rstrip().split()
        X.append(float(A[0]))
        Y.append(float(A[1]))
        D.append(float(A[0]))
        D.append(float(A[1]))

    width=5
    height=3

    fig = plt.figure(figsize=(width,height),dpi=300)
    ax = fig.add_subplot(1,2,1)
    ax.boxplot(L)
    ax = fig.add_subplot(1,2,2)
    ax.hist(D)
    plt.savefig(out_file,bbox_inches='tight')
