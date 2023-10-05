import os
import subprocess

# Obtém o nome de usuário do sistema operacional
user = os.getlogin()

# Define as rotas com base no nome de usuário
home_route = f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\Python311"
base_route = f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\Python311"

# Define o caminho completo para o arquivo pyvenv.cfg no diretório .venv
pyvenv_cfg_path = os.path.join(".venv", "pyvenv.cfg")

# Cria o conteúdo do arquivo pyvenv.cfg com as rotas ajustadas
pyvenv_cfg_content = f"""\
home = {home_route}
implementation = CPython
version_info = 3.11.1.final.0
virtualenv = 20.17.1
include-system-site-packages = false
base-prefix = {base_route}
base-exec-prefix = {base_route}
base-executable = {os.path.join(base_route, 'python.exe')}
"""

# Escreve o conteúdo no arquivo pyvenv.cfg no diretório .venv
with open(pyvenv_cfg_path, "w") as f:
    f.write(pyvenv_cfg_content)

# Ativar o ambiente virtual no mesmo diretório
activate_script = os.path.join(".venv", "Scripts", "activate_this.py")
exec(open(activate_script).read(), dict(__file__=activate_script))

print("Arquivo pyvenv.cfg gerado com sucesso no diretório .venv e ambiente virtual ativado.")
