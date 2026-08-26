def create_plan(task):

    task = task.lower()



    # 專案分析優先
    if any(word in task for word in [
        "專案",
        "架構",
        "結構",
        "程式架構",
        "myai"
    ]):

        return [
            "分析專案需求",
            "使用專案分析工具",
            "整理專案結構"
        ]



    # 備份

    if "備份" in task:

        return [
            "分析需要備份的目標",
            "確認資料大小",
            "建立備份檔案",
            "回報結果"
        ]



    # 整理

    if "整理" in task:

        return [
            "分析檔案結構",
            "分類資料",
            "整理目錄"
        ]



    # 檔案與資料夾

    if any(word in task for word in [
        "目錄",
        "資料夾",
        "檔案",
        "文件"
    ]):

        return [
            "判斷需要檔案資訊",
            "使用檔案工具",
            "整理結果"
        ]



    # 系統資訊

    if any(word in task for word in [
        "系統",
        "手機",
        "android",
        "環境",
        "空間"
    ]):

        return [
            "分析系統環境",
            "使用系統資訊工具",
            "整理結果"
        ]



    # 時間

    if any(word in task for word in [
        "時間",
        "幾點",
        "日期"
    ]):

        return [
            "取得目前時間",
            "整理結果"
        ]



    return [
        "分析使用者需求",
        "決定需要的工具"
    ]
