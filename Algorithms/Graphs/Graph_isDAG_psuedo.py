def isDAG(v):
    status[v] = ACTIVE
    for edges v->w:
        if status[w] == ACTIVE:
            return False
        elif status[w] == NEW:
            if isDAG(w) == False:
                return False
    status[v] = DONE
    return True
    
