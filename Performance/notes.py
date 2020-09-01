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

# PROFILING

"""

------------------------
DETERMINISTIC PROFILING
------------------------

* All functions calls, returns, and the exception events are monitored, and precise timings are made for the intervals
  between these events. Also called statistical profiling.

* Python, being an interpreted language, already has a certain overhead in terms of metadata kept by the interpreter. 
  Most deterministic profiling tools makes use of this information and hence only add very little extra processing 
  overhead for most applications. Hence deterministic profiling in Python is not a very expensive operation.


---------
cProfiler
---------

* Built-in profiler.(check official documentation for details)

* Generates a report in the following manner : 

    * ncalls : The number of calls per funciton.
    
    * tottime : The time spent in the call.
    
    * cumtime : The cumulative time in this function plus any child function.
    
    * percall : Another percall column.
    
    * filename : lineno(function). The filename and line number of the function call.
    

---------------------
Third Party Profiler
---------------------

* LINE PROFILER is able to profile code line by line, a granular statistics in given out.

* Line profiler comes with a script called kernprof.py that makes it easy to profile code using line profiler. 
  One needs only to decorate the functions that need to be profiled with the @profile decorator when using kernprof.

* MEMORY PROFILER : 
    
    * profiles line by line, instead profiles memory consumption.
    
    * Used similarly, by decorating the function to be profiled with @profile.
    
Use both memory and time profilers in hand with each other to check for the memory and time complexity of the written
code block.

* Profile visualization tools : Objgraph, Pympler. 

"""

# PYTHON DATA STRUCTURES FOR PERFORMANCE

"""

* Lists are appropriate for object access via a known index. Dictionaries provide a near constant time look-up for 
  objects with known keys. Sets are useful to keep groups of items while dropping duplicates and finding their 
  difference, intersection, union, and so on in near linear time.

------
LIST
------    

* O(1) opertions : 
    * get(index)
    * append(item)

* O(n) opertions : 
    * search an item operation
    * insert an index

A list is ideal in the following cases:
    • If you need a mutable store to keep different types or classes of items(heterogeneous).
    • If your search of objects involves getting the item by a known index.
    • If you don't have a lot of lookups via searching the list (item in list).
    • If any of your elements are non-hashable. Dictionaries and sets require their entries to be hashable. So in 
      this case, you almost default to using a list.

-------------
DICTIONARIES
-------------

* O(1) : Setting, getting, Deleting items via key

* Dictionaries taken slightly more memory than lists for the same data.

* Useful cases : 
        
        * no insertion order 
        
        * no duplicate keys needed

-----
SETS
-----

* They are in between list and dictionaries.

* Sets are usually used in Python as intermediate data structures for processing other containers – for operations 
  such as dropping duplicates, finding common items across two containers, and so on.

* Keeping heterogeneous, unordered data from another collection while dropping duplicates.


------
TUPLES
------

* Immutables, same time complexity for index and search as the list.

* Memory overhead much less compared to the lists.(lists C implemenation uses pointer to store the values whereas tuples
are fixed sized and are directly referenced to in the tuple).

* Tuples can be used whenever there are use cases for reading, returning, or creating a container of data that is not 
  going to be changed but requires iteration.


-------------------
COLLECTION MODULES
-------------------

* Supplies high performance alternatives to the built-in default container types in Python, namely list, set, dict, 
  and tuple.


DEQUE :

* A deque or double ended queue is like a list but supports nearly constant (O(1)) time appends and pops from either 
  side as opposed to a list, which has an O(n) cost for pops and inserts at the left.

DEFAULTDICT :

* Default dicts are dict sub-classed that use type factories to provide default values to dictionary keys.

* A common problem one encounters in Python when looping over a list of items and trying to increment a dictionary 
  count is that there may not be any existing entry for the item.

ORDEREDDICT :

* OrderedDict is a sub-class of dict that remembers the order of the insertion of entries. It kind of behaves as a 
  dictionary and list hybrid. It behaves like a mapping type but also has list-like behavior in remembering the 
  insertion order plus supporting methods such as popitem to remove the last or first entry.

* Drop duplicated without losing the order.

* LRU - least recently used cache can be implemented using the ordereddict.

COUNTERS : 

* A counter is a subclass of a dictionary to keep a count of hashable objects. Elements are stored as dictionary 
  keys and their counts get stored as the values.

* A counter is a natural choice for keeping the frequency of items encountered when processing any container.


CHAINMAPS : 

* When you have a scenario where you keep updating keys from a source dictionary to a target dictionary over and over 
  again, a ChainMap class can work in your favor in terms of performance, especially if the number of updates is large.

* A ChainMap class keeps the previous mappings in its maps attribute. However, when you update a dictionary with 
  mappings from another dictionary, the original dictionary state is lost.

• A programmer can keep the GET and POST arguments of a web framework in separate dictionaries and keep the 
  configuration updated via a single ChainMap.

• Keeping multilayered configuration overrides in applications.

• Iterating over multiple dictionaries as a view when there are no overlapping
keys.


NAMEDTUPLES : 

* A namedtuple is much more memory-efficient when compared to a class which has the same fields. Hence a namedtuple 
  is very useful in the following scenarios:
    
    • A large amount of data needs to be loaded as read-only with keys and values from a store. Examples are loading 
      columns and values via a DB query or loading data from a large CSV file.
    
    • When a lot of instances of a class need to be created but not many write or set operations need to be done on 
      the attributes. Instead of creating class instances, namedtuple instances can be created to save on memory.

"""