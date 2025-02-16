import os
import platform
import shutil
import tempfile
from unittest import mock
from zipped_archive import create_backup, get_backup_filename

def test_create_backup_windows(mocker):
    """Test the create_backup function on Windows."""
    mocker.patch("platform.system", return_value="Windows")
    mocker.patch("os.path.expanduser", return_value="C:\\Users\\user")
    mocker.patch("shutil.copytree")
    mocker.patch("shutil.make_archive")
    mocker.patch("tempfile.TemporaryDirectory", return_value=mock.MagicMock())
    mocker.patch("os.makedirs")
    mocker.patch("zipped_archive.get_backup_filename", return_value="backup_test.zip")

    backup_path = create_backup()

    # Normalize the paths to ensure consistent separators
    expected_backup_path = os.path.normpath("C:\\Users\\user\\Backups\\backup_test.zip")
    assert os.path.normpath(backup_path) == expected_backup_path


def test_create_backup_linux(mocker):
    """Test the create_backup function on Linux."""
    mocker.patch("platform.system", return_value="Linux")
    mocker.patch("os.path.expanduser", return_value="/home/user")
    mocker.patch("shutil.copytree")
    mocker.patch("shutil.make_archive")
    mocker.patch("tempfile.TemporaryDirectory", return_value=mock.MagicMock())
    mocker.patch("os.makedirs")
    mocker.patch("zipped_archive.get_backup_filename", return_value="backup_test.tar.gz")

    backup_path = create_backup()
    expected_backup_path = os.path.normpath("/home/user/Backups/backup_test.tar.gz")
    assert os.path.normpath(backup_path) == expected_backup_path

def test_create_backup_mac(mocker):
    """Test the create_backup function on MacOS."""
    mocker.patch("platform.system", return_value="Darwin")
    mocker.patch("os.path.expanduser", return_value="/Users/user")
    mocker.patch("shutil.copytree")
    mocker.patch("shutil.make_archive")
    mocker.patch("tempfile.TemporaryDirectory", return_value=mock.MagicMock())
    mocker.patch("os.makedirs")
    mocker.patch("zipped_archive.get_backup_filename", return_value="backup_test.tar.gz")

    backup_path = create_backup()
    expected_backup_path = os.path.normpath("/Users/user/Backups/backup_test.tar.gz")
    assert os.path.normpath(backup_path) == expected_backup_path