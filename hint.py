import random
import checkeResponse

def disp_hint(num,mode):
    ls=[1]     # for which type of choice to display
    num_list=[]     # stores digits of num
    temp=num
    while(temp):
        num_list.append(temp%10)
        temp//=10
    num_list.reverse()
    hint_no=random.choice(ls)
    if(hint_no == 1):
        if(mode=='C'):
            s=sum(num_list)
            print('1.]  Sum of the digits of the number is :\t',s)
            mTh=random.choice(range(0,len(num_list)))
            print('2.]  The ',mTh,' digit is ',num_list[mTh])
            nTh=mTh
            while(nTh==mTh):
                nTh = random.choice(range(0, len(num_list)))
            print('3.]  The ',nTh,' digit is ',num_list[nTh])
            response=int(input('-------  guess   --------'))
            checkeResponse.checker(response,num)
        else:
            s = sum(num_list)
            print('1.]  Sum of the digits of the number is :\t', s)
            print('2.]  The number of digits is ',len(num_list))
            if(len(num_list)%2==0):
                print('3.]  sum of middle numbers is ',sum(num_list[len(num_list)//2],num_list[len(num_list)//2+1]))
            else:
                print('3.] middle element is ',num_list[len(num_list)//2])
                response = int(input('-------  guess   --------'))
                checkeResponse.checker(response, num)