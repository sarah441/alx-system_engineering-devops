#!/usr/bin/env ruby
# match hbtt tttttn
puts ARGV[0].scan(/hbt{2,5}n/).join
