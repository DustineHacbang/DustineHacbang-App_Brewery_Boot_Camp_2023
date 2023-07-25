# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
partner1 = name1.lower()
partner2 = name2.lower()
combined_partner =partner1 + partner2

# print(combined_partner)
# print(partner2)
# print(partner1)

true_counter= 0
true_counter += combined_partner.count("t")
true_counter += combined_partner.count("r")
true_counter += combined_partner.count("u")
true_counter += combined_partner.count("e")

love_counter=0
love_counter += combined_partner.count("l")
love_counter += combined_partner.count("o")
love_counter += combined_partner.count("v")
love_counter += combined_partner.count("e")

# print(true_counter)

true_love_rating = str(true_counter) + str(love_counter)
true_love_num = int(true_love_rating)

if true_love_num < 10 or true_love_num > 90:
        print(f"Your score is {true_love_num}, you go together like coke and mentos.")
elif true_love_num > 40 and  true_love_num < 50:
        print(f"Your score is {true_love_num}, you are alright together.")
else:       
    print(f"Your score is {true_love_num}.")