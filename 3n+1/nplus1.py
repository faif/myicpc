#    nplus1.py Solution of the 3n+1 ICPC problem
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

ERR = 1

class InvalidInputError(ValueError):
    '''raised when non-acceptable input is given'''

def cycle_length(n):
    '''calculate the cycle length of n'''
    if n <= 0:
        raise InvalidInputError('error: input must be positive')
    c = 0
    while n != 1:
        if n % 2 != 0:
            n = 3 * n + 1
        else:
            n = n / 2
        c += 1
    c += 1                      # for the last number
    assert(1 == n)              # should always be 1
    return c

if __name__ == '__main__':
    with open('data') as fin:
        for line in fin:
            try:
                i, j = line.split()
                i = int(i)
                j = int(j)
            except ValueError as e:
                print('input error: {}'.format(e))
                exit(ERR)

            # find the maximum cycle length
            x = list(range(i, j))
            max_cl = 0
            for y in x:
                cl = cycle_length(y)
                max_cl = max(cl, max_cl)

        print('{} {} {}'.format(i, j, max_cl))
