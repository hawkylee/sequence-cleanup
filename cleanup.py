import sys
import os

""" Definition to split the string by determined length """
def splt(string, length):
  return ' '.join(string[i:i+length] for i in range(0,len(string), length))

""" Open a file in the same folder... """
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'dna.txt'))


content = f.read()
f.close()

""" Remove all digits, Email traces, New lines, and spaces """
c = ''.join(i for i in content if not i.isdigit())
n1 = c.replace('> ', '')
n2 = n1.replace('\n', '')
n3 = n2.replace(' ', '')

""" Use split defintion """
n4 = splt(n3, 3)

f = open('output.txt', 'w')
f.write(new_contents4)
f.close()
