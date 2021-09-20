# Shikaku

Author: Aukhatov Roman (roma.aukhatov@yandex.ru)

## Description
This application is realization of puzzle "shikaku"

## Game rules

Playing field is rectangle m x n with numbers (1 <= number <= m x n).
You need break this field into rectangles:

* Each rectangle has exactly ONE number

* square of rectangle equal number

## Realization
* module "solution" take field from file "in.txt" 
and find all solutions in this field with brute-force algorithm
* module "puzzle_generator" get height and width from console
and make field randomly

## Run
only from directory .\solver:

"python solution.py" for find solution of field in "in.txt" 

or

"python puzzle_generator.py" for generate random field
and find its solutions 

## Conditions
 Field must be rectangular, exist in file "in.txt" and have a kind of type:
 
'- - - 4'

'4 - - -'

'- 2 2 -'