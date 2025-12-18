
def dividir(a,b):
    if b== 0:
        raise Exception("division by zero")
    return a/b

try:
    a = dividir(1,0)
    print(a)
except Exception as e:
    print("no se puede dividir",e)