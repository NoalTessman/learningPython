
try:
    f = open('text_file.txt')
    var = "bad_var"
except FileNotFoundError:
    print('Error!')
except Exception as e:print("sorry, Something went wrong:", e)
else:
    print(f.read())
    f.close()