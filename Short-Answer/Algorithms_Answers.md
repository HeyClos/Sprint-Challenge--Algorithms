#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)



b) O(n Log n)


c) O(n)

## Exercise II

# dont make this OVER COMPLICATED, YOU'RE JUST SEARCHING FOR A FOR LOOP?
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


use binary search
grab lengh of building size
divide length/2

at middle index, check if egg breaks

if egg breaks go delete higher floors
    set floor under current floor to new max

if egg doesnt break delete lower floors
    ser floor over current to new min


