from Output import Output

def present_csp_violation_list(csp_info_db):
    """
    CSPポリシー違反リストを表示する

    Parameters
    ----------
    csp_info_db: CSPInfoDB
        CSP自動構成用データベース
    """

    violation_list = csp_info_db.get_violation_list()

    for violation_info in violation_list:
        category = violation_info["category"]
        filename = violation_info["filename"]
        line_ = violation_info["line"]

        if line_ == -1:
            line = ""
        else:
            line = "(Line {})".format(line_)

        if category == csp_info_db.VIOLATION_CATEGORY_JAVASCRIPT_SCHEME:
            Output.warn("javascript: scheme in {}".format(filename))
        
        if category == csp_info_db.VIOLATION_CATEGORY_INNER_OUTER_HTML:
            Output.warn("innerHTML / outerHTML in {} {}".format(filename, line))

        if category == csp_info_db.VIOLATION_CATEGORY_DOCUMENT_WRITE:
            Output.warn("document.write(ln) in {} {}".format(filename, line))

        if category == csp_info_db.VIOLATION_CATEGORY_EVAL:
            Output.warn("eval() Function in {} {}".format(filename, line))

        if category == csp_info_db.VIOLATION_CATEGORY_FUNCTION_CONSTRUCTOR:
            Output.warn("Function() Constructor in {} {}".format(filename, line))

        if category == csp_info_db.VIOLATION_CATEGORY_STYLE_ATTRIBUTE:
            Output.warn("style attribute in {}".format(filename))

