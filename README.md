# QTExcelMaker

Takes relevant information from the "Trading Slips", provided by Questrade, 
and creates Excel spreadsheets.

Provide the script with a directory (via `--directory={PATH}`) and it will 
search for all CSVs in `PATH` and create spreadsheets for each. Useful for
when you want to add selected data to a master spreadsheet that contains
all your trades.

**Output spreadsheets in the same directory as the script**\
`python populater`

**Specify directory:**\
`python populater --directory=PATH`