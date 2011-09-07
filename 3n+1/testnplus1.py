#    testnplus1.py Unit testing for the 3n+1 problem
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

import unittest
import nplus1

class CycleLenBadInput(unittest.TestCase):
    def test_negative(self):
        '''cycle_length should fail with negative/zero input'''
        self.assertRaises(nplus1.InvalidInputError, nplus1.cycle_length, 0)

class KnownCycleLengths(unittest.TestCase):
    known_lengths = ( (1, 1),
                      (2, 2),
                      (4, 3),
                      (22, 16),
                      (50, 25))

    def test_known_lengths(self):
        '''cycle_length should give the expected result with known input'''
        for num, cyc_len in self.known_lengths:
            result = nplus1.cycle_length(num)
            self.assertEqual(result, cyc_len)

if __name__ == '__main__':
    unittest.main()
