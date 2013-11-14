def fibonacci(number):
    l = [0]
    i = number
    prev_total = 0
    most_recent  = 1
    seq_track = 1
    total = 0
    print prev_total
    print ("The first item in the fibonacci sequence is 0.")
    while i > 1:
        total = prev_total + most_recent
        l.append(total)
        seq_track += 1
        if prev_total != 0:
            ratio = float(float(total) / float(prev_total))
            print ratio
        print total
        print l
        print ("The number {seq_track} item in the fibonacci sequence is {total}.".format(**vars()))
        most_recent = prev_total
        prev_total = total
        i -= 1


user = float(raw_input("Enter the number in the Fibonacci series you want me to return:"))

fibonacci(user)
