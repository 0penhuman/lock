from PIL import Image
image=Image.open('pngfromcode.png')
pixels = image.load()
width, height = image.size
pixels = [[image.getpixel((x, y)) for x in range(width)] for y in range(height)]
print(pixels)
# 本程序读到的：[[(0, 83, 61), (0, 89, 119), (0, 88, 241), (0, 89, 43), (0, 78, 12)], [(0, 123, 52), (0, 78, 7), (0, 127, 143), (0, 255, 20), (0, 0, 113)], [(0, 0, 119), (0, 0, 127), (0, 0, 103), (0, 0, 32), (0, 0, 128)], [(0, 0, 114), (0, 0, 118), (1, 244, 154), (0, 0, 0), (0, 0, 0)]]
# 生成的：((0, 83, 61), (0, 89, 119), (0, 88, 241), (0, 89, 43), (0, 78, 12), (0, 123, 52), (0, 78, 7), (0, 127, 143), (0, 255, 20), (0, 0, 113), (0, 0, 119), (0, 0, 127), (0, 0, 103), (0, 0, 32), (0, 0, 128), (0, 0, 114), (0, 0, 118), (1, 244, 154), (0, 0, 0), (0, 0, 0))
word=[]
for i in pixels:
    for j in i:
        for k in range(0,3):
            word.append(str(hex(j[k])[2:]))
print(word)
i=0
for i in range(0,len(word)):
    if len(word[i])<2:word[i]='0'+word[i]
word=''.join(word)
while word[-6:]=='000000':
    word=word[:len(word)-6:]
print(word)
with open('codingfrompng.code','w') as file:
    file.write(word)