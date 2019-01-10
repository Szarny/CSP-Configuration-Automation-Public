from .Pycolor import pycolor

def prompt_format(color, mark, message):
    """
    カラーの記号付きメッセージをを出力する．

    Parameters
    ----------
    color : Pycolor
        記号色
    mark : str
        記号
    message : str
        出力メッセージ
    """

    return "[" + color + mark + pycolor.END + "]" + " " + message