Writeup 3 - Pentesting I
======

Name: *Kate Mann*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Kate Mann*

## Assignment 4 Writeup

### Part 1 (45 pts)
* Flag: CMSC389R-{p1ng_as_a_$erv1c3}

I began by searching the CVE database using linux ping AND command injection as my search terms. 
I then began looking through the various CVE's listed until I came upon CVE-2017-1000473. 
I followed the link to [github](https://github.com/afaqurk/linux-dash/issues/447)
I then used `nc cornerstoneairlines.co 45` command.
For the IP address I then put `module=;ls -al`. This gave me the directory listings. 
I then put `module=;cd home && ls -al`
This listed flag.txt so then I executed `module=;cat /home/flag.txt`


### Part 2 (55 pts)
*Put your writeup >= 200 words here in response to part 2 prompt. Your code for part 2 should be copied into a file in the /writeup directory and pushed there as well*
