mk=str(input('Masukkan Kata:'))
def funPalindrome():
    if mk==mk[::-1]:
        print ("Yes")
        print ("Jika dibalik: ",mk[::-1])
    else:
        print ("No")
        print ("Jika dibalik: ",mk)

funPalindrome()