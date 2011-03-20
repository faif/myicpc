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

from pprint import pprint

ERR = -1
NO_ERR = 0

# tests whether a command is illegal
# @param b1 the first block
# @param b2 the second block
# @param idx1 the index of the first block
# @param idx1 the index of the second block
# @param w the block world
# @returns True if the command is illegal; False 
# otherwise
def illegal(b1, b2, idx1, idx2, w):
    res = False

    # the blocks or the indices
    # are the same
    if b1 is b2 or idx1 is idx2:
        res = True
    # the blocks are in the same stack
    elif b1 in w[idx1] and b2 in w[idx1] or \
            b1 in w[idx2] and b2 in w[idx2]: \
            res = True

    # otherwise assume this is a legal command
    return res

# removes all the elements of a source container
# until reaching the (value of the) item passed as 
# an argument
# @param src the source container
# @param i the element which indicates termination
def remove_until(src, i):
    for x in src[:]:
        # terminate if requested
        if x is i:
            return
        try:
            src.remove(x)
        except Exception as e:
            print('error:', e)
            exit(ERR)
        

# removes all the elements of a source container
# and copies them to their initial positions;
# optionally terminates when it reaches an item which 
# contains the same value with the item passed as an
# argument (conditional item)
# @param src the source container
# @param con the conditional item
def move(w, src, con=None):
    # creating a copy with [:] is necessary...
    for x in src[:]:
        # terminate if requested
        if con is not None and x is con:
            return
        try:
            src.remove(x)
            # avoid duplicates
            if x not in w[x]:
                w[x].append(x)
        except Exception as e:
            print('error:', e)
            exit(ERR)


# searches for an item in a container
# @param i the item
# @param c the container
# @return the index of the item if found;
# -1 otherwise
def lookup(i, c):
    idx = 0
    for x in c:
        if i in x:
            return idx
        idx += 1
    return -1


# puts a block on top of another, after returning any blocks 
# that are stacked on top of both blocks to their initial
# positions
# @param b1 the base block
# @param b2 the stacked block
# @param w the world (current stacks)
# @param idx1 the index of the first block in the world
# @param idx2 the index of the second block in the world
def move_onto(b1, b2, w, idx1, idx2):

    # return any blocks that are stacked on top of 
    # b1 and b2 to their initial positions
    move(w, w[idx1], b1)
    move(w, w[idx2], b2)

    # remove b1 from the old stack
    if b1 in w[idx1]:
        w[idx1].remove(b1)

    # make the new stack look like a stack ([0] being the top)
    tmp = [b1]
    tmp.extend(w[idx2])
    w[idx2] = tmp


# puts a block on top of the stack which contains another block,
# after returning all the blocks that are stacked on top of the 
# moved block to their initial positions
# @param b1 the base block
# @param b2 the stacked block
# @param w the world (current stacks)
# @param idx1 the index of the first block in the world
# @param idx2 the index of the second block in the world
def move_over(b1, b2, w, idx1, idx2):

    # return any blocks that are stacked on top of 
    # b1 to their initial positions
    move(w, w[idx1], b1)

    # remove b1 from the old stack
    if b1 in w[idx1]:
        w[idx1].remove(b1)

    # make the new stack look like a stack ([0] being the top)
    tmp = [b1]
    tmp.extend(w[idx2])
    w[idx2] = tmp

# puts the pile of blocks consisting of a source block and any 
# blocks on top of it, onto a destination block; all blocks on
# top of the destination block are moved to their initial 
# positions
# @param b1 the base block
# @param b2 the stacked block
# @param w the world (current stacks)
# @param idx1 the index of the first block in the world
# @param idx2 the index of the second block in the world
def pile_onto(b1, b2, w, idx1, idx2):

    # return any blocks that are stacked on top of 
    # b2 to their initial positions
    move(w, w[idx2], b2)

    # save the pile of b1 and the blocks stacked on it
    try:
        idx = w[idx1].index(b1)
    except Exception as e:
        print('error', e)
        exit(ERR)

    pile = w[idx1][:idx+1]

    # cleanup the stack of b1
    remove_until(w[idx1], b1)
    # remove b1 manually since remove_until 
    # does not remove it
    del w[idx1][0]
    
    # put the pile of b1 on the stack of b2
    pile.extend(w[idx2])
    w[idx2] = pile


# @param b1 the base block
# @param b2 the stacked block
# @param w the world (current stacks)
# @param idx1 the index of the first block in the world
# @param idx2 the index of the second block in the world
def pile_over(b1, b2, w, idx1, idx2):
    # save the pile of b1 and the blocks stacked on it
    try:
        idx = w[idx1].index(b1)
    except Exception as e:
        print('error', e)
        exit(ERR)

    pile = w[idx1][:idx+1]

    # cleanup the stack of b1
    remove_until(w[idx1], b1)
    # remove b1 manually since remove_until 
    # does not remove it
    del w[idx1][0]
    
    # put the pile of b1 on the stack of b2
    pile.extend(w[idx2])
    w[idx2] = pile


# prints the block world in the standard output
# @param w a list of lists representing the world
def show_output(w):
    for i in range(len(w)):
        w[i].reverse()          # to print it as required
        print(i, ':', w[i], sep='')
        

# beginning of the main program

fin = None 

# open the input file
try:
    fin = open('data')
except IOError as e:
    print('file error:', e)
    exit(ERR)

n_blocks = None                 # number of blocks
c1 = c2 = None                  # commands
b1 = b2 = None                  # blocks
world = list()                  # the block world (list of lists) 

# read the input
for line in fin:
    try:
        # exit on quit
        if 'quit' in line:
            show_output(world)
            exit(NO_ERR)

        # initialisation
        if None is n_blocks:
            # initialise the blocks
            n_blocks = int(line)
            # initialise the world
            [world.append(list([i])) for i in range(n_blocks)]
            # world[5] = []
            # world[6] = []
            # world[7] = []
            # world[4] = []
            # world[2] = []
            # world[3] = []
            # world[0] = []
            # world[8] = [] 
            # world[1] = [5, 1, 7, 8]
            # world[9] = [4, 2, 9, 3]
            # print(world)
        # processing
        else:
            # parse a single line
            c1, b1, c2, b2 = line.split()
            b1 = int(b1)
            b2 = int(b2)
            assert(b1 >= 0 and b2 >= 0)

            # get the indices of the blocks
            # not necessary in this case since index = item
            # but takes care of index != item
            idx1 = lookup(b1, world)
            idx2 = lookup(b2, world)

            # ignore the illegal commands
            if illegal(b1, b2, idx1, idx2, world):
                continue

            # handle the move commands
            if 'move' in c1:
                if 'onto' in c2:
                    move_onto(b1, b2, world, idx1, idx2)
                elif 'over' in c2:
                    move_over(b1, b2, world, idx1, idx2)
            # handle the pile commands
            elif 'pile' in c1:
                if 'onto' in c2:
                    pile_onto(b1, b2, world, idx1, idx2)
                elif 'over' in c2:
                    pile_over(b1, b2, world, idx1, idx2)
            # print(world)

    except ValueError as e:
        print('input error:', e)
        exit(ERR)
