# Extract Transform Load (ETL)
The ETL process is a generic three stage process responsible for bringing data from a source system and format into a destination system and format. Not all the steps need to be applied, and there are a million different ways each step can be implimented.

The steps individually are:

#### Extract
The extract step involves retrieving information from a remote system and possibly extracting pieces of information from the retrieved information.

For example we may download financial statements from a website and extract the totals of assets from the balance sheet.

#### Transform
In the transform step, we apply rules and runctions to our extracted date so that it is prepared to be loaded into our destination system.

An example might be convering the asset totals into a proper format so that it can be loaded as a floating point number rather than a string. In a classical example, we might remove the '$' and ',' characters from the extracted totals.

#### Load
I this step we transfer the extracted and transformed data into the final data store. It could be that memory is the final rontier, or we may want to store the data in a sql server or csv file instead for example.

## In This Directory
This directory holds a number of notebooks explaining how to perform ETL operations using popular python data science libraries including numpy and pandas.

## Key Observations
Depending on the technology being used, the ETL process may not be followed to the letter of the law. Steps may be mergered for example. The basic process order will be the same however.