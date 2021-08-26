def main():
    # Escribe tu código abajo de esta línea
    func3()
def func1():
    print('proceso 1:')
    horas=float(input('Introduce las horas: '))
    minut=float(input('Introduce las minutos: '))
    segent=float(input('Introduce las segundos: '))
    seg=(horas*3600)+(minut*60)+segent
    return(seg)
    
def func2():
    print('proceso 2:')
    horas=float(input('Introduce las horas: '))
    minut=float(input('Introduce las minutos: '))
    segent=float(input('Introduce las segundos: '))
    seg=(horas*3600)+(minut*60)+segent
    return(seg)

def func3():
    b1=func1()
    b2=func2()
    print('proceso 1:' ,int(b1))
    print('proceso 2:' ,int(b2))



if __name__ == '__main__':
    main()
