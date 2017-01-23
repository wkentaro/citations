#!/usr/bin/env python

import os.path as osp

import bibtexparser


this_dir = osp.dirname(osp.realpath(__file__))


def main():
    bib_file = osp.join(this_dir, 'citations.bib')
    with open(bib_file) as f:
        bib = bibtexparser.loads(f.read())

    required_fields = ['title', 'author', 'booktitle', 'link']
    for entry in bib.entries:
        cite_id = entry['ID']
        missing = [k for k in required_fields if k not in entry]
        if missing:
            print('WARNING: entry [%s] has missing info: %s' %
                  (cite_id, ', '.join(missing)))

    writer = bibtexparser.bwriter.BibTexWriter()
    with open(bib_file, 'w') as f:
        f.write(writer.write(bib)[:-1])


if __name__ == '__main__':
    main()
