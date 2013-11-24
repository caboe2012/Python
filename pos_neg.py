def pos_neg_Chad(a,b,negative):
	if a<0 and b<0 and negative==True:
		return True
	elif (a*b)<0 and negative==False:
		return True
	else:
		False
