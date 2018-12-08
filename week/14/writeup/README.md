Writeup 10 - Crypto II
=====

Name: *Kate Mann*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Kate Mann*

## Assignment 10 Writeup

### Part 1 (40 Pts)
Well the first thing I did was look around the website. It didn't look like there was any place for user input. 
However, I noticed in the url bar that when I clicked on an item link, the url displayed `item?id=0`. First thing
I tried was just inputting a succession of numbers. Once I got to `item?id=3` a blank page was displayed. 
Which I thought was interesting because obviously this was a database rather than actual linked pages because 
otherwise I would have received a 404 error. So obviously this was the correct parameter to try and craft an
exploit. 

I decided it was time to try some other query types to see what they would return. The first two that I tried 
were directly from the slides on WAF bypasses. However, neither one produced interesting results. 
Both just brought me directly back to the item page. Then I decided to test whether this was the correct format 
for the injections by forcefully causing an error with incorrect results. I tried inputting `' && 0x50 is null` 
which should have caused an error to occur but didn't. It still brought me back to the same item page. At this
point I realized that there must be some more sql command parameters after my inputted text. After looking back 
through the Web I slides I realize I should try using a comment at the end of my input. 
Using `' || 0x50 is not null -- -` did the trick! The entire database was dumped to the webpage. Inside 
the database was the flag `CMSC389R-{yOU-are_the_5ql_n1nja}` which is priceless!


### Part 2 (60 Pts)
* Question 1: Upon seeing the user input box, I decided to try and submit `<script> alert("testing") </script>` to 
determine what would happen. Once I clicked search my alert popped up. 

* Question 2: For this challenge the first thing I tried to do was submit the same html that I did previously. 
this produced nothing in terms of text or alerts. I then looked around to determine another way to inject 
javascript into a website. I then stumbled upon inline html attributes. I then created a button that when clicked
executed the javascript alert
`<button type="button" onclick="alert('Hello World')">Show Alert</button>`. This did indeed create a button
in the chat message window. I then clicked the button and the alert popped up. 

* Question 3: The first thing I did was look up what an execution sink was since I'd never heard the term before.
I learned from [here](https://blog.mindedsecurity.com/2011/07/jquery-is-sink.html) that a sink is a function or 
method that accepts untrusted input and executes it. From this information, I now knew I needed to find where 
this method or function was within the code and exploit it. At first pass through of the code, I saw that 
chooseTab was accepting a number argument and was parsing it as an integer using `parseint()` and then appending 
the number to get the correct image. So then it was time to determine what to input into the url. Since this was 
already using the img tag, the smartest thing to do would be to close out the src attribute and use another
attribute. The hardest part was determining which attribute to use. Looking at [w3](https://www.w3schools.com/tags/tag_img.asp)
I learned that img tag also supported the HTML event attributes. At first I tried `' onload='alert("testing")'/> <!--`
when I tried loading the page this did not work. Looking through the rest of the attributes I eventaully tried
`' onerror='alert("testing")'/> <!--` This worked! 

* Question 4: The first thing was click the create timer button to determine what actually happened. Afterwards, I 
then started to dig through the code to determine the path of my supplied input so that I could determine the 
best way to create and exploit. Eventually I ran across `onload="startTimer('{{ timer }}');"` which looked 
interesting. To test out what would happen if I prematurely closed `{{` I typed `}}'` into the timer input
box. After clicking create timer, the program just ran infinitely. This looked like a promising start for an 
exploit. So after inputting various ways to prematurely exit the startTimer function it was time to figure out
how to execute the alert. At first I tried using the `<script>` tags however that caused syntx errors. It was at 
that point I realized this was using javascript rather than HTML so then I issued `');  alert('testing` and got 
my alert pop up. 

* Question 5: Since digging through the code provided a lot of help for the last two challenges, I decided to start
there first this time. After I looked through the code I noticed `<a href="{{ next }}">Next >></a>` seemed like a
strange way to change links. Normally you would just have the link directly written in the href attribute. To 
test this out I changed `next=confirm` to `next=welcome` to see if it really was linking pages based off this. 
Sure enough, I was taken to the welcome page directly rather than to the confirm page. Next item on the to do 
list was to determine how I could exploit this to execute an alert. Luckily Google came to my rescue 
via a link to [StackOverflow](https://stackoverflow.com/questions/5519059/inline-javascript-in-href). 
Once I changed `next=confirm` to `next=javascript:alert("Testing")` I was through this challenge. 

* Question 6: Looking through the code it was easy to find the exploitable code since they highlighted it with
the suggestive comment `// This will totally prevent us from loading evil URLs!`. However, I wasn't exactly sure
what I was supposed to do with this information since gadget.js was completely empty. I wasn't sure if finding
a random javascript file online was going to work. It seemed a little bit too simple. The biggest issue was 
finding a javascript file that actually used alert(). After looking around for an hour, I decided to check
out the hints that were provided to see if anything was mentioned. Luckily they provided a
[Google](https://www.google.com/jsapi?callback=foo) link of a javascript file. Interestingly, this 
file did not contain an alert but would load into the url after removing the `https:` from the url. 
So I looked at the provided url and decided to see if changing `callback=foo` to `callback=alert` 
would give me a javascript file with an alert. Which it did! So I put this [new file](https://www.google.com/jsapi?callback=alert)
into the url and passed the challenge. 