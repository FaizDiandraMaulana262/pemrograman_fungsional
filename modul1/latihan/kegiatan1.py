def plus(bilangan_pertaman, bilangan_kedua):
    return bilangan_pertaman + bilangan_kedua

def minus(bilangan_pertaman, bilangan_kedua):
    return bilangan_pertaman - bilangan_kedua

def multi(bilangan_pertaman, bilangan_kedua):
    return bilangan_pertaman * bilangan_kedua

def dev(bilangan_pertaman, bilangan_kedua):
    return bilangan_pertaman // bilangan_kedua

def tree(node):
    if type(node) in (int, float):
        return(node)
    else :
        operator = ""
        tmpRes = []
        for i in range(len(node)) : 
            print()
            if (len(node[i]) == 1):
                operator = node[i][0]
            else:
                if node[i][0] == '+':
                    tmpRes.append(plus(tree(node[i][1]), tree(node[i][2]))) 
                elif node[i][0] == '-':
                    tmpRes.append(minus(tree(node[i][1]), tree(node[i][2]))) 
                elif node[i][0] == '/':
                    tmpRes.append(dev(tree(node[i][1]), tree(node[i][2]))) 
                elif node[i][0] == '*':
                    tmpRes.append(multi(tree(node[i][1]), tree(node[i][2]))) 

        return eval(str(tmpRes[0]) +operator+str(tmpRes[1]))
        
expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))
result = tree(expression_tree)

print(result)    