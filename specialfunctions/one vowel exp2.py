#program for accepting line of text and get words which contains at least one vowel
# def vow(words):
#     r=False
#     for val in words:
#         if val.lower() in list("aeiou"):
#             r=True
#             break
#     return r
# #mainprogram
# w=input("enter a line of text:")
# words=w.split()
# v=list(filter(vow,words))
# print(v)

#proceess-2

# def vow(words):
#     res=not(set(words.lower()).isdisjoint((set("aeiou"))))
#     return res
# #mainprogram
# w=input("enter a line of text:")
# words=w.split()
# v=list(filter(vow,words))
# print(v)

#anunymou fun
w=input("enter a line of text:")
words=w.split()
v=list(filter(lambda words:not(set(words.lower()).isdisjoint(set("aeiou"))),words))
print(v)
