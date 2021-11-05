#Program which takes string as input and prints the letters in decreasing order of frequency
Str1= input('Please enter a string ') #take input from the user 
def most_frequent(string):    #function to display number of character in decreasing order of frequency
    d = dict()                #an empty dictionary
    for key in string:        #calculate frequency of all letters
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
            
    sorted_keys = sorted(d, key=d.get, reverse=True) #sort frquency in decreasing order 
    for r in sorted_keys:   #printing frequency
        print(r, d[r])
       
   
most_frequent(Str1) #function call

