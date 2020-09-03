# Scalability is the ability of the system to distribute its work parallely and being able to perform it concurrently to
# reduce latency and increase the throughput of the system.

# SCALABILITY AND PERFORMANCE

"""

1. When performance of one of the components in a system goes up, generally the performance of the overall
   system goes up.

2. When an application scales in a single machine by increasing its concurrency, it has the potential to improve
   performance, and hence, the net scalability of the system in deployment.

3. When a system reduces its performance time, or its latency, at the server, it positively contributes to scalability.

---------------------------------------------------------------------
Concurrency         Latency         Performance         Scalability
---------------------------------------------------------------------
 High                 Low               High                High
 High                 High              Variable            Variable
 Low                  High              Poor                Poor

Ideal - High Concurrency and low latency

"""

# CONCURRENCY

"""

* The degree to which system can perform tasks simultaneously instead of sequentially.

* A concurrent application can execute more per unit work in a given time than a sequential of serial application.

* Concurrency can be achieved by different techniques:

1. Multithreading: 
   The simplest form of concurrency is to rewrite the application to perform parallel tasks in 
   different threads. A thread is the simplest sequence of programming instructions that can be performed by a
   CPU. A program can consist of any number of threads. By distributing tasks to multiple threads, a program can 
   execute more work simultaneously. All threads run inside the same process.

2. Multiprocessing: 
   Another way to concurrently scale up a program is to run it in multiple processes instead of a 
   single process. Multiprocessing involves more overhead than multithreading in terms of message passing and shared 
   memory. However, programs that perform a lot of CPU-intensive computations can benefit more from multiple processes 
   than multiple threads.

3. Asynchronous Processing: 
   In this technique, operations are performed asynchronously with no specific ordering of 
   tasks with respect to time. Asynchronous processing usually picks tasks from a queue of tasks, and schedules them 
   to execute at a future time, often receiving the results in callback functions or special future objects. 
   Asynchronous processing usually happens in a single thread.

Built in python modules for concurrency

* Asyncio - Asynchronous processing.
* threading - multi-threading.
* multiprocessing - multi-processing.

"""

# CONCURRENCY VS PARALLELISM

"""

* Concurrency - execution starts together, but doesnot mean, things will end together. - single core CPU with multi-
  threads.
  
* Parallelism - start and end of a task together - multicore CPUs with multiple threads.


--------------------------------------------
Resource Constraint - Semaphore versus lock
--------------------------------------------

1. The version using Lock protects all the code that modifies the resource—in this case, checking the counter, saving 
   the thumbnail, and incrementing the counter—to make sure that there are no data inconsistencies.

2. The Semaphore version is implemented more like a gate—a door that is open while the count is below the limit, and 
   through which any number of threads can pass, and that only closes when the limit is reached. In other words, it 
   doesn't mutually exclude threads from calling the thumbnail saving function.
   
Conclusion - in resource constraint problems try to use semaphore instead of the lock, its faster.

----------------------------------------------------------
Resource Constraint - use of conditions(Condition objects)
----------------------------------------------------------

In the producer/consumer systems in real life, the following three kinds of scenario
can occur with respect to the rate of data production and consumption:

1. Producers produce data at a faster pace than consumers can consume. This causes the consumers to always play catch 
up with the producers. Excess data by the producers can accumulate in the queue, which causes the queue to consume a 
higher memory and CPU usage in every loop causing the program to slow down.

2. Consumers consume data at a faster rate than producers. This causes the consumers to always wait on the queue—for 
data. This, in itself, is not a problem as long as the producers don't lag too much. In the worst case, this leads to 
half of the system, that is, the consumers, remaining idle, while the other half—the producers—try to keep up with 
the demand.

3. Both producers and consumers work at nearly the same pace keeping the queue size within limits. 
This is the ideal scenario.

Ways to solve the problem :

1. Queue with a fixed size: 
   Producers would be forced to wait till data is consumed by a consumer once the queue size limit is reached. 
   However this would almost always keeps the queue full.

2. Provide the workers with timeouts plus other responsibilities: 
   Rather than remain blocked on the queue, producers 
   and/or consumers can use a timeout to wait on the queue. When they time out they can either sleep or perform some 
   other responsibilities before coming back and waiting on the queue.

3. Dynamically configure the number of workers: 
   This is an approach where the worker pool size automatically increases or decreases upon demand. If one class of 
   workers is ahead, the system will launch just the required number of workers of the opposite class to keep 
   the balance.

4. Adjust the data generation rate: 
   In this approach, we statically or dynamically adjust the data generation rate by the producers. For example, the 
   system can be configured to produce data at a fixed rate, say, 50 URLs in a minute or it can calculate the rate of 
   consumption by the consumers, and adjust the data production rate of the producers dynamically to keep things
   in balance.

"""


# MULTI-PROCESSING VERSUS MULTI-THREADING


