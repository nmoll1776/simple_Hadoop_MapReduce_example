#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    #make lower case
    line = line.split()
	
    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    stopwords = set(['the', 'and', 'a', 'for', 'I', 'go', 'four', 'three', 'not', 'to', 'be', 'railing', 'or'])  

  for word in words:
      if word not in stopwords:
        print '%s\t%s' % (word, "1")
