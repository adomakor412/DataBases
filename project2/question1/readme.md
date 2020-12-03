Create a database containing the following table:

```sql
CREATE TABLE DirectedEdges(source INT, target INT, PRIMARY KEY (source, target));
```

The table stores the directed edges of a graph with integer vertices as an adjacency list.  There is an edge between
the vertices `n` and `m` if and only if the table contains an entry `(n, m)`.  You may assume that there is no edge
from a vertex to itself.

## Part 1
Write a stored procedure which takes three input parameters `source`, `target`, `length` and an output parameter
`connected`.
The stored procedure should assign `true` to `connected` if there is a directed path from `source` to `target` of
length less than `length`, and false otherwise.

## Part 2
Write a view called `ReversedEdges` which contains the entry `(n, m)` if and only if the table `DirectedEdges` contains
an entry `(m, n)`.

## Part 3
Write a view called `UndirectedEdges` which contains the entry `(n, m)` if and only if the table `DirectedEdges`
contains the entry `(n, m)` or the entry `(m, n)`.

## Details
You *must* use the given table structure, you cannot change it by adding additional columns.  You *may* use
[temporary tables](https://dev.mysql.com/doc/refman/8.0/en/create-temporary-table.html) inside of your stored
procedure.

What you need to submit:
* A file containing your stored procedure and views.

You can test your solution by importing the data in `graph.csv` and ensuring that your stored procedure gives the
correct answer to the following examples:
* There is a directed path between `0` and `7` of length 4.
* There is not a directed path between `0` and `7` of length 3.
* There is a directed path between `3` and `12` of length 3.
* There is a directed path between `3` and `50` of length 2.

If you are using MySQL, the data in `graph.csv` can be imported into the table defined above with a command similar to:

```sql
LOAD DATA INFILE '/full/path/to/graph.csv'
INTO TABLE DirectedEdges
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```

