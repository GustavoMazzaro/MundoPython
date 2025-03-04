from datetime import datetime

hoje = datetime.today()

nascimento = input('Digite a sua data de nascimento no formato ( dd/mm/yyyy): ')

nascimento_datetime = datetime.strptime(nascimento, '%d/%m/%Y')

diferenca = hoje - nascimento_datetime

idade = diferenca.days // 365

print(f"Sua idade é {idade} anos.")
