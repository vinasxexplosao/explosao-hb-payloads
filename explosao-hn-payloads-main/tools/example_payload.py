import platform

def run():
    return f"Sistema: {platform.system()} | Versão: {platform.version()}"

if __name__ == '__main__':
    print(run())
