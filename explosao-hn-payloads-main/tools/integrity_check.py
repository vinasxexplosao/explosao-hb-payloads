import hashlib
import os

def check_integrity():
    print("Verificando integridade dos payloads...")
    
    required_dirs = ['payloads', 'docs', 'tools', 'config']
    for folder in required_dirs:
        if os.path.exists(folder):
            print(f"[OK] {folder}/ encontrado.")
        else:
            print(f"[ERRO] {folder}/ faltando!")
    
    print("\nHashes SHA-256 dos arquivos em /payloads:")
    if os.path.exists('payloads'):
        for f in os.listdir('payloads'):
            path = os.path.join('payloads', f)
            if os.path.isfile(path):
                with open(path, 'rb') as file:
                    h = hashlib.sha256(file.read()).hexdigest()
                    print(f"  {f}: {h}")

if __name__ == '__main__':
    check_integrity()
