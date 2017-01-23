#!/usr/bin/env python

import os.path as osp

import bibtexparser
import tabulate


def abbreviate_booktitle(booktitle, year):
    if 'Computer Vision and Pattern Recognition' in booktitle:
        return 'CVPR' + year
    elif 'International Conference on Robotics and Automation' in booktitle:
        return 'ICRA' + year
    elif 'International Conference on Humanoid Robots' in booktitle:
        return 'Humanoids' + year
    elif 'Intelligent Robots and Systems' in booktitle:
        return 'IROS' + year
    elif 'International Conference on Machine Learning' in booktitle:
        return 'ICML' + year
    elif 'International Conference on Learning Representations' in booktitle:
        return 'ICLR' + year
    elif 'International Symposium on Experimental Robotics' in booktitle:
        return 'ISER' + year
    elif 'ISRR' in booktitle:
        return 'ISRR' + year
    elif 'Proceedings of Robotics: Science and Systems' in booktitle:
        return 'RSS' + year
    elif 'International Conference on Technologies for Practical Robot Applications' in booktitle:
        return 'TePRA' + year
    elif 'International Conference on Mechatronics and Automation' in booktitle:
        return 'ICMA' + year
    elif 'International Journal of Computer Vision' in booktitle:
        return 'IJCV' + year
    elif 'International Journal of Robotics Research' in booktitle:
        return 'IJRR' + year
    elif 'Neural Information Processing Systems' in booktitle:
        return 'NIPS' + year
    elif 'DAAAM' in booktitle:
        return 'DAAAM' + year
    elif 'arXiv' in booktitle:
        return 'arXiv' + year
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
    with open(bib_file) as f:
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
            booktitle = entry.get('booktitle') or entry['journal']
            book = abbreviate_booktitle(booktitle, entry['year'])
            citations.append((tex, linked_title, author, book))
        md_table = tabulate.tabulate(citations, headers=headers,
                                    tablefmt='pipe', stralign='center')
        f.write(md_table + '\n')


if __name__ == '__main__':
    main()
