import os

def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_amount(prompt):
    while True:
        amount = input(prompt)
        try:
            amount = int(amount)
            return amount
        except ValueError:
            print("Неправильный ввод. Пожалуйста, введите целое число.")

def calculate_commission(amount):
    commission = amount * 0.015
    commission = max(commission, 30)  # Минимальная комиссия 30
    commission = min(commission, 600)  # Максимальная комиссия 600
    return commission

def apply_tax(amount):
    return amount * 0.9

def deposit_funds(balance, transaction_count):
    console_clear()
    deposit = input_amount("Введите сумму для пополнения: ")
    if deposit % 50 == 0:
        transaction_count += 1
        if transaction_count % 3 == 0:
            commission = balance * 0.03  # Комиссия 3% при каждой третей операции
            balance += deposit - commission
        else:
            balance += deposit
            commission = 0
        
        transactions.append(("Внесение наличных", deposit, commission))  # Добавление транзкции в список
        print("Пополнение прошло успешно.")
        print(f"Комиссия составляет: {commission} у.е.")
    else:
        print("Сумма пополнения должна быть кратной 50.")
    return balance, transaction_count

def withdraw_funds(balance, transaction_count):
    console_clear()
    if balance == 0:
        print("На счете нет средств. Снятие недоступно.")
        return balance, transaction_count

    withdrawal = input_amount("Введите сумму для снятия: ")
    
    if withdrawal % 50 != 0:
        print("Сумма снятия должна быть кратной 50.")
        return balance, transaction_count

    if balance < withdrawal:
        print("Недостаточно средств на счете.")
        return balance, transaction_count

    transaction_count += 1
    if transaction_count % 3 == 0:
        commission = calculate_commission(withdrawal * 0.97)  # Комиссия 3% при каждой третьей операции
    else:
        commission = calculate_commission(withdrawal)

    total_amount = withdrawal + commission
    if balance - total_amount > 5000000: #налог на богатство
        total_amount = apply_tax(total_amount)

    if balance - total_amount >= 0:
        balance -= total_amount
        transactions.append(("Снятие наличных", withdrawal, commission))  # Добавление транзакции в список
        print("Снятие прошло успешно.")
        print(f"Комиссия составляет: {commission} у.е.")
    else:
        print("Недостаточно средств на счете.")

    return balance, transaction_count


def display_transaction_history():
    console_clear()
    if len(transactions) == 0:
        print("Нет операций.")
    else:
        print("История операций:")
        for operation, amount, commission in transactions:
            print(f"{operation.capitalize()}: {amount} у.е. (Комиссия: {commission} у.е.)")

transactions = [] 

def atm():
    balance = 0
    transaction_count = 0

    while True:
        console_clear()
        print(f"Сумма денег на счете: {balance} у.е.")
        print("Выберите действие:")
        print("1. Пополнить")
        print("2. Снять")
        print("3. История операций")
        print("4. Выйти")

        action = input("Введите номер действия: ")
        match action:
            case "1":
                balance, transaction_count = deposit_funds(balance, transaction_count)
            case "2":
                balance, transaction_count = withdraw_funds(balance, transaction_count)
            case "3":
                display_transaction_history()
            case "4":
                print("Работа с банкоматом завершена.")
                break
            case _:
                print("Неверный номер действия. Пожалуйста, повторите попытку.")

        if balance >= 5000000:
            balance = apply_tax(balance)
        
        print()
        input("Нажмите Enter для продолжения...")

    display_transaction_history()

atm()
