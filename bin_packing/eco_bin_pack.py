#    <one line to give the program's name and a brief idea of what it does.>
#    Copyright (C) <year> Sakis Kasampalis <faif at dtek period gr> 

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


# beginning of the main program

fin = None 
bin = list()

# open the input file
try:
    fin = open('data')
except IOError as e:
    print('file error:', e)
    exit(ERR)

# read the input
for line in fin:
    bin = line.split()
    print(bin)
