score=[]
for i in range(5):
    x= [int(x) for x in input("Enter_Score :").split()]
    print(x)
    Sum_score=sum(x)
    print(Sum_score)
    score.append(Sum_score)
print(score.index(max(score))+1,max(score))


