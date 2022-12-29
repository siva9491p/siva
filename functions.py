#arguments###
def ret(*args):
    a=ret(8)
    print(a)

 def rocky(value_1):
    if (value_1%7==0):
        print("true")
    else:
        print("false")
a=rocky(27)
print(a)

###########################
value=rocky("abcd")
print(value)

def rocky(value):
    b=value[1]
    return(b)
c=rocky("wrdgs")
print(c)
##########################

def prefil(a):
    return "welcome "+a

########################
def rocky(wins,draw,loss):
    wins_1=wins*4
    print(wins_1)
    draw_1=draw*2
    print(draw_1)
    loss_1=loss*-1
    print(loss_1)
    total=(wins_1+draw_1-loss_1)
    print(total)
wins=int(input())
draw=int(input())
loss=int(input())
rocky(wins,draw,loss)
#############################

def rocky(value_1):
    for i in value_1:
        if (i%3==0 and i%5==0):
            print("MarcoPolo")
           if(i%3==0):


                print("Marco")
           elif(i%5==0):

                print("Polo")

value_2=rocky([1,5,10,24,45])
print(value_2)






