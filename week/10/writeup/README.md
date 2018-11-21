Writeup 10 - Crypto II
=====

Name: *Kate Mann*
Section: *0121*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Kate Mann*

## Assignment 10 Writeup

### Part 1 (70 Pts)


### Part 2 (30 Pts)

This portion of the assignment was pretty straightforward. 
The first command I executed was: `gpg --gen-key`.
I was then prompted to enter my name and email. Once I had my keys set up I checked to make sure that 
they were stored in my systems by executing `gpg --list-secret-keys`. Once I assured myself that 
they were there, I then imported the provided public key `gpg --import pgpassignment.key`. Now it was time
to create an actual message file. Once I finished that it was time to encrypt it by using 
`gpg -e -u "Kate Mann" -r "UMD Cybersecurity Club" message.txt`. After this, I renamed the outputted file
 and moved it into the correct directory. 
