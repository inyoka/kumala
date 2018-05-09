#!/usr/bin/env python3.6

# Written by Gabi from helpfulsheep http://helpfulsheep.com/2015-03-25-converting-svg-fonts-to-svg/
# Improved by iSWORD14 (see above link) and
# A-B-B https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist/14364249#14364249
# Reformatted, colated and converted to Python3 by Inyoka.

import sys, re, pathlib


def main():
    '''
    Create an svg font file using fontastic etc, run this program in the same directory
    to split all the glyphs into separate .svg files for easy inclusion into web projects.
    '''
    if len(sys.argv) < 2:
        print('Usage: python {} webfont-file.svg'.format(sys.argv[0]))
        sys.exit()
    with open(sys.argv[1], 'r') as r:
        lines = r.read().split('\n')
        glyphs = [x for x in lines if '<glyph' in x]
        # for every glyph element in the file

        for i in range(0, len(glyphs)):
            filename = re.search(r'glyph-name="([^"]+)"', glyphs[i])
            filename = filename.group(1) if filename else str(i + 1).rjust(3, '0')

            pathlib.Path('font-folder').mkdir(exist_ok=True)
            with open("font-folder/icon-" + filename + ".svg", 'w') as w:
                w.write('<?xml version="1.0" standalone="no"?>\n')
                w.write('<svg fill="currentColor" width="1500px" height="1500px" version="1.1" xmlns="http://www.w3.org/2000/svg">\n')
                # replace 'glyph' with 'path' and flip vertically
                w.write(glyphs[i].replace('<glyph', '<path transform="scale(1, -1) translate(0, -1500)"') + '\n')
                w.write('</svg>')


if __name__ == '__main__':
    main()
