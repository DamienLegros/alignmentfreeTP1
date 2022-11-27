from loading import load_directory
from kmers import encode2kmr, encode2str, encode2scr
from collections import Counter
import time
import numpy as np
import pandas as pd
import dataframe_image as dfi


def similarity(A, inter, B):
    """ Calculate the similarity score
    :param list A: List of integer kmers of genome A
    :param list inter: List of integer kmers of the intersection between A et B
    :param list B: List of integer kmers of genome B
    :return float: Similarity score calculated"""
    return (len(inter)/(len(A)), len(inter)/(len(B)))


def jaccard(A, inter, B):
    """ Calculate the jaccard score
    :param list A: List of integer kmers of genome A
    :param list inter: List of integer kmers of the intersection between A et B
    :param list B: List of integer kmers of genome B
    :return float: Jaccard score calculated"""
    return (len(inter)/(len(A)+len(B)-len(inter)))


def method1(file1, file2, k):
    """ Calculate A, inter and B using the method1
    :param list file1: data of genome A
    :param list file2: data of genome B
    :param int k: size of the kmer
    :return tuple: list of A, inter and B spaces"""
    inter = []
    A = encode2kmr("".join(file1), k)
    A_dict = Counter(A)
    seq = "".join(file2)
    B = []
    kmr = 0
    rkmr = 0
    mask = (1 << ((k-1)*2))-1
    scores = {"A": 0, "C": 1, "T": 2, "G": 3}
    rscores = {"A": 2, "C": 3, "T": 0, "G": 1}
    for i in range(k-1):
        kmr = kmr << 2
        rkmr = rkmr >> 2
        kmr += encode2scr(seq[i], scores)
        rkmr += encode2scr(seq[i], rscores) << (k-1)*2
    for ncl in seq[k-1:]:
        kmr = kmr & mask
        kmr = kmr << 2
        rkmr = rkmr >> 2
        kmr += encode2scr(ncl, scores)
        rkmr += encode2scr(ncl, rscores) << (k-1)*2
        Kmr = min(kmr, rkmr)
        B.append(Kmr)
        if Kmr in A_dict:
            inter.append(Kmr)
            if A_dict[Kmr] == 1:
                del A_dict[Kmr]
            else:
                A_dict[Kmr] = A_dict[Kmr]-1
    return A, inter, B


def method2(file1, file2, k):
    """ Calculate A, inter and B using the method2
    :param list file1: data of genome A
    :param list file2: data of genome B
    :param int k: size of the kmer
    :return tuple: list of A, inter and B spaces"""
    A = sorted(encode2kmr("".join(file1), k))
    B = sorted(encode2kmr("".join(file2), k))
    i = 0
    j = 0
    inter = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            inter.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return A, inter, B


if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21
    names = ['ASM584', 'ASM694', 'ASM886', 'ASM2216', 'ASM824478']
    matrix_jaccard = np.zeros((len(files), len(files)))
    matrix_similarity1 = np.zeros((len(files), len(files)))
    matrix_similarity2 = np.zeros((len(files), len(files)))
    filenames = list(files.keys())
    for i in range(len(files)):
        for j in range(len(files)):
            start_t = time.time()
            A, inter, B = method1(
                files[filenames[i]], files[filenames[j]], k)
            #A, inter, B = method2(files[filenames[i]], files[filenames[j]], k)
            end_t = time.time()
            print("Names of .fna files for comparison: " +
                  filenames[i] + ' ' + filenames[j])
            matrix_jaccard[i][j] = jaccard(A, inter, B)
            print("Jaccard score: " + str(jaccard(A, inter, B)))
            matrix_similarity1[i][j] = similarity(A, inter, B)[0]
            matrix_similarity2[i][j] = similarity(A, inter, B)[1]
            print("Similarity score: " + str(similarity(A, inter, B)))
            print("Time spent: " + str(end_t-start_t))

    df_jaccard = pd.DataFrame(
        matrix_jaccard, index=names, columns=names)
    df_similarity1 = pd.DataFrame(
        matrix_similarity1, index=names, columns=names)
    df_similarity2 = pd.DataFrame(
        matrix_similarity2, index=names, columns=names)
    dfi.export(df_jaccard, 'df_jaccard.png')
    dfi.export(df_similarity1, 'df_similarity1.png')
    dfi.export(df_similarity2, 'df_similarity2.png')
