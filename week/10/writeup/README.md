Writeup 10 - Crypto II
=====

Name: *Kate Mann*
Section: *0121*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Kate Mann*

## Assignment 10 Writeup

### Part 1 (70 Pts)
The first thing I did was create the sockets necessary to interact with the server. After doing that, 
I proceed to loop through the commands until receiving my first hash with the message. Once I had the hash,
the program then computed the fake hash. Then it was on to creating the padding. I mostly followed the 
slides for the week on how to compute the length of the padding and what information needed to be placed in. 
The only exception, was instead of calculating lengths on bits I used bytes. To ensure that my padding was 
indeed the correct length, I verified that the padding adding with the lengths of the message and secret 
equaled 64. Since this was the case it was time to send it back through the server to find the flag. 

### Part 2 (30 Pts)

This portion of the assignment was pretty straightforward. 
The first command I executed was: `gpg --gen-key`.
I was then prompted to enter my name and email. Once I had my keys set up I checked to make sure that 
they were stored in my systems by executing `gpg --list-secret-keys`. Once I assured myself that 
they were there, I then imported the provided public key `gpg --import pgpassignment.key`. Now it was time
to create an actual message file. Once I finished that it was time to encrypt it by using 
`gpg -e -u "Kate Mann" -r "UMD Cybersecurity Club" message.txt`. After this, I renamed the outputted file
 and moved it into the correct directory. 
