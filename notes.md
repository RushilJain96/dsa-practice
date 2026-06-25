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


---------------------------------------------------------------------------------------------
## Important Linked list Notes
- curr= curr.next changes where the pointer points and doesnt modify the list
- curr.next=something brings changes to the list 
- whenever you make a dummy listnode at the end return dummy.next as that is the point from where the head starts 

## Reverse Linked List
- we used a 3 pointer technique where we store a previous element as well while moving the curr pointer
- every iteration nxt points to curr.next and curr.next points to prev
- This way opposite linked list keeps getting formed and then prev becomes curr and curr becomes nxt

## Merge Two Sorted List
- we use a dummy node + tail pointer
- always connect the smaller value by comparing both the lists value and adding it to tail->next
- after each iteraion move the tail ahead and list1 or list2 based on whose value we are taking
- if some elements remain in any of the list add them at the end of the tail
- REMEMBER: tail.next= list1 doesnt copy the value but connects the entire node 

## Reorder List
- we use slow and fast pointers to find the middle 
- instead of reversing the whole list we just reverse the second part which is the part after the middle 
- split using second= slow.next and slow.next= None
- Then we alternate merge by adding one element alternatively by taking two temporary variables storing the next of both the split parts 

## Remove Nth Node From The End Of The List
- One way is to find the length of the list by first traversing the list and then finding length
- Then traversing to the position just before the node to remove and changing its next to next.next. This takes two passes
- We use dummy to handle cases of deletion of head node 
- Better Solution is use two pointers : Fast moves n steps ahead and then slow and fast move together
- when fast reaches the end slow points to the node just before the target and thus we can delete it  like above (slow starts from dummy and fast from head)

## Copy List With Random Pointer
- Use a hash map to make a copy of each already existing nodes this will store mapping
- for the first pass create all copied nodes
- in the second pass, connect pointers like set the next and random pointers of the copied nodes by getting it from the hash map
- hash map acts as a translator for original node to copied node 
- use get() to get value from hash map as in cases of none it doesnt give error but returns None 

