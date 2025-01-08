def calculate_love_score(name1, name2):
    word1 = "true"
    word2 = "love"
    name = name1+name2
    #print(name)
    counter1 = 0
    counter2 = 0
    for i in word1:
        c1 = 0
        #print(i)
        for j in name:
            if i == j:
                c1 += 1
        counter1 += c1
        
    for k in word2:
        c2 = 0
        for l in name:
            if k == l:
                c2 += 1 
        counter2 += c2
    print(str(counter1) + str(counter2))
    
calculate_love_score(name1= "bharathi", name2="pravallika")