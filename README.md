awsarmy
=======

a simple distribution framework to distribute work to a dozen of AWS boxes using python flask,boto..etc.

-------------------------------------------------

myfunction -> myinput.txt -> start_master.py -> start_slaves.py
Directories: 

awsudf.py contains the source code to control the AWS resources myfunction.py contains the atomic code to let the soldier do, you can do unit test by calling the test function myinput.txt contains the list of input to the atomic function distributed to the worker, records need to be line separated output_test.txt: contains the test output, you need to test myfunction.py before distributing start_master.py: after you finish the myfunciton.py, test it by uncommenting the test part, and then you can run the start.py start_slaves.py: start master first and then start slaves.


Dependencies: 1. flask 2. mongodb 3. pymongo
