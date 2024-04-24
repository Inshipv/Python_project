from time import *
import random as r
def mistake(partext , usertext):
    error =0 
    for i in range(len(partext)):
        try:
            if partext[i]!= usertext[i]:
                error = error +1
        except:
            error = error +1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay,2)
    speed = len(userinput)/time_r
    return round(speed)

text = ['''Ladies and gentlemen,'''

'''Today, as we gather here, we celebrate a cornerstone of our society, a principle that is fundamental to the fabric of our civilization - democracy. Democracy isn't merely a system of governance; it's a testament to the power of collective voice, the embodiment of freedom, and the cornerstone of justice.'''


'''As we look to the future, let us recommit ourselves to the principles of democracy. Let us strive to build a world where every voice is heard, every person is valued, and every individual has the opportunity to shape their own destiny. Let us stand together in defense of democracy, knowing that it is not merely a form of governance but a beacon of hope for generations to come.

Thank you''']
    
while True:
    ck = input("Ready for test : yes / no  ")
    if ck == "yes":
        test_1 = r.choice(text)
        print("****** Typic Speed ********")
        print(test_1)
        print()
        print()
        time_1 = time()
        testinput = input("enter: ")
        time_2 = time()
        print('speed : ', speed_time(time_1 , time_2, testinput), "w/sec ")
        print("Error :", mistake(test_1,testinput))
    elif(ck =="No"):
        print("Thank You")
        break
    else:
        print("Worng input")
        break