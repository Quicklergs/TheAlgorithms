# code by @JymPatel
# edited by @bupboi1337, (editors can put their name here && thanks for contribution :)

# this code uses MIT LICENSE
print("this code uses MIT LICENSE")
print("some features aren't supported due to unsupported file type for repo. get it at github.com/JymPatel/Python-FirstEdition")
print()

# start of code
# import library
import pickle
import os
import sys
# imports from our py files
import functions as fuN
import encrypt10n as encrypt

# check encryption status and get array
encryption_status = False
encryption_key = input("ENCRYPTION KEY ('noKEY' or is default KEY): ")
if encryption_key.upper() == 'NOENCRYPTION' or encryption_key.upper() == '' or encryption_key.upper() == 'NOKEY':
    print("your data is not encrypted")
    print("you can encrypt while saving program")
    encryption_key = "noENCRYPTION"
else:
    encryption_status = True
array = encrypt.getArray(encryption_key)
# sometimes wrong key doesn't make sense to decrypt like chr(9589395959359)
if array == 'ERRORx379':
    print("PROGRAM EXITED WITH ERROR CODE 379!")
    print("379 :(\n")
    print("ERROR OCCURED WHILE DECRYPTING DATA DUE TO WRONG KEY")
    print("YOUR DATA IS STILL SAFE JUST ENTER CORRECT KEY ON NEXT RUN")
    sys.exit()

# get premium ACCESS key if path exists
keyfound = False
path = 'data/pickle-key'
if os.path.isfile('data/pickle-key'):
    pklekey = open('data/pickle-key', 'rb')
    key = pickle.load(pklekey)
    pklekey.close()
    if key == 'SKD0DW99SAMXI19#DJI9':
        keyfound = True
        print()
        print("key found & is correct")
        print("YOU GOT PREMIUM ACCESS")
    else:
        print("key is WRONG\nYOU ARE RUNNING WITH STANDARD ACCESS")
        print("check https://github.com/JymPatel/Python-FirstEdition/tree/Main/PyPrograms/contacts for PREMIUM ACCESS, it's free")
else:
    print("key not found\nYOU ARE RUNNING WITH STANDARD ACCESS")
    print("check https://github.com/JymPatel/Python-FirstEdition/tree/Main/PyPrograms/contacts for PREMIUM ACCESS, it's free")


# for ease in reading
fname = 0
lname = 1
number = 2
email = 3
# getting some variables
promptvar = 1
loopvar = 0


# making loop to run
while loopvar < 1:

    # ask user what to do
    print("")
    if promptvar == 1: # 0 is for off 
        print("0.  exit program")
        print("1.  get all contacts")
        print("2.  add new contact")
        print("3.  remove any contact")
        print("4.  sort contacts by first name")
        print("9.  toggle on/off this prompt")
    a = input("WHAT WOULD YOU LIKE TO DO?  ")

    # check for integer & calculate length of array
    try:
        a = int(a)
    except ValueError:
        print("!! PLEASE ENTER AN INTEGRAL VALUE")
    arraylen = len(array[fname])

    # functions
    if a == 1:
        fuN.printallcontacts(arraylen, array)
    
    elif a == 2:
        array = fuN.addnewcontact(arraylen, array)
    
    elif a == 3:
        array = fuN.deleteOldContact(arraylen, array)
    
    elif a == 4:
        if keyfound == True:
            array = fuN.sorTarray(arraylen, array)
        else:
            print("NEED PREMIUM ACCESS TO ENABLE THIS FEATURE")

    # change prompt settings
    elif a == 9:
        if keyfound:
            if promptvar == 0: 
                promptvar += 1
                print("you won't get prompt now!")
            else:
                promptvar -= 1
        else:
            print("NEED PREMIUM ACCESS TO ENABLE THIS FEATURE")


    # ending program
    elif a == 0:
        if encryption_status == False:
            # ask to encrypt data
            print("would you like to encrypt your data")
            stra = input("y/n?  ")
            try:
                if stra[0].upper() == 'Y':
                    encryption_key = input("create your encryption key ...")
                    print("\n YOUR ENCRYPTION KEY IS", encryption_key)
                    print("\n IF YOU FORGET KEY, FORGET YOUR DATA")
            except IndexError:
                encryption_key = 'noENCRYPTION'
        # saving data to pickle file
        print("Saving your Data ...")
        encrypt.saveData(array, encryption_key)
        print("YOUR DATA HAS BEEN SAVED SUCESSFULLY!")
        loopvar += 1

    # if no true option is selected
    else:
        print("!! PLEASE ENTER VALUE FROM GIVEN INTEGER")

# end of code
print("")
print("get this code at https://github.com/JymPatel/Python-FirstEdition")
