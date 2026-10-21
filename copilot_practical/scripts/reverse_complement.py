# reverse_complement.py
# Reads a DNA sequence from a FASTA file and prints its
# reverse complement.

COMPLEMENT = {
    "A": "T", "T": "A", "C": "G", "G": "C",
}

def read_fasta_sequence(path):
    """Return the sequence (str) from a single-record FASTA file."""
    sequence_lines = []
    found_header = False

    with open(path, encoding="utf-8") as fasta:
        for line in fasta:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if found_header or sequence_lines:
                    raise ValueError("Expected a single FASTA record")
                found_header = True
                continue
            sequence_lines.append("".join(line.split()))

    sequence = "".join(sequence_lines)
    if not sequence:
        raise ValueError("FASTA file does not contain a sequence")
    return sequence

def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    try:
        return "".join(COMPLEMENT[base] for base in reversed(seq))
    except KeyError as error:
        raise ValueError(
            f"Invalid DNA base {error.args[0]!r}; sequence may contain only A, T, C, or G."
        ) from error

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Print a DNA sequence's reverse complement.")
    parser.add_argument("fasta", help="path to a single-record FASTA file")
    args = parser.parse_args()

    seq = read_fasta_sequence(args.fasta)
    print(reverse_complement(seq))
