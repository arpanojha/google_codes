#import cv2

#a= [1,0,2,9,3,8,4,7,5,6]
a= [1,3,3,2]
def main():
    m, n , o= find_next_biggest(a)
    sumval = max(a)
    sumval = add_beauty(sumval, m)
    l= (len(a)-2)/2
    while(l > 1):
    	print(sumval)
    	sumval = add_beauty(sumval, a[n+o])

    	n=n+o
    	l = l-1
    print(sumval)




def find_next_biggest(a):
	k = a.index(max(a)) 
	#print(k)
	if k==0:
		return a[k+1], k+1 , 1
	elif k==len(a)-1:
		return a[k-1], k-1, -1
	if a[k+1]>a[k-1]:
		return a[k+1], k+1, 1
	else:
		return a[k-1], k-1, -1
def add_beauty(a, b):
	a = a+b
	return a


if __name__ =="__main__":main()