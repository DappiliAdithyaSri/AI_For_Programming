### GC Content

`scripts/gc_content.py` reports the GC content of sequences in a FASTA file. It accepts a FASTA file path and outputs each record’s header and GC percentage, rounded to two decimal places. Empty sequences are skipped with a warning. The optional `--min-gc <float>` setting displays only records with GC content strictly above the specified percentage.
