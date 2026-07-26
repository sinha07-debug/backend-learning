# Module 03 — SQL Fundamentals

## Objective

The goal of this module is to understand relational databases and SQL from a backend engineering perspective.

Instead of memorizing SQL syntax, the focus is on understanding:

- Why databases exist
- How data is modeled
- How relationships are designed
- How SQL retrieves and modifies data
- How a backend communicates with a relational database

By the end of this module, I should be able to design a relational schema, populate it with sample data, and write SQL queries confidently.

---

## Learning Outcomes

By the end of this module, I should understand:

- Why Databases Exist
- Relational Databases
- Tables
- Rows & Columns
- Primary Keys
- Foreign Keys
- Constraints
- Data Types
- Relationships
- Normalization
- CRUD Operations
- Filtering
- Sorting
- Aggregation
- Joins
- Transactions
- Indexes
- ACID Properties

---

## Technologies

- PostgreSQL
- pgAdmin / psql
- SQL

---

## Project

Design and implement a relational database for a **Video Game Store**.

The database will contain relationships between:

- Games
- Developers
- Customers
- Purchases
- Reviews

The goal is to design the schema first and then query it using SQL.

---

## Project Structure

```
03_sql/

README.md
architecture.md

code/
│
├── schema.sql
├── sample_data.sql
└── queries.sql
```

---

## Skills Practiced

- Designing relational schemas
- Choosing primary keys
- Creating foreign key relationships
- Writing CRUD queries
- Writing JOIN queries
- Aggregating data
- Designing normalized tables
- Understanding transactions
- Using indexes

---

## Workflow

```
Understand Databases
        ↓
Identify Entities
        ↓
Draw Relationships
        ↓
Design Tables
        ↓
Create Schema
        ↓
Insert Sample Data
        ↓
Write Queries
        ↓
Test Queries
        ↓
Normalize
        ↓
Optimize
```

---

## Completion Criteria

This module is complete only if I can:

- Explain relational databases
- Design a schema from scratch
- Choose appropriate primary and foreign keys
- Write SQL queries without copying
- Explain every JOIN used
- Normalize simple databases
- Use PostgreSQL documentation confidently

---

## Key Takeaways

- A good schema is more valuable than clever SQL.
- Relationships are the foundation of relational databases.
- SQL is a language for communicating with relational databases.
- Every table should represent a single entity.
- Constraints protect data integrity.
- Indexes improve read performance but have trade-offs.