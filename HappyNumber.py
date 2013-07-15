def HappyNumber(number):
    s = str(number)
    total = 0
    i = 0
    print number
    for each in s:
        a = int(each)
        total = total + (a**2)
    print total
    if total != 1:
        while i < 20:
            print "Not sure yet if this is a Happy Number."
            print "Recalculating"
            i += 1
            a = total
            for each in str(total):
                b = int(each)
                total = total + (b**2)
            total = total - a
            print total
            if total == 1:
                print "This is a Happy Number!"
                break
            if i == 20:
                print "This is an Unhappy Number!"
                break
    else:
        print "This is indeed a Happy Number!"

print HappyNumber(11)