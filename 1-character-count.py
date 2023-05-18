'''
1. Character Count:
given a string count each letter in the string and then print the result.

Example 1:

character_count('banana')

Input: 'banana'
Output (in the console): 
the character b occurs 1 times
the character a occurs 3 times
the character n occurs 2 times

Example 2:

character_count('hello world')

Input: 'hello world'
Output (in the console): 
the character h occurs 1 times
the character e occurs 1 times
the character l occurs 3 times
the character o occurs 2 times
the character   occurs 1 times
the character w occurs 1 times
the character r occurs 1 times
the character d occurs 1 times
'''
def character_count(string):
  hash_table = {}
  for letter in string:
      if letter in hash_table:
        hash_table[letter] += 1
      else:
        hash_table[letter] = 1
  for key in hash_table:
    print(f"the character {key} occurs {hash_table[key]} times.")

character_count("elephant") 
    
    
