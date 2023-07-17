# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# * При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# * Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extension>
from pathlib import Path


def rename_files(up_name, ext, up_ext):
    files_rename = [f for f in Path(Path().cwd()).iterdir() if f.suffix == f'.{ext}']
    for i, file in enumerate(files_rename, start=1):
        file.rename(f'{file.stem}_{up_name}_{i}.{up_ext}')

