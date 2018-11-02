Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: *Kate Mann*
Section: *0101*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Kate Mann*

## Assignment 8 Writeup

### Part 1 (45 Pts)
So the first thing I did was to open the provided pcap file into Wireshark. I initially began by 
filtering for the string username. Which was nice because the correct packets immediately popped up. 
From there I was able to answer the questions below. 

1. [University of Maryland Cybersecurity](http://csec.umiacs.umd.edu/) (128.8.120.43)

2. Names: laz0rh4x and c0uchpot4doz

3. IP Address: 
* 142.93.118.186 : North Bergen, New Jersey (Possibly the West View Towers, or The North Hudson regional Fire Department)
* 104.248.224.85 : North Bergen, New Jersey (Possibly the West View Towers, or The North Hudson regional Fire Department)

They are connecting from Cornerstone Airlines
4. Source Port: 2749
Destination Port: 33794

5. They are doing something tomorrow at 1500. 

6. They sent a google drive [link](https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view)
Which lets you download a file called update.fpff. 

7. They will see each other tomorrow at 1500. c0uchpot4doz shouldn't be late

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*

Initially I began starting to at least parse the header information. 
After finally resolving the complete header, I then began to work my way through the rest of the file. 
I kept parsing information for each section, creating the needed functions to decode/convert the 
section information. Once I finally finished all the sections, I realized there was still more data left at the
end of the file. This led me to go ahead and continue parsing through the file until I reached the end of the file.
Good thing too, because there were two more sections at the end. After finishing working though the file, 
I then went through and created the rest of the decode/convert for sections that were not present in the file. 
This created a program that would be able to decode any .fpff file rather than specifically this one. Once I was
done finishing the code, I decided to start flag hunting.

The easiest flag to find was hidden in the .png file that was parsed. 
However, when I initially parsed, section 6 I thought it was weird that portions of the text were incorrect. I initially 
thought it was an error in the way I was converting the information but I eventually realized that it was a flag.
The last flag I found came from the last section. When I initially saw it I just thought it was gibberish.  
After going through my class notes trying to determine what this gibberish might be, I had notes on doing
base64 conversion. After finding a converter online I was gifted with my last flag. 

1. The file was created on 2018-10-24 20:40:07

2. The author of the file was laz0rh4x

3. There are 9 sections in the file. There are really 11 sections in the file. 

4.

* 2018-10-24 20:40:07 laz0 rh4x 9 
* <===========Section 1==============>
    * 9 51 (Type: ASCII)
    * Call this number to get your flag: (422) 537 - 7
* <===========Section 2==============>
    * 5 60  (Type: WORDS)
    * [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
* <===========Section 3==============>
    * 6 16 (Type: COORD)
    * 328479099.0 1078165229.0 924964157.0 3226681795.0 
* <===========Section 4==============>
    * 7 4 (Type: REFERENCE)
    * 1
* <===========Section 5==============>
    * 9 60 (Type: ASCII)
    * The imfamous security pr0s at CMSC389R will never find this!
* <===========Section 6==============>
    * 9 991 (Type: ASCII)
    * The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.
* <===========Section 7==============>
    * 6 16 (Type: COORD)
    * 736452888.0 1078165212.0 113084771.0 3226680243.0 
* <===========Section 8==============>
    * 1 245614 (Type: PNG)
    * saved as the_picture.png
* <===========Section 9==============>
    * 9 22 (Type: ASCII)
    * AF(saSAdf1AD)Snz**as
* <===========Section 10==============>
    * 9 45 (Type: ASCII)
    * Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9
* <===========Section 11==============>
    * 2 48 (Type: DWORDS)
    * [4, 8, 15, 16, 23, 42]


5. 
* CMSC389R-{c0rn3rs0ne_airlin3s_to_the_m00n}
* CMS389R-{PlaIN_dIfF_FLAG}
* CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}

