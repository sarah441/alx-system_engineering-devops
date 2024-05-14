#!/usr/bin/env ruby
# match phone number but has to only it no other chars or words
puts ARGV[0].scan(/^\d{10}$/).join
