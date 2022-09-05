input_str = "abbur"
print("old string :",input_str)
input_str_list = list(input_str)
string = ""
index = 2 #int(input("Enter the letter's INDEX to remove:"))
ins_char = 'd' #input("Enter the letter:")
input_str_list[index] = ins_char
for j in input_str_list:
    string += j
print("New string :",string)
