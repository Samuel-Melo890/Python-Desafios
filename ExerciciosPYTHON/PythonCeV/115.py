print('='*8,'Arquivos em Python','='*8)
from modulos import menu
from time import sleep

while True:
    try:
        menu.menu(['Cadastrar uma nova pessoa', 'Ver lista de pessoas cadastradas', 'Sair do Programa'])
        op = int(input('Escolha uma opção: '))
        print('Carregando...')
        sleep(2)
    except (ValueError, TypeError):
        print('\033[31mValores dados inválidos! Tente novamente!\033[m')
    except KeyboardInterrupt:
        print('\n\033[36mDados não fornecidos pelo usuário\033[m')
    else:
        if op == 1:
            while True:
                try:
                    menu.titulo('< Cadastro da Pessoa >')
                    arquivo = open('115py.txt', 'a')
                    n = str(input('Nome: ')).strip().title()
                    idade = int(input('Idade: '))
                    arquivo.write(f'{n:<15}{str(idade):>5} anos\n')
                    arquivo.close()
                    sleep(2)
                    print('\033[32mDados cadastrados com sucesso!\033[m')
                    sleep(1)
                    break
                except (ValueError, TypeError):
                    print('\033[31mDados relatados não são válidos!\033[m')
                except KeyboardInterrupt:
                    print('\033[36mUsuário não relatou os dados necessários!\033[m')
        elif op == 2:
            try:
                menu.titulo('< Pessoas Cadastradas >')
                arquivo = open('115py.txt', 'r')
                for l in arquivo:
                    print(f'{l}'.replace('\n', ''))
                arquivo.close()
                sleep(2)
            except FileNotFoundError:
                print('\033[1mArquivo de cadastro não encontrado!\033[m')
        elif op == 3:
            menu.titulo('Saindo do Sistema...')
            sleep(2)
            break
        else:
            print('\033[31mOpção Inválida! Tente de novo!\033[m')
print('\033[1;34mPrograma Finalizado!\033[m')
