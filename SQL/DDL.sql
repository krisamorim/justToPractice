--CREATE
CREATE DATABASE [DataBase_Name]

CREATE TABLE [TableName] (
  id INT NOT NULL,
  name VARCHAR(99),
  age INT,
  address VARCHAR(199)
  PRIMARY KEY (id)
)

--ALTER
--add column
ALTER TABLE [TableName] ADD [ColumnName] [DataType]
e.g.: ALTER TABLE constumers ADD address VARCHAR(180) 
--remove column
ALTER TABLE [TableName] DROP COLUMN [ColumnName]
--drop index
ALTER TABLE [TableName] DROP INDEX [IndexName]

--DROP
--delete table
DROP TABLE [TableName]
--delete database
DROP DATABASE [DataBaseName]

--RENAME
RENAME TABLE [TableName] to [NewTableName]

--TRUNCATE
--To remove table's data
TRUNCATE TABLE [TableName]