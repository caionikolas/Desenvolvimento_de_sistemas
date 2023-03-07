def pt(num ,i=1, j=2, k=3):
    if (i * j * k) == num:
        return True
    elif (i * j * k) < num:
        return pt(num, i+1, j+1, k+1)
    else:
        return False 
             
print(pt(210))