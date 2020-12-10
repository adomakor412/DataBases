Create a database containing the following table:

```sql
CREATE TABLE Comments(
    id INT PRIMARY KEY,
    parent INT,
    text VARCHAR(255),
    FOREIGN KEY (parent) REFERENCES Comments(id));
```

The table stores comments made on a social media website, where comments are limited in length to only 255 bytes.
The user id has been removed from the table to protect their identities.
If a comment has a non null `parent` field, then it is a response to the comment with the `id` of `parent`.

## Part 1
Write a query which gives all of the children of a parent.  It should have the schema `(parent_id, child_id)`.

## Part 2
Write a query which gives all of the comments which have no responses.

## Part 3
Design a table which will allow you to select all of the descendants of a comment, no matter haw many levels of
nesting.  You may wish to search for how to manage hierarchical data in SQL.  Give a query which will give all of the
children of a given comment `id` using your new table.

You may assume that you have all of the data "up front".  You do not need to worry about how new data will be inserted
over time.

## Details
For parts 1 and 2, you *must* use the given table structure, you cannot change it by adding additional columns.

What you need to submit:
* A file containing your queries and your new table.

For your convenience, the example data in `comments.csv` can be imported into the table defined above (using MySQL)
with a command similar to:

```sql
LOAD DATA INFILE '/full/path/to/comments.csv'
INTO TABLE Comments
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```

