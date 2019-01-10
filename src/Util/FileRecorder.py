import datetime

def record(filename, contents):
    """
    ファイルを日時情報付きで記録する

    Parameters
    ----------
    filename : str
        ファイル名
    contents : str
        ファイルコンテンツ
    """

    try:
        ymdhms = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        filename_ = "Result/{}-{}.txt".format(ymdhms, filename)

        with open(filename_, "w") as f:
            f.write(contents)

        return filename_

    except:
        Output.error("Failed to store file")
        sys.exit()