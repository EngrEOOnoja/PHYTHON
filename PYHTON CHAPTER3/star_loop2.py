Skip to content
geeksforgeeks
Tutorials
Go Premium
Search...

Sign In
Python Tutorial
Interview Questions
Python Quiz
Python Glossary
Python Projects
Practice Python
Data Science With Python
Python Web Dev
DSA with Python
Python OOPs
Next Article:
Python program to calculate the number of words and characters in the string
Next article icon



Python program to calculate the number of digits and letters in a string
Last Updated : 23 Jul, 2025
In this article, we will check various methods to calculate the number of digits and letters in a string. Using a for loop to remove empty strings from a list involves iterating through the list, checking if each string is not empty, and adding it to a new list.














s = "Hello123!"
​
# Initialize counters for letters and digits
l_c = 0
d_c = 0
​
# Iterate through each character in the string
for char in s:
  
  # Check if the character is a letter
    if char.isalpha():  
        l_c += 1
        
   # Check if the character is a digit
    elif char.isdigit(): 
        d_c += 1
​
print(f"Letters: {l_c}")
print(f"Digits: {d_c}")

Output
Letters: 5
Digits: 3
Explanation

for loop iterates through each character in the string s, using char.isalpha() to check if a character is a letter and char.isdigit() to check if it is a digit.
counters l_c and d_c are incremented based on the character type, and the final counts of letters and digits are printed.
Using filter()
Using filter() to remove empty strings from a list allows you to apply a filtering condition, such as checking whether each string is non-empty, and return a list of only the strings that meet the condition.




s = "Hello123!"
​
# Count letters using filter and len
l_c = len(list(filter(str.isalpha, s)))
​
# Count digits using filter and len
d_c = len(list(filter(str.isdigit, s)))
​
print(f"Letters: {l_c}")
print(f"Digits: {d_c}")

Output
Letters: 5
Digits: 3
Explanation

filter(str.isalpha, s) filters out only the alphabetic characters from the string s, and len(list(...)) counts the number of alphabetic characters.
filter(str.isdigit, s) filters out the digits, and len(list(...)) counts the number of digits in the string, with both counts being printed.
Using collections.Counter
Using collections.Counter to count the number of letters and digits in a string allows to check the occurrences of each character. The Counter class creates a dictionary-like object where characters are keys, and their counts are values.




from collections import Counter
​
# Input string
s = "Hello123!"
​
# Count frequencies of each character
f = Counter(s)
​
# Count letters and digits
l_c = sum(1 for char in f if char.isalpha())
d_c = sum(1 for char in f if char.isdigit())
​
# Print the counts
print(f"Letters: {l_c}")
print(f"Digits: {d_c}")

Output
Letters: 4
Digits: 3
Explanation

The Counter(s) counts the frequency of each character in the string s, storing the results in a Counter object f.
The sum(1 for char in f if char.isalpha()) counts the number of alphabetic characters, and sum(1 for char in f if char.isdigit()) counts the number of digits in the string, with the counts being printed.


Comment

More info

Advertise with us
Next Article 
Python program to calculate the number of words and characters in the string
Similar Reads
Python program to calculate the number of words and characters in the string
We are given a string we need to find the total number of words and total number of character in the given string.For Example we are given a string s = "Geeksforgeeks is best Computer Science Portal" we need to count the total words in the given string and the total characters in the given string. I
3 min read
Python program to check if a string has at least one letter and one number
The task is to verify whether a given string contains both at least one letter (either uppercase or lowercase) and at least one number. For example, if the input string is "Hello123", the program should return True since it contains both letters and numbers. On the other hand, a string like "Hello"
3 min read
Python program to count the number of spaces in string
In Python, there are various ways to Count the number of spaces in a String.Using count() Methodcount() method in Python is used to return the number of occurrences of a specified element in a list or stringPythons = "Count the spaces in this string." # Count spaces using the count() method space_co
3 min read
Python Program to move numbers to the end of the string
Given a string, the task is to write a Python program to move all the numbers in it to its end. Examples: Input : test_str = 'geek2eeks4g1eek5sbest6forall9' Output : geekeeksgeeksbestforall241569 Explanation : All numbers are moved to end. Input : test_str = 'geekeeksg1eek5sbest6forall9' Output : ge
6 min read
Count the number of characters in a String - Python
The goal here is to count the number of characters in a string, which involves determining the total length of the string. For example, given a string like "GeeksForGeeks", we want to calculate how many characters it contains. Letâ€™s explore different approaches to accomplish this.Using len()len() is
2 min read
Count the number of characters in a String - Python
The goal here is to count the number of characters in a string, which involves determining the total length of the string. For example, given a string like "GeeksForGeeks", we want to calculate how many characters it contains. Letâ€™s explore different approaches to accomplish this.Using len()len() is
2 min read




geeksforgeeks-footer-logo
Corporate & Communications Address:
A-143, 7th Floor, Sovereign Corporate Tower, Sector- 136, Noida, Uttar Pradesh (201305)
Registered Address:
K 061, Tower K, Gulshan Vivante Apartment, Sector 137, Noida, Gautam Buddh Nagar, Uttar Pradesh, 201305
GFG App on Play Store
GFG App on App Store
Advertise with us
Company
About Us
Legal
Privacy Policy
In Media
Contact Us
Advertise with us
GFG Corporate Solution
Placement Training Program
Languages
Python
Java
C++
PHP
GoLang
SQL
R Language
Android Tutorial
Tutorials Archive
DSA
DSA Tutorial
Basic DSA Problems
DSA Roadmap
Top 100 DSA Interview Problems
DSA Roadmap by Sandeep Jain
All Cheat Sheets
Data Science & ML
Data Science With Python
Data Science For Beginner
Machine Learning
ML Maths
Data Visualisation
Pandas
NumPy
NLP
Deep Learning
Web Technologies
HTML
CSS
JavaScript
TypeScript
ReactJS
NextJS
Bootstrap
Web Design
Python Tutorial
Python Programming Examples
Python Projects
Python Tkinter
Python Web Scraping
OpenCV Tutorial
Python Interview Question
Django
Computer Science
Operating Systems
Computer Network
Database Management System
Software Engineering
Digital Logic Design
Engineering Maths
Software Development
Software Testing
DevOps
Git
Linux
AWS
Docker
Kubernetes
Azure
GCP
DevOps Roadmap
System Design
High Level Design
Low Level Design
UML Diagrams
Interview Guide
Design Patterns
OOAD
System Design Bootcamp
Interview Questions
Inteview Preparation
Competitive Programming
Top DS or Algo for CP
Company-Wise Recruitment Process
Company-Wise Preparation
Aptitude Preparation
Puzzles
School Subjects
Mathematics
Physics
Chemistry
Biology
Social Science
English Grammar
Commerce
World GK
GeeksforGeeks Videos
DSA
Python
Java
C++
Web Development
Data Science
CS Subjects
@GeeksforGeeks, Sanchhaya Education Private Limited, All rights reserved
We use cookies to ensure you have the best browsing experience on our website. By using our site, you acknowledge that you have read and understood our Cookie Policy & Privacy Policy
Got It !
Lightbox