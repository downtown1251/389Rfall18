Writeup 5 - Binaries I
======

Name: *Kate Mann*
Section: *0101*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Kate Mann*

## Assignment 5 Writeup
I've never used System V assembly so I decided the first course of action was to google it to see what was going 
I needed to do. After, looking around google and realizing that it wasn't going to be much help, I decided to put
the provided C code into [compiler explorer](www.godbolt.com). However, this didn't really provide much insight into
what I needed to begin since it does not convert to System V assembly. (*That would have been too easy and I should
have known that*)

Since google and compiler explorer didn't give much help, I decided it was time to reread the project prompt. (*I should
have read it all the way through the first time, lesson learned*) In the prompt we were given links to 
[here](https://c9x.me/x86/) and [here](https://www.felixcloutier.com/x86/). Thankfully, I could finally know which 
assembly commands were the correct ones. So after finally seeing the light, I decided to start on my_memset. I decided
that looping through the string and replacing each character would probably do the trick. I created my loop, however, 
I then ran into what would become my biggest problem, how to copy the replacement character into the string. Trying 
to just move the replacement character into the string index was causing segmentation faults. After looking at 
gdb, it was easy to see that the character was not listed like a string but as a number. This made it obvious that 
the issue was that. (*At this point in time, beating my head against the computer seemed like the most logical 
course of action*)

Eventually, after hours googling how to copy a character into a string, I learned how to correctly use the movb command. 
Finally this method was done and produced the correct results. So now it was time to tackle my_strncpy. 

At first I figured I could just use the same loop from my_memset to do the same thing, as the two methods are 
fairly similar. This did not work in the slightest bit. Gdb showed me that in fact this loop did nothing to the string
at all. So, the next thing I decided to try was to add a null character
in the index corresponding to the length argument and copy over the source to the destination. However, this did not 
work at all either. (*It wouldn't even compile*) So, I decided to revist the project prompt to see if it could 
provide me any more inspiration for this problem and it did! I didn't look at the rep command. After reading up on it, 
I decided to give that a shot. Since the arguments were already in the correct registers, with the exception of the 
length argument, which was simple enough to move, It was time to let it run. That worked like a charm! 