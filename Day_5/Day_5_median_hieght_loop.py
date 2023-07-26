# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
median_hieght =0
len_counter = 0

for hieght in student_heights:
    median_hieght += hieght
    len_counter += 1

median_hieght = median_hieght/len_counter

print(round(median_hieght))

