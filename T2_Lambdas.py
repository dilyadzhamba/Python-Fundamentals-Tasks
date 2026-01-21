
# T2. Lambdas
#Use map, filter and sorted functions of lambda funtions

# Task 1
sentence = "This is a lAmBdA FuNction task"
words=sentence.split(" ")

result=list(map(lambda x:[x,x.upper(),x.lower(),len(x)],words))

print (result)



for i in x:
    mylist=[]
    mylist.append(i)
    mylist.append(i.upper())
    mylist.append(i.lower())
    mylist.append(len(i))
    print( mylist)
 


# Task2

sentence = "This is a lAmBdA FuNction task"
words=sentence.split(" ")

def upper_func(word):
    return word.upper()

def lower_func(word):
    return word.lower()

def length_func(word):
    return len(word)

result=list(map(lambda x:[x,upper_func(x),lower_func(x),length_func(x)],words))
print (result)


# Task 3
a = [1, 11, 23, 44, 16]
b = [2, 3, 5, 6, 7, 8, 44, 16]


print(list(filter(lambda x:x in a, b)))


# Task 4
sentence = "This is a lAmBdA FuNction task"

words=sentence.split(" ")

sorted_values=sorted(words,key=lambda x:x[-1])
print(list((sorted_values)))