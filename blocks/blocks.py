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

ERR, NO_ERR = (1, 0)

def _illegal(b1, b2, idx1, idx2, w):
    '''Check whether a command is illegal using the blocks b1
    and b2, their indices idx1 and idx2 in w, and the world w'''
    res = False

    # the blocks or their indices
    # are the same
    if b1 == b2 or idx1 == idx2:
        res = True
    # the blocks are in the same stack
    elif b1 in w[idx1] and b2 in w[idx1] or \
            b1 in w[idx2] and b2 in w[idx2]: \
            res = True

    return res

def remove_until(src, i):
    '''Remove all the elements of src until reaching i (i
    is not removed)'''
    for x in src[:]:
        # terminate if requested
        if x == i:
            return
        try:
            src.remove(x)
        except ValueError as e:
            print('ERROR: remove_until: {}'.format(e))
            exit(ERR)

def _move(w, src, con=None):
    '''Move (append) all the elements from src to w;
    optionally terminate when reaching con'''
    for x in src[:]:
        # terminate if requested
        if con and x == con:
            return
        try:
            src.remove(x)
            # avoid duplicates
            if x not in w[x]:
                w[x].append(x)
        except ValueError as e:
            print('ERROR: move: {}'.format(e))
            exit(ERR)

def lookup(i, c):
    '''Search for i in c; if found return its index;
    each element of c must be iterable, for example
    c should be a list of lists'''
    idx = 0
    for x in c:
        if i in x:
            return idx
        idx += 1
    return -1

def _to_stack(t, idx, c):
    '''Reorder c[idx] to make it look like a stack
    (t being on top)'''
    tmp = [t]
    tmp.extend(c[idx])
    c[idx] = tmp

def _clean_old_stack(i, s):
    if i in s:
        s.remove(i)

def move_onto(b1, b2, w, idx1, idx2):
    '''Put b1 on top of b2, after returning any blocks 
    that are stacked on top of both blocks to their initial
    positions'''
    # return any blocks that are stacked on top of
    # b1 and b2 to their initial positions
    _move(w, w[idx1], b1)
    _move(w, w[idx2], b2)

    # remove b1 from the old stack
    _clean_old_stack(b1, w[idx1])

    # make the new stack look like a stack ([0] being the top)
    _to_stack(b1, idx2, w)

def move_over(b1, b2, w, idx1, idx2):
    '''Put b1 on top of b2, after returning all the blocks 
    that are stacked on top of b1 to their initial positions'''
    # return any blocks that are stacked on top of
    # b1 to their initial positions
    _move(w, w[idx1], b1)

    # remove b1 from the old stack
    _clean_old_stack(b1, w[idx1])

    # make the new stack look like a stack ([0] being the top)
    _to_stack(b1, idx2, w)

def _cleanup(w, b):
    remove_until(w, b)
    # remove the final element manually since
    # remove_until does not remove it
    del w[0]

def _extend_pile(p, c, idx):
    p.extend(c[idx])
    c[idx] = p

def pile_onto(b1, b2, w, idx1, idx2):
    '''Put the pile of blocks consisting of b1 and any blocks
    on top of it onto b2; all blocks on top of b2 are moved to
    their initial positions'''
    # return any blocks that are stacked on top of 
    # b2 to their initial positions
    _move(w, w[idx2], b2)

    # save the pile of b1 and the blocks stacked on it
    try:
        idx = w[idx1].index(b1)
    except ValueError as e:
        print('ERROR: pile_onto: {}'.format(e))
        exit(ERR)

    pile = w[idx1][:idx+1]

    # cleanup the stack of b1
    _cleanup(w[idx1], b1)

    # put the pile of b1 on the stack of b2
    _extend_pile(pile, w, idx2)

def pile_over(b1, b2, w, idx1, idx2):
    '''Put the pile of blocks consisting of b1 and any blocks 
    that are stacked on top of it onto b2; all blocks on top of
    b2 retain their original positions'''
    # save the pile of b1 and the blocks stacked on it
    try:
        idx = w[idx1].index(b1)
    except Exception as e:
        print('ERROR: pile_over: {}'.format(e))
        exit(ERR)

    pile = w[idx1][:idx+1]

    # cleanup the stack of b1
    _cleanup(w[idx1], b1)

    # put the pile of b1 on the stack of b2
    _extend_pile(pile, w, idx2)    

def show_output(w):
    for i in range(len(w)):
        w[i].reverse()          # to print it as required
        # convert the list into the required output
        str_w = str(w[i])
        str_w = str_w.replace(']', '').replace('[', '').replace(',', '')
        print('{}: {}'.format(i, str_w))

if __name__ == '__main__':
    n_blocks = None                 # number of blocks
    c1 = c2 = None                  # commands
    b1 = b2 = None                  # blocks
    world = list()                  # the block world (list of lists)

    with open('data') as fin:
        for line in fin:
            if 'quit' in line:
                show_output(world)
                exit(NO_ERR)
            # initialisation
            if not n_blocks:
                n_blocks = int(line)
                [world.append(list([i])) for i in range(n_blocks)]
            # processing
            else:
                c1, b1, c2, b2 = line.split()
                b1 = int(b1)
                b2 = int(b2)
                assert(b1 >= 0 and b2 >= 0)

                # get the indices of the blocks
                # not necessary in this case since index = item
                # but takes care of index != item
                idx1 = lookup(b1, world)
                idx2 = lookup(b2, world)

                if _illegal(b1, b2, idx1, idx2, world):
                    continue

                if 'move' in c1:
                    if 'onto' in c2:
                        move_onto(b1, b2, world, idx1, idx2)
                    elif 'over' in c2:
                        move_over(b1, b2, world, idx1, idx2)
                elif 'pile' in c1:
                    if 'onto' in c2:
                        pile_onto(b1, b2, world, idx1, idx2)
                    elif 'over' in c2:
                        pile_over(b1, b2, world, idx1, idx2)
