import unittest
import filecmp
from huffman import *

class TestList(unittest.TestCase):
   def test_01_encodefile(self):
      huffman_encode("file1.txt", "output1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("output1.txt", "output1_soln.txt"))
      huffman_encode("morechar.txt", "encoded_morechar.txt")
      self.assertTrue(filecmp.cmp("encoded_morechar.txt", "encoded_morechar_soln.txt"))
   
   def test_01_decodefile(self):
      freqlist = cnt_freq("file1.txt")
      huffman_decode(freqlist,"output1.txt", "decodefile1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodefile1.txt", "file1.txt"))

   def test_cnt_freq(self):
      freqlist  = cnt_freq("file1.txt")
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
   
   def test_preord(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      self.assertEqual(tree_preord(hufftree), "00001a1f1b1c1d")

   def test_onechar_file(self):
      freqlist  = cnt_freq("onechar.txt")
      anslist = [0]*256
      anslist[97:98] = [3]
      self.assertListEqual(freqlist[97:98], anslist[97:98])
      huffman_encode("onechar.txt", "encoded_onechar.txt")
      self.assertTrue(filecmp.cmp("encoded_onechar.txt", "encoded_onechar_soln.txt"))

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
      huffman_encode("empty.txt", "encoded_empty.txt")
      self.assertTrue(filecmp.cmp("encoded_empty.txt", "empty.txt")) 
if __name__ == '__main__': 
   unittest.main()
