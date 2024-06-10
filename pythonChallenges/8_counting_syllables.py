def count(str):
    return len(str.split('-'))
   
#  Este método divide la cadena syllables
# en una lista de subcadenas donde quiera
# que haya un guion (-). Por ejemplo, "ho-tel" se convierte en ["ho", "tel"]

print(count("ho-tel"))          # 2
print(count("cat"))             # 1
print(count("met-a-phor"))      # 3
print(count("ter-min-a-tor"))   # 4
print(count("a-maz-ing"))       # 3
print(count("in-ter-na-tion-al"))  # 5
