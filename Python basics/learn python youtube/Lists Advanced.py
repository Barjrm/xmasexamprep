lucky_numbers = [4,2,52,42,3]
freinds = ["Joey","Chandler", "Monica","Ross"]
print(freinds)

freinds.extend(lucky_numbers)
print(freinds)

freinds.append("Creed")
print(freinds)

freinds.insert(0, "Captain America")
print(freinds)

freinds.remove("Ross")
print(freinds)

freinds.pop()
print(freinds)

print(freinds.index("Monica"))

print(freinds.count("Chandler"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

freinds2 = freinds.copy()
print(freinds)
print(freinds2)



#freinds.clear()