#!/usr/bin/env python

from Bio import SeqIO
import sys
import argparse

parser = argparse.ArgumentParser('This script takes a multifasta file and reorders the sequences according to the headers provided.')

required = parser.add_argument_group('required arguments')

required.add_argument("-i", "--input_fasta", help="Original fasta file", action="store", dest="input_fasta", required=True)
required.add_argument("-w", "--wanted_sequence_order", help="Single-column file with headers in desired order", action="store", dest="ordered_headers", required=True)
parser.add_argument("-o", "--output_prefix", help='Prefix added to output fasta (default: "Reordered").', dest="output_prefix", default="Reordered")

args = parser.parse_args()

ordered_seqs = open(args.ordered_headers, "r")

ordered_list = list(line.strip() for line in ordered_seqs)

fasta_dict = SeqIO.index(args.input_fasta, "fasta")

fasta_out = open(args.output_prefix + "_" + args.input_fasta, "w")

for header in ordered_list:
  fasta_out.write(fasta_dict.get_raw(header))

ordered_seqs.close()
fasta_out.close()
