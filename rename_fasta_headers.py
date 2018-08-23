#!/usr/bin/env python

from Bio import SeqIO
import sys
import argparse

parser = argparse.ArgumentParser(description='This script will rename all sequences of a multifasta with the same name with an appended number to keep them unique.')

required = parser.add_argument_group('required arguments')

required.add_argument("-i", "--input_fasta", help="Starting fasta file", action="store", dest="input_fasta", required=True)
parser.add_argument("-w", "--desired_name", help='Name to give seqs (default: "Seq"', action="store", dest="wanted_name", default="Seq")
parser.add_argument("-o", "--output_prefix", help='Prefix added to output fasta (default: "Renamed").', dest="output_prefix", default="Renamed")

args = parser.parse_args()

in_fasta = open(args.input_fasta, "r")
new_header = args.wanted_name
out_fasta = open(args.output_prefix + "_" + args.input_fasta, "w")

n = 0

for seq_record in SeqIO.parse(in_fasta, "fasta"):
	n = n + 1
	out_fasta.write(">" + new_header  + "_" + str(n) + "\n")
	out_fasta.write(str(seq_record.seq) + "\n")

in_fasta.close()
out_fasta.close()

