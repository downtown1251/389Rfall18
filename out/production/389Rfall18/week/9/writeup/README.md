Writeup 9 - Crypto I
=====

Name: *Kate Mann*
Section: *0101*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Kate Mann*

## Assignment 9 Writeup

### Part 1 (60 Pts)
The first thing I did when tackling this assignment was to reread the crypto slides to determine a good place to start. 
After rereading that, it was time to delve into the Python library hashlib and read through it to give some insight.
After reading through the library I decided it would be prudent to google some examples of using the hashlibrary.
Once I read through the documentation, it was time to take a crack at part1.py. 

Looping through the salts was already provided so the next item to create were the loops through the passwords and 
hashes. Once I got the loops set up, it was time to create the salted password and send it through 
`shalib.sha512().hexdigest()` to get the guessed digest for checking against the stolen hashes. When I ran the code at
this point, I received an error

Running the code the first time did not return any results. It took me a while to figure out that the password list
contained newline characters at the end of the password. This newline was being factored into the hash so they needed
to be stripped out. After, stripping the newline from the end of the guessed password, I reran the code. This time
the code printed out: 

```
<===== Passwords =====>
Hash: 9a23df618219099dae46ccb917fbc42ddf1bcf80583ec980d95eaab4ebee49c7a6e1bac13882cf5dd8d3850c137fdff378e53810e98f7e9508ca8516e883458e
Salt: k Password: neptune
Hash: c35eb97205dd1c1a251ad9ea824c384e5d0668899ce7fbf269f99f6457bd06055440fba178593b1f9d4bfbc7e968d48709bc03e7ff57056230a79bc6b85d92c8
Salt: m Password: jordan
Hash: 70a2fc11b142c8974c10a8935b218186e9ecdad4d1c4f28ec2e91553bd60cfff2cc9b5be07e206a2dae3906b75c83062e1afe28ebe0748a214307bcb03ad116f
Salt: p Password: pizza
Hash: d39d933d91c3e4455beb4add6de0a48dafcf9cb7acd23e3c066542161dcc8a719cbac9ae1eb7c9e71a7530400795f574bd55df17a2d496089cd70f8ae34bf267
Salt: u Password: loveyou
 ```
### Part 2 (40 Pts)


