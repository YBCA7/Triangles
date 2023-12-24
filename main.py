from math import sqrt, acos, pi, sin, tan
a = float(input('Please enter the edge a: '))
b = float(input('Please enter the edge b: '))
c = float(input('Please enter the edge c: '))
if a+b > c and a+c > b and b+c > a:
    print('\nThis is really a triangle!\n')
    
    p = (a+b+c)/2
    cosA = (b*b+c*c-a*a)/(2*b*c)
    cosB = (a*a+c*c-b*b)/(2*a*c)
    cosC = (a*a+b*b-c*c)/(2*a*b)
    radA = acos(cosA)
    radB = acos(cosB)
    radC = acos(cosC)
    degA = float(radA*180/pi)
    degB = float(radB*180/pi)
    degC = float(radC*180/pi)
    
    print('C = %f.' % float(2*p))
    print('S = %f.\n' % sqrt(p*(p-a)*(p-b)*(p-c)))

    print('∠A = %f°.' % degA)
    print('∠B = %f°.' % degB)
    print('∠C = %f°.\n' % degC)

    print('sinA = %f.' % sin(radA))
    print('sinB = %f.' % sin(radB))
    print('sinC = %f.' % sin(radC))
    print('cosA = %f.' % cosA)
    print('cosB = %f.' % cosB)
    print('cosC = %f.' % cosC)
    print('tanA = %f.' % tan(radA))
    print('tanB = %f.' % tan(radB))
    print('tanC = %f.' % tan(radC))
else:
    print('This is not really a triangle.')
input()
