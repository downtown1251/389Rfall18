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
The first course of action was to get a copy of the lecture slides from the repository. The slides helped determine 
which tools would most likely be needed with this weeks assignment. I then began to explore them to determine how 
best to use them. From there, I created a plan of attack for this problem. Then it was time to explore the 
command `nc cornerstoneairlines.co 45` to determine what happened occurs when connecting to that port. From there, 
it was time to start trying different inputs to the prompt. 

![Connecting to Cornerstone Airlines](cornerstoneairlines.png)
 
#### Attack Vector Discovery
After completing this step, I decided to start with Mitre's CVE list. I began by searching 
`linux ping AND command injection` which returned 42 results. I then went through each result to determine if it 
provided a viable attack vector for this assignment. For the CVEs that contained references I would follow the link
and determine if there was an attack or description of attack that I could search for on github or google. I continued 
this process until I reached `CVE-2017-1000473`. The reference inside of this 
[CVE](https://github.com/afaqurk/linux-dash/issues/447) lead to a github issue discussing the command injection 
vulnerabilities for linux-dash. I copied and pasted the command injection line `;ls -al` fdcarl used on 
the issue in place of an IP address on cornerstoneairlines.co port 45. This immediately listed out the entire 
directory listing under the root directory. Success!!

![Attack Success!](attackshot.png)

#### Finding the Flag
After determining the attack vector was indeed the correct one, I then began to dig around inside the directories
to find the correct flag by using `;cd directory name && ls -a`. After searching around for a while I finally landed in 
the home directory which contained only the file `flag.txt`. From there, I then executed the command
`cat /home/flag.txt` to get the print out of the correct flag. 

![Flag!!!](flag.png)

#### How to protect system from this vulnerability
Sanitize User Input: User input should never be blindly trusted. Since it is easy to explore the entire root 
directory by using command injection it is important to ensure that input from the users are properly sanitized. 
Ideally this input would be checked and sanitized directly after the input is received but it should always be 
validated and sanitized before it is used. Commonly, it is easier to create a whitelist for validation of user input. 
This list will check the input against what input characters and numbers are allowed and if any
input is received containing characters not in the list will automatically be ignored. 

#### Sources
* 1: [OWASP](https://www.owasp.org/index.php/Input_Validation_Cheat_Sheet#Goals_of_Input_Validation)

### Part 2 (55 pts)

#### Initial Process
