#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[23]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self,letter):
        ## Initialize this node in the Trie
        self.letter=letter
        self.children={}
        self.is_end_of_word=False
        
    
    def insert(self, char):
        ## Add a child node in this Trie
        curr_node=self.root
        if letter  in curr_node.children and letter not in char:
            curr_node=curr_node.children[letter]
            curr_node.is_end_of_word=True
        
        if  letter not in curr_node.children and letter in char:
            curr_node.children[letter]=TrieNode(letter)
            
        
    
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self,letter):
        ## Initialize this Trie (add a root node)
        self.root=TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        curr_node=self.root
        if letter  in curr_node.children and letter not in char:
            curr_node=curr_node.children[letter]
            curr_node.is_end_of_word=True
        
        if  letter not in curr_node.children and letter in char:
            curr_node.children[letter]=TrieNode(letter)

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if prefix=="":
            return True
        curr_node=self.root
        while  letter in prefix:
            if letter not in curr_node.children:
                curr_node=curr_node.children[letter]
            else:
                return False
                
            
        return curr_node.is_end_of_word


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[24]:


class TrieNode:
    def __init__(self,letter):
        ## Initialize this node in the Trie
        self.letter=letter
        self.children={}
        self.is_end_of_word=False
        
    
    def insert(self, char):
        ## Add a child node in this Trie
        curr_node=self.root
        if letter  in curr_node.children and letter not in char:
            curr_node=curr_node.children[letter]
            curr_node.is_end_of_word=True
        
        if  letter not in curr_node.children and letter in char:
            curr_node.children[letter]=TrieNode(letter)
        
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffix_list=[]
        curr_node=self.root
        
        if curr_node.is_end_of_word and suffix !='':
            suffix_list.append(suffix)
        
        if len(curr_node.children)==0:
            return suffix_list
        
        
        for char in curr_node.children:
            suffix_list.extend(curr_node.children[char].suffixes(suffix=suffix+char))
        
        
        return suffix_list
            
        


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[25]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[16]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:




