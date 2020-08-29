# PERFORMANCE

"""
* The degree to which the system is able to meet its throughput and/or latency requirement in terms of the number of
transactions per second or time taken for a single transaction.

* Bad software compensated with scaling hardware.

* Improving software(efficient) to scale performance on the same hardware.

* Ideally, The software written should go in hand with the hardware and should scale linearly.

* Traditionally SDLC - software development life cycle - development done and then performane testing.

* SPE - Software performance engineering - Performance testing go in hand with development and architecture development
as feedback mechanism.

"""

# PERFORMANCE TESTING AND MEASUREMENT TOOLS

"""

* Two types a) Performance testing and diagnostics
            b) Performance metrics gathering and instrumentation

* Performance testing and diagnostics :
    
    * Stress testing tools : Generate peak workloads in production. Simulate high stress or periodic burst of very high
                             traffic. called "load generators".
                             Examples - httpperf, ApacheBench, LoadRunner, Apache JMeter and Locust.
    
    * Monitoring tools : Generates time and memory per function, number of function calls made per request-response loop
    
    * Instrumentation tools : Trace metrics, time and memory required for each computing step, track events, exceptions
                              in the code, covering such details as the module/function/line number.
                              
    * Profiling tools : These tools generate statistics about the functions, their frequency of duration. Dynamic 
                        program analysis. Find the bottelnecks in the code. Optimization after profiling is highly 
                        advisable.

-----------------------------------
Performance Measurement Complexity
-----------------------------------

* The performance complexity of a routine or function is defined in terms of how they respond to changes in the input 
  size typically in terms of the time spent in executing the code.

* Big-O notation - Bachmann Landau notation or asymptotic notation.

* Order Complexity

    * O(1) - Constant time - Looking for a key in a constant look-up table such as a HashMap or dictionary in Python.
    
    * O(log (n)) - Logarithmic Searching for an item in a sorted array with a binary search. All operations on a heapq 
                   in Python.
                   
    * O(n) - Linear Searching an item in an array (list in Python) by traversing it.
    
    * O(n*k) - Linear Worst-case complexity of Radix sort.
    
    * O(n * log (n)) - n log-star n Worst-case complexity in a mergesort or heapsort algorithm.
    
    * O(n2) - Quadratic Simple sorting algorithms such as bubblesort, insertion sort, and selection sort. Worst-case
              complexity on some sorting algorithms such as quicksort, shellsort, and so on.
              
    * O(2^n) - Exponential Trying to break a password of size n using brute force, solving the travelling salesman 
              problem using dynamic programming.
              
    * O(n!) - Factorial Generating all partitions of a set.
    
    Ideally a programmer should try to solve the problem in first 5 complexities itself.
    

"""