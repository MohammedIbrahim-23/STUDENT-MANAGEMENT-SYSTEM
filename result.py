def results(m1, m2, m3, m4, m5):
    sums = m1 + m2 + m3 + m4 + m5
    if 450 < sums <= 500:
        return 'A'
    elif 400 < sums <= 450:
        return 'B'
    elif 350 < sums <= 400:
        return 'C'
    elif 300 < sums <= 350:
        return 'D'
    elif 250 < sums <= 300:
        return 'E'
    else:
        return 'FAIL'


m1 = int(input("Enter M1 :"))
m2 = int(input("Enter M2 :"))
m3 = int(input("Enter M3 :"))
m4 = int(input("Enter M4 :"))
m5 = int(input("Enter M5 :"))
results(m1, m2, m3, m4, m5)
