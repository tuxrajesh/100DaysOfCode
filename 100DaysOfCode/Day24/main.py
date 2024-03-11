outpath = "Output\\ReadyToSend\\"
with open("Input\\Letters\\starting_letter.txt") as template:
    content = template.read()
    template.close()

with open("Input\\Names\\invited_names.txt") as list:
    names = list.readlines()
    list.close()
    
for name in names:
    filename = outpath + name.strip() + ".txt"
    with open(file=filename, mode="w") as out:                
        out.write(content.replace("[name]", name.strip()))

print("Done!")