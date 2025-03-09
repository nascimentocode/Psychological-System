# 🧠 Gerenciador de Pacientes para Psicólogos

Um sistema web para psicólogos gerenciarem seus pacientes, registrarem consultas e acompanharem a evolução do humor dos pacientes ao longo do tempo.
Este projeto foi desenvolvido durante a imersão "4 Days 4 Projects - Edição 2" da Pythonando.

---

## 🚀 **Funcionalidades**

✅ **Cadastro de pacientes** – Psicólogos podem adicionar novos pacientes ao sistema.  
✅ **Registro de consultas** – Cada consulta é salva e fica associada ao paciente.  
✅ **Gravação e compartilhamento** – Cada consulta gera um link onde o paciente pode acessar detalhes e atividades recomendadas.  
✅ **Tarefas/Exercícios personalizados** – O psicólogo pode adicionar tarefas para o paciente realizar entre as consultas.  
✅ **Monitoramento do humor** – Cada consulta tem um campo para registrar o humor do paciente, e esses dados são exibidos em um gráfico geral.  

---

## 🛠 **Tecnologias Utilizadas**

- **Python**  
- **Django** (Framework Web)  
- **SQLite** (Banco de dados)  
- **Chart.js** (Geração de gráficos)  

---

## 📥 **Instalação e Execução**

1. **Clone o repositório:**  
   ```sh
   git clone https://github.com/nascimentocode/Psychological-System.git
   cd Psychological-System
   ```  
   Ou, se preferir clonar com chave SSH:
   ```sh
   git clone git@github.com:nascimentocode/Psychological-System.git
   cd Psychological-System
   ```
   
2. **Crie um ambiente virtual e ative:**  
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```  

3. **Instale as dependências:**  
   ```sh
   pip install -r requirements.txt
   ```  

4. **Execute as migrações do banco de dados:**  
   ```sh
   python manage.py migrate
   ```  

5. **Inicie o servidor localmente:**  
   ```sh
   python manage.py runserver
   ```  

6. Acesse no navegador:  
   ```
   http://127.0.0.1:8000/
   ```  
   
---

## 🏗 **Estrutura do Projeto**

```
Psychological-System/
├── core/
├── pacientes/
├── templates/
├── db.sqlite3  
└── manage.py
```

---

## 📝 **Licença**

Este projeto foi desenvolvido durante a imersão **"4 Days 4 Projects - Edição 2" da Pythonando** e está disponível apenas para fins de estudo.

---
