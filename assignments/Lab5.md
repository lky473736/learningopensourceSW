# Lecture Note (Lecture 5. CLI-1)  
  
#### Student  \: Lim Gyu-yeon (202334734, Department of Computer science and engineering)  
  
------  
  
**<I/O redirection>**  
Standard output : pasting ">" after command creates the current standard output (== command window) as a txt file  
                   (">>" : Additional creation without overwriting the original one)
                   cat~~~.txt : txt file output  
  
standard input : command <A.txt> apply the command and save it as a different name.txt<==A.txt  
                 ex) sort < a.txt > b.txt  
  
---------  
  
**pipeline "|"** : command1 | command2 ... <==put the output of command1 as the input of command2  
               Multiple commands can be combined and short-coded   
               ex) ls -lh | stress : Scroll as much as you want to and check the list   
  
**expansion** : special characters (with a specific meaning)  
            echo A : print A (printf)  
            echo * : file output in the current directory (* : expansion containing the current directory)  
            echo ~ : current user's home directory output (~ : expansion containing the current user's home directory)  
  
**permissions** : read, write, execution  
              Linux is multi-user system -> Rights are critical because they can touch or breach each other's files  
              Therefore, authorization of files or directories in three stages (owner/group/others of files)  
  
**Long format**  
        file permissions, owner, group, size in bytes, modification time, file name  
  
Break 3 digits to determine  
  
ex) -rwxrwxrwx : owner = rwx  
group of files = rwx  
others = rwx  
  
Use the chmod command to change permissions  
chmod <value> <file name> : Depending on the meaning of the value, which fiChange the permissions of le (value values vary by binary)  
  
**superuser** : administrator privileges  
            sudo~  execute the command with administrator privileges  
            sudo-i : When enabled, continue to use commands as administrator privileges in the future  
  
**text editors** : Basic text editor provided in the CLI
               vi, vim : Written only on keyboard and has many shortcuts  
               emacs, nano-do CLI text editors example  
  
**shell script** : allows the shell command to be executed as a file at once  
               nano myscript.sh  
