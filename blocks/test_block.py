#    blocks.py Unit testing for the blocks ICPC problem
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

import blocks
import unittest

class MoveOverPiles(unittest.TestCase):
    piles = ( (0, 8, list([i] for i in range(10)),
               [[], [1], [2], [3], [4], [5], [6], [7], [0, 8], [9]]),
              (9, 7, [[0], [], [2], [], [4], [5], [6], [7], [8], [1, 3, 9]],
               [[0], [1], [2], [3], [4], [5], [6], [9, 7], [8], []]))

    def test_move_over_piles(self):
        '''move_over should give the expected result with known input'''
        for b1, b2, w, r in self.piles:
            blocks.move_over(b1, b2, w, b1, b2)
            self.assertEqual(w, r)

if __name__ == '__main__':
    unittest.main()
