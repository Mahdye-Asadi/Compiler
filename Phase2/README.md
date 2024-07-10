# KNTU compiler project winter 1402
We have three files for each section: one for the lexer (lexer.py), one for the parser (parserr.py), and the third one (main.py) is for viewing the output. In this project, our purpose is to discuss the 'parserr.py' and 'main.py' files.

## Structure 
Parser.py: First, we write all the rules of the grammar with their conditions and precedence. An important part of that is the 'slice_to_production' function, which creates a list that contains all the productions.

Main.py: In this file, we provide a 'rule_numbers' dictionary that contains the rule numbers. When we write to our output file, we also add these rule numbers to our output.

## P.S
Please just run 'main.py' and the output will be created as 'output.txt' file.

Thanks for your time.
M.Asadi, N.Vatankhah
