
Sum=["sum","add","adding","summation","jod","+","addition"]

subtract=["sub","ghatana","subtract","-"]

def val_frm_txt(text):
    val = []
    char=[]
    for ch in text.split(' '):
        try:
            val.append(float(ch))
        except Exception:
            char.append(ch)
    return val,char

input_val=input("Enter what you want !")
a,b=val_frm_txt(input_val)

for ch in b:
    if(ch.lower() in Sum):
        add=0
        for i in a:
            add=add + i
        print(add)
        break
    elif(ch.lower() in subtract):
        sub = 0
        for i in a:
            sub = sub + i
        print(sub)
        break
else:
    print("Sorry we could not find what you want from these expressions")

