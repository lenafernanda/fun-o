---

### 🐶 **Projeto: Cadastro de Pet no Petshop Virtual**

#### 🎯 Objetivo didático:

Explorar e fixar os **tipos de dados básicos em Python**:

* `str` (texto)
* `int` (inteiro)
* `float` (decimal)
* `bool` (booleano)

---

### 🧠 Conceito lúdico:

A aluna vai **criar um sistema simples de cadastro de pets**, onde o usuário preenche os dados do animal de estimação e o sistema responde com uma ficha completa, destacando o **tipo de dado** de cada informação.

---

### 📄 Código Base (didático e comentado):

```python
print("🐾 Bem-vindo ao Petshop Virtual! 🐾")
print("Vamos cadastrar um novo pet!\n")

# Coletando dados
nome = input("Digite o nome do pet: ")         # tipo str
idade = int(input("Digite a idade do pet: "))  # tipo int
peso = float(input("Digite o peso (kg): "))    # tipo float
vacinado = input("O pet está vacinado? (s/n): ").lower() == "s"  # tipo bool

# Mostrando a ficha do pet
print("\n📋 Ficha do Pet:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")
print(f"Vacinado: {vacinado}")

# Mensagem final
if vacinado:
    print("✅ Este pet está vacinado! Pronto para passear!")
else:
    print("⚠️ O pet precisa ser vacinado antes de sair!")
```

---

### ✨ Pontos de destaque da Aula:

* Uso do `input()` para coletar dados de usuário&#x20;
* Conversão de dado para númro inteiro `int()`.
* Conversão de dado para número decimal` float()`.
* Explicação de `True/False` usando expressões booleanas.
* Como `str`, `int`, `float` e `bool` se comportam.
* Fluxo de decisão com `if`.
