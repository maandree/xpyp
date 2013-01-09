#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
xpyp – compresses python scripts

Copyright © 2013  Mattias Andrée (maandree@kth.se)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
from subprocess import Popen, PIPE


def printerr(text = '', end = '\n'):
    sys.stderr.buffer.write((str(text) + end).encode('utf-8'))
    sys.stderr.buffer.flush()


class xpyp:
    def __init__(self, remove_comments      = True, remove_blank_lines = True,
                       remove_documentation = True, remove_spaces      = True,
                       compress_indention   = True, parse_escapes      = True,
                       remove_lines         = True):
        self.removeComments = remove_comments
        self.removeBlankLines = remove_blank_lines
        self.removeDocumentation = remove_documentation
        self.removeSpaces = remove_spaces
        self.compressIndention = compress_indention
        self.parseEscapes = parse_escapes
        self.removeLines = remove_lines
    
    
    
    def getEncoding(self, scriptfile):
        return None
    
    
    def pack(self, scriptfile, encoding):
        script = []
        with open(scriptfile, 'rb'):
            script = scriptfile.read().decode(encoding.lower(), 'replace')
            script = script.replace('\r', '\n').replace('\f', '\n')
            script = [line.replace('\n') for line in script.split('\n')]
        
        if self.removeComments      : self.packComments     (script)
        if self.removeDocumentation : self.packDocumentation(script)
        if self.removeSpaces        : self.packSpaces       (script)
        if self.removeBlankLines    : self.packBlankLines   (script)
        if self.compressIndention   : self.packIndention    (script)
        if self.parseEscapes        : self.packEscapes      (script)
        if self.removeLines         : self.packLines        (script)
        
        script = '\n'.join(script) + '\n'
        with open(scriptfile, 'wb'):
            scriptfile.write(script.encode(encoding.lower()))
            scriptfile.flush()
    
    
    
    def packComments(self, code):
        pass
    
    
    def packDocumentation(self, code):
        pass
    
    
    def packSpaces(self, code):
        pass
    
    
    def packBlankLines(self, code):
        pass
    
    
    def packIndention(self, code):
        pass
    
    
    def packEscapes(self, code):
        pass
    
    
    def packLines(self, code):
        pass



if __name__ == '__main__':
    scriptfiles = []
    dashed = False
    c = False
    d = False
    s = False
    b = False
    i = False
    e = False
    l = False
    for arg in sys.argv[1:]:
        if dashed:
            scriptfiles.append(arg)
        elif arg == '--':
            dashed = True
        elif arg == '-c' : c = True
        elif arg == '-d' : d = True
        elif arg == '-s' : s = True
        elif arg == '-b' : b = True
        elif arg == '-i' : i = True
        elif arg == '-e' : e = True
        elif arg == '-l' : l = True
        elif not arg.startsWith('-'):
            scriptfiles.append(arg)
        else:
            printerr('Unrecognised option: ' + arg)
    packer = xpyp()
    if c or d or s or b or i or e or l:
        packer = xpyp(c, d, s, b, i, e, l)
    for scriptfile in scriptfiles:
        encoding = packer.getEncoding(scriptfile)
        if encoding != None:
            packer.pack(scriptfile, encoding)
        else:
            printerr('Cannot not compress file')

