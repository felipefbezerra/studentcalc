import tkinter as tk
from tkinter import messagebox

def calculate_average(notas):
    return (notas[0] + notas[1]) / 2

def calcular():
    try:
        num_alunos = int(entry_num_alunos.get())
        
        if num_alunos < 2 or num_alunos > 7:
            messagebox.showerror("Erro", "Informe um valor entre 2 e 7 para a quantidade de alunos.")
            return
        
        turma = []
        
        for i in range(num_alunos):
            nome = entry_nomes[i].get()
            nota1 = float(entry_notas1[i].get())
            nota2 = float(entry_notas2[i].get())
            
            if not (0 <= nota1 <= 10) or not (0 <= nota2 <= 10):
                messagebox.showerror("Erro", "As notas devem estar entre 0,0 e 10,0.")
                return
            
            turma.append({"nome": nome, "notas": [nota1, nota2]})
        
        for aluno in turma:
            aluno["media"] = calculate_average(aluno["notas"])
        
        media_turma = sum(aluno["media"] for aluno in turma) / num_alunos
        aluno_maior_media = max(turma, key=lambda x: x["media"])
        aluno_menor_media = min(turma, key=lambda x: x["media"])
        
        resultado = (
            f"A média da turma é: {media_turma:.2f}\n"
            f"O aluno com maior média foi {aluno_maior_media['nome']} com {aluno_maior_media['media']:.2f}\n"
            f"O aluno com menor média foi {aluno_menor_media['nome']} com {aluno_menor_media['media']:.2f}"
        )
        messagebox.showinfo("Resultado", resultado)
    
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos.")

janela = tk.Tk()
janela.title("Cálculo de Média de Alunos")

tk.Label(janela, text="Informe a quantidade de alunos (entre 2 e 7):").grid(row=0, column=0)
entry_num_alunos = tk.Entry(janela)
entry_num_alunos.grid(row=0, column=1)

entry_nomes = []
entry_notas1 = []
entry_notas2 = []

def criar_campos():
    for widget in janela.winfo_children()[2:]:
        widget.destroy()

    try:
        num_alunos = int(entry_num_alunos.get())
        if num_alunos < 2 or num_alunos > 7:
            messagebox.showerror("Erro", "Informe um valor entre 2 e 7 para a quantidade de alunos.")
            return
        
        for i in range(num_alunos):
            tk.Label(janela, text=f"Nome do aluno {i + 1}:").grid(row=i + 1, column=0)
            nome_entry = tk.Entry(janela)
            nome_entry.grid(row=i + 1, column=1)
            entry_nomes.append(nome_entry)
            
            tk.Label(janela, text=f"Nota 1 do aluno {i + 1}:").grid(row=i + 1, column=2)
            nota1_entry = tk.Entry(janela)
            nota1_entry.grid(row=i + 1, column=3)
            entry_notas1.append(nota1_entry)
            
            tk.Label(janela, text=f"Nota 2 do aluno {i + 1}:").grid(row=i + 1, column=4)
            nota2_entry = tk.Entry(janela)
            nota2_entry.grid(row=i + 1, column=5)
            entry_notas2.append(nota2_entry)
        
        tk.Button(janela, text="Calcular Média", command=calcular).grid(row=num_alunos + 1, column=0, columnspan=6)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido de alunos.")

tk.Button(janela, text="Criar Campos", command=criar_campos).grid(row=1, column=0, columnspan=2)

janela.mainloop()
