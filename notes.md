# Pattern Notes

## Grouping by shared property → defaultdict with property as key
- Group Anagrams: sorted word or freq array as key

## Frequency problems → Counter
- most_common(k) gives top k directly
- bucket sort gives O(n) when k matters

## Prefix + Suffix → eliminate self from product
- Product Except Self: build prefix left to right, suffix right to left