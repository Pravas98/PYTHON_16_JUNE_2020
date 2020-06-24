st = "This is Python and Python is fun"

for c in sorted(set(st)):
    print(f"{c}  - {st.count(c)}")

