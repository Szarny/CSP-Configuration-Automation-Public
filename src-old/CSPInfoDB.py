class CSPInfoDB:
    def __init__(self):
        self.violation_list = []
        self.script_src_list = []
        self.style_src_list = []
        self.inline_script_list = []
        self.inline_style_list = []
        self.connect_src_list = []
        self.external_script_list = []
        self.external_script_src_and_hash_list = []

        self.VIOLATION_CATEGORY_JAVASCRIPT_SCHEME = 1
        self.VIOLATION_CATEGORY_INNER_OUTER_HTML = 2
        self.VIOLATION_CATEGORY_DOCUMENT_WRITE = 3
        self.VIOLATION_CATEGORY_EVAL = 4
        self.VIOLATION_CATEGORY_FUNCTION_CONSTRUCTOR = 5
        self.VIOLATION_CATEGORY_STYLE_ATTRIBUTE = 6

    def __str__(self):
        print("violation_list", self.violation_list)
        print("script_src_list", self.script_src_list)
        print("style_src_list", self.style_src_list)
        print("inline_script_list", self.inline_script_list)
        print("inline_style_list", self.inline_style_list)
        print("connect_src_list", self.connect_src_list)
        return ""

    def add_violation_list(self, category, filename, line):
        """
        CSPポリシー違反リストに違反内容を追加する

        Parameters
        ----------
        category: int
            違反の種別
        filename: str
            違反が発見されたファイル名
        line: int
            違反が存在する行番号
        """

        violation_item = {
            "category": category,
            "filename": filename,
            "line": line
        }
        self.violation_list.append(violation_item)

    
    def get_violation_list(self):
        """
        CSPポリシー違反リストを取得する

        Returns
        ----------
        violation_list: list
            CSPポリシー違反リスト
        """

        return self.violation_list

    
    def add_script_src_list(self, script_src):
        """
        JavaScript読み込み元オリジンリストに追加する

        Parameters
        ----------
        script_src: str
            JavaScript読み込み元オリジン
        """

        self.script_src_list.append(script_src)


    def get_script_src_list(self):
        """
        JavaScript読み込み元オリジンリストを取得する

        Returns
        ----------
        script_src_list: list
            JavaScript読み込み元オリジンリスト
        """

        return self.script_src_list

    
    def add_style_src_list(self, style_src):
        """
        CSS読み込み元オリジンリストに追加する

        Parameters
        ----------
        style_src: str
            CSS読み込み元オリジン
        """

        self.style_src_list.append(style_src)


    def get_style_src_list(self):
        """
        CSS読み込み元オリジンリストを取得する

        Returns
        ----------
        style_src_list: list
            CSS読み込み元オリジンリスト
        """

        return self.style_src_list

    
    def add_inline_script_list(self, inline_script):
        """
        インラインスクリプトリストに追加する

        Parameters
        ----------
        inline_script: str
            インラインスクリプト
        """

        self.inline_script_list.append(inline_script)

    
    def get_inline_script_list(self):
        """
        インラインスクリプトリストを取得する

        Returns
        ----------
        inline_script_list: list
            インラインスクリプトリスト
        """

        return self.inline_script_list


    def add_inline_style_list(self, inline_style):
        """
        インラインスタイルリストに追加する

        Parameters
        ----------
        inline_style: str
            インラインスタイル
        """

        self.inline_style_list.append(inline_style)

    
    def get_inline_style_list(self):
        """
        インラインスタイルリストを取得する

        Returns
        ----------
        inline_style_list: list
            インラインスタイルリスト
        """

        return self.inline_style_list


    def add_connect_src_list(self, connect_src):
        """
        接続先リストに追加する

        Parameters
        ----------
        connect_src: str
            接続先
        """

        self.connect_src_list.append(connect_src)

    
    def get_connect_src_list(self):
        """
        接続先リストを取得する

        Returns
        ----------
        connect_src_list: list
            接続先リスト
        """

        return self.connect_src_list


    def add_external_script_list(self, filename, original_src, contents):
        """
        外部参照を行うスクリプトリストに追加する

        Parameters
        ----------
        filename: str
            読み込み元オリジンのフルパス
        original_src: str
            scriptタグのsrc属性に指定された値
        contents: str
            スクリプトのコンテンツ
        """

        self.external_script_list.append({
            "filename": filename,
            "original_src": original_src,
            "contents": contents
        })


    def get_external_script_list(self):
        """
        外部参照を行うスクリプトリストを取得する

        Returns
        ----------
        external_script_list: list
            外部参照を行うスクリプトリスト
        """

        return self.external_script_list


    def set_external_script_src_and_hash_list(self, src, hash_value):
        """
        外部参照を行うスクリプトリストの読み込み元とハッシュ値のリストに追加する

        Parameters
        ----------
        src: str
            scriptタグのsrc属性に指定された値
        hash_value: str
            スクリプトのコンテンツのハッシュ値
        """

        self.external_script_src_and_hash_list.append({
            "src": src,
            "hash_value": hash_value
        })

    def get_external_script_src_and_hash_list(self):
        """
        外部参照を行うスクリプトリストの読み込み元とハッシュ値のリストを取得する

        Returns
        ----------
        external_script_src_and_hash_list: list
            外部参照を行うスクリプトリストの読み込み元とハッシュ値のリスト
        """
        return self.external_script_src_and_hash_list
    