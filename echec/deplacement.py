def ok( i, j ):
	return i>= 0 and i < 8 and j>=0 and j <8
	
def cases_fou(col,lig):
	res=[]
	for t in range(1,8) :
		i = lig + t
		j = col + t 
		if ok(i,j):
			res.append((j,i))   
	for t in range(1,8) :
		i = lig + t
		j = col - t 
		if ok(i,j):
			res.append((j,i))
	for t in range(1,8) :
		i = lig - t
		j = col - t 
		if ok(i,j):
			res.append((j,i))
	for t in range(1,8) :
		i = lig - t
		j = col + t 
		if ok(i,j):
			res.append((j,i))
	return res

def cases_tour(col,lig):

    res = []
    for j in range(col+1,8):
    	res += [(j,lig)]
    for i in range(lig+1,8):
    	res += [(col, i)]
    for i in range(lig-1,-1,-1):
    	res += [(col,i)]
    for j in range(col-1,-1,-1):
    	res += [(j, lig)] 
    
    return res

    return res

def cases_roi(col,lig):

    return cases_fou(col,lig) + cases_tour(col,lig)

def cases_reine(col,lig):

    roi=[]
    if lig-1>=0:
        roi.append((col,lig-1))
    if lig+1<8:
        roi.append((col,lig+1))
    if col-1>=0:
        roi.append((col-1,lig))
    if col+1<8:
        roi.append((col+1,lig))
    if lig-1>=0 and col-1>=0:
        roi.append((col-1, lig-1))
    if lig-1>=0 and col+1<8:
        roi.append((col+1,lig-1))
    if lig+1<8 and col-1>=0:
        roi.append((col-1,lig+1))
    if lig+1<8 and col+1<8:
        roi.append((col+1, lig+1))
    
    return roi

def cases_cavalier(col,lig):
    res =[]
    for i,j in [(col+1,lig+2), (col+1,lig-2), (col-1,lig+2), (col-1, lig-2), (col+2,lig+1), (col+2,lig-1), (col-2,lig+1),(col-2,lig-1)]:
        if 0<=i<8 and 0 <= j<8:
            res.append((i,j))
    return res
        
    return []

def cases_pion(col,lig):
    res=[]
    if lig<6 and lig!=0:
        res+= [(col,lig-1)]
    elif lig==6:
        res+=[(col,lig-1),(col,lig-2)]
    
    return res
  
