import sys
import requests

from Output import Output


def html_loader(url):
    """
    HTMLコンテンツをダウンロードする．

    Parameters
    ----------
    url: str
        対象となるURL

    Returns
    ----------
    html_response: requests.models.Response
        requestsによって取得したレスポンス結果
    """

    try:
        html_response = requests.get(url)
        Output.add("Loaded {}".format(url))
    except:
        Output.error("Failed to get {}".format(url))
        sys.exit()

    return html_response
    

def js_loader(url, js_link_list, csp_info_db):
    """
    JavaScriptコンテンツをダウンロードする．

    Parameters
    ----------
    url: str
        対象となるURL
    js_link_list: list
        scriptタグから抽出したJavaScriptリンクのリスト
    csp_info_db: CSPInfoDB
        CSP自動構成用データベース
    """

    for js_link in js_link_list:
        
        # 相対パスのJavaScriptリンクについては
        # 正しいURLになるように変換
        if js_link.startswith("http"):
            target_js_link = js_link
        else:
            url_ = "/".join(url.split("/")[:-1])
            js_link_ = "/".join(js_link.split("/")[1:])
            target_js_link = url_ + "/" + js_link_

        try:
            js_response = requests.get(target_js_link)

            Output.add("Loaded {}".format(target_js_link))

            csp_info_db.add_external_script_list(
                filename=target_js_link,
                original_src=js_link,
                contents=js_response.text
            )

        except:
            Output.warn("Failed to load {}".format(target_js_link))