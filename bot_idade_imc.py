import pyautogui

#Pergunta a Idade
idade = pyautogui.prompt("Digite sua Idade: ")

#Converte a entrada para número inteiro
idade = int(idade)

if idade<18:
    pyautogui.alert("Você é menor!")
else:
    pyautogui.alert("Você é maior. Vamos calcular seu IMC.")

    #Perguta Peso e Altura
    peso = pyautogui.prompt("Digite seu peso em kg: ")
    altura = pyautogui.prompt("Digite sua altura em metros: ")

    #Converter os valores para float
    peso = float(peso)
    altura = float(altura)

    #Calcula o IMC
    imc = peso /(altura*altura)

    #Avalia o IMC e exibe a Classificação
    if imc < 18.5:
        pyautogui.alert(f"Seu IMC é {imc :. 2f}. Classificação: Baixo")
    elif 25.0 <= imc <= 29.9:
        pyautogui.alert(f"Seu IMC é {imc :. 2f}. Classificação: Médio")
    elif 30.0 <= imc <= 34.9:
        pyautogui.alert(f"Seu IMC é {imc :. 2f}. Classificação: Moderado")
    elif 35.0 <= imc <= 39.9:
        pyautogui.alert(f"Seu IMC é {imc :. 2f}. Classificação: Grava")
    elif imc >= 40.0:
        pyautogui.alert(f"Seu IMC é {imc :. 2f}. Classificação: Muito Grave")
    else:
        pyautogui.alert(f"Seu IMC é {imc :. 2f}. Classificação: Normal")
