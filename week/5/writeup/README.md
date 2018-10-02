Writeup 5 - Binaries I
======

Name: *Kate Mann*
Section: *0101*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Kate Mann*

## Assignment 5 Writeup
* First thing I did was google examples of System V assembly code. 
* Then I plugged the c code into compiler explorer. This gave an assembly output but not necessary the correct version. 
But, it provided a starting point. 
* I figured the best place to start would be to create the loop first. 
* Once I figured how to make it loop without sigfaulting I then had to figure out how to 
get the correct values in the correct registers. 
* After getting the values into registers that were not temporary.  A problem arose. Whenever 
I would copy the character into the string, I would lose the last portion of the array.
I feel this is most likely because the char has a null value at the end. But, I need to 
figure out how copy the value over without the null character. 