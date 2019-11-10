
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
input_yes_no="yes"
while(input_yes_no == "yes"):
    input_val = input("Enter what you want !")
    val, operation = val_frm_txt(input_val)
    for ch in operation:
        if(ch.lower() in Sum):
            add=0
            for i in val:
                add=add + i
            print(add)
            break
        elif(ch.lower() in subtract):
            sub = val[0]
            del val[0]
            for i in val:
                sub = sub - i
            print(sub)
            break
    else:
        print(" Sorry we could not find what you want from these expressions ")
    input_yes_no = input("Do you want continue::yes/no ")

print("!!!!!!!  Thanks for Using this Smart Calculator  !!!!!!!")
