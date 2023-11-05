import random



def select_nums() :
    nums = []
    a = random.randint(0,9)
    nums.append(a)
    b = random.randint(0,9)
    if b == nums[0]:

        while nums[0] == b:
            b = random.randint(0,9)
        nums.append(b)

    else:
        nums.append(b)

    c = random.randint(0,9)

    if c == nums[0] or c == nums[1]:
        while c == a or c == b:
            c = random.randint(0,9)
        nums.append(c)
    else:
        nums.append(c)

    return nums


random_num = select_nums()

for x in range(len(random_num)):
    random_num[x] = str(random_num[x])
guess = ""

while True:
    print(random_num)
    guess = input("enter your guess here:")
    while len(guess) != 3:
        print("please enter a 3 digit number")
        guess = input("enter your guess here:")


    print("your guess is " +guess)

    if guess[0] == random_num[0] and guess[1] == random_num[1] and guess[2] == random_num[2]:
        print('you are winner')
        break
    if guess[0] == random_num[0] or guess[1] == random_num[1] or guess[2] == random_num[2]:
        print("match")
    elif guess[0] in random_num or guess[1] in random_num or guess[2] in random_num:
        print("close")
    else:
        print("nope")
    quit = int(input("press 0 to continue or 1 to quit"))
    if quit == 1:
        print("quitted")
        break
    else:
        continue
