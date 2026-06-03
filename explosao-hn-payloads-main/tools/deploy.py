import os

def deploy():
    dirs = ['config', 'tools', 'payloads', 'docs']
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print("Estrutura de diretórios criada com sucesso!")

if __name__ == '__main__':
    deploy()
