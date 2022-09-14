import numpy as n

# alphabet and english freq vector
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
freq_eng = [0.082, 0.015, 0.027, 0.047, 0.13, 0.022, 0.02, 0.062, 0.069, 0.0016, 0.0081, 0.04, 0.0027, 0.067, 0.078, 0.019, 0.011, 0.059, 0.062, 0.096, 0.027, 0.097, 0.024, 0.0015, 0.02, 0.00078] 
max_abs_vals = []
# imports text from file
with open('text.txt', 'r') as file:
    data1 = file.read().replace('\n', '')
with open('text2.txt', 'r') as file:
    data2 = file.read().replace('\n', '')
with open('text3.txt', 'r') as file:
    data3 = file.read().replace('\n', '')    
with open('text4.txt', 'r') as file:
    data4 = file.read().replace('\n', '')     
with open('text5.txt', 'r') as file:
    data5 = file.read().replace('\n', '')      
with open('text6.txt', 'r') as file:
    data6 = file.read().replace('\n', '')          
with open('text7.txt', 'r') as file:
    data7 = file.read().replace('\n', '')    
with open('text8.txt', 'r') as file:
    data8 = file.read().replace('\n', '') 
with open('text9.txt', 'r') as file:
    data9 = file.read().replace('\n', '') 


#####################
# not using right now
def shift_text(input, shift, way):
    news = []
    input = input.lower()
    for i in input:
        if i == ' ':
            news.append(' ')
        elif not i.isalpha():
            news.append(i)
        else:
            if way == "forwards":
                news.append(chr((ord(i) - 97 + shift) % 26 + 97))
            else:
                news.append(chr((ord(i) - 97 - shift) % 26 + 97))

    return ''.join(news)
 #####################


# gets rid of everything but the letters and creates a new string   
def shift_text_but_without(input, shift, way):
    news = []
    input = input.lower()
    for i in input:
        if not i == ' ' and i.isalpha():
                if way == "forwards":
                    news.append(chr((ord(i) - 97 + shift) % 26 + 97))
                else:
                    news.append(chr((ord(i) - 97 - shift) % 26 + 97))

    return ''.join(news)    
    
# main code    
def decode(input):
    sum = 0
    #go through all possible keys
    all_freqvs = []
    # goes through 1 - 25
    # gets curr shift freq vector
    for num in range(1, 26):
        curr = get_freq_vector(shift_text_but_without(input, num, "back"))
        sorted_dict = {}
        sorted_keys = sorted(curr, key=curr.get, reverse=True)
        # creates new sorted hash but isn't used right now
        for w in sorted_keys:
            sorted_dict[w] = curr[w]
        print(sorted_dict)
        all_freqvs.append(sorted_dict)
        # gets difference between the first of sorted freq hash and 'e'
        shift = alphabet.index(list(sorted_dict.keys())[0]) - alphabet.index('e')
        # dots current freq vector and english freq vector
        print(n.dot(list(curr.values()), freq_eng))
        print(n.dot(freq_eng, freq_eng))
        print(freq_eng)
        print(" ")
        # print(all_freqvs)   

# go through each shift make sure big gap between 0.2 and other
# see minimum         
# then do aphine
def decode_1st(input):
    sum = 0
    list_of_shifts = []
    #go through all possible keys
    all_freqvs = []
    # goes through 1 - 25
    # gets curr shift freq vector
      
    for what_on in range(1, 26):
        curr = get_freq_vector(shift_text_but_without(input, what_on, "back"))
        for num in range(1, 26):
            sum = sum + (abs(freq_eng[num] - list(curr.values())[num]))
        list_of_shifts.append(sum)
        sum = 0
    print("incorrect text: ", list_of_shifts)    
    sum = 0
    curr = get_freq_vector(shift_text_but_without(input, 1, "back"))    
    for num in range(1, 26):
        sum = sum + (abs(freq_eng[num] - list(curr.values())[num]))
    print("correct text: ", sum)

def decode_2nd(input):
    sum = 0
    #go through all possible keys
    all_freqvs = []
    # goes through 1 - 25
        # gets curr shift freq vector
    list_of_shifts = []    
    for what_on in range(1, 26):
        curr = get_freq_vector(shift_text_but_without(input, what_on, "back"))    
        for num in range(1, 26):
            sum = sum + ((freq_eng[num] - list(curr.values())[num])**2)
        list_of_shifts.append(sum)    
        sum = 0    
    print("incorrect text: ", list_of_shifts)  
    curr = get_freq_vector(shift_text_but_without(input, 1, "back"))    
    sum = 0
    for num in range(1, 26):
        sum = sum + ((freq_eng[num] - list(curr.values())[num])**2)
    print("correct text: ", sum) 

#input has to have all but letters removed
# creates frequency vector in a hash (key is letter, freq is value)  
def get_freq_vector(input):
    length = len(input)
    fvect = [0] * 26
    vecthash = {}
    for i in input:
        fvect[(ord(i) - 97) % 26] = fvect[(ord(i) - 97) % 26] + 1
    for j, val in enumerate(fvect):   
        fvect[j] = fvect[j]/length
    for k, val in enumerate(fvect):
        vecthash[alphabet[k]] = round(val, 2)  
    return vecthash

print("regular")
print(" ")
print("DATA 1: ")
print("with abs and subtracting: ")
decode_1st(shift_text(data1, 1, "forwards"))
print("with squaring and subtracting: ")
decode_2nd(shift_text(data1, 1, "forwards"))
print(" ")
print("DATA 2: ")
print("with abs and subtracting: ")
decode_1st(shift_text(data2, 1, "forwards"))
print("with squaring and subtracting: ")
decode_2nd(shift_text(data2, 1, "forwards"))
print(" ")
print("DATA 3: ")
print("with abs and subtracting: ")
decode_1st(shift_text(data3, 1, "forwards"))
print("with squaring and subtracting: ")
decode_2nd(shift_text(data3, 1, "forwards"))
print(" ")
print("DATA 4: ")
print("with abs and subtracting: ")
decode_1st(shift_text(data4, 1, "forwards"))
print("with squaring and subtracting: ")
decode_2nd(shift_text(data4, 1, "forwards"))
print(" ")
print("DATA 5: ")
print("with abs and subtracting: ")
decode_1st(shift_text(data5, 1, "forwards"))
print("with squaring and subtracting: ")
decode_2nd(shift_text(data5, 1, "forwards"))
print(" ")
print("DATA 6: ")
print("with abs and subtracting: ")
decode_1st(shift_text(data6, 1, "forwards"))
print("with squaring and subtracting: ")
decode_2nd(shift_text(data6, 1, "forwards"))
print(" ")
print("DATA 7: ")
print("with abs and subtracting: ")
decode_1st(shift_text(data7, 1, "forwards"))
print("with squaring and subtracting: ")
decode_2nd(shift_text(data7, 1, "forwards"))
print(" ")
print("DATA 8: ")
print("with abs and subtracting: ")
decode_1st(shift_text(data8, 1, "forwards"))
print("with squaring and subtracting: ")
decode_2nd(shift_text(data8, 1, "forwards"))
print(" ")
print("DATA 9: ")
print("with abs and subtracting: ")
decode_1st(shift_text(data9, 1, "forwards"))
print("with squaring and subtracting: ")
decode_2nd(shift_text(data9, 1, "forwards"))