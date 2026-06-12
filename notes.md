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

---------------------------------------------------------------------------------------------

## valid_palindrome
- use isalnum() to check if a character is an alphanumeric character or not 
- use two pointers to travers from left and right 

## two_sum_II 
- use two pointers starting from the start and end
- since its sorted find the sum of each pair
- if it exceeds then we have to reduce the value hence decrement right and if it is short of target we have to increase value and thus increment left 

## three sum
- fix one element at a time and find the other two by finding sum=0
- skip the duplicates for the fixed element by checking if the current number is equal to its previous one
- similiary when u find a triplet skip the duplicates for the left and right pointers as well 

## container with most water
- take two pointers and find area by multiplying the width with the min of the left right height
- traverse continuously and find max area calculating area for each round but stoeing it only if it is the max area
- for traversal if right is taller than left then move left inward and vice versa

## trapping rain water
- water at any index is the min of the max boundaries (left and right) subtracted by the height at that index
- for traversal if height at left is leass than at right then we process left
- process meaning we again find see if the left max has changed or not for each increase in left we do in the previous iterationns andalways calculate area based on the max left value 

---------------------------------------------------------------------------------------------

## Sliding Window
- whenever you see atmost k changes or replacements think sliding window  

## best time to buy and sell stock
- while traversng the prices, always find the samllest price and store it 
- profit= price - min price 
- maintain a max for profit as well by calculating in each iteration 

## length of longest substring without duplicate
- use a window 
- take a variable that traverses towards the right till you  dont encounter a duplicate
- every new element you see you add it in your window and find the length of the substring found till now 
- always store max length 
- if duplicate is found you start moving your left pointer and remove elements from window until the starting duplicate is not removed  

## longest repeating character duplicate 
- need maximum valid window
- replacement needed is window_size- most frequent character which sould always be less than and equal to k 
- expand by moving right till condition is sattisifed 
- if invalid start moving 9inwards with your left pointer and note you max window size always 

## Permuatation In String
- remember that window size is always len(s1) as permutations will have length preserved
- build and check fr the first window 
- after that for each move build right and check counter 
- remove left if doesnt match and keep moving forward

## Minimum Window Subsring
- we need frequency requirement to be satisfied not the exact string match 
- take variable need which is the number of unique elements and variable have which strores number of  currently satisfied requirements 
- valid window is when have== need and keep moving left to reduce the size as we need minimum window
- if it becomes invalid again after shrinking keep moving right until valid again and track minimum track always 
- for every character you check of s keep checking the counter you are making with the counter of gthe substring t for ensuring all the characters are included in the window 

--------------------------------------------------------------------------------------

## Binary Search
- standard find mid using low+high//2 
- move left if target is less than mid and right otherwise

## Search 2D matrix
- optimally combine and consider it as one whole array and apply binary search
- otherwise find mid of matrix and check if value is between the first and last element of that mid
- if it is use binary search in that array
- otherwise move left if target is less than first element of mid and update or move right similiarly

## Koko eating banana
- we are searching min speed k so we apply binary search on the range of values of k 
- range starts from 1 with 1 being the min speed and max is the max value in piles 
- number of hours is the cieling value of number of bananas in pile divided by k 
- ciel can also be written as (piles[i]+k-1)//k instead of math.ciel(piles[i]/k)
- if hours is less than h then we can move slower and vice versa 

## Find min in Rotated Sorted array
- we again take high and low variables as the first and last element 
- store a minimum variable that calculates the min for each binary operation between the current mid and the old minimum 
- check if your middle element is less than or greater than the last element
- if it is less means smaller element can be in the left side not in the right 
- if it is greater that means element is in the right side it could also be the middle element so thats why we store min element
- another way is to not calculate minimum but return low by using slightly different conditions accordingly


## Search in rotated sorted array
- main method is to find the part that is sorted 
- if the left is smaller than the mid element it means that the left side of the mid is sorted 
- if the target lies between the left and mid then perform binary search there otherwise move left to mid+1
- similiarly if right is greater than mid then the right side of mid is sorted and target lies between right and mid , perform binary search there
- otherwise move right to mid-1

## Time Based Key Value Store
- timestamps are inserted in increasing order so each timestamp is already sorted 
- in set simply append, if key is not there add it and then simply append value and timestamp
- for get() , the largest timestamp<=  given timestamp
- we find the last value which is smaller or equal to the target
- if timestamp at mid is smaller than the target we store the value and move left to find a timestamp greater than this that might satisfy the condition

## Median of two sorted arrays
- goal is to find the correct partition that is all left side elements <= right side elements
- mark the two arrays num1 and num2 as A and B where A represnts the smaller one out of the two
- partition is valid when Aleft<= Bright and Aright>= Bleft 
- if Aleft> Bright then partition is too left and we have to shift right to i-1 and if Bleft> Aright then move right 
- if total len is odd the median is min(Aright, Bright) and if its even it is max(Aleft, Bleft)+ min(Aright,Bright)/2.0