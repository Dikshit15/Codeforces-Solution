k = input()
l = input()
m = input()
n = input()
d = input()
cnt =0
for i in range(1,d+1):
	if i%k == 0 or i%l == 0 or i%m ==0 or i%n ==0:
		cnt+=1
print cnt