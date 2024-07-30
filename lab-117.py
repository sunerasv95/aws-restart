# -----Retrieving the protein sequence of human preproinsulin
import os

def file_character_length_check(file_name, required_length):
    text_len=0;
    
    with open(file_name, 'r') as f:
        text = f.read()
        text_len = len(text)
        f.close()
    
    if(text_len == required_length):
        print(f'{file_name} has met required character length {text_len}')
        print("\n-------------------------------------------------------")
    else:
        print(f"Invalid character length {text_len} for {file_name}")

# ----- Data Cleaning

# Step 1. 
# Create preproinsulin-seq-clean.txt file and
# Confirm that your file has 110 characters of lowercase letters, 
# which represent the amino acids in the sequence of human preproinsulin.

file_character_length_check('preproinsulin-seq-clean.txt', 110)

# this file will be used for extracting different portions 
# of the insulin 
with open('preproinsulin-seq-clean.txt', 'r') as f:
    base_insulin = f.read()
    print('\n')
    print(f'BASE INSULIN CODE: \n{base_insulin}')
    print("\n-------------------------------------------------------")
    f.close()


# Step 2.
# Create lsinsulin-seq-clean.txt file for save amino acids 1–24,
# Verify that your file has 30 characters
ls_insulin = base_insulin[0:24]
bi_insulin = base_insulin[24:54];
ci_insulin = base_insulin[54:89];
ai_insulin = base_insulin[89:110];

with open('lsinsulin-seq-clean.txt', 'a') as f:
    f.write(ls_insulin)
    f.close()
file_character_length_check('lsinsulin-seq-clean.txt', 24)

with open('biinsulin-seq-clean.txt', 'a') as f:
    f.write(bi_insulin)
    f.close()
file_character_length_check('biinsulin-seq-clean.txt', 30)

with open('ciinsulin-seq-clean.txt', 'a') as f:
    f.write(ci_insulin)
    f.close()
file_character_length_check('ciinsulin-seq-clean.txt', 35)

with open('aiinsulin-seq-clean.txt', 'a') as f:
    f.write(ai_insulin)
    f.close()
file_character_length_check('aiinsulin-seq-clean.txt', 21)
    





