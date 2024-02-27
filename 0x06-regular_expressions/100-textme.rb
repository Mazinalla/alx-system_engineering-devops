#!/usr/bin/env ruby

def parse_log_entry(log_entry)
    sender = log_entry.match(/\[from:([^\]]+)\]/)&.captures&.first
    receiver = log_entry.match(/\[to:([^\]]+)\]/)&.captures&.first
    flags = log_entry.match(/\[flags:([^\]]+)\]/)&.captures&.first
  
    "#{sender},#{receiver},#{flags}"
  end
  
  if ARGV.length != 1
    puts "Usage: #{$PROGRAM_NAME} 'log_entry'"
    exit 1
  end
  
  log_entry = ARGV[0]
  result = parse_log_entry(log_entry)
  puts result
  