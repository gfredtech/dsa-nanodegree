# Problem 5

Using a trie, we are able to reduce computational complexity down to
a single traversal.
In this particular case, n is representative of the number of
words, and we'll have c represent the length of each word.
For time complexity of having to iterate our tree,
it will take however long it takes to iterate through each
character of each word, so we're looking here at a
Big O of O(n \* c). For space complexity,
we're creating a new node for each respective letter,
so in this case, where n represents number of letters,
we're looking at a Big O of O(n).
