Writeup 3 - OSINT II, OpSec and RE
======

Name: *Kate Mann*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Kate Mann*

## Assignment 3 Writeup

### Part 1 (100 pts)
##### Weakness 1
* Weakness: Secure web server password 

  * Issues: 
    * The password was too simple. It did not include any capital letters, number, or special characters. 
    * The password was easy to guess through research of Fred Krueger's instagram and twitter accounts. 
    * There was no multi-factor authentication for web server login. 

* Recommendations:  
    * Passwords:
        * Passwords should be a minimum of 8 characters and contain letters, numbers, and special characters. 
        * Use a unique password for every account. While this might be hard to do for every account I recommend 
          important accounts having their own unique password. 
        * Don't make passwords easy to guess. Avoid using common words. Avoid using personal information or interests 
          as a password. 
        * Consider using a password manager (more information listed below). 
        * Always logout of accounts when done using a computer. Some browsers will remain logged into accounts even 
          after closing the browser. 
        * Consider using Multi-factor authentication (more information listed below). 
      
    * Password Manager: 
        * A password manager generates and stores random, long, and unique passwords for a variety of accounts.
        * Password Managers authenticate through one password from the user. 
        * This user provided password must be a strong password, otherwise a hacker will have access to all user accounts. 
        
    * Multi-factor authentication: 
        * Multi-factor authentication requires a user to present two different forms of evidence to prove identity. 
          A user must present something they know (i.e. username and password) and something they have (pin received on 
          token or sent to phone). This ensures that anyone attempting to brute force a password would not be able to 
          into the secure web server. 

* Sources:
    * 1: [Creating and Managing Secure Passwords, U.S. Cert, 27 March 2018](https://www.us-cert.gov/ncas/current-activity/2018/03/27/Creating-and-Managing-Strong-Passwords)
    * 2: [Security tip (ST04-002), U.S. Cert, 21 MAY 2009](https://www.us-cert.gov/ncas/tips/ST04-002)
    * 3: [Creating a Password Tip Card, DHS, undated](https://www.dhs.gov/sites/default/files/publications/Best%20Practices%20for%20Creating%20a%20Password.pdf)
    * 4: [Everything You Need to Know About Password Managers, Consumer Reports, 07 February 2017](https://www.consumerreports.org/digital-security/everything-you-need-to-know-about-password-managers/)

##### Weakness 2
* Weakness: Social Media Vulnerabilities

    * Issues: 
        * Business and personal information integrated into public viewing social media accounts.
        * Personal flight information posted on public Instagram account. 
        * Company secure web server password easy to guess from social media account activity. 
        * Public facing social media accounts leave the user open to social engineering and phishing attacks. 

* Recommendations:
    * Secure Social Media Accounts:
        * Recommend taking advantage of social media account privacy settings. Social media accounts should not be 
          open to the public. Users should restrict the viewing of their pages to a small select group of people. 
        * Recommend that business and personal social media accounts and information remain separated from each other. 
        * Recommend never posting sensitive information on social media (i.e. airline ticket). This allows potential
          attackers an attack vector for social engineering. (example: could email about customer satisfaction to gain 
          more personal information)
        * Recommend removing Fred Krueger's email address off cornerstoneairlines about section. Should create a 
          generic business email address rather than using personal email address. 
        
* Sources: 
    * 1: [Security Tip (ST05-013), U.S. Cert, 22 June 2005](https://www.us-cert.gov/ncas/tips/ST06-003)
    * 2: [Security Tip (ST04-014), U.S. Cert, 22 October 2009](https://www.us-cert.gov/ncas/tips/ST04-014)
    

##### Weakness 3
* Weakness: IP Address listed on Cornerstone Airlines admin page with exposed port. 

    * Issues: 

* Recommendations:

* Sources: 