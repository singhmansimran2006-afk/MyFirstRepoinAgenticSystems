1. Explain why databases are important in real-world AI systems. Mention examples of the types of data typically stored in databases and why structured storage is necessary.

Ans - Databases are important in real-world AI systems because they are used to store, organize and manage large datasets        efficiently.

Examples of types of data stored in databases:= Names, Age, Transactions like orders and payments, etc.

Structured storage is necessary because it ensured data reliability and easy querying using languages like SQL.

2. Describe the relational database mental model. Explain what tables, rows, and columns represent, and why each table should represent a single entity.

Ans - The relational database organizes the data into tables made with rows and columns.
      
      Tables - it represents entities such as users, products or orders.
      Rows - each row represents a single record.
      Columns - each column represnts a sspecific attribute.

Each table should represent a single entity to keep the database organized.

3. Explain the concept of a primary key. Describe why primary keys must be unique and non-null, and how they help identify records in a table.

Ans - Primary Key - it is a column that uniquely identifies each row in a table.

primary keys must be unique because no 2 rows can have the same value.
primary keys must be non-null because every record must have a value.

it helps identify records in a table because the records are unique and the database return only one record which helps to accurately manage data.

4. Explain what a database schema is. Describe what information a schema defines and why schemas are important for maintaining consistent data structure.

Ans - Database Schema defines the structure of the database.

The information that a schema defines are tables, columns, relationships between tables, primary keys, foreign keys, etc.

Schemas are important for maintaining consistent data structure as the data is organized in a structure like tables containing rows and columns and it ensures that data follows the same structure

5. Explain how relationships between tables work in relational databases. Describe the role of foreign keys and how tables such as users and orders can be connected.

Ans - Relationships between tables work in relational databases through foreign keys. 

Foreign key is a column that references the primary key of another table.

Take an example of Users table it has a primary key named USERID and then the we have an orders table which has a USERID column but the USERID column in Orders table is a foreign key and it connects users table to orders table.

This creates relationships between tables.