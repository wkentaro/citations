#!/usr/bin/env python

import os.path as osp

import bibtexparser
import tabulate


def abbreviate_booktitle(booktitle):
    if 'Computer Vision and Pattern Recognition' in booktitle:
        return 'CVPR'
    elif 'International Conference on Robotics and Automation' in booktitle:
        return 'ICRA'
    elif 'ICRA' in booktitle:
        return 'ICRA'
    elif 'International Conference on Humanoid Robots' in booktitle:
        return 'Humanoids'
    elif 'Intelligent Robots and Systems' in booktitle:
        return 'IROS'
    elif 'International Conference on Machine Learning' in booktitle:
        return 'ICML'
    elif 'International Conference on Learning Representations' in booktitle:
        return 'ICLR'
    elif 'International Symposium on Experimental Robotics' in booktitle:
        return 'ISER'
    elif 'ISRR' in booktitle:
        return 'ISRR'
    elif 'Proceedings of Robotics: Science and Systems' in booktitle:
        return 'RSS'
    elif 'International Conference on Technologies for Practical Robot Applications' in booktitle:  # NOQA
        return 'TePRA'
    elif 'International Conference on Mechatronics and Automation' in booktitle:
        return 'ICMA'
    elif 'International Journal of Computer Vision' in booktitle:
        return 'IJCV'
    elif 'ECCV' in booktitle:
        return 'ECCV'
    elif 'International Conference on Computer Vision' in booktitle:
        return 'ICCV'
    elif 'International Journal of Robotics Research' in booktitle:
        return 'IJRR'
    elif 'Neural Information Processing Systems' in booktitle:
        return 'NIPS'
    elif 'DAAAM' in booktitle:
        return 'DAAAM'
    elif 'arXiv' in booktitle:
        return 'arXiv'
    else:
        return booktitle


def abbreviate_author(author):
    authors = author.split(' and ')
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
        f.write('# citations (%d)\n' % len(bib.entries))
        f.write('\n')

        citations = []
        headers = ['tex', 'title', 'author', 'book', 'year']

        for entry in bib.entries:
            tex = '`\cite{%s}`' % entry['ID']
            linked_title = '[%s](%s)' % (entry['title'], entry['pdf'])
            author = abbreviate_author(entry['author'])
            booktitle = entry.get('booktitle') or entry['journal']
            book = abbreviate_booktitle(booktitle)
            year = int(entry['year'])
            citations.append((tex, linked_title, author, book, year))
        citations = sorted(citations, key=lambda x: (x[4], x[3]), reverse=True)
        md_table = tabulate.tabulate(citations, headers=headers,
                                     tablefmt='pipe', stralign='center')
        f.write(md_table + '\n')


if __name__ == '__main__':
    main()
