#!/usr/bin/env python

import os.path as osp

import bibtexparser
import tabulate


def abbreviate_booktitle(booktitle, year):
    if 'Computer Vision and Pattern Recognition' in booktitle:
        return 'CVPR' + year
    else:
        return booktitle


def abbreviate_author(author):
    authors = author.split('and')
    if len(authors) > 1:
        abbreviated = authors[0] + 'et al.'
    else:
        abbreviated = authors[0]
    return abbreviated


this_dir = osp.dirname(osp.realpath(__file__))


def main():
    bib_file = osp.join(this_dir, 'citations.bib')
    with open(bib_file, 'r') as f:
        bib = bibtexparser.loads(f.read())

    readme_file = osp.join(this_dir, 'README.md')
    with open(readme_file, 'w') as f:
        f.write('# citations\n')
        f.write('\n')

        citations = []
        headers = ['tex', 'title', 'author', 'book']
        for entry in bib.entries:
            tex = '`\cite{%s}`' % entry['ID']
            linked_title = '[%s](%s)' % (entry['title'], entry['link'])
            author = abbreviate_author(entry['author'])
            book = abbreviate_booktitle(entry['booktitle'], entry['year'])
            citations.append((tex, linked_title, author, book))
        md_table = tabulate.tabulate(citations, headers=headers,
                                    tablefmt='pipe', stralign='center')
        f.write(md_table + '\n')


if __name__ == '__main__':
    main()
