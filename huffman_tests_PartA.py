#Part A: Test cnt_freq, create_huff_tree, and create_code
import unittest
import filecmp
from huffman import *

class TestList(unittest.TestCase):
   def test_cnt_freq(self):
      freqlist	= cnt_freq("file1.txt")
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0] 
      self.assertListEqual(freqlist[97:104], anslist[97:104])

   def test_create_huff_tree(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      numchars = 32
      charforroot = "a"
      self.assertEqual(hufftree.freq, 32)
      self.assertEqual(hufftree.char, 97) 

      left = hufftree.left
      self.assertEqual(left.freq, 16)
      self.assertEqual(left.char, 97)
      right = hufftree.right
      self.assertEqual(right.freq, 16)
      self.assertEqual(right.char, 100)

   def test_create_code(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('d')], '1')
      self.assertEqual(codes[ord('a')], '0000')
      self.assertEqual(codes[ord('f')], '0001')

   
   
   def test_onechar_file(self):
      freqlist	= cnt_freq("onechar.txt")
      anslist = [0]*256
      anslist[97:98] = [3] 
      self.assertListEqual(freqlist[97:98], anslist[97:98])

   def test_create_code_onechar(self):
      freqlist = cnt_freq("onechar.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('a')], '')

   def test_empty_file(self):
      freqlist = cnt_freq("empty.txt")
      hufftree = create_huff_tree(freqlist)
      numchars = 0
      self.assertEqual(hufftree, None)

if __name__ == '__main__': 
   unittest.main()
