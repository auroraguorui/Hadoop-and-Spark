Implementing MapReduce algorithms for a variety of common data processing tasks, including:

0. Warm up: word count. See 0_Word_count.

1. Create an Inverted index. See 1_Inverted_index.
   - Given a set of documents, an inverted index is a dictionary where each word is associated with a list of the document identifiers in which that word appears.
   
2. Implement a relational join as a MapReduce query. See 2_Join.
  - Consider the following query:
  - SELECT * FROM Orders, LineItem WHERE Order.order_id = LineItem.order_id
  - The MapReduce query should produce the same result as this SQL query executed against an appropriate database.
  
3. Number of friends. See Friend_count.
  - Consider a simple social network dataset consisting of a set of key-value pairs (person, friend) representing a friend relationship between two people. Describe a MapReduce algorithm to count the number of friends for each person.
  
4. Symmetric friend relationships. See 4_Asymmetric_friendships.
  - The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. Implement a MapReduce algorithm to check whether this property holds. Generate a list of all non-symmetric friend relationships.

5. DNA sequence. See 5_Unique_trims
  - Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA.... Write a MapReduce query to remove the last 10 characters from each string of nucleotides, then remove any duplicates generated.

6. Matrix multiplication. See 6_Multipy
  - Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value. Design a MapReduce algorithm to compute the matrix multiplication A x B

The full description of assignments 1-6 can be found [here](http://htmlpreview.github.io/?https://github.com/auroraguorui/Hadoop-and-Spark/blob/master/Hadoop-MapReduce/Problem.html)

7. Some other interesting designs can be found in folder Design