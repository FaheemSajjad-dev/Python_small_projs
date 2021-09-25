import random 

rand_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./<>?;:-=:\|[]" 

while 1:  # 1 means true
    pass_length = int(input("What should be the length of password: "))
    pass_count = int(input("How many passwords should be generated: ")) # in one shot
    for x in range(0,pass_count):
        password = ""
        for x in range(0,pass_length):
            pass_char = random.choice(rand_chars)
            password = password + pass_char
        print(password)
        
        