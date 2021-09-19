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
and find all solves in this field with brute-force algorithm
* module "puzzle_generator" get height and width from console
and make field randomly