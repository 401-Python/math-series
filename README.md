## Lab 01: Fibbonacci Lucas Testing Modules

### Author: Alvian Joseph

### Links and Resources
* [PR]()
* [![Build Status](https://www.travis-ci.com/alvian-401-advanced-javascript/lab-13-bearer-auth.svg?branch=master)](https://www.travis-ci.com/alvian-401-advanced-javascript/lab-13-bearer-auth)
* [front end]()

### Tasks
Create a module series.py.
Add a file test_series.py to your repository. As you work on the tasks below, use TDD practices. Write tests first, then implement code. Make small changes with many cycles of Red-Green-Refactor
This is not an overly long assignment, so take the time to do the testing right.

Create a function called fibonacci. The function should have one parameter n. The function should return the nth value in the fibonacci series. You may implement the function using recursion or iteration. If you are feeling particularly frisky, do both as separate functions.

Ensure that your function(s) has a well-formed docstring

In your series.py module, add a new function lucas that returns the nth value in the lucas numbers Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring.

Both the fibonacci series and the lucas numbers are based on an identical formula. Add a third function called sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series. Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring.

### Modules
#### series.py
  This module defines 4 methods: ```validate_input```, ```fibbonacci```, ```lucas()```, and ```sum_series()```
  #### methods
  * ```validate_input()```
    This is a helper function to ensure each function receives a valid input. It returns False if the input doesn't meet the specified conditions, and True if it does.

  * ```fibbonacci()```
    This function takes in 3 parameters:
      ```n``` which corresponds to the nth number in the series
      ```tortoise``` and ```hare``` which correspond to the starting pair of numbers for the series. By default these 2 values are equal to 0 and 1 respectively, the starting numbers for a fibbonacci sequence.
      Using a for loop I iterate from 2 (because the first 2 numbers are established) to n  
      
      At each iteration there are 4 actions:  
        First, I store the sum of tortoise and hare in a new variable, ```fib```   
        Second, I print the value of ```fib``` 
        Third, I reassign the variable ```tortoise``` to the value of ```hare``` which moves it up in the sequence  
        Fourth, ```hare``` is reassigned to the value of ```fib``` which moves it up in the sequence  
        Finally, I return ```fib``` (I could also return hare at this point but fib made more sense in my head)  


  * ```lucas()```
    This method simply returns the ```fibbonacci()``` function but passes in the value of tortoise as 2


  * ```sum_series()```
    This function will return either a Fibbonacci sequence or Lucas sequence depending on if the tortoise parameter is passed in, by default it will return fibbonacci

### Testing
  pytest
  ptw
  

