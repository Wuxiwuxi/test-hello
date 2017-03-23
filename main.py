# This is a comment


''' Hello
 I am talking to myself


 have a nice day'''


 """ Have 

 a 


 nice


 day

 """

name
id
price
date



#Step 1:
print " Download  https://nextmovesoftware.com/blog/2014/02/27/unleashing-over-a-million-reactions-into-the-wild/"


#Step 2:
print " open first file and work out how data is given "


#step 3:
print " write a very very simple python script to STORE the data. "


f = open('1IDU.pdb',r)
lines = f.readlines()

words = lines[0].split() 

name =  words[1]
id = words [3]
date = words[2] 


assert name == "OXIDOREDUCTASE"
assert id =="1IDU"
assert date == '5-APR-01'


# I want a node to be a molecule in neo4j

# I want many molecules to be nodes in neo4j 

# I have 1 million reactions

# I have ~3 million molecules.


# I have downloaded these reactions as text files.




print " hello"
