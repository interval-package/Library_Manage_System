from PyQt5 import QtWidgets


def UserReaction_GetDir(Filepath=None):
    directory = QtWidgets.QFileDialog. \
        getExistingDirectory(None, "Choose the folder", "C:/")  # 起始路径
    return directory

