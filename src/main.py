import sys

from Output import Output
from Util import FileRecorder
from Util.Timer import Timer


import WebLoader
from JSLinkExtractor import js_link_extractor
from Analyzer import HTMLAnalyzer, JSAnalyzer
from CSPInfoDB import CSPInfoDB
from CSPConfigurator import configure_csp
from CSPViolationListPresenter import present_csp_violation_list


def main():
    Output.info("CSP Configuration Automation System activated")

    # 対象となるURLを取得
    target_url = Output.ask("Target URL >> ")

    # 時間計測用

    # 時間計測用
    timer = Timer()
    timer.start()

    # CSP自動構成用データソースのインスタンスを生成
    csp_info_db = CSPInfoDB()

    ##########
    # STEP 1 #
    ##########
    print()
    Output.info("(1/6) Load contents")

    # 対象となるURLからHTMLコンテンツを取得
    html_response = WebLoader.html_loader(target_url)
    html_contents = html_response.text

    # HTMLコンテンツからJavaScriptコンテンツへのリンクを抽出
    js_link_list, parsed_html = js_link_extractor(html_contents)

    # JavaScriptリンクとコンテンツのリストを取得
    WebLoader.js_loader(target_url, js_link_list, csp_info_db)

    ##########
    # STEP 2 #
    ##########
    print()
    Output.info("(2/6) Analyze HTML")

    # HTMLAnalyzerでHTMLを解析
    is_success_to_analyze_HTML = HTMLAnalyzer.analyze(
        parsed_html, csp_info_db, target_url)

    if not is_success_to_analyze_HTML:
        Output.error("Failed to analyze HTML")
        sys.exit()

    ##########
    # STEP 3 #
    ##########
    print()
    Output.info("(3/6) Analyze JavaScript")
    
    # JSAnalyzerでJavaScriptを解析
    # JavaScriptに関するデータそのものはcsp_info_db経由で渡す
    is_success_to_analyze_js = JSAnalyzer.analyze(csp_info_db)

    if not is_success_to_analyze_js:
        Output.error("Failed to analyze JavaScript")
        sys.exit()

    ##########
    # STEP 4 #
    ##########
    print()
    Output.info("(4/6) Configure CSP")

    csp_info_meta_format, csp_info_for_display, csp_info_external_script_integrity = configure_csp(csp_info_db, parsed_html, timer)

    ##########
    # STEP 5 #
    ##########
    print()
    Output.info("(5/6) Show and Record CSP")
    
    record_contents = "[CSP Configuration]\n{}\n\n[External Script with Integrity]\n{}\n".format(csp_info_meta_format, csp_info_external_script_integrity)
    recorded_filename = FileRecorder.record(target_url.split("/")[-1], record_contents)
    
    print(csp_info_for_display)

    ##########
    # STEP 6 #
    ##########
    print()
    Output.info("(6/6) Present CSP Violation List")
    
    if len(csp_info_db.get_violation_list()) == 0:
        Output.info("Violations are not detected")
    else:
        Output.warn("Following violations may violate CSP policy")
        Output.warn("Modification recommended")
        present_csp_violation_list(csp_info_db)

    print()
    Output.info("CSP Configuration is stored at {}".format(recorded_filename))

    timer.stop()
    time = timer.get_total_time()
    Output.info("CSP Configuration Automation System terminated successfully ({:.2} sec)".format(time))

if __name__ == '__main__':
    main()