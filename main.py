import os
import humanize

def get_size(path):
    """Retorna o tamanho do arquivo ou diretório especificado."""
    if os.path.isfile(path):
        return os.path.getsize(path)
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def list_directory_sizes():
    """Lista os tamanhos de arquivos e diretórios no diretório atual."""
    current_directory = os.getcwd()
    items = os.listdir(current_directory)

    for item in items:
        item_path = os.path.join(current_directory, item)
        size = get_size(item_path)
        print(f"{item}: {humanize.naturalsize(size)}")

if __name__ == "__main__":
    list_directory_sizes()
    input("\nPressione Enter para sair...")  # Mantém o terminal aberto