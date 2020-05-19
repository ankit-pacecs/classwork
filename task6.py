#question 1
# i=0
# while i in range(150):

#     try:
#         i=int(input("enter the number to check odd/even"))
#         if i%2==0:
#             print("this is even number ", i )
#     except ValueError:
#         print("there is problem with input ")
            
#     finally:
#         print("do you want to try again ?")
#         break 

#question 2

#question 3
l=list(input("enter four numbers "))


try:
    if (len(l))<4:
        print("if block")
    else:
        print("the number is not big")
except Exception :
    print("number " )

