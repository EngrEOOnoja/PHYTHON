#3.28 (Intro to Data Science: Mean, Median and Mode) Calculate the mean, median and
#mode of the values 9, 11, 22, 34, 17, 22, 34, 22 and 40. Suppose the values included another 34. What problem might occur?

import statistics
grades = 9, 11, 22, 34, 17, 22, 34, 22, 40
print("mean : ", + statistics.mean(grades))
print("median : ", + statistics.median(grades))
print("mode : ", + statistics.mode(grades))
#print("sorted : ", + sorted(grades))
