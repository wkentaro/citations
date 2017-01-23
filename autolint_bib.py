#!/usr/bin/env python

import os.path as osp

import bibtexparser


this_dir = osp.dirname(osp.realpath(__file__))


def main():
    bib_file = osp.join(this_dir, 'citations.bib')
    with open(bib_file) as f:
        bib = bibtexparser.loads(f.read())

    required_fields = ['title', 'author', ['booktitle', 'journal'], 'pdf']
    for entry in bib.entries:
        cite_id = entry['ID']
        missing = []
        for k in required_fields:
            if isinstance(k, list):
                if not any(kk in entry for kk in k):
                    missing.append(' or '.join(k))
            else:
                if not k in entry:
                    missing.append(k)
        if missing:
            print('ERROR: entry [%s] has missing info: %s' %
                  (cite_id, ', '.join(missing)))

        entry['author'] = entry['author'].replace('\n', ' ')

    writer = bibtexparser.bwriter.BibTexWriter()
    with open(bib_file, 'w') as f:
        f.write(writer.write(bib).encode('utf-8')[:-1])


if __name__ == '__main__':
    main()
