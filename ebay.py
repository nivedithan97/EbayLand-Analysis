'''
Name: Niveditha Nagasubramanian
Student ID: 28037758
Assignment 2: Ebay(Dynamic programming)

'''
#Dynamic Programming- Bottom up Solution

def MaximizeProfit1(pdtcode,price,profit,PriceLimit):
    '''
    Task 1: Maximize Profit when there is no item limit and just price limit
    this function determines the products to maximise the profit for a given price limit
    :param Input --> pdtcode Array, price Array, profit Array and the PriceLimit
    :param Output --> the total price of the items, the total items sold and the profit generated (note: this profit has to be
                      the maximum profit for the given price limit)
    Worst case time complexity --> O(PN) where P represents the P for-loop(time complexity:O(P)) and N represents the N for-loop(time complexity:O(N)).
                                   Since P for-loop and N for-loop are nested, therefore complexity is O(PN)       
                                 
    Worst case space complexity--> O(P+N) where memo array takes P space and the price array takes N space.
    
    
    '''
    memo=[0] #this is to keep track of the profits for each price till the priceLimit for eg at memo[1], it stores the maxProfit when the priceLimit is $1
    decisions=[] #this will store the price and the product 
    pro_price=[0] #this is just a temperory array
    for P in range(1,(PriceLimit+1)):
        maxProfit=0 #initialising maxProfit to 0
        for N in range(len(price)): #calculating maximum Profit at the given Price Limit(P)
            if int(price[N])<=P: #if the price of the item is greater than the PriceLimit, don't bother considering that item
                thisProfit=int(profit[N])+memo[P-int(price[N])] #calculating profit using bottom up solution
                if thisProfit>maxProfit: #if the Profit calculated(thisProfit) is greater than the maxProfit at the given PriceLimit, maxProfit=thisProfit
                    maxProfit=thisProfit
                    pro_price=[pdtcode[N],price[N],profit[N]]
                   
        memo.append(maxProfit)#append the maxProfit to the memo
        decisions.append(pro_price)
        pro_price=[] 
    #we have the profits for each PriceLimit, now its time to list out all the items for that given PriceLimit
    pricing=[] #calculates the total price of all the items
    solution=[] #this will append the items
    v=PriceLimit-1
    while v>0: 
        solution.append(decisions[v])#append the item in the decisions[v] into the solution
        pricing.append(int(decisions[v][1])) #append the price of that item in to the pricing array
       
        v=v-int(decisions[v][1])#you subtract the price of that item from the PriceLimit and then use that Price as an index in the decision array and append it to the solution array
        
   #this is to store all the unique items in the solution array into another array called Arr 
    Arr=[]

    for m in range(len(solution)-1):
        
        if solution[m][0] != solution[m+1][0] and solution[m] in Arr:
            Arr.append(solution[m+1])
        elif solution[m][0] != solution[m+1][0] and solution[m+1] in Arr:
            Arr.append(solution[m+1])
        elif solution[m][0] != solution[m+1][0]:
            Arr.append(solution[m])
            Arr.append(solution[m+1])
    
    #display the solution aka all the items such that it meets the PriceLimit
    count=[0]*len(Arr)
    n=0
    p=0
    print('Strategy for price limit only')
    print('***********************************')
    while n<len(Arr) and p<len(solution):
        if solution[p][0]==Arr[n][0]:
            count[n]=count[n]+1
            p+=1
        else:
            n+=1
           
    
    for i in range(len(Arr)):
       print(count[i],' X ',Arr[i])

    print('Total Price of items sold: ',sum(pricing))       
    print('Total Items sold: ',sum(count))
    print('Total Profit: ',memo[PriceLimit])
            
    
    return solution


