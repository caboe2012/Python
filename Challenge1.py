my_dict = { 
	
	'A':'C', 'B':'D', 'C':'E', 'D':'F', 'E':'G', 'F':'H', 'G':'I', 'H':'J', 'I':'K', 'J':'L', 'K':'M', 'L':'N', 'M':'O', 'N':'P', 
	'O':'Q', 'P':'R', 'Q':'S', 'R':'T' , 'S':'U', 'T':'V', 'U':'W', 'V':'X', 'W':'Y', 'X':'Z' , 'Y':'A' , 'Z':'B', " ": " ", ".": ".",
	'(':'(', ')':')', "'": "'"
}

def dictionary(text):
	l = []
	b = text.upper()
	for each in b:
		l.append(my_dict[each])
	c = "".join(l)
	d = c.lower()
	print d

#dictionary('g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq gq pcamkkclbcb. lmu ynnjw ml rfc spj')

dictionary("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
dictionary("map")