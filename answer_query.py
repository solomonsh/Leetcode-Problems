def answerQueries(queries,n):
    inital_array = [False]*n
    result = []
    
    for query in enumerate(queries):
        if query[0] == 1:
            inital_array[query[1]-1] =  True
        elif query[0] == 2:
         
            if True in inital_array[query[1]-1:]:
                result.append(len(inital_array[0:query[1]-1]) + inital_array[query[1]-1:].index(True)+1)
            else:
                result.append(-1)


    return result


print(answerQueries([[2,3],[1,2],[2,1],[2,3],[2,2],[1,3],[2,3],[2,1]],5)==[-1, 2, -1, 2, 3, 2]) 

print(answerQueries([[1,2],[1,4],[2,1],[2,2],[2,3],[2,4]],5)==[2,2,4,4]) 

