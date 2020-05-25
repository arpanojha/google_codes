## Guess a number

BIG = "TOO_BIG"
SMALL = "TOO_SMALL"
CORRECT = "CORRECT"
INCORRECT = "INCORRECT"
a=1
b=100
t=5

def main():
    print()
    print("Guess value between "+ str(a) +" and "+ str(b))
    k =guess_value(a,b,t)
    if k == 0 :
    	print("Given UP")
    elif k == 1:
    	print()






def show_options(a,b,t):
	print("Select One")
	print(BIG)
	print(SMALL)
	g=input("[]:")
	if g == BIG:
		guess_value(a,(a+b)/2,t)
		return -1
	elif g == SMALL:
		guess_value((a+b)/2,b,t)
	    #return 2
	else:
		print("Select again")
		return show_options(a,b,t)

def guess_value(a,b,t):
	if a == b:
		return 0
	if t == 0:
		return 0
	print("Our guess:",(a+b)/2)
	k = input(CORRECT+" or "+INCORRECT+":")
	if k == CORRECT:
		return 1
	else:
		j = show_options(a,b,t-1)
		return 0



if __name__=="__main__": main()