#!/usr/bin/env python

import bibtexparser
import tabulate


def abbreviate_booktitle(booktitle, year):
    if 'Computer Vision and Pattern Recognition' in booktitle:
        return 'CVPR' + year
    else:
        return booktitle


with open('citations.bib', 'r') as f:
    bib = bibtexparser.loads(f.read())


with open('README.md', 'w') as f:
    f.write('# citations\n')
    f.write('\n')

    citations = []
    headers = ['tex', 'title', 'author', 'book']
    for entry in bib.entries:
        tex = '`\cite{%s}`' % entry['ID']
        linked_title = '[%s](%s)' % (entry['title'], entry['link'])
        authors = entry['author'].split('and')
        if len(authors) > 1:
            author = authors[0] + 'et al.'
        else:
            author = author[0]
        book = abbreviate_booktitle(entry['booktitle'], entry['year'])
        citations.append((tex, linked_title, author, book))
    md_table = tabulate.tabulate(citations, headers=headers,
                                 tablefmt='pipe', stralign='center')
    f.write(md_table + '\n')
