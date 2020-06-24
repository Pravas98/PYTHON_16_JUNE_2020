s1 = "Abcd Xyz Pqr"
s2 = "Xy  Pqpqr Cde"

common = set(s1) & set(s2)
print(sorted(common))
