def cprint(*args, sep=" ", end="\n", color=u"\033[0m"):
    text = ""
    for arg in args:
        text += arg+sep
    text = text[0:-2]+end
    print(color+text+u"\033[0m")
    del arg, args

def cinput(prompt, color=u"\033[32m"):
    ret = input(color+prompt)
    print(u"\033[0m", end="")
    return ret

cprint("Hello World", color=u"\033[32m")
name = u"\033[35m"+cinput("Hello, What is your name", color=u"\033[34m")
cprint(f"\nHello {name}!", color=u"\033[92m")
