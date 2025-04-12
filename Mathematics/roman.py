
def roman_to_int(a):
    roman={'1':1,'v':5,'x':10,'L':50,'c':100,'D':500,'N':1000}
    int_form=0
    for i in range(len(a)):
        if i+1<len(a) and roman[a[i]]<roman[a[i+1]]:
            int_form-=roman[a[i]]
        else:
            int_form+=roman[a[i]]
            return int_form
        
        #a=input("enter a roman numeral:")
        # print("interger form of",a,"is",roman_to_int(a))
        