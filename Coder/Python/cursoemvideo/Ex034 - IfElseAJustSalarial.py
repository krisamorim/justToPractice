sal = float(input('Qual seu salário?\nR$'))
aumentoMaiorSal = 0.1
aumentoMenorSal = 0.15
if sal >=1.200:
    print('Seu salário é de R${:.3f} por isso você tem direito a R${:.3f} de aumento.\nSeu novo salário é de R${:.3f}'.format(sal,sal*aumentoMaiorSal,(sal*aumentoMaiorSal)+sal))
else:
    print('Seu salário é de R${:.3f} por isso você tem direito a R${:.3f} de aumento.\nSeu novo salário é de R${:.3f}'.format(sal,sal*aumentoMenorSal,(sal*aumentoMenorSal)+sal))