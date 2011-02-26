#    blocks.py Solution of the blocks ICPC problem
#    Copyright (C) 2011 Sakis Kasampalis <faif at dtek period gr> 

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

ERR = -1
NO_ERR = 0
fin = None 

# open the input file
try:
    fin = open('data')
except IOError as e:
    print('file error:', e)
    exit(ERR)

n_blocks = None

# read the input
for line in fin:
    try:
        print(line, end='')
        if None is n_blocks:
            n_blocks = int(line)
        if 'quit' in line:
            exit(NO_ERR)
    except ValueError as e:
        print('input error:', e)
        exit(ERR)
