#1.从键盘接收整数的一百分制成绩(0～100),要求输出其对应的成绩等级A～E。
#其中,90分(包含)以上为A,80～89(均包含)分为B,70～79(均包含)分为C，
#60～69(均包含)分为D,60分以下为E。
Score =int(input("请输入成绩:"))
while 0 <= Score <= 100:
    if Score >= 90:
        print('A')
        break
    elif 80<= Score <= 89:
        print('B')
        break
    elif 70 <= Score <=79:
        print('C')
        break
    elif 60 <= Score <=69:
        print('D')
        break
    else:
        print('E')
        break


# 2．预设一个0～9之间的整数﹐让用户猜―猜并输人所猜的数。如果大于预设的数，显
#示“太大”;小于预设的数，显示“太小”。如此循环，直至猜中该数，显示“恭喜!你猜
#中了!”。
import random
answer = random.randint(0,9)
while 1:
    guess=int(input("请输入你要猜的数字:"))
    if guess == answer:
        print("恭喜!你猜中了!答案为",guess)
        break
    if guess < answer:
        print("小了!")
    else:
        print("大了!")


#3．某电商平台上销售不同规格包装、不同价格的水笔。编写程序，在不考虑运费的情
#况下,从键盘分别输人两种水笔的包装和价格，分别计算单根水笔的价格,根据价格就低原
#则打印输出选择购买哪种产品。
Spec=input("请输入A水笔的规格和B水笔的规格:")
Price=input("请输入A水笔的价格和B水笔的价格:")
SpecA,SpecB=map(int,Spec.split())
PriceA,PriceB=map(float,Price.split())
singlePriceA=PriceA / SpecA
singlePriceB=PriceB / SpecB
if singlePriceA < singlePriceB:
    print("买A水笔划算.")
elif singlePriceA == singlePriceB:
    print("买A和买B水笔都可以.")
else:
    print("买B水笔划算.")

#4.输出1000以内的素数以及这些素数之和
sum=0
for i in range(1,1000):
    j=2
    flag=0;
    while j < i:
        if i % j == 0:
            flag=1
            break
        j+=1
    if flag == 0:
        print(i,end=" ")
    
#5.输入一个时间（小时：分钟：秒），输出该时间经过5分30秒后的时间
time =input("请输入时间:")
h,m,s=map(int ,time.split())
m=m+5
s=s+30
if s>=60:
    s=s%60
    m=m+1
if m>=60:
    m=m%60
    h=h+1
if h>=24:
    h=h%24
    print("时间为:",h,":",m,":",s)

#6.按公式 s=1^2+2^2+3^2+……+n^2,求累加的和s不超过1000的最大项数n
s=0
i=1
while i>0:
    s=s+pow(i,2)
    if s>=1000:
        print("累计和不超过1000的最大项为:",i-1)
        break
    i+=1

