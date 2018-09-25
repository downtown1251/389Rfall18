Writeup 3 - Pentesting I
======

Name: *Kate Mann*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Kate Mann*

## Assignment 4 Writeup

### Part 1 (45 pts)
* Flag: CMSC389R-{p1ng_as_a_$erv1c3}

#### Initial Steps
The first thing I did for this assignment was to get a copy of the lecture slides from the repository. This allowed
me to go through them and start making a plan of attack. I used the slides to determine which tools would most likely
help with this weeks assignment and then began to explore them to determine how best to use them. I then 
executed the command `nc cornerstoneairlines.co 45` to determine what happened when I opened the connection and 
what behavior occurred after inputting text.

#### Attack Vector Discovery
After completing this step, I decided to start with Mitre's CVE list. I began by searching 
`linux ping AND command injection` which returned 42 results. I then went through each result to determine if it 
provided a viable attack vector for this assignment. For the CVEs that contained references I would follow the link
and determine if there was an attack or description of attack that I could search for on github or google. I continued 
this process until I reached `CVE-2017-1000473`. The reference inside of this 
[CVE](https://github.com/afaqurk/linux-dash/issues/447) lead to a github issue discussing the command injection 
vulnerabilities for linux-dash. I copied and pasted the command injection line `;ls -al` fdcarl used on 
the issue in place of an IP address on cornerstoneairlines.co port 45. This immediately listed out the entire 
directory listing under the root directory.

#### Finding the Flag
After determining the attack vector was indeed the correct one, I then began to dig around inside the directories
to find the correct flag by using `;cd directory name && ls -a`. After searching around for a while I finally landed in 
the home directory which contained only the file `flag.txt`. From there, I then executed the command
`cat /home/flag.txt` to get the print out of the correct flag. 



### Part 2 (55 pts)
*Put your writeup >= 200 words here in response to part 2 prompt. Your code for part 2 should be copied into a file in the /writeup directory and pushed there as well*
