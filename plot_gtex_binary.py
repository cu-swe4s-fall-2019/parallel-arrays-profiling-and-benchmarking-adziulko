import gzip
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
import argparse
import data_viz
import importlib
sys.path.append('hash-tables-adziulko')
hf = importlib.import_module('hash-tables-adziulko.hash_functions')
ht = importlib.import_module('hash-tables-adziulko.hash_tables')


def linear_search(key, L):
    for i  in range(len(L)):
        curr =  L[i]
        if key == curr:
            return i
    return -1


def binary_search(key, D):
    lo = -1
    hi = len(D)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == D[mid][0]:
            return D[mid][1]

        if (key < D[mid][0]):
            hi = mid
        else:
            lo = mid

    return -1



def main():
    parser = argparse.ArgumentParser(description=
                                     'boxplot gene expression distribution across \
                                      tissue groups or tissue types for a gene')

    parser.add_argument('--fngr', '-file_name_gene_reads',
                        type=str,
                        help='Input RNA Seq gene read file (gziped)',
                        required = True)

    parser.add_argument('--fna', '-file_name_annotations',
                        type=str,
                        help='Input sample attributes file (txt)',
                        required = True)

    parser.add_argument('--t', '-tissue',
                        type=str,
                        help='Input either tissue group (SMTS) or tissue type (SMTSD)',
                        required = True)

    parser.add_argument('--tg', '-target_gene',
                        type=str,
                        help='Input target gene',
                        required = True)

    parser.add_argument('--bfn', '-boxplot_file_name',
                        type=str,
                        help='Name of output boxplot file',
                        required = True)

    args = parser.parse_args()


    data_file_name = args.fngr
    sample_info_file_name = args.fna
    group_col_name = args.t
    gene_name = args.tg
    boxplot_name = args.bfn

    sample_id_col_name = 'SAMPID'

    samples_to_count_map = ht.LPHashTable(1000001, hf.h_rolling)

    version = None
    dim = None
    header = None
    num_headers = 3
    counts = []
    for line in data_file_name:
        A = line.rstrip().split('\t')

        if version == None:
            version = A
            continue

        if dim == None:
            dime = A
            continue

        if header == None:
            header = A
            continue

        if A[1] == gene_name:
            for a in A[2:]:
                counts.append(int(a))
            break
        data_file_name.close()

        samples = header[2:]


#binary_serach
    samples = []
    sample_info_header = None
    for l in open(sample_info_file_name):
        if sample_info_header == None:
            sample_info_header = l.rstrip().split('\t')
        else:
            samples.append(l.rstrip().split('\t'))

    group_col_idx = linear_search(group_col_name, sample_info_header)
    sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)

    groups = []
    members = []

    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]

        curr_group_idx = linear_search(curr_group, groups)

        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])

        members[curr_group_idx].append(sample_name)

    version = None
    dim = None
    data_header = None

    gene_name_col = 1


    group_counts = [ [] for i in range(len(groups)) ]

    for l in gzip.open(data_file_name, 'rt'):
        if version == None:
            version = l
            continue

        if dim == None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if data_header == None:
            data_header = []
            i = 0
            for field in l.rstrip().split('\t'):
                data_header.append([field, i])
                i += 1
            data_header.sort(key=lambda tup: tup[0])

            continue

        A = l.rstrip().split('\t')

        if A[gene_name_col] == gene_name:
            for group_idx in range(len(groups)):
                for member in members[group_idx]:
                    member_idx = binary_search(member, data_header)
                    if member_idx != -1:
                        group_counts[group_idx].append(int(A[member_idx]))
            break

    #fig = plt.figure(figsize=(10,3), dpi=300)
    #ax = fig.add_subplot(1,1,1)
    #ax.boxplot(group_counts)
    #plt.savefig(gene_name + '.ls.png', bbox_inches='tight')
    data_viz.boxplot(group_counts, groups, group_col_name, gene_name, boxplot_name)

if __name__ == '__main__':
    main()
