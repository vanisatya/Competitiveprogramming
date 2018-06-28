import unittest
dictionary={}
class Trie(object):

  def add_word(self, word):
      global dictionary
      d = dictionary
      new = False
      for i in word:
          if i not in d:
              new = True
              d.update({i:{}})
             
          d= d[i]
          
      if "that's ending" not in d:
          new = True
          d.update({"that's ending":{}})

      return new