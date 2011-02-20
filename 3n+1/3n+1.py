#    3n+1.py Solution of the 3n+1 ICPC problem
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

# calculates the cycle length of the given number
# @param the input number
# @return the cycle length as an integer
def cycle_length(n):
    assert(n > 0)
    c = 0
    while n != 1:
        # print(n)
        if n % 2 != 0:
            n = 3 * n + 1
        else:
            n = n / 2
        c += 1
    c += 1                      # for the last number
    # print(n)                  # should always be 1
    return c

fin = None 

# open the input file
try:
    fin = open('data')
except IOError as e:
    print('file error:', e)
    exit(ERR)

# read the input
for line in fin:
    try:
        i, j = line.split()
        i = int(i)
        j = int(j)
    except ValueError as e:
        print('input error:', e)
        exit(ERR)

    # find the maximum cycle length
    x = range(i, j)
    max_cl = 0
    for y in x:
        cl = cycle_length(y)
        if cl > max_cl:
            max_cl = cl

    # print the result
    print(i, j, max_cl)
