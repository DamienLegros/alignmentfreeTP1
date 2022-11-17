
def encode2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)


def encode2scr(ncl, scores):
    """ Transform a nucleotide character into a its score integer
    :param char ncl: A nucleotide character
    :param dict scores: The dict of score corresponding to each nucleotide
    :return int: The score integer of ncl
    """
    if ncl in scores:
        return scores[ncl]
    else:
        return 0


def encode2kmr(seq, k):
    """ Transform a sequence to a list of integers each corresponding to a kmer
    :param list seq: A sequence of nucleotides
    :param int k: The number of nucleotides involved into the kmer
    :return list: The list of integers corresponding to kmers
    """
    list_kmr = []
    kmr = 0
    rkmr = 0
    mask = (1 << ((k-1)*2))-1
    rmask = (1 << (k*2))-1-3
    scores = {"A": 0, "C": 1, "T": 2, "G": 3}
    rscores = {"A": 2, "C": 3, "T": 0, "G": 1}
    for i in range(k-1):
        kmr = kmr << 2
        rkmr = rkmr >> 2
        kmr += encode2scr(seq[i], scores)
        rkmr += encode2scr(seq[i], rscores) << (k-1)*2
    for nucl in seq[k-1:]:
        kmr = kmr & mask
        # rkmr=rkmr&rmask
        kmr = kmr << 2
        rkmr = rkmr >> 2
        kmr += encode2scr(nucl, scores)
        rkmr += encode2scr(nucl, rscores) << (k-1)*2
        list_kmr.append(min(kmr, rkmr))
    return list_kmr
