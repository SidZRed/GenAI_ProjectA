# Automation process:
>Take input of function as a string containing the code generation. 
>Run this code using automated testing --> ``` exec() & compile() functions ```.
>Try any exceptions or errors that may have been caused during the testing.
>Form a method to iterate over the code samples and then check which all code strings compile and execute successfully.
>Extract the code samples which pass the execution and run those samples against a fixed set of Doctests using doctest module or Hypothesis module by running against standard tests.
>Use a module (name) to find the valid tests to run (forgot the name of module)
>Compare all the valid solutions from the above test against the Ground truth solution which is provided and check which are equivalent solutions and which are inequivalent solutions but still pass the necessary conditions.
>These are the solutions which have the potential to be good Refute problems.
>Calssify these into various equivalent classes as not all of them are independent inequivalent solutions.  
