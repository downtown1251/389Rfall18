Writeup 2 - OSINT (Open Source Intelligence)
======

Name: *Kate Mann*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Kate Mann*

## Assignment 2 writeup

### Part 1 (45 pts)

1. What is kruegster1990's real name? 
    * ######Answer
    * Name: Fred Krueger
        * How: Basic google search returned [kruegster1990 twitter page](https://twitter.com/kruegster1990)

2. List all personal information (including social media accounts) you can find about him. For each, briefly detail how you discovered them.

    * ######Answer
    * Email: kruegster@tutanota.com
        * How: Bio [link](http://cornerstoneairlines.co/about.html) about section.
     
    * Job: Fred Krueger is the owner of cornerstone airlines
        * How: The about section of cornerstone airlines website. 

    * Twitter: [kruegster1990 twitter page](https://twitter.com/kruegster1990)
        * How: Basic Twitter search
     
    * Instagram: [kruegster1990 instagram page](https://www.instagram.com/kruegster1990/)
        * How: IntelTechniques username search
    
    * Likes: Fred Krueger really loves Pokemon
        * How: Twitter has a link to Pokemon Go cyber risk article and Instagram has Pokemon pictures. 

3. What is the IP address of the webserver hosting his company's site? How did you discover this?
    * ######Answer
    * Ip Address: 142.93.118.186
        * How: ran command nmap cornerstoneairlines.co and it was listed underneath. 

4. List any hidden files or directories you found on this website. Did you find any flags?
    * ######Answer
    * Secret Page: Found hidden web address [secret web address](www.cornerstoneairlines.co/secret)
        * How: Looked up [www.cornerstoneairlines.co/robots.txt](www.cornerstoneairlines.co/robots.txt)

    * Flag: Yes a flag was found on by inspecting the element on [secret web page](www.cornerstoneairlines.co/secret)
        * Flag: CMSC389R-{fly_th3_sk1es_w1th_u5}

5. Did you find any other IP addresses associated with this website? What do they link to, or where did you find them?
    * ######Answer
    * Admin: [Admin Website](http://142.93.117.193/) 142.93.117.193
        * How: Clicked on the admin section of the website. 

6. If you found any associated server(s), where are they located? How did you discover this?
    * ######Answer
    * What: The admin page is hosted by an nginx web server
        * using [shodan](https://www.shodan.io/host/142.93.117.193) and inputting the admin page ip address lists a different web server than 
        the main website. 
     
7. Which operating system is running on the associated server(s)? How did you discover this?
    * ######Answer
    * OS: Ubuntu
        * How: When checking [shodan](https://www.shodan.io/host/142.93.117.193) it was listed.

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)
    * ######Answer

    * Flag: CMSC389R-{h1dden_fl4g_in_s0urce} 
        * Location: found in source code of [cornerstone airlines home page](http://cornerstoneairlines.co/index.html)

    * Flag: CMSC389R-{dns-txt-rec0rd-ftw}
        * Location: found searching cornerstoneairlines.co on dnsdumpster.com

    * Flag: CMSC389R-{fly_th3_sk1es_w1th_u5}
        * Location: found after looking at robot.txt and adding /secret to cornerstoneairlines.co domain name.
     
    * Flags: CMSC389R-{c0rn3rstone-air-27600} up to CMSC389R-{c0rn3rstone-air-27999}
        * Location: after running `$: cat *` in the flight_records directory I learned that every record had a different
                    flag associated with it. 


### Part 2 (55 pts)

######Setup
The first thing I did was to determine the correct ip address and port number. I was able to determine that the admin 
IP address was most likely the correct address. After using nmap -p- on the IP address I tried nc <IP> <Port> for 
every port until I got a login prompt for port 1337. After finding the correct port, I then went to work on stub.py. 
After studying how to use python sockets, I set up the stub.py to successfully connect to the IP and port to 
attempt a brute force attack. 

######Brute Force Attack
I then began to run my previously built attack with different user names. I initially used the names of the 
pokemon characters shown on the Instagram page. However, it became more likely to me that this was  a 
password rather than a username. Mostly because I kept seeing pokemon as a password in rockyou.txt. From there, 
I start looking at user names centered around Fred Krueger himself to include his email address and various other 
personal and company related user names.

After locating the correct username which was a part of kruegster1990's email address access to the admin shell 
was achieved. From there, I determined the first place to look was within the home directory. From there I moved 
into the flight records directory where I used the posted ticket on [instagram](https://www.instagram.com/kruegster1990/) 
to find the correct flight information and flag. The flag is CMSC389R-{c0rn3rstone-air-27670}. 

