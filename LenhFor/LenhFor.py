''' Lệnh for:       for x in A: B '''
''' Lệnh while:     while bthuc_logic: A '''
''' Hàm zip ''' # lấy lần lượt từng bộ số, số bộ số tính theo số phần tử của list nhỏ nhất



'''
a=[4,7,2,8]
b=['a','b','c']
c= list(zip(a,b))
print(c)
d=[4,5,6,7,8,9]
e=list(zip(a,b,d))
print(e)


#nhap n = 1*2+2*3+3*4+4*5+ ... (n-1)*n

n = int(input())
a = range(n+1)
b= [x*y for x,y in zip(a,a[1:])]
print(sum(b))


# in day fibonaci
from os import sep


n = int(input())
F = [1] * 2;    # tạo một list 2 số 1 

for i in range(n): F.append(F[-1] + F[-2])  #F[-1]: phần tử cuối cùng   F[-2]: phần tử gần cuối
print(*F[:n],sep="+", end = " ")                               #F[:n]: in từ F[0] đến F[n-1]       lệnh sep để in kí hiệu giữa 2 phần tử
print("= " ,sum(F[:n]))



# Tam giác * căn giữa

n = int(input())
for i in range(1,n+1):
    x='*'*(2*i-1)
    print(x.center(2*n))



# Tính e^x = 1 + (x/1!) +(x^2/2!) + ... + (x^n/n!)


from math import exp

x,n = input().split()
n = int(n)
x = float(x)
s=1
for i in range(n,0,-1): s=1+s*x/i
print(s)
print("e^x = ",exp(x))


# dem so nghich the:    4 7 2 8 1 6 có 8
from itertools import combinations
a=[4,7,2,8,1,6]
b=list(combinations(a,2))   #Tổ hợp chập 2, không tính thứ tự
c=[1 for u,v in b if u>v]
print('songhichthe',sum(c))



# Kiểm tra dãy tăng dần

from ast import List


a=list(map(int,input().split()))
b=[x<y for x,y in zip(a,a[1:])]
print("tang dan" if all(b) else "Không tang dan")


# giai phuong trinh x^x = a, với a thuoc [1,100]
a = float(input())

L,R = 1,10

while R-L>1e-6:
    M = (L+R)/2
    if M**M<a: L=M # '**' là ^
    else: R=M 
print(R) 
print(L) 


# Tìm điểm trong đường tròn (O,r) gần M nhất
from math import sqrt
def  kc(xA,yA,xB.yB): return sqrt((xA-xB)**2+(yA-yb)**2)

if __name__ == "__main__":
    if(kc())

'''
