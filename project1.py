#Это игра камень ножницы бумуга на python
import random

print('Введите: Камень, Ножницы или Бумага ')

player = input('Введите имя: ')

game = ['Камень', 'Ножницы', 'Бумага']

player1 = input(player + " : ")
player2 = random.choice(game)

print('Бот: ' + player2)

#операции с камнем
if player1 == 'Камень' and player2 == 'Камень':
     print("Ничья")
elif player1 == 'Камень' and player2 == 'Ножницы':
     print(player  + ' победил')
elif player1 == 'Камень' and player2 == 'Бумага':
     print("Бот победил")
#операции с ножницами
elif player1 == 'Ножницы' and player2 == 'Камень':
     print("Бот победил")
elif player1 == 'Ножницы' and player2 == 'Ножницы':
     print("Ничья")
elif player1 == 'Ножницы' and player2 == 'Бумага':
     print(player + " победил")
#операции с бумагой
elif player1 == 'Бумага' and player2 == 'Камень':
     print(player + ' победил')
elif player1 == 'Бумага' and player2 == 'Ножницы':
     print("Бот победил")
elif player1 == 'Бумага' and player2 == 'Бумага':
     print("Ничья")
else:
     print("Введите название кости правильно!")
