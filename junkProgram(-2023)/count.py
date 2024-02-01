val = []
val_len = 0

while True:
    input_line = input(">> ")
    if input_line:
        val.append(input_line)
    else:
        break

if val:
    for i in range(len(val)):
        val_len+=len(val[i])
    print(val_len)
