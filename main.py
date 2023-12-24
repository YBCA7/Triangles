from math import sqrt, acos, pi
a = float(input('Please enter the edge a: '))
b = float(input('Please enter the edge b: '))
c = float(input('Please enter the edge c: '))
if a+b > c and a+c > b and b+c > a:
    print('\nThis is really a triangle!\n')
    p = (a+b+c)/2
    cosA = (b*b+c*c-a*a)/(2*b*c)
    cosB = (a*a+c*c-b*b)/(2*a*c)
    cosC = (a*a+b*b-c*c)/(2*a*b)
    A = float(acos(cosA)*180/pi)
    B = float(acos(cosB)*180/pi)
    C = float(acos(cosC)*180/pi)
    print('C = %f.' % float(2*p))
    print('S = %f.\n' % sqrt(p*(p-a)*(p-b)*(p-c)))
    print('cosA = %f.' % cosA)
    print('cosB = %f.' % cosB)
    print('cosC = %f.\n' % cosC)
    print('∠A = %f°.' % A)
    print('∠B = %f°.' % B)
    print('∠C = %f°.' % C)
else:
    print('This is not really a triangle.')
input()
