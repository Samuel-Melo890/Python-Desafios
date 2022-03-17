print('='*8,'Analisando e Gerando Dicionários','='*8)
def notas(* n, sit=False):
    """Realiza a análise de notas e situaçao de vários alunos.

    Args:
        n (float): Uma ou mais notas de alunos (aceita várias).
        sit (bool, optional): Mostrar ou nao a situaçao da turma. Defaults to False.

    Returns:
        dict: Dicionário com os dados da turma.
    """
    dnotas = {}
    dnotas['Quantidade de notas'] = len(n)
    dnotas['Maior nota'] = max(n)
    dnotas['Menor nota'] = min(n)
    dnotas['Média da Turma'] = sum(n) / len(n)
    if sit == True:
        if dnotas['Média da Turma'] <= 5:
            dnotas['Situação'] = 'Reprovada'
        elif 5 < dnotas['Média da Turma'] < 7:
            dnotas['Situação'] = 'Recuperação'
        else:
            dnotas['Situação'] = 'Aprovada'
    return dnotas


resp = notas(5, 6, 7, 2, 10, 10, 3, 9, 8, 8, sit = True)
print(resp)
