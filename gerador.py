#!/usr/bin/env python3

# importações
import PySimpleGUI as sg
from random import choice

sg.theme('DarkTeal1') # tema de cores

# layout do programa
layout = [
	[sg.Checkbox('ABCDE', default=True, key = 'test'), sg.Checkbox('abcde', key = 'test1'), sg.Checkbox('12345', key = 'test2'), sg.Checkbox('!@#$%', key = 'test3')],
	[sg.Combo(values=list(range(21)), key = 'qntd', default_value = 8, size=(3, 1))],
	[sg.Button('Gerar Senha')],
	[sg.Output(size=(30, 5))],
	[sg.Button('Exit')]
		]

# janela do programa
window = sg.Window('Gerador de senhas', layout)


# loop de funções do programa
while True:

	event, values = window.read()

	if event == sg.WINDOW_CLOSED or event == 'Exit':
		break
	if event == 'Gerar Senha':

		# listas de caracteres
		todos = []

		#listas de condições
		mai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
			'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
		min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
		 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
		sim = ['!', '@', '#', '$', '%', '&',
		 '¨', '*', '(', ')', '-', '_']

		if values['test'] == True or values['test1'] == True or values['test2'] == True or values['test3'] == True:

			if values['test'] == True:
				for a in mai:
					todos.append(a)
			if values['test1'] == True:
				for b in min:
					todos.append(b)
			if values['test2'] == True:
				for c in num:
					todos.append(c)
			if values['test3'] == True:
				for d in sim:
					todos.append(d)

			# código que printa a senha
			lista = []
			k = values['qntd']
			k = int(k)
			for i in range(k):
				a = choice(todos)
				lista.append(a)
			for n in lista:
				print(f'{n}', end='')
			print('')
			print('----------------------------------------------------')

		else:
			print('null - selecione um box')
			print('----------------------------------------------------')



window.close()
