import os

XXS_KEYWORDS = ['innerHTML', 'document.cookie', 'document.write']

def detect(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()

        for line_number, line in enumerate(lines, start=1):
            for keyword in XXS_KEYWORDS:
                if keyword in line:
                    print(f"VULNERABILIDADE ENCONTRADA. Linha:{line_number} - Texto:{line}")


if __name__ == '__main__':
    file = 'index.html'
    detect(file)
