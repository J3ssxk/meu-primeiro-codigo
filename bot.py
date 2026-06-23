print("Olá, Mundo!")
bot_name = "Cobrita"
print(f"Meu nome é {bot_name}")
adm_name = "Jéssica"
print(f"O nome da minha criadora é {adm_name}")
print(f"Este é o primeiro código em Python da {adm_name}")
user_name = input("Qual é o seu nome?: ")
print(f"Muito prazer em te conhecer, {user_name}!")
user_age = int(input("E qual sua idade?: "))
if user_age >= 18:
  print("Você é maior de idade)
else:
  print("Você é menor de idade")
bot_age = 1
print(f"Uau, vc tem {user_age} anos! Eu tenho apenas {bot_age} ano!")
age_difference = user_age - bot_age
print(f"Nossa diferença de idade é de {age_difference} anos!")
verification_age = input(f"{user_name}, vc é maior de idade? (sim/não): ")
if user_age and verification_age == 18 and verification_age == "sim":
    print(f"Que bom, {user_name}, obrigada por falar a verdade!")
elif user_age and verification_age != 18 and verification_age =="sim":
    print("Não minta")
else: print(f"Que bom, {user_name}, obrigada por falar a verdade!")