def MaximizeProfit2(pdtcode,price,profit,PriceLimit,ItemLimit):
    '''
    Task 2: Maximize Profit when there is both item limit and price limit
    this function determines the products to maximise the profit for a given price and item limit
    :param Input --> pdtcode Array, price Array, profit Array, ItemLimit and the PriceLimit
    :param Output --> the total price of the items, the total items sold and the profit generated (note: this profit has to be
                      the maximum profit for the given price and item limit)
    Worst case time complexity --> O(IPN) where I represents the I for-loop(time complexity:O(I)),
                                   P represents the P for-loop(time complexity:O(P)) and N represents the N for-loop(time complexity:O(N)).
                                   Since I for-loop, P for-loop and N for-loop are nested, therefore complexity is O(IPN)       
                                 
    Worst case space complexity--> O(IP+N) where memo array takes IP space because memo array is a two dimensional array
                                   and the price array takes N space.

    
    This is what I have done for this function such that it meets the pricelimit and itemlimit
    for eg. I create a two dimensional array(3 by 4) where the row represents the pricelimit and the column represents itemlimit and the x
    represents the profit for each pricelimit and itemlimit. For instance memo[1][2] whereby the 1 represents the itemlimit of 1 and 2 represents the
    pricelimit.
    
               0 1 2 3
             0 0 0 0 0
             1 0 x x x 
             2 0 x x x
    
    
    '''
    memo=[] #this is to keep track of the profits for each price till the priceLimit and itemlimit for eg at memo[1][2], it stores the maxProfit when the priceLimit is $2 and the itemLimit is 1
    decisions=[] #this will store the price and the product 
    pro_price=[0] #this is just a temperory array
    for i in range(ItemLimit+1): #creating a two dimensional array for memo and decisions
        node=[-1]*(PriceLimit+1)
        node1=[0]*(PriceLimit+1)
        memo.append(node)
        decisions.append(node1)
        node=[]
        node1=[]
    for i in range(len(memo)): #in the two dimensional memo array when either the row or column is 0 make the memo[i][j]=0
        for j in range(len(memo[i])):
            if i==0 or j==0:
                memo[i][j]=0
    
    for I in range(1,(ItemLimit+1)):
        for P in range(1,(PriceLimit+1)):
            maxProfit=0 #initialising maxProfit to 0
            for N in range(len(price)): #calculating maxProfit at the given PriceLimit(P) and ItemLimit(I)
                if int(price[N])<=P: #if the price of the item is greater than the PriceLimit, don't bother considering that item
                    thisProfit=int(profit[N])+memo[I-1][P-int(price[N])]  #calculating profit using bottom up solution
                    if thisProfit>maxProfit:#if the Profit calculated(thisProfit) is greater than the maxProfit at the given PriceLimit, maxProfit=thisProfit
                        maxProfit=thisProfit
                        pro_price=[pdtcode[N],price[N],profit[N]]
            memo[I][P]=maxProfit # assign the maxProfit to the memo[ItemLimit][PriceLimit]
            decisions[I][P]=pro_price #assign the product, price and profit to the decisions[ItemLimit][PriceLimit]
            pro_price=[0] #re-initialise pro_price
            
   #we have the profits for each PriceLimit and ItemLimit, now its time to list out all the items for that given PriceLimit and ItemLimit
    pricing=[]        
    solution=[]
    v=PriceLimit
    i=ItemLimit
    while i>0:
        solution.append(decisions[i][v])
        pricing.append(int(decisions[i][v][1]))
        v=v-int(decisions[i][v][1])
        i-=1
    
#this is to store all the unique items in the solution array into another array called tempArr 
    tempArr=[]
    
   
    for i in range(len(solution)):
        if solution[i] not in tempArr:
            tempArr.append(solution[i])
    
    #display the solution aka all the items such that it meets the Price and Item limit        
    count=[0]*len(tempArr)
    n=0
    p=0

    while n<len(tempArr):
        
        if solution[p][0]==tempArr[n][0]:
            count[n]=count[n]+1
        p+=1

        if p==len(solution):
            n+=1
            p=0

        
         
    print("Strategy for both item and price limit")
    print("***************************************")
    for i in range(len(tempArr)):
       print(count[i],' X ',tempArr[i])

    print('Total Price of items sold: ',sum(pricing))       
    print('Total Items sold: ',sum(count))
    print('Total Profit: ',memo[ItemLimit][PriceLimit])       

      




#main function


infile=open('products.txt')
Product=[]
node=[]

for line in infile:
    for element in line.replace('\n','').replace(':',',').replace(',',':').split(':'):
        node.append(element)

    Product.append(node)
    node=[]

price=[]
profit=[]
pdtcode=[]
for i in range(len(Product)):
    price.append(Product[i][2])
    profit.append(Product[i][3])
    pdtcode.append(Product[i][1])
PriceLimit=int(input('Enter the price limit '))
ItemLimit=int(input('Enter the item limit '))

sol=MaximizeProfit1(pdtcode,price,profit,PriceLimit)
print('\n')
sol1=MaximizeProfit2(pdtcode,price,profit,PriceLimit,ItemLimit)
