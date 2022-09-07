list_integer = [1, 2, 3, 10, 100, 250]
list_string = ["Dewi", "nazla", "lulu"]
list_mix = [20, "Arya", True, "Bryan"]

print("data sebelum diubah", list_string)
list_string[0] = "kazu"
print("data setelah diubah", list_string)

print("data sebelum diubah", list_string)
list_string[0] = "kazu"
list_string[1] = "rui"
list_string[2] = "knox"
print("data setelah diubah", list_string)

print("data sebelum diubah", list_mix)
list_mix[0] = 13
list_mix[1] = "knox"
list_mix[2] = False
list_mix[3] = "baron"
print("data setelah diubah", list_mix)

# perulangan for
x = ['kazu', 'rui', 'knox']

for y in x:
    print(y)

for o in list_string:
    print(o)

for s in list_integer:
    print(s)

for t in list_mix:
    print(t)