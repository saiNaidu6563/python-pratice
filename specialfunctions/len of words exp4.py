
#program for accepting list of values which contains numbers and words and get word which contain at least one vowel
#and whose length between 2&3
print("enter list of values which contains numbers and words separated by space:")
wl=[v for v in input().split()]
print("given values =",wl)
word=list(filter(lambda val:not(set(val.lower()).isdisjoint(set("aeiou")))and len(val) in[2,3],wl))
print(word)