
# TESTABILITY

"""
* The degree of ease with which a software system exposes its faults through execution-based testing.

* higher accessibility to the system's issues.

* Find and fix bug faster.

* Fixed output to a fixed input, less variability.

* Deterministic behavior is also important to assure the testability of a system.

                        -----------------------------------------
                        Determinism     Complexity  Testability
                        ----------------------------------------
                            High            Low          High
                            Low             High         Low

"""


# TESTABILITY ARCHITECTURAL ASPECTS

"""
* Functional testing : This involves testing software for verifying functionality.
    
    * White-box testing : Implemented by the developer(with visibility to the code). The units being tested here are 
                          functions, methods, classes or modules of the software. The basic form of white-box testing 
                          is Unit testing.
    
    * Black-box testing : Testing performed by someone outside the development team. Entire system is treated as a black
                          box.Black-box testing tests the end user functionality of the system without bothering about 
                          its internal details.(performed by QA engineers).
                          Now a days, black-box test on web applications can be automated by using testing framework 
                          like selenium.

* Performance Testing : measures responsiveness and robustness under high workloads.

    * Load Testing : test system under a specified load.
    
    * Stress Testing : Test robustness and response of the system when sudden or high rate of growth of inputs fed.
    
    * Stability Testing : Running the system for continuous period of time.
    
    * Scalability Testing : Measure how much the system can scale out or scale up when the load is increased.
    
* Security Testing : Test vulnerabilities to be exploited by outside person to penetrate the system and result in
                     malfunctioning. Authorization, data protection and access falls under this category.

* Usability Testing : How much intuitive the interface is to the user, this tests the front end design. It is done using
                      a set of people unknown about the product to operate and report the difficulties faced in the 
                      operations.
 
* Installation Testing : Tests and verifies that all the steps involved in building and/or installing the software at
                         the customer's end work as expected. This also involves testing the updates.
                         
* Accessibility Testing : Accessibility testing aims to assess the accessibility of software with respect to these 
                          standards, wherever applicable.

"""

# TESTABILITY - STRATEGIES

"""
-------------------------
REDUCE SYSTEM COMPLEXITY
-------------------------

* Reducing coupling : To isolate components so that coupling is reduced in the system. Inter-component dependencies 
                      should be well defined, and if possible, documented.

* Increasing cohesion : To increase cohesion of modules, that is, to make sure that a particular module or class 
                        performs only a well-defined set of functions.
                        
* Providing well-defined interfaces : Try to provide well-defined interfaces for getting/setting the state of the 
                                      components and classes involved.

* Reducing class complexity : To reduce the number of classes a class derives from. A metric called Response For Class 
                              (RFC) is a set of methods of a class C, plus the methods on other classes called by the 
                              methods of class C. It is suggested to keep the RFC of a class in manageable limits, 
                              usually not more than 50 for small- to mediumsized systems.

-------------------------                              
IMPROVING PREDICTABILITY 
-------------------------

* Correct exception handling : Missing or improperly-written exception handlers is one of the main reasons for bugs 
                               and thence, unpredictable behavior in software systems. It is important to find out 
                               places in the code where exceptions can occur, and then handle errors.

* Infinite loops and/or blocked wait : When writing loops that depend on specific conditions such as availability of an 
                                       external resource, or getting handle to or data from a shared resource, say a 
                                       shared mutex or queue, it is important to make sure that there are always safe 
                                       exit or break conditions provided in the code.

* Logic that is time dependent : When implementing logic that is dependent on certain times of the day (hours or specifi
                                 c weekdays), make sure that the code works in a predictable fashion. When testing such 
                                 code, one often needs to isolate such dependencies by using mocks or stubs.

* Concurrency : In writing the code that uses multi-threading/processes, make sure system logic is not dependent on
                threads or processes starting in a specific order. The system should be initialized in a clean manner.

* Memory Management : A very common reason for software errors and unpredictability is incorrect usage and mismanagement
                      of memory.


-----------------------------------------
CONTROL AND ISOLATE EXTERNAL DEPENDENCIES
-----------------------------------------

* A system might have dependencies on external sources like databases, weblinks etc. So these dependencies are needed to
be pruned and test the system in isolation. These dependencies can lead to increased complexity in the system.

* Isolating such external dependencies is very important in designing and writing repeatable tests.

* Data Sources : 
    
    * Using local files instead of a database.
    
    * Using an in-memory database: Rather than connecting to a real database, a small in-memory database could be used. 
      A good example is the SQLite DB, a file or memory-based database which implements a good, but minimal, 
      subset of SQL.
    
    * Using a test database: If the test really requires a database, the operation can use a test database which 
      uses transactions. The database is set up in the setUp() method of the test case, and rolled back in the 
      tearDown() method so that no real data remains at the end of the operation.
    
* Resource Virtualization : Build smal version of dependencies to mimic the behaviour.

    * Stubs : Stubs provide standard (canned) responses to function calls made during a test. A Stub() function replaces
      the details of the function it replaces, only returning the response as required.
    
    * Mocks : Mocks fake the API of the real-world objects they replace. One programs mock objects directly in the 
      test by setting expectations—in terms of the type and order of the arguments the functions will expect and the 
      responses they will return.

The main difference between Mocks and Stubs is that a Stub implements just enough behavior for the object under test to 
execute the test. A Mock usually goes beyond by also verifying that the object under test calls the Mock as expected.

"""

