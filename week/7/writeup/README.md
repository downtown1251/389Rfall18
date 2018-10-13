Writeup 7 - Forensics I
======

Name: *Kate Mann*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Kate Mann*

## Assignment 7 writeup

### Part 1 (40 pts)

1. JPEG, jpg

2. Chicago, Illinois, USA : John Hancock Building 

3. Time: 2018:08:22 16:33:24Z

4. Apple iPhone 8 Back camera : 3.99MM f/1.8

5. 540 meters (1,7770 feet)

6. `CMSC389R-{look_I_f0und_a_str1ng}` Found by doing a hexdump of the image. Also, could have used the 
strings command `strings image | grep -C1 "CMSC"`

### Part 2 (55 pts)
Steps: 
* ran `sudo dd if=binary of=sdX.img bs =4M` to make a copy of the binary so I didn't 
it up
* then ran `sha512sum sdX.img` 
* ran `strings sdX.img | grep -C1 "flag"` which returned 
```
   []A\A]A^A_
   Where is your flag?
   ;*3$"
```
* ran `binwalk sdX.img`
* ran `binwalk -e sdX.img`
* ran `binwalk -dd="elf:elf sdX.img` which created the directory `_sdX.img.extracted` which contained 0.elf. 
I then ran hexdump on the file to see if there was anything interesting. There really wasn't. So then I started
looking into readelf command. I then worked to figure out how to run the .elf file. I finally figured out that 
it wasn't running becuase I hadn't made it executable. I created a copy of the .elf file and executed 
`chmod +x binary.elf` to make this executable. I then just ran it, and it printed `Where is your flag?`. 
Since the file was now running it was time to open up gdb and see if I could figure out where the flag
was within the program. 

After stepping through the file it looked like it was writing to a file `/tmp/.stego` 
After cd'ing to the directory I found that the program was indeed writing to a file named .stego. 
I ran `file .stego` which said that this was a data file. I then ran `binwalk .stego`
to see what came up. Binwalk determined that this was a jpeg file. I then ran `binwalk -e .stego` which 
extracted the picture. Looked like a dinasaur which I went ahead and guessed it was a stegosaurus. So 
then I ran `steghide extract -sf 1.jpeg -xf out.txt` and used the passphrase `stegosaurus`. Which then wrote 
the flag to out.txt. After viewing out.txt, I finally found the flag `CMSC389R-{dropping_files_is_fun}`