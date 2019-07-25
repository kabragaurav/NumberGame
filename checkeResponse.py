def checker(response,number):
    if(response == number):
        print('WOW: You cracked it !!')
    else:
        count=2
        while(count and response!=number):
            print(count,' more try')
            response=int(input())
            count-=1
        if(response == number):
            print('Finally cracked')
        else:
            print("Woops !! Number was ",number)
