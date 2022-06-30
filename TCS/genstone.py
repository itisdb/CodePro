R = (int)(input("Enter the count of Ruby: "))
G = (int)(input("Enter the count of Garnet: "))
T = (int)(input("Enter the count of Topaz: "))

def Ways(r, g, t, last):
	if r==1 and g==0 and t==0 and last==0:
		return 1
	if r==0 and g==1 and t==0 and last==1:
		return 1
	if r==0 and g==0 and t==1 and last==2:
		return 1
	if r<0 or g<0 or t<0:
		return 0

	if last==0:
		return Ways(r-1,g,t,last=1)+Ways(r-1,g,t,last=2)
	if last==1:
		return Ways(r,g-1,t,last=0)+Ways(r,g-1,t,last=2)
	if last==2:
		return Ways(r,g,t-1,last=0)+Ways(r,g,t-1,last=1)

def start(r,g,t):
	return Ways(r,g,t,0)+Ways(r,g,t,1)+Ways(r,g,t,2)

print(start(R,G,T))