import os
import shutil
import platform
import tempfile
from datetime import datetime

def get_backup_filename():
    """Génère un nom de fichier basé sur la date et l'OS."""
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if platform.system() == "Windows":
        return f"backup_{date_str}.zip"
    else:
        return f"backup_{date_str}.tar.gz"

def create_backup():
    """Crée une archive compressée du répertoire personnel de l'utilisateur en excluant certains fichiers."""
    home_dir = os.path.expanduser("~")
    backup_filename = get_backup_filename()
    backup_path = os.path.join(home_dir, "Backups", backup_filename)
    os.makedirs(os.path.dirname(backup_path), exist_ok=True)

    exclusions = {"NTUSER.DAT", "NTUSER.DAT.LOG1", "NTUSER.DAT.LOG2", "AppData"}

    def ignore_files(dir, files):
        return [f for f in files if f in exclusions]

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_backup_path = os.path.join(temp_dir, "backup")
        shutil.copytree(home_dir, temp_backup_path, ignore=ignore_files, dirs_exist_ok=True)

        if platform.system() == "Windows":
            shutil.make_archive(backup_path[:-4], 'zip', temp_backup_path)
        else:
            shutil.make_archive(backup_path[:-7], 'gztar', temp_backup_path)

    return backup_path

if __name__ == "__main__":
    backup_file = create_backup()
    print(f"Sauvegarde créée : {backup_file}")