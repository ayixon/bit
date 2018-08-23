#!/usr/bin/env python

from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description="This script takes a multifasta as input and returns a tab-delimited file with two columns, header and number of bases or amino acids, for each sequence." )

required = parser.add_argument_group('required arguments')

required.add_argument("-i", "--input_fasta", help="Original fasta file", action="store", dest="input_fasta")
parser.add_argument("-o", "--output_txt_file", help='Name of output txt file (default: "Num_bps.txt")', action="store", dest="output_file", default="Num_bps.txt")

args = parser.parse_args()

in_fasta = open(args.input_fasta, "r")
out_file = open(args.output_file, "w")

for seq_record in SeqIO.parse(in_fasta, "fasta"):
  out_file.write(seq_record.id + "\t" + str(len(seq_record.seq)) + "\n")

in_fasta.close()
out_file.close()


