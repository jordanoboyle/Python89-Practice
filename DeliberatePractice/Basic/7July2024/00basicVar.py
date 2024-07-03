def space_bar():
  space = ""
  for i in range(0, 21):
    space += "%"
  return print(space)

space_bar()

#### Set 1: Writing number and string variables with built-in methods####

# # 1 Write a program that uses a variable to store a number, then prints that number plus 10.
the_number_ten = 10
print(the_number_ten + 10);
space_bar()

# # 2 Write a program that uses a variable to store a word, then prints that word with all capital letters.
w = "this needs to be capital letters"
print(w.upper())
space_bar()

# # 3 Write a program that uses variables to store two numbers, then prints the numbers added together.
x = 55
y = 51
print(x + y)
space_bar()

# # 4 Write a program that uses a variable to store a word, then prints that word in reverse order.
reverse_this = "esrever siht ni tnirp"
def reverse(string):
  rev = []
  i = -1
  while i > -(len(string)) - 1:
    rev.append(string[i])
    i -= 1
  return  print("".join(rev))
reverse(reverse_this)
space_bar()

# # 5 Write a program that uses a variable to store a number, then prints the number times 10.
number_one = 13
print((str(number_one) + " ") * 10)
print(number_one)
space_bar()

# # 6 Write a program that uses variables to store two words, then prints both words on the same line in all capital letters.
h = "hell "
j = "in caps"
print((h + j).upper())
space_bar()

# # 7 Write a program that uses a variable to store a word, then prints the number of letters in the word.
word_find_length = "wejustwanttoknowhowlongthiswordis"
print(len(word_find_length))
#or
def find_length_string(string):
  length = 0
  for i in string:
    length += 1
  return print(length)
find_length_string(word_find_length)
space_bar()

# # 8 Write a program that uses a variable to store a number with decimals, then prints the number as an integer.
this_is_a_float = 55.456 # ==> 55
number_one = 55.667
print(int(this_is_a_float))
print(int(number_one))
print(int((str(number_one))[0:2]))
space_bar()

# # 9 Write a program that uses a variable to store two numbers, then prints the two numbers multiplied together.
num_one = 10
num_two = 12
print(num_one * num_two) # ==> 120
space_bar()

# # 10 Write a program that uses a variable to store a word, then prints the word with all lowercase letters.
word_to_lower = "WE WANT TO PUT THIS INTO LOWERCASE"
print(word_to_lower.lower())
#or for fun
def to_lower_case(string):
  shrink = []
  for i in string:
    shrink.append(i.lower())
  return print(shrink)
to_lower_case("".join(word_to_lower))
space_bar()
# Personal Builds below, add to practice sessions at leisure

# # SP1 Take two words and store them using one line to two different variables. Replace all vowels with 
# # $ signs and print the words in both uppercase and lowercase. 
word_three, word_four = "hello", "world"

def replace_vowels(string1, string2):
  new_string1 = string1
  new_string2 = string2

  for vowel in "aeiou":
    new_string1 = new_string1.replace(vowel, "$")
    new_string2 = new_string2.replace(vowel, "#")
  
  return new_string1 + " " + new_string2
result = replace_vowels(word_three, word_four)
print(result)
space_bar()
print("here is an interesting one")

numbers_array = [1, 2, 3, 4, 5, 6, 67]
## to get these numbers to join just using "".join we would get a typeerror however....
join_numbers = ", ".join(map(str, numbers_array))
print(join_numbers)

