# MODIFIABILITY

"""
What is Modifiability ?

It is the degree of ease at which changes can be made to a system,and the flexibility with which the system adapts to
such changes.

Aspects of Modifiability

* Readability : The ease with which a program's logic can be followed and understood.

* Modularity : Software system is written in well encapsulated modules.

* Reusability : Code, tools, designs and others, that can be reused in other parts of the system with zero or very
little modification.

* Maintainability : The ease and efficiency with which the system can be updated and kept working in a useful state by its
intended stakeholders.

"""

# READABILITY

"""
* Well written : simple syntax, clear logic and concise, clearly defined functions, modules, variable names etc.

* Well documented : inline comments, docstrings providing function/ class signature and return types.

* Well formatted : indentation and formatting, PEP-8 conventions followed.

* Lack of readability affects modifiability, and hence, maintainability of the code, thereby incurring ever-increasing
cost for the organization in terms of resources - mainly people and time - in maintaining the system in a useful state.
"""

# READABILITY ANTI-PATTERNS

"""
* Code with little or no comments : If no proper documentation is done, it is difficult to figure out why certain
approach was implemented or what exactly is the code's logic.

* Code which breaks best practices of the language

* Antipatterns : 
    
    * Spaghetti code: A piece of code with no discernible structure or control flow.
    
    * Big ball of mud: It is basically cluster of Spaghetti code.
    
    * Copy-Paste programming: Produces long repetitive chunks of code.
    
    * Cargo-Cult programming: Same design pattern is followed again and again.
    
    * Ego-Programming: An experienced programmer, favour personal style of coding, could lead to cryptic and difficult
    to read for the others, specially, young or less-experienced programmers.

* Antipatterns specific to Python:

    * Mixed indentation
    
    * Mixed string literals
    
    * Overuse of the functional construct: Programmer coming from a functional programming background to python overuses
    these constructs producing code that is too cryptic. 
    
"""

# TECHNIQUES FOR READABILITY

"""
* Inline documentation : function doc-strings, class doc-strings, Module doc-strings

* External documentation

* User Manuals

* Follow coding and style guidelines(PEP-8)

* Review and refactor code : quick fixes over time leads to code bloat if not documented properly. This can create a
debt for the engineering team, and overall fixes could be time consuming and costly.

* A fresh set of eyes, is often useful in detecting the bugs that the original authors may have overlooked.

* Comments should be descriptive and should explain the code.

* Inline comments to be used as little as possible. It can cause bugs if accidentally the separating character is 
deleted.

* Try to avoid comments which are superfluous and add little value.

"""

# COHESION AND COUPLING

"""
* Cohesion refers to how tightly the responsibilities of a module are related to each other.

* A module in which alot of functionality is dumped without a thought as to the core functionality would have low
cohesion.

* Coupling : The degree to which the functionality of the two modules A and B are related. Two modules are strongly 
coupled if their functionality overlaps strongly at the code level. Any change in A requires a change in B.

* High Cohesion and Low coupling is admired in the coding practice.

* Bidirectional Coupling between the two modules ties their modifiability to each other very strongly. => This is a bad 
form of coupling. 
"""

# EXPLORING STRATEGIES FOR MODIFIABILITY

"""
* Provide explicit interfaces to the functiond, methods and APIs.

* Reduce two-way dependencies

* Abstract common services - helper modules or in case of classes a base class.

* Late Binding Techniques: 
    
    * The practice of postponing the binding of values to parameters as late as possible in the order of execution of a
    code. Late binding allows the programmer to defer the factors which influence the code execution, and hence the 
    results of execution and performance of the code.
    
    * Plugin mechanisms: Plugin likes python modules, names fetched at the run-time.
    
    * Brokers/Registry lookup services.
    
    * Notification services.
    
    * Deployment time binding.
    
The combined deployment/Configuration time or dynamic binding, can greatly increase the flexibility of a system and aid
its modifiability.

"""

# METRICS - TOOL FOR STATIC ANALYSIS

"""

* Pylint : coding errors, coding smells, style errors.

* Pyflakes : performs only logic checks in the code.

* McCabe : computes the McCabe complexity of your code.

* Pycodestyle : check against PEP-8 conventions.

* Flake8 : wrapper over pycodestyle, McCabe and Pyflakes.

"""

# CODE SMELLS

"""
* Code smells are not bugs, but they are patterns that indicate that the approach to solving problems adopted in the
code is not right, and should be fixed by refactoring.

* Common code smells:
    
    * God objects : Single class doing all the work, low cohesion.
    
    * Constant Class : Class just a collection of constants.
    
    * Refused Bequest : Class that breaks the substitution principle of inheritance from base class.
    
    * Freeloader : A class with few functions, do almost nothing.
    
    * Feature Envy : A class highly dependent on the methods of another class indicating high coupling.
    
* Long methods.

* Parameter creep : too many parameters in the signature.

* Cyclomatic complexity : too many branches or nest loops which creates a convoluted logic that is difficult to follow.

* Overly long and short identifiers.

"""

# CYCLOMATIC COMPLEXITY - McCABE METRIC

"""
* Cyclomatic complexity is a measure of complexity of a computer program. It is computed as the number of linearly
independent paths through the program's source code from start to finish.

* The control graph is pictures as a directed graph, where the nodes represent the blocks of the program and edges 
represent the control flow from one block to another.

                                FORMULA = E - N + 2P

E -> Number of edges in the graph
N -> Number of node in the graph
P -> NUmber of connected components

"""

# REFACTORING THE CODE

"""
* Fix complex code first : remove code smells.

* Do an analysis of the code : complexity checkers.

* Fix code smell if left.

* Run checkers : Pylint

* Fix low hanging fruits : code style, convention errors etc.

* Perform a final check using checkers : Pylint.

"""


