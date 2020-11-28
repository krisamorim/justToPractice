--INSERT
INSERT INTO [TableName] VALUES ([Value1 of the 1st column], [Value2 of the 2nd clumn])
e.g.: INSERT INTO costumers VALUES (1, 'Joao', 30, '(91) 9999-9999') 

--UPDATE
UPDATE [TableName] SET [colmunName]=[Value] WHERE [referenceData]=[value's reference Data] AND [AnotherreferenceData]=[value's another reference Data] 
e.g.: UPDATE costumers SET name='Jonas' WHERE idcode = 1 AND age = 30

--DELETE
DELTE FROM [TableName] WHERE [Atribute]=[value]
DELETE FROM costumers WHERE name='Joao'