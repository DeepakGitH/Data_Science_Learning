
#Basic Memory and Stuff
1. Processor can access any point in the memory - that is why random access
2. When processor asks for a memory few adjacent memories are also returned. THis is put into the cache
3.
Fractions: Store two numbers: the numerator and the denominator.
Decimals: Also two numbers: 1) the number with the decimal point taken out, and 2) the position where the decimal point goes (how many digits over from the leftmost digit).
Negative Numbers: Reserve the leftmost bit for expressing the sign of the number. 0 for positive and 1 for negative.

4. Python automatically assigns extra memories for integers
5. Accessing arrays are O(1)
6. Strings are character arrays
7. Pointers and creating the arrays of pointers to store an array of strings
8. Dynamic arrays are like Python List
9. Worst case update is O(n) for dynamic list
10. Linked list and Hash tables


Chapter 1 #Introduction
1. Tuples are immutable (value can not be changed once initialized) while lists are not
2. Set is a collection of immutables so set of lists is not possible
3. Python’s built-in sequence types (str, tuple, and list) 
4. Bitwise Operators

Chapter 2 #Class and Object Oriented
1. Operator Overloading can be done using __len__ or __add__
2. Inheritance can be expressed in the following way - super(PredatoryCreditCard, self).__init__(customer, bank, acnt, limit)
3. The namespace > Instance Namespace > Class Namespace > Superclass Namespace > ... (AttributeError)
   This has an effect of overriding

Chapter 3 # Computational Complexity of Algorithms
1. The function 8n+5 is O(n). Justification: By the big-Oh definition, we need to find a real constant c > 0 and
an integer constant n0 ≥ 1 such that 8n+5 ≤ cn for every integer n ≥ n0. It is easy
to see that a possible choice is c = 9 and n0 = 5. Indeed, this is one of infinitely
many choices available because there is a trade-off between c and n0. For example,
we could rely on constants c = 13 and n0 = 1.

2. Example 3.8: 5n4 +3n3 +2n2 +4n+1 is O(n4). Justification: Note that 5n4 +3n3 +2n2 +4n+1 ≤ (5+3+2+4+1)n4 = cn4,
for c = 15, when n ≥ n0 = 1.
