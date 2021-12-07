CREATE SCHEMA [web]
GO

CREATE USER PythonWebApp FOR LOGIN PythonWebApp;  
GO 

EXEC sp_addrolemember 'SqlPool', 'PythonWebApp';  
Go

CREATE TABLE [web].[Claim]
(
	[name] [varchar](30) NULL,
	[ID] [varchar](30) NULL,
	[ChangeType] [varchar](30) NULL,
	[PublicID] [varchar](30) NULL
)
WITH
(
	DISTRIBUTION = HASH ( [name] ),
	CLUSTERED COLUMNSTORE INDEX
)
GO

INSERT INTO [web].[Claim]
           ([name]
           ,[ID]
           ,[ChangeType]
           ,[PublicID])
     VALUES
           ('1',
           'Claim1',
           'Insert',
           'ID1')


INSERT INTO [web].[Claim]
           ([name]
           ,[ID]
           ,[ChangeType]
           ,[PublicID])
     VALUES
           ('2',
           'Claim2',
           'Insert',
           'ID2')