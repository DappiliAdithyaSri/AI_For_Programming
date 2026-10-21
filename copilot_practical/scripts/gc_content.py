"""Print the GC percentage for each sequence in a FASTA file."""

import argparse
import sys


def read_fasta_records(path):
    """Yield (header, sequence) pairs from a multi-record FASTA file."""
    header = None
    sequence_lines = []

    with open(path, encoding="utf-8") as fasta:
        for line in fasta:
            line = line.strip()
            if line.startswith(">"):
                if header is not None:
                    yield header, "".join(sequence_lines)
                header = line[1:]
                sequence_lines = []
            elif line and header is not None:
                sequence_lines.append("".join(line.split()))

    if header is not None:
        yield header, "".join(sequence_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Print GC content for each sequence in a FASTA file."
    )
    parser.add_argument("fasta", help="path to a FASTA file")
    parser.add_argument(
        "--min-gc",
        type=float,
        default=None,
        metavar="<float>",
        help="only print records with GC content strictly above this percentage",
    )
    args = parser.parse_args()
    if args.min_gc is not None and not 0 <= args.min_gc <= 100:
        parser.error("--min-gc must be between 0 and 100")

    for header, sequence in read_fasta_records(args.fasta):
        if not sequence:
            print(f"Warning: skipping empty sequence for record {header!r}.", file=sys.stderr)
            continue
        gc_percent = sum(base in "GgCc" for base in sequence) / len(sequence) * 100
        if args.min_gc is not None and gc_percent <= args.min_gc:
            continue
        print(f"{header}\t{gc_percent:.2f}%")


if __name__ == "__main__":
    main()
