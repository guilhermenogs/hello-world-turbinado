nome = input("Qual é o seu nome? ")
idade = int(input("Quantos anos você tem? "))

print(f"\nPrazer, {nome}!")
print(f"Você já viveu aproximadamente {idade * 365} dias.\n")

if idade < 18:
    {
        print("Bora curtir também, mas com responsabilidade!\n\n")
    }

else:
    {
        print("Você é maior de idade. Bora curtir!\n")
    }