## Bioinformatics Tools (bit)
These are a collection of one-liners and short scripts I use frequently enough that it's been worth it for me to have them instantly available anywhere. This includes things like: downloading NCBI assemblies in different formats by just providing accession numbers; removing those annoying line wraps from fasta files that keep you from doing things like `grep`-ing sequences of interest by header; quickly counting the number of bases or amino acids in a file; calculating GC; pulling out sequences by their coordinates; splitting a fasta file based on headers; and other such things that are just handy to have handy. Some require <a href="https://biopython.org/wiki/Download" target="_blank">biopython</a> and <a href="https://pypi.org/project/pybedtools/" target="_blank">pybedtools</a>.

For installation, you can clone this git repo and add it to your PATH. If you're new to this stuff, you can find help on <a href="https://astrobiomike.github.io/bash/installing_tools#my-bioinformatics-tools-bit" target="_blank">installing these tools here</a>, info about <a href="https://astrobiomike.github.io/bash/modifying_your_path" target="_blank">what exactly your PATH is here</a>, and all other kinds of helpful things at <a href="https://astrobiomike.github.io" target="_blank">my site</a> 🙂  

Each command has a help menu accessible by either entering the command alone or by providing `-h` as the only argument. Once downloaded and in your PATH, you can see all by entering `bit-` and pressing tab twice.
