# Lecture Note (Lecture 4. CLI-1)   
 
#### Student  \: Lim Gyu-yeon (202334734, Department of Computer science and engineering) 
   
------ 
   
**CLI (command line interface)**: This is the way to enter letters and give commands to the computer. Most notable examples include Unix shell environments represented by dos, command prompts, and bash.
   
**Linux**: open-source made similar to Unix (highest share on web servers)   
(Various variations: Ubuntu, Fedora, Debian...)    
feature : Excellent security, stable    
CLI Based (Terminal)    
    
**kernel (at OS)**: the core of the OS. Located between hardware and software    
**shell** : the role of communicating with kernel. Command Input Window    
    
**pwd** : print out the name of the directory you are currently working on     
(broadest range: root / creating a directory under root: mount)    
    
**ls** : output directories just below root    
**cd A** : Move directory to A    
    
**\<arguments\> : after cd**    
/ take root    
. Current Directory (Current Directory)     
.. parent directory (parent directory)    
~ Current user's home    
/[Directory name] Absolute path (absolute path)    
./[Directory name] Relative path (relative path)    
..../[Directory name] Relative path (relative path)    
    
**\<options\> : after ls**    
-l : Outputs detailed information (permissions to files, ownership information for files, file capacity, creation date...) 
   
-lh : It's the same as -l, when dealing with large units, -lh rather than -l    
/[directory] : output information from other directories while maintaining the current directory    
...    
    
**<Long format>**    
file permissions, owner, group, size in bytes, modification time, file name    
    
***Linux is very important because there are a lot of users, due to security)***    
    
**\<Tip: Automatic completion\>**    
TAB: Automatic completion function    
up arrow : previously used command    
    
**clear** :  empty terminal window    
    
**cp [File you want to copy] [What name to copy]** : Copy file     
**cp -r [directories you want to copy] [Where to locate the copy]** : Copy the directory (-r : also import all the nested directories)    
    
**mv [Specific File] [Specific Name]** : Replacing a particular file with specific names     
**mv [Specific Directory Files] [Other Specific Directory]** : Move a specific directory file to another specific directory    
    
**rm [file name]** : clear file    
***rm in the CLI is not recoverable (permanently erased)***    
    
**\<Wild Card\>**    
 \* : All file names    
ex) \*.py : All files with the .py extension in the current directory    
Any character file that starts with g* : g    
Data??? : Files with three consecutive letters starting with Data    
