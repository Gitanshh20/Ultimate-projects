# Arthematic Progressions

Ap = input("Enter Your AP Sequence: ")

lst_Ap = Ap.split(",")

Sequence = [int(num) for num in lst_Ap]

n = int(input("Enter Your nᵗʰ Term: "))

a = Sequence[0]
d = Sequence[1] - Sequence[0]
nᵗʰ = n
rule = a + ((nᵗʰ-1)*d)

print(f"Here {nᵗʰ} Term of Ap is: {rule}")