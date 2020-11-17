# MapReduce Paradigm
Introductory activity about MapReduce paradigm

We'll use the streaming possibilities offered by operating systems such as in the Hadoop framework. Streaming consists of receiving data on standard input (often called stdin in programming languages) and sending the result to standard output (i.e. stdout).

### The Task :  Translate the following request into a mapreduce. Average call duration for each user living in Paris.
```
SELECT nom, avg(durée)
FROM calls C, users U
WHERE C.de= U.tel AND ville='Paris'
GROUP BY nom);
```

### How to Run the scripts
* Linux distros : cat users.txt calls.txt | mapperMass.py | combinerMass.py | sort | reducerMass.py | sort > result.txt
* Windows cmd : type users.txt calls.txt target.txt | mapperMass.py | combinerMass.py | sort | reducerMass.py | sort > result.txt
