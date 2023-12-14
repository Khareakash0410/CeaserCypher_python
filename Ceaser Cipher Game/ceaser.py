encode#--------------------------  Ceaser Cipher----------------------                  
   # 1--- Encryption---------
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b',
        'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from ceaser_logo import logo
print(logo)
#  ----- list  is taken large and repeating because for values like x y z it show error for key so values is repeating to avoid occur----
continue_counter = True
while continue_counter:
 Request = input("type 'encode' to encrypt the message or 'decode' to decrypt the message.")
 if Request == "encode":
    Input = input("enter the message.").lower()
    Key = int(input("enter the required key number."))
 elif Request == "decode":
      Input = input("enter the message.").lower()
      Key = int(input("enter the required key number."))
# else:       for enter a valid input as encode or decode
     # print("please Enter a valid input.")
 #def my_function(Input1,Key1):
  #  encrypted_message = ""
  # for private in Input1:
   # Private = list.index(private) + Key1 
# ------  index() has property fot repeatinf value in list like to take singlr time only items.-----
    # new_private = list[Private]
   # encrypted_message += new_private
  # print(f"your encrypted message is {encrypted_message}")
     # 2 --- Decryption.
# def my_function1(Input2,Key2):
  # decrypted_message = ""
  # for letter in Input2:
   # new_letter =  list.index(letter) - Key2
   # new_name = list[new_letter]
   # decrypted_message += new_name
  # print(f"your decrypted message is {decrypted_message}")
# if Request == "encode":
  # my_function(Input,Key)
# elif Request == "decode":
  # my_function1(Input,Key)
#  ---- combine into single function  -----
 def ceaser(My_input,My_Key,Direction):
   Message = ""
   for repeat in My_input:   
    if repeat in list:      #  ----- for making non alphabet as same in input. -------
     My_var = list.index(repeat)
     if Direction == "encode":
      My_new_var = My_var + (My_Key%26) 
     elif Direction == "decode":
      My_new_var = My_var - (My_Key%26) 
     My_New_Name = list[My_new_var]
    # My_New_Name2 = My_New_Name 
    # My_New_Name2 = "*"                 it can be used to make like (***** 123&%^%^ $%^%^)
    # Message += My_New_Name2
     Message += My_New_Name
    else:            # ------- everything except  symbol will be same . --------
        #  ------ can also use symbol/number/spaces. in list for making it more efficient . ---------
      Message += repeat
   print(f"your message is {Message}.")
 ceaser(Input,Key,Request)
 New_Tasks = input("Type 'Yes' to continue or 'No' to exit.")
 if New_Tasks == "No":
   continue_counter = False
   print("let say me goodbye!")