# WHITE-BOX TESTING PRINCIPLES

"""

-------------
UNIT TESTING
-------------

* Unit testing is the most fundamental type of testing performed by developers. A unit test applies the most basic 
unit of software code—typically, functions or class methods—by using executable assertions, which check the output 
of the unit being tested against an expected outcome.

* Python has built-in module called unittest.
    
    * Test Cases : The unittest module provides the TestCase class, which provides support for test cases. A new test 
      case class can be set up by inheriting from this class, and setting up the test methods. Each test method will 
      implement unit tests by checking the response against an expected outcome.
    
    * Test Fixtures : Test fixtures represent any setup or preparation required for one or more tests followed by 
      any cleanup actions.
    
    * Test suites : A test suite allows to group test cases that perform functionally similar tests on a software system
      , and whose results should be read or analyzed together. The unittest module provides support for test suites 
      through the TestSuite class.
    
    * Test runners: A test runner is an object that manages and runs the test cases, and provides the results to the 
      tester. A test runner can use a text interface or a GUI.
    
    * Test results: Test result classes manage the test result output shown to the tester. Test results summarize the 
      number of successful, failed, and erred-out test cases.
      

* Pytest and nose2 are thirdy party packages for testing. Checkout the their documentation for usage.

--------------
CODE COVERAGE
--------------

* The degree to which the source code under test is covered by a specific test suite. The test suite should aim for the 
higher code coverage, as this would expose a larger percentage of the source code to tests and helps tp uncover the bugs.

* Code coverage metrics are reported typically as a percentage of Lines of Code (LOC), or a percentage of the 
subroutines (functions) covered by a test suite.

* Code coverage can be tested using py.test, nose2 and coverage package, all can be installed as thirdy party packages
using pip.

-------------------
INTEGRATION TESTS
-------------------

* Each component may have defined its own unit test, it is also important to verify the combined functionality of the 
system by writing integration tests.

* Integration tests are usually written after unit testing is completed, and before
validation testing is done.

* Advantage of the integration tests
    
    * Testing components interoperability.
    
    * Testing for system requirement modifications.
    
    * Testing external dependencies and APIs. (Stubs are static, while mocks are determined at the run-time)
    
    * Debugging hardware issues : helpful in getting information on hardware problems, and debugging such tests gives
                                  the developer data about whether an update or change in the hardware configuration is
                                  required.
    
    * Uncovering exceptions in the code path : Higher code coverage with integrated components can open up the scope for
                                               identifying new bugs and exception cases which unit testing couldn't find
                                               out.
    
* Three approaches to write integration tests : 
    
    * Bottom-up : Low level unit testing done and then test results are used to integrate tests of the higher-level 
                  components in the chain. In this approach, critical modules at the top of the hierarchy may be tested
                  inadequately.
    
    * Top-down : Components at the top level of the hierarchy are tested first and the lower-level modules are 
                 tested last. In this approach, critical modules are tested on priority, so we can identify major 
                 design or development flaws first and fix them.
                 
                 Lower-level modules can be replaced by Stubs which mock their functionality. Early prototypes are 
                 possible in this approach, as lower-level module logic can be stubbed out.
    
    * Big-Bang : This is the approach is one where all the components are integrated and tested at the very end of 
                 development. Since the integration tests come at the end, this approach saves time for development. 
                 However, this may not give enough time to test critical modules, as there may not be enough time to 
                 spend equally on all the components.

* Testing automation can be achieved using selenium.[Read offical documentation for the details]

"""

# TEST-DRIVEN DEVELOPMENT

"""

* An agile practice of software development, which uses a very short development cycle, where code is written 
  to satisfy an incremental test case.

* In TDD, a functional requirement is mapped to a specific test case. Code is written to pass the first test case. 
  Any new requirement is added as a new test case. Code is refactored to support the new test case. The process 
  continues till the code is able to support the entire spectrum of user functionality.

* Steps : 

    1. Write first unit test case.
    2. Test the code.
    3. If passes done else refactor the code.
    4. Add a new test case.
    5. Repeat the steps 2 and 3.
    6. Repeat 4 and 5.

"""




