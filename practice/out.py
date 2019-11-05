# write file
# filename = input('enter a new file name')
filename = "test"

wf = open(f"{filename}.txt", 'w')

for i in range(5):
    wf.write(f"{i+1}번쨰 줄입니다\n")


wf.close()

print(f"a new file ({filename}) was created")