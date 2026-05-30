# Pattern Notes

## Grouping by shared property → defaultdict with property as key
- Group Anagrams: sorted word or freq array as key

## Frequency problems → Counter
- most_common(k) gives top k directly
- bucket sort gives O(n) when k matters

## Prefix + Suffix → eliminate self from product
- Product Except Self: build prefix left to right, suffix right to left

## longest consecutive sequence 
- sorting and then finding wont give O(n) time complexity
- Better to find number from where we start meaning its previous number doesnt exist in the set and thuis calculate length from there 

## valid sudoku
- for dividing in blocks use //3 to find the exact  box number through the row and column number 
- check each row, column and block if num doesnt already exist  
- if it doesnt add in each and if it does return invalid

## encode_decode string
- for encoding multiple strings into one use their length
- new string should have (length of string + seperator + string)
- for decoding just traverse till u find the seperator read the number and read that many characters to find the string  