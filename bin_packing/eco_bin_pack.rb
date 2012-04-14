#    eco_bin_pack.rb Solution of the ecological bin packing ICPC problem
#    Copyright (C) 2012 Sakis Kasampalis <faif at dtek period gr> 

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

BLUE = 0
GREEN = 1
CLEAR = 2

def bgc(bin1, bin2, bin3)
  moved = 0

  # the order matters: greater indexes
  # must be removed before the smaller
  moved += bin1.delete_at(CLEAR)
  moved += bin1.delete_at(GREEN)

  moved += bin2.delete_at(CLEAR)
  moved += bin2.delete_at(BLUE)

  moved += bin3.delete_at(GREEN)
  moved += bin3.delete_at(BLUE)

  return moved
end

def gbc(bin1, bin2, bin3)
  moved = 0

  moved += bin1.delete_at(CLEAR)
  moved += bin1.delete_at(BLUE)

  moved += bin2.delete_at(CLEAR)
  moved += bin2.delete_at(GREEN)

  moved += bin3.delete_at(GREEN)
  moved += bin3.delete_at(BLUE)

  return moved
end

def cbg(bin1, bin2, bin3)
  moved = 0

  moved += bin1.delete_at(GREEN)
  moved += bin1.delete_at(BLUE)

  moved += bin2.delete_at(CLEAR)
  moved += bin2.delete_at(GREEN)
  
  moved += bin3.delete_at(CLEAR)
  moved += bin3.delete_at(BLUE)

  return moved
end

def cgb(bin1, bin2, bin3)
  moved = 0

  moved += bin1.delete_at(GREEN)
  moved += bin1.delete_at(BLUE)

  moved += bin2.delete_at(CLEAR)
  moved += bin2.delete_at(BLUE)

  moved += bin3.delete_at(CLEAR)
  moved += bin3.delete_at(GREEN)
  
  return moved
end

def gcb(bin1, bin2, bin3)
  moved = 0

  moved += bin1.delete_at(CLEAR)
  moved += bin1.delete_at(BLUE)
  
  moved += bin2.delete_at(GREEN)
  moved += bin2.delete_at(BLUE)

  moved += bin3.delete_at(CLEAR)
  moved += bin3.delete_at(GREEN)

  return moved
end

def bcg(bin1, bin2, bin3)
  moved = 0

  moved += bin1.delete_at(CLEAR)
  moved += bin1.delete_at(GREEN)
  
  moved += bin2.delete_at(GREEN)
  moved += bin2.delete_at(BLUE)

  moved += bin3.delete_at(CLEAR)
  moved += bin3.delete_at(BLUE)

  return moved
end

begin
  File.foreach('data') { |test_case|
    bottles = test_case.split
    bin1 = []
    bin2 = []
    bin3 = []
    # fill the bins with the bottles
    bottles[0..2].each do |s| 
      bin1.push(s.to_i)
    end
    bottles[3..5].each do |s| 
      bin2.push(s.to_i)
    end
    bottles[6..9].each do |s| 
      bin3.push(s.to_i)
    end
    # run all the combinations
    cases = {
      "BGC" => bgc(Array.new(bin1), 
                   Array.new(bin2), 
                   Array.new(bin3)),

      "GBC" => gbc(Array.new(bin1), 
                   Array.new(bin2), 
                   Array.new(bin3)),

      "CBG" => cbg(Array.new(bin1), 
                   Array.new(bin2), 
                   Array.new(bin3)),

      "CGB" => cgb(Array.new(bin1), 
                   Array.new(bin2), 
                   Array.new(bin3)),

      "GCB" => gcb(Array.new(bin1), 
                   Array.new(bin2), 
                   Array.new(bin3)),

      "BCG" => bcg(Array.new(bin1), 
                   Array.new(bin2), 
                   Array.new(bin3))
    }
    # find the best case and format
    # the output to be as expected
    cases = cases.sort { |l, r| l[1] <=> r[1] }
    # the best case is the first
    puts "#{cases[0][0]} #{cases[0][1]}"
  }
rescue StandardError => err
  puts "Error: #{err}"
end
