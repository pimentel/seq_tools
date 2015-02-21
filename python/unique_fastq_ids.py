import os
import sys

from Bio import SeqIO

def usage():
    print >> sys.stderr, "python unique_fastq_ids.py some_reads.fastq out.fastq"

def unique_id_filter(records):
    ids_seen = set()
    for rec in records:
        if rec.id in ids_seen:
            print sys.stderr, "Seen id: {0}. Skiping.".format(rec.id)
            continue
        ids_seen.add(rec.id)
        yield rec

def main():
    if len(sys.argv) != 3:
        usage()

    reads = sys.argv[1]
    # check if file exists
    if not os.path.isfile(reads):
        print >> sys.stderr, "Error: Couldn't find file {0}".format(reads)
        sys.exit(1)

    fastq_parse = SeqIO.parse(reads, "fastq")
    with open(sys.argv[2], "w") as out_hande:
        SeqIO.write(unique_id_filter(fastq_parse), out_hande, "fastq")

if __name__ == '__main__':
    main()
