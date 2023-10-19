# Lecture Note (Lecture 6. Git)  
  
#### Student  \: Lim Gyu-yeon (202334734, Department of Computer science and engineering)  
  
------  

##### why is git important?
- version-control
- collaboration (working together)

##### version control
- basic version control : making copies 
- example : homework.txt, homework_final.txt, homework_seriousfinal.txt ...
- we need a specific version management for my workers (who edit it, when edit it..)

##### changes vs snapshots (git uses snapshots)
- version control way : changes, snapshots
- changes : base version + delta at version N
- snapshots : snapshots at situation that programs is changed

##### collaboration (git uses distributed)
* local : version control at one computer
* centralized : receive the version from central server that can do version control
* distributed : all computer have copy of version database

##### state in git
* modified
* staged
* commited 

##### git config
* system level : --system (administrative)
* global level : --global (all repositories of a current user)
* local level : --local (current repository)

##### initialzing a repository in an existing directory
* git init 

##### checking repository status
* git status

##### adding a new file at stage area
* git add [filename]

##### adding all files at stage area
* git add .

##### unstaging (In real, file doesn't be removed -> removing file staging at git)
* git rm --cached [filename]

##### ignoring a file
* .gitignore : a file that would find the file that have to be ignored

##### commit
* git commit -m "commit message"
