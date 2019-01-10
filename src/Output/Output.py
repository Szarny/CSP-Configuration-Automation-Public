from .Pycolor import pycolor
from .PromptFormat import prompt_format


def info(message):
    """
    予備情報を出力する．

    Parameters
    ----------
    message : str
        出力メッセージ
    """

    print(prompt_format(pycolor.GREEN, "*", message))


def ask(message):
    """
    入力プロンプトを返却する．

    Parameters
    ----------
    message : str
        出力メッセージ

    Returns
    ----------
    input : str
        入力プロンプト
    """

    return input(prompt_format(pycolor.GREEN, "?", message))


def add(message):
    """
    ファイル追加情報等を出力する．

    Parameters
    ----------
    message : str
        出力メッセージ
    """

    print(prompt_format(pycolor.BLUE, "+", message))


def warn(message):
    """
    警告情報を出力する．

    Parameters
    ----------
    message : str
        出力メッセージ
    """

    print(prompt_format(pycolor.PURPLE, "-", message))


def error(message):
    """
    エラー情報を出力する．

    Parameters
    ----------
    message : str
        出力メッセージ
    """

    print(prompt_format(pycolor.RED, "!", message))
    print(prompt_format(pycolor.RED, "!", "System terminated"))