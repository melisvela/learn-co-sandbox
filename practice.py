# 1. Grab the number 6 from this nested_list and set it equal to the number_six variable
nested_list = [1, [2, [4, [5, [6]], 3]]]
number_six = None

#answer
number_six = nested_list[1][1][1][1][0]
number_six #6

# 2. Sort the cats list in alphabetical order

cats = ['Maine Coon', 'Tabby', 'Siamese', 'Garfield', 'Sylvester']

#answer
cats.sort()

# 3. Look up a new string or list method and explain how it works

#answer
cats.count #how many times a unique element in a list is present

# 4. Create a new list cat_jrs by appending 'Jr.' to each of the cats names

#answer

jrs = ' Jr."

cat_jrs = [c + jrs for c in cats]

#answer

cat_jrs = []
for element in cats:
  cat_jrs.append(element + ' Jr.')
  
cat_jrs

# 5. create a pets array that contains the elements of the cats and dogs lists
cats = ['Maine Coon', 'Tabby', 'Siamese', 'Garfield', 'Sylvester']
dogs = ['Scooby', 'Scrappy', 'Clifford', 'Pickles', 'Floyd']
animals =



# 6. add the cats in more_cats to the original list of cats

cats = ['Maine Coon', 'Tabby', 'Siamese', 'Garfield', 'Sylvester']
more_cats = ['Horatio', 'Whiskers', 'Chesire']

#answer

cats.extend[more_cats]

#answer

cats + more_cats

# BONUS: Sorts the cats list in alphabetical order by third character of each element
cats = ['Maine Coon', 'Tabby', 'Siamese', 'Garfield', 'Sylvester']

#answer

sorted_by_third_char = sorted(cats, key=lambda element: element[2])
sorted_by_third_char

# We have a for loop that cycles through each number from 1 to 100. Write the logic to produce the following outcomes

# We expect numbers divisible by 3 to print "Fizz"
# We expect numbers divisible by 5 to print "Buzz"
# We expect numbers divisible by 3 and 5 to print "FizzBuzz"

# starter code
# for n in range(1, 101):
# print(n)

#answer

for n in range (1, 101):
   if n % 3 ==00 and n % 5 ==:
      print('FizzBuzz')
    elif n % 3 ==0:
      print ('Fizz')
    elif n % 5 == 0:
    print ('Buzz')
    else:
        print(n)
    