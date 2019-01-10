import re

from Output import Output


def analyze(csp_info_db):
    """
    JavaScriptファイルを解析し，以下の項目をCSPデータベースに保存する．
    - innerHTML/outerHTMLでscriptタグを出力している箇所
    - document.write(ln)でscriptタグを出力している箇所
    - eval関数を用いている箇所
    - Functionコンストラクタを用いている箇所

    Parameters
    ----------
    csp_info_db : class
        CSP自動構成用データソース

    Returns
    -----------
    result : bool
        実行結果
    """

    js_contents_list = []

    inline_script_list = csp_info_db.get_inline_script_list()
    for inline_script in inline_script_list:
        js_contents_list.append({
            "filename": "inline script",
            "contents": inline_script
        })

    external_script_list = csp_info_db.get_external_script_list()
    for external_script in external_script_list:
        js_contents_list.append({
            "filename": external_script["filename"],
            "contents": external_script["contents"]
        })

    try:
        for js_contents in js_contents_list:
            filename = js_contents["filename"]
            contents = js_contents["contents"]

            for line, contents_line in enumerate(contents.split("\n"), start=1):
                is_exist_inner_outer_html = "innerHTML" in contents_line or "outerHTML" in contents_line
                is_exist_document_write = "document.write" in contents_line or "document.writeln" in contents_line
                is_exist_eval = "eval(" in contents_line
                is_exist_Function = "new Function(" in contents_line

                if is_exist_inner_outer_html:
                    csp_info_db.add_violation_list(
                        category=csp_info_db.VIOLATION_CATEGORY_INNER_OUTER_HTML,
                        filename=filename,
                        line=line
                    )

                    Output.warn("Extracted innerHTML / outerHTML in {}\n{}".format(
                        filename, contents_line
                    ))

                
                if is_exist_document_write:
                    csp_info_db.add_violation_list(
                        category=csp_info_db.VIOLATION_CATEGORY_DOCUMENT_WRITE,
                        filename=filename,
                        line=line
                    )

                    Output.warn("Extracted document.write(ln) in {}\n{}".format(
                        filename, contents_line
                    ))

                
                if is_exist_eval:
                    csp_info_db.add_violation_list(
                        category=csp_info_db.VIOLATION_CATEGORY_EVAL,
                        filename=filename,
                        line=line
                    )

                    Output.warn("Extracted eval() Function in {}\n{}".format(
                        filename, contents_line
                    ))

                
                if is_exist_Function:
                    csp_info_db.add_violation_list(
                        category=csp_info_db.VIOLATION_CATEGORY_FUNCTION_CONSTRUCTOR,
                        filename=filename,
                        line=line
                    )

                    Output.warn("Extracted Function() Constructor in {}\n{}".format(
                        filename, contents_line
                    ))

                url_list = re.findall(
                    "https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", contents_line)

                for url in url_list:
                    Output.add("Extracted URL in {}: {}".format(filename, url))
                    csp_info_db.add_connect_src_list(url)
                
        
        return True

    except:
        return False
