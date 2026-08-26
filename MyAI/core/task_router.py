def route_task(text):

    text = text.lower()



    # 專案分析

    if any(word in text for word in [
        "myai",
        "專案",
        "架構",
        "程式架構",
        "專案結構",
        "目錄結構",
        "source code"
    ]):

        return {
            "tool": "project_scanner",
            "action": "analyze",
            "path": "~/MyAI"
        }



    # 網路搜尋

    if any(word in text for word in [
        "搜尋",
        "查詢",
        "網路",
        "最新",
        "新聞",
        "消息",
        "github",
        "官方"
    ]):

        return {
            "tool": "browser",
            "command": "search",
        "keyword": text
        }



    # 系統資訊

    if any(word in text for word in [
        "手機",
        "android",
        "cpu",
        "ram",
        "空間",
        "系統版本",
        "termux"
    ]):

        return {
            "tool": "system_info"
        }



    # 時間

    if any(word in text for word in [
        "時間",
        "幾點",
        "日期"
    ]):

        return {
            "tool": "current_time"
        }



    return None
