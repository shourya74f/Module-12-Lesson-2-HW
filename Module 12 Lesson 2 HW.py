n=int(input("Enter the characters to be previewed: "))
file=open("Science Facts.txt", "r")
print(file.read(n))
file.close()
print()

file=open("Science Facts.txt", "r")
l=file.readlines()
file.close()
for i in range(len(l)):
    print(i+1, "-", l[i].strip())

s=input("Skip lines starting with: ")
file=open("Science Facts.txt", "r")
for line in file:
    if line.startswith(s):
        print("Skipping line:", line.strip())
    else:
        print("Keeping line:", line.strip())
file.close()