import pytest
import platform
from zipped_archive import get_backup_filename, create_backup

def test_get_backup_filename_windows(mocker):
    """Teste le nom de fichier sous Windows."""
    mocker.patch("platform.system", return_value="Windows")
    filename = get_backup_filename()
    assert filename.startswith("backup_")
    assert filename.endswith(".zip")

def test_get_backup_filename_linux(mocker):
    """Teste le nom de fichier sous Linux."""
    mocker.patch("platform.system", return_value="Linux")
    filename = get_backup_filename()
    assert filename.startswith("backup_")
    assert filename.endswith(".tar.gz")

def test_get_backup_filename_mac(mocker):
    """Teste le nom de fichier sous MacOS."""
    mocker.patch("platform.system", return_value="Darwin")
    filename = get_backup_filename()
    assert filename.startswith("backup_")
    assert filename.endswith(".tar.gz")