## Add Two Numbers
- At every position we find the digit value of both the lists if list has not reached none otherwise assign it 0 and find the sum 
- total includes the two digits and the carry as well
- value(total%10) to be added and carry(total//10) are again calculated 
- each result is added onto the tail as a node and tail is moved forward
- we also check if any list is finished if they are not only then we move them forward 
- the while conditions continjes till the lists or carry are not finished

## Linked List Cycle
- It used Floyd's Tortoise and Hare algorithm
- take two pointers slow and fast and move them such that fast moves 2* speed of slow 
- if a cycle exists eventually slow and fast will meet otherwise while fast is not None we keep checking 

## Find The Duplicate Number
- It used Floyd's Cycle Detection on an array 
- Key insight is that we treat nums[i] as a next pointer like in a linked list so whenever there is a duplicate element it tells us that there is a cycle
- Also since the numbers are in range of the indexes it gives a hint that they can be treated as pointers
- First we find the meeting point by taking slow=nums[slow] and fast= nums[nums[fast]]
- Remember meeting point is not the duplicate it could be some point inside the cycle
- In phase-2 we reset slow=0 and fast=meeting point and then we traverse one step at a time 
- it is the mathematical property of Floyd's algo that distance from the start to cycle start point is same as the dist from the meeting point inside cycle to the start so eventually they will meet again at the cycle starting point 
- it takes constant space 

## LRU Cache
- Hash map gives O(1) lookup but doesnt tell us the least recently used item hence we use a doubly linked list as once we know a node we can insert or remove it in O(1) time (no traversal is required)
- Hash map stores the key to the node and doubly linked list tracks the usage order left being the least recently used and right the mru
- for deletion just store the next of the prev node as next and the prev of the next node as node.prev
- for get(key) function find the node using the hashmap remove the node, reinsert it at mru position and return value
- for put(key, value) if key exists remove the old node and insert updated node if capacity exceeds remove left.next because it has lru node

## Merge K Sorted Lists
- instead of merging one by one we merge the lists in pairs
- main condition is we keep merging till length of lists is greater than one and the inner loop runs in intervals of k
- in the inner loop for each inner i we assign i to l1 and if i+1 is in bunds we assign i+1 to l2 and then apply merging and sorting on both the lists through a different function
- that function works the same as the problem of merging two independent sorted lists
- the returned list is appended in a merged list which is copied to the original list given 

## Reverse Nodes In K Group
- Main problem pattrn is Finfthe Kth node , reverse the segment reconnect and repeat
- Important pointers we use include groupPrev that stores the Node before the current group which is being reversed
- Kth is a variable used to find the last node of the current group
- groupNext is the first node after the current node basically kth.next
- tmp is the old head of the group , after reversal old head= tail of the group , it is used to move the groupPrev= tmp
- Dummy head is needed as the head may change  after the first reversal 
- Always save thenext groups start before reversing and then reverse 
- Most importantly usually prev= None when we reverse a full list but here we assign prev= groupNext as after reversing we want the reversed groups tail to already point to groupNext 

----------------------------------------------------------------------------------------------------------------------

## TREE
- Whenever using recursion, dont forget to add the base case 
- Recusrsion function can return information upward and downward and update a global variable

## Invert Binary Tree
- For evert node , we swap the left and right child then recursively invert the left and right subtree
- invert(node)= swap(left, right) + invert(left) + invert(right)

## Maximum Depth Of Binary Tree
- Core idea is asking how deep is my left subtree and how deep is my right subtree
- current node depth is 1+max(left depth , right depth)
- we add 1 for the node itself
- parent only needs one info that is height of child subtree

## Diameter Of Binary Tree
- we consider height of leaf node to be 1 and if node is null we return 0
- diameter through any node is the sum of left and right height
- we add a helper height function that returns the height and a global variable that stores maximum diameter

## Balanced Binary Tree
- Every node must satisfy the condition abs(height(left)-height(right))<=1
- We use a helper function height that returns the height or -1 indicating that tree is unbalanced
- if left or right ==-1 then we return -1 meaning once imbalance is found propogate it upwards

## Same Tree
- Trees are same if:
- 1. Both are none
- 2. Values match
- 3. Left and right subtrees match
- Each recursive call returns true or false and the parent combines the answer

## Subtree Of Another Tree
- For every node in root we check with a helper function isSameTree(node, subRoot)
- if any comparison return true return true
- So pattern is current matches or search left or search right 
- return left or right as if any of left or right returns true means subtree exists

## Binary Tree Level Order Traversal
- We use a queue for bfs as it processes a tree level by level
- Add the root to the queue and process all the nodes currently in the queue
- add their children and repeat until queue is empty
- maintain a level size that stores the length of the current queue and we process only that many nodes

## Lowest Common Ancestor Of A Binary Search Tree
- at every node we check three conditions
1. if both the nodes(p and q) are smaller than the current node we move left
2. if both nodes are larger then node is in the right ssubtree hece move right 
3. if nodes p and q split that is one in left and one in right this means we are at the lca node and thus return node 

- general solution involves checking different conditions
1. if root is equal to p or q we return the root
2. then we recusrsively check the left and right 
3. if (both left and right) condition holds means root is at a split hence return root
- else if only one side finds something return left or right and pass it upwards 

## Binary Tree Right Side View
- we need the first node visible from the right side at every depth doesnt matter if its in the right or left subtree
- one way is to perform normal bfs(level order traversal) using queue 
- we store the level size for each level we traverse so whenever i is equal to the level size meaning we have reached the last element of that level we append it to the result list  

## Count Good Nodes In Binary Tree
- This is where we use dfs and the pattern of transporting info from ancestors to children
- a node is good if its value is greater or equal to the max value seen on that path 
- so current root needs informations from ancestors and not children
- we maintain a variable max_so_far that keeps track of the max value seen so far
- if value of node is greater or equal to max-so_far then we make good=1 else good=0
- max_so_far is updated in each iteration by finding max between current node val and previous max_so_far
- final answer returned is the good(of that current node) + left +right

## Validate Binary Search Tree
- we perform dfs with range constraints
- just checking if node.left< node< node.right is not sufficient we need to check if all nodes in left subtree are less than the root and similiar for right
- so every node must stay within a range defined by low< node.val< high
- when we dfs left then we update high to current node value and when we go right we updae low to current node val
- if node doesnt fall in the range we return false else true 

## Kth Smallest Element In BST
- Most important thing to remember here is that inorder traversal of a BST gives elements in a sorted way 
- so we perform inorder traversal( left, root, right) recusrsion on left and right and append the root val 
- then return the kth element from the list

## Construct Binary Tree From Preorder and Inorder
- There are two ways to solve this 
1. O(n^2) Method
    1. First element of preorder always gives the root
    2. We find the index of the root(using .index() which takes O(n) time) in the given inorder traversal since inorder is of the form (left | root | right)
    3. Then we recursively pass the new preorder and inorder lists by specifying the indexes range

2. O(n) Method
    1. Instead of using index() function, we maintain an inorder hash map to instantly get index of root node
    2. We also take maintain an index for the preorder list
    3. Add a helper function build() which takes in the left and right indexes (extremes) of both left and right subtree and then stores the root and finds the root index using the dictionary and recursively calls the left and right by passing the necessary indexes

## Binary Tree Maximum Path Sum
- Use DFS + the pattern of maintaining a global answer
- Path doesnt need to start at root or end at leaf 
- At every node 
 - Value returned upward is the best path usable by the parent which is the node.val+ max(left, right)
 - parent can only continue at one branch and not split
- value used for the answer is the path passing through the node which is left + node.val+ right 
- here it can use both the branches 
- Never include negative gain hence whenever you find left or right you choose the max value between what you got from the recursive one and zero 

## Serialize And Deserialize Binary Tree
- Use BFS + Reconstruction
- For Serialization:
    - Perform level order traversal and store the node values as string
    - if value is null store them as 'N' since without null markers many diiferent trees become identical hence we need structure information
    - use join() to return the whole as a string
- For Deserialization:
    - use split() to seperate the string 
    - use a queue - every node consumes next left child and next right child from serialized data
    - while queue exists starting from the second element since first is already stored as root 
        - if value is not 'N' then we add that value as the left of the node we popped from the queue and move forward
        - again if value is not 'N' we add the value to the right of the node we popped and the right to the queue and move forward
        - this continues till the queue is not empty 

----------------------------------------------------------------------------------------------------------------------------------

## HEAPS & PRIORITY QUEUE
- heeapq is imported to perform heap functions
- python by default stores a min heap to get a max heap use negative values 
- heapq.heapify(list)---> it is used to turn a list into a heap O(n)
- heapq.heappop(list)---> used to pop the smallest element in the heap + reorganize the heap after removing O(log n)
- heapq.heappush(list, val)----> used to add the val in the heap + reorganise it as well O(log n)
- using heap of tuples [(1, 'a'), (2, 'b')] sorts by the first element 

## Kth Largest Element In A Stream
- we dont need all elements seen so far , we only need the largest k elements 
- The smallest element among these k elements is the kth largest overall
- Maintain a min heap of size k , root of the heap always stores the kth element 
- push the val in the heap, if size increases than k then heappop and return heap[0]

## Last Stone Weight
- We need to rapidly check the largest andthe smallest stone so we maintain a max heap
- Simulate a max heap by storing negative values hence the largest stone now appears at the root
- While heap size is >1 we pop the largest and second largest element 
- If both are not equal we find the diff and push that in the heap

## K Closest Points To Origin
- Distance from origin is x^2 + y^2 and we dont need to calculate root as for comparison it works fine
- Again we care only about k closest points and not all points so we maintain a heap of size k 
- Heap stores (-distance, point) , we use a negative distance to simulate a max heap which stores the kth closest point at the root
- For every point, compute distance and push (-distance, point) Whenever heap size exceeds k , remove the farthest point
- Return all points remaining in heap

## Kth Largest Element In An Array
- We want the Kth Largest element hence we maintain a min heap of k size 
- Keeps only the largest k elements inside a min heap and the smallest element among them is the answer
- For each number push into heap if size exceeds, pop and then return heap[0]
