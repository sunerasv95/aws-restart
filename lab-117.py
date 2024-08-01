# -----Retrieving the protein sequence of human preproinsulin

def check_molecular_length(type_of_inculin, required_length):
    text_len=0;
    file_name = type_of_inculin+"-seq-clean.txt"
    
    with open(file_name, 'r') as f:
        text = f.read()
        text_len = len(text)
        f.close()
    
    if(text_len == required_length):
        print(f'{type_of_inculin} has total number of molecules {text_len}')
        print("\n-------------------------------------------------------")
    else:
        print(f"Invalid molecules for {type_of_inculin}")

# ----- Data Cleaning

# Step 1. 
# Create preproinsulin-seq-clean.txt file and
# Confirm that your file has 110 characters of lowercase letters, 
# which represent the amino acids in the sequence of human preproinsulin.

check_molecular_length('preproinsulin', 110)

# this file will be used for extracting different portions 
# of the insulin 
with open('preproinsulin-seq-clean.txt', 'r') as f:
    base_insulin = f.read()
    print('\n')
    print(f'the sequence of human insulin: \n{base_insulin}')
    print("\n-------------------------------------------------------")
    f.close()


# Step 2.
# Create lsinsulin-seq-clean.txt file for save amino acids 1–24,
# Verify that your file has 30 characters
lsinsulin = base_insulin[0:24]
binsulin = base_insulin[24:54]
cinsulin = base_insulin[54:89]
ainsulin = base_insulin[89:110]
insulin = binsulin + ainsulin

with open('lsinsulin-seq-clean.txt', 'w') as f:
    f.write(lsinsulin)
    f.close()
print("The sequence of human insulin, chain ls: " + lsinsulin)
check_molecular_length('lsinsulin', 24)

with open('binsulin-seq-clean.txt', 'w') as f:
    f.write(binsulin)
    f.close()
print("The sequence of human insulin, chain b: " + binsulin)
check_molecular_length('binsulin', 30)

with open('cinsulin-seq-clean.txt', 'w') as f:
    f.write(cinsulin)
    f.close()
print("The sequence of human insulin, chain c: " + cinsulin)
check_molecular_length('cinsulin', 35)

with open('ainsulin-seq-clean.txt', 'w') as f:
    f.write(ainsulin)
    f.close()
print("The sequence of human insulin, chain a: " + ainsulin)
check_molecular_length('ainsulin', 21)




# ------ Calculating the rough molecular weight of human insulin using 
# the given code

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aa_weights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  

# Count the number of each amino acids  
aa_count_insulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  

# Multiply the count by the weights  
molecular_weight_insulin = sum({x: (aa_count_insulin[x]*aa_weights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  

print("The rough molecular weight of insulin: " +str(molecular_weight_insulin))

molecular_weight_insulin_actual = 5807.63
error_percentage = str(((molecular_weight_insulin - molecular_weight_insulin_actual)/molecular_weight_insulin_actual)*100)
print("Error percentage: " + error_percentage)


pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}
pH=0

seq_count = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
print(f'seqcount {seq_count}')  

while (pH <= 14):
    net_charge = (
        +(sum({x: ((seq_count[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seq_count[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values())))
        
    print('{0:.2f}'.format(pH), net_charge)
    pH +=1






