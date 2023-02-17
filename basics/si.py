# si = p * r * t / 100
p = int(input('Principal: '))
r = float(input('Rate of interest: '))
t = int(input('Time: '))
si = p * r * t / 100
print("Simple Interest calc")
print(f'{p=}')
print(f'{r=}')
print(f'{t=}')
print(f'Simple interest: {si}')