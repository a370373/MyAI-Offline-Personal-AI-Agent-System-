## 🤖 MyAI — Offline Personal AI Agent System

«運行於個人裝置上的離線私人 AI Agent 系統。»

MyAI 不只是單純的聊天機器人。

# 它是一個以 Offline-First（離線優先） 為核心設計的私人 AI Agent 系統。

MyAI 將：

- 🧠 Local AI
- 🧬 MoE Expert Routing
- 🤖 Agent Core
- 🎯 Goal Mode
- 🛠️ Tool Framework
- 💾 Memory
- 🧩 Context
- 🌐 Browser Automation
- 🌍 Network Tools
- 🛡️ Security
- 🔧 Self-Repair
- 🧬 Self-Extension
- 🧪 Universal Training Engine（UTE）
- 🚀 Self-Upgrade
- ⚙️ Runtime

整合成一個可以在個人裝置上運作的 AI 工作環境。

核心理念：

«不要只給 AI 一顆大腦。

給它記憶、工具，以及一個可以工作的環境。 🤖»

---

## 🎯 1. Product Identity — 產品定位

MyAI 的定位：

Offline Personal AI Agent System

它可以作為：

- 🤖 個人 AI 助手
- 🧠 本地 AI Agent
- 💻 本地 AI 工作環境
- 🛠️ AI Tool Execution Platform
- 🌐 Browser Automation Agent
- 💾 Memory / Knowledge System
- 🧬 Multi-Model Expert Routing System
- 🎯 Goal-oriented Task Execution System
- 🧪 Local Model Training Integration
- 🔧 可擴充 Agent Framework

MyAI 的核心不是「聊天」。

而是：

理解 → 思考 → 使用工具 → 觀察結果 → 反思 → 修正 → 驗證 → 完成任務

---

## 🧠 2. Overall Architecture — 整體架構
```
                         👤 User
                           │
                           ▼
                  ┌─────────────────┐
                  │ 🤖 MyAI Agent   │
                  │      Core       │
                  └────────┬────────┘
                           │
       ┌───────────────────┼────────────────────┐
       │                   │                    │
       ▼                   ▼                    ▼
   🧠 Local AI          💾 Memory           🛠️ Tools
       │                   │                    │
       ▼                   │         ┌──────────┼──────────┐
   🧬 MoE Router            │         ▼          ▼          ▼
       │                   │       Shell       File     Browser
       ▼                   │                               │
   Expert Models           │                               ▼
       │                   │                          🌐 Chromium
       └───────────────────┼───────────────────────────────┘
                           │
                           ▼
                    🧩 Context System
                           │
                           ▼
                      🎯 Goal Mode
                           │
                           ▼
                    🛡️ Security Layer
                           │
                           ▼
                     ⚙️ Runtime Layer
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
        📱 Termux Runtime          🐧 Linux RootFS

                  🧪 Universal Training Engine
                           │
                           ▼
                 Model Training / Validation
                           │
                           ▼
                    Expert Model
                           │
                           ▼
                     🧬 MoE Router
```
MyAI 採用模組化架構。

各個模組可以獨立發展，並透過明確的介面互相協作。

核心模組不應被單一模型、單一 Runtime 或單一平台綁死。

---

## 📴 3. Offline-First — 離線優先

MyAI 的核心設計理念是：

Offline First，而不是 Cloud First。

在沒有網路的情況下，MyAI 的核心能力仍然可以在本地運作。

包括：

- 🧠 Local AI
- 💾 Memory
- 🧩 Context
- 🛠️ Local Tools
- 💻 Shell
- 📁 File Operations
- 🔍 Project Analysis
- 🤖 Agent Reasoning
- 🎯 Goal Execution
- 🔧 Self-Repair / Recovery

網路不是 MyAI 的核心依賴。

---

## 🌐 4. Network Tools — 有網路時擴充能力

MyAI 並不是永遠不能上網。

當裝置有網路時，Agent 可以選擇使用 Network Tools。

例如：

- 🔎 Web Search
- 🌐 Browser
- 📡 Network-based Tools
- 📚 Online Information
- 🌍 External Services

核心邏輯：

                 👤 User
                    │
                    ▼
                 🤖 MyAI
                    │
                    ▼
             Can answer locally?
              ┌─────┴─────┐
             YES           NO / Online Needed
              │                    │
              ▼                    ▼
         🧠 Local AI          🌐 Network Tools
              │                    │
              └─────────┬──────────┘
                        ▼
                     Result

«離線時使用本地能力。

有網路時，可以主動使用網路工具。»

網路是能力擴充，而不是核心依賴。

---

## 🤖 5. Agent Core — AI 的大腦

Agent Core 負責整個任務執行流程。

主要能力：

- 🔍 Task Analysis
- 🧠 Planning
- 🧭 Task Routing
- 🛠️ Tool Selection
- ⚡ Tool Execution
- 👀 Observation
- 🤔 Reflection
- 🎯 Goal Verification
- 🔧 Recovery
- 🧬 Self-Correction

基本流程：
```
👤 User Request
       ↓
🔍 Task Analysis
       ↓
🧠 Planning
       ↓
🧬 Model Routing
       ↓
🛠️ Tool Selection
       ↓
🛡️ Permission / Risk Check
       ↓
⚡ Execute
       ↓
👀 Observe
       ↓
🤔 Reflection
       ↓
🎯 Goal Verification
       ↓
   ┌───┴───┐
   │       │
 成功     失敗
   │       │
   ▼       ▼
 STOP    Recovery
             │
             ▼
          Retry
```
Agent Core 是整個系統的主要控制中心。

MoE Router 負責選擇推理模型，但不取代 Agent Core 的任務管理、工具管理與安全控制。

---

## 🎯 6. Goal Mode — 目標導向任務執行

Goal Mode 是 MyAI 內建的目標執行模式。

它讓 MyAI 不必只針對使用者的一次輸入產生一次回答，而是可以圍繞一個明確目標，進行多輪執行、觀察、反思與驗證。

使用者可以透過：

/goal <目標>

啟動 Goal Mode。

例如：

/goal 分析目前專案的 Rust workspace，找出編譯錯誤並修復。

或：

/goal 檢查目前系統的 Chromium Runtime 是否正常運作。

6.1 Goal Execution — 目標執行流程
```
👤 User
   │
   ▼
/goal <Objective>
   │
   ▼
🎯 Goal Controller
   │
   ▼
🔍 Analyze Goal
   │
   ▼
🧠 Generate Next Step
   │
   ▼
🤖 Agent Core
   │
   ▼
🛠️ Tool Execution
   │
   ▼
👀 Observe Result
   │
   ▼
💾 Record History
   │
   ▼
🤔 Reflection
   │
   ▼
🎯 Goal Verification
   │
   ├───────────────┐
   ▼               ▼
 Complete        Continue
   │               │
   ▼               ▼
  STOP          Next Round
                   │
                   └──────↻
```
6.2 Reflection — 反思機制

每一輪任務執行後，Goal Controller 可以將執行結果交回模型進行反思。

反思內容包括：

- 目前目標是否已完成？
- 上一輪執行結果是否符合預期？
- 是否還有未完成的工作？
- 下一步應該執行什麼？
- 是否需要調整原本的策略？
- 是否應該重試？
- 是否應該停止任務？

Reflection 的目的不是單純重複對話。

而是讓 Agent 根據實際執行結果決定下一步。

6.3 Goal History — 任務歷史紀錄

Goal Mode 會保留每一輪的重要執行結果。

歷史紀錄可以包含：

- Round Number
- Execution Phase
- Reflection Result
- Tool Execution Result
- Pending Action Result
- Error / Failure Information

概念：
```
Goal History
    │
    ├── Round 1
    │     ├── Reflection
    │     └── Execution Result
    │
    ├── Round 2
    │     ├── Reflection
    │     └── Execution Result
    │
    └── Round 3
          ├── Reflection
          └── Execution Result
```
這讓後續反思可以參考先前的任務進度，而不是每一輪都從零開始。

6.4 Pending Action — 待確認操作

當 Agent 產生需要使用者確認的操作時，Goal Mode 必須尊重原有的 Pending Action 流程。

例如：

- 高風險 Shell 操作
- 需要人工確認的工具呼叫
- 需要使用者授權的動作

流程：
```
🤖 Agent
   │
   ▼
🛠️ Pending Action
   │
   ▼
🛡️ Permission Check
   │
   ▼
👤 User Confirmation
   │
   ├──────────┐
   ▼          ▼
 Confirm     Cancel
   │          │
   ▼          ▼
 Execute    Record Result
   │          │
   └────┬─────┘
        ▼
    Goal History
        │
        ▼
    Reflection
```
Goal Mode 不應繞過 Agent Core 原有的安全機制。

6.5 Goal Configuration — 設定檔

Goal Mode 的設定檔：

MyAI/config/goal_config.json

目前確認的設定範例：

{
  "enabled": true,
  "max_reflections": 10,
  "max_tool_calls": 20,
  "allow_retry": true,
  "detect_repeated_actions": true
}

設定說明：

欄位| 用途| 範例值
"enabled"| 是否啟用 Goal Mode| "true"
"max_reflections"| 最大反思輪數| "10"
"max_tool_calls"| 任務工具呼叫預算| "20"
"allow_retry"| 是否允許重試| "true"
"detect_repeated_actions"| 是否偵測重複操作| "true"

設定建議

- "enabled"：設為 "true" 才能啟用 Goal Mode。
- "max_reflections"：控制反思迭代上限。
- "max_tool_calls"：限制任務期間可使用的工具呼叫預算。
- "allow_retry"：允許在適當情況下重新嘗試。
- "detect_repeated_actions"：避免 Agent 一直重複相同操作。

以上是目前確認的設定欄位與範例值。使用者可以依照裝置效能、任務複雜度與安全需求調整。

6.6 Iteration Control — 迭代控制

為避免 Agent 無限制執行，Goal Mode 受到：

- Maximum Reflection Rounds
- Tool Call Budget
- Timeout
- Retry Policy
- Goal Verification
- Duplicate Action Detection
- Pending Action Confirmation

等機制控制。

6.7 Goal Mode Design Philosophy

«使用者提供目標。

Agent 負責規劃、執行、觀察與反思。

直到目標完成，或確認應該停止。»

Goal Mode 讓 MyAI 從單次對話，朝向持續性任務執行系統發展。

---

## 🧠 7. Local AI Engine — 本地 AI

MyAI 將 AI 模型視為可替換的推理引擎。

MyAI 本身不綁定特定模型。

使用者可以自行準備：

- llama.cpp
- 相容的 GGUF 模型

概念：

              🤖 MyAI
                 │
                 ▼
          🧠 Local AI Engine
                 │
                 ▼
             llama.cpp
                 │
                 ▼
             GGUF Model

模型可以依照使用者裝置自行選擇。

例如根據：

- RAM
- CPU
- GPU / NPU
- Storage
- Model Size
- Quantization
- Language
- Performance

選擇適合自己的模型。

MyAI 也可以透過 MoE Expert Routing，使用多個不同的專業模型，而不是永遠依賴單一模型。

---

## 🧬 8. MoE Expert Routing — 專家模型路由系統

MyAI 支援外部 Expert Router（專家模型路由器）架構。

透過 MoE Router，MyAI 可以根據使用者的需求，在 Main Model 與不同的 Expert Model 之間選擇合適的推理模型。

8.1 Architecture — 架構

目前採用：

External Expert Routing / MoE Simulation

這不是直接修改 LLM 內部的 Mixture of Experts 結構。

而是在 Agent Core 與 Local AI Model 之間建立一個獨立的模型路由層。

                 🤖 MyAI Agent Core
                         │
                         ▼
                  🧩 Context System
                         │
                         ▼
                    🧬 MoE Router
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       🔍 Expert Matching       No Match
              │                     │
              ▼                     ▼
       🧠 Expert Model          🧠 Main Model
              │                     │
              ▼                     ▼
       Expert Response         Main Response
              │                     │
              └──────────┬──────────┘
                         ▼
                    🤖 Agent Core
                         │
                         ▼
                   🛡️ Security

8.2 Expert Selection — 專家選擇

MoE Router 會掃描 "expert/" 目錄，讀取各個 Expert 的 "expert.json" 設定。

目前使用關鍵字匹配進行初步分類。

例如：

Expert| 關鍵字範例
Python Expert| Python、程式碼、Debug、除錯
Rust Expert| Rust、Cargo、Crate
Linux Expert| Linux、Shell、系統管理

Router 會根據關鍵字命中情況選擇適合的 Expert。

目前選擇邏輯：

- 比對使用者訊息與各 Expert 的關鍵字。
- 統計關鍵字命中數量。
- 優先選擇命中數較多的 Expert。
- 命中數相同時，參考命中關鍵字的總長度。
- 無法明確選出專家時，使用 Main Model。

目前屬於規則式路由，並非語意模型評分或自動判斷模型能力。

8.3 Expert Identity — 專家身份設定

每個 Expert 都可以擁有自己的 "expert.json"。

目前支援的設定欄位：

欄位| 用途
"enabled"| 是否啟用 Expert
"name"| Expert 名稱
"model"| GGUF 模型檔案
"keywords"| 路由關鍵字
"port"| 模型服務連接埠
"ctx_size"| 上下文長度
"n_gpu_layers"| GPU Offload 層數
"threads"| CPU 執行緒數

範例：

{
  "enabled": true,
  "name": "Python Expert",
  "model": "python-expert.gguf",
  "keywords": [
    "python",
    "程式碼",
    "debug",
    "除錯",
    "函式"
  ],
  "port": 8101,
  "ctx_size": 8192,
  "n_gpu_layers": 0,
  "threads": 8
}

注意： "keywords" 必須提供非空的關鍵字清單，不能只保留空陣列 "[]"。

8.4 Expert Runtime — 專家模型執行環境

當 Router 找到符合條件的 Expert：

1. 啟動對應的 llama-server。
2. 建立獨立的模型服務。
3. 將 Context 傳送給 Expert。
4. 接收 Expert Response。
5. 將回答交回 Agent Core。

每個 Expert 可以使用自己的 GGUF 模型與執行設定。

8.5 Fallback — 主模型回退機制

MyAI 不會因為某個 Expert 無法使用，就讓整個 Agent 停止工作。

Fallback 條件包括：

- 沒有符合條件的 Expert。
- Expert 啟動失敗。
- Expert 推論失敗。

發生上述情況時，Router 會改用原本的 Main Model。

          🧬 MoE Router
                 │
                 ▼
          Select Expert
                 │
          ┌──────┴──────┐
          ▼             ▼
       Success        Failure
          │             │
          ▼             ▼
     Expert Model    Main Model
          │             │
          └──────┬──────┘
                 ▼
           Agent Response

8.6 Security Integration — 安全整合

Expert Model 不會因為具有專業能力，就自動取得額外系統權限。

所有工具操作仍然必須經過 Agent Core 原有的安全流程：

- Tool Parser
- Permission System
- Command Guard
- Risk Analyzer
- Human Confirmation

Expert 負責產生回答與工具請求，實際操作仍由 Agent Core 管理。

8.7 Design Philosophy — 設計理念

«一個主模型負責通用推理，多個專家模型負責特定領域。

讓 MyAI 可以依照任務選擇適合的大腦，而不是永遠使用同一個模型。»

---

## 🧪 9. UTE — Universal Training Engine

UTE（Universal Training Engine，通用訓練引擎）是 MyAI 的獨立模型訓練與擴充專案。

它不是 MyAI 內建的一般 Tool，也不是 MoE Router。

UTE 的定位是：

提供可獨立使用、可配置、可整合的模型訓練工作流程。

需要模型訓練、微調或建立專業模型功能的使用者，可以前往以下 Repository 下載 UTE：

## 🔗 UTE 官方 Repository

https://github.com/a370373/UTE-Universal-Training-Engine

UTE 的完整功能介紹、使用方式、安裝需求、訓練流程與設定說明，請以該 Repository 的 README 與文件為準。

9.1 UTE 與 MyAI 的關係

             🤖 MyAI
                │
                ▼
         🧬 MoE Expert Routing
                ▲
                │
        Expert Model / Config
                │
                │
        🧪 UTE — Separate Project
                │
       ┌────────┼─────────┐
       ▼        ▼         ▼
    Dataset  Training  Validation
       │        │         │
       └────────┼─────────┘
                ▼
          Adapter / Model
                │
                ▼
          GGUF Conversion
                │
                ▼
          Expert Deployment

兩個專案的責任分工：

專案 / 模組| 責任
MyAI Agent Core| Agent 任務管理與協調
Goal Mode| 多輪目標執行與反思
MoE Router| 選擇合適的模型
UTE| 模型訓練與產出
llama.cpp| 本地模型推理服務
GGUF Model| 實際推理使用的模型檔案

UTE 不會取代 MyAI 的 Agent Core。

MyAI 也不需要將 UTE 的全部原始碼直接複製進自己的 Repository。

## 需要 UTE 功能的使用者，可以獨立下載與配置 UTE，再依照相容的模型格式與路徑，將產出模型整合至 MyAI。

9.2 UTE Features — 訓練能力

UTE 的設計方向包含：

- Dataset Preparation
- Dataset Validation
- Training Configuration
- Base Model Selection
- Supervised Fine-Tuning（SFT）
- LoRA Training
- QLoRA Training
- Adapter Management
- Adapter Merge
- Model Conversion
- GGUF Export
- Model Validation

UTE 目前的主要訓練定位為 Hugging Face Causal Language Model 的 SFT + LoRA 工作流程。

它不應被描述成可以訓練所有模型架構或所有模型類型的通用魔法工具。

實際支援範圍以 UTE Repository 的版本與文件為準。

9.3 LoRA / QLoRA — 參數高效率微調

UTE 可以整合 LoRA 與 QLoRA 訓練流程。

這類方法可以在不必重新訓練整個模型所有參數的情況下，針對特定任務進行模型微調。

概念：

           🧠 Base Model
                 │
                 ▼
          LoRA / QLoRA
                 │
                 ▼
          Training Dataset
                 │
                 ▼
           Fine-Tuning
                 │
                 ▼
              Adapter

這使 MyAI 可以朝向建立不同領域的專家模型發展。

9.4 Adapter Merge & GGUF Export

訓練完成後，可以依照模型架構與轉換工具支援情況，進行：

       🧠 Base Model
              +
         LoRA Adapter
              │
              ▼
        Adapter Merge
              │
              ▼
       Merged Model
              │
              ▼
       GGUF Conversion
              │
              ▼
       Quantization
              │
              ▼
        GGUF Model

實際支援的模型架構、轉換方式與量化選項，取決於對應的轉換工具及模型格式。

9.5 Model Validation — 模型驗證

模型不能只因為成功產出，就直接視為可用。

UTE 的設計包含模型驗證階段。

例如：

- Model File Validation
- Model Format Validation
- Conversion Validation
- Inference Test
- Basic Response Evaluation
- Training Reports

如果模型驗證失敗，就不應直接將它當成正式可用的 Expert。

9.6 UTE Configuration — 設定檔

MyAI 端的 UTE 整合設定檔：

MyAI/tools/ute_config.json

UTE 是獨立專案，因此使用者必須先準備 UTE 本身的執行環境，再透過 MyAI 的設定指向它。

目前確認的重要設定項目如下：

設定項目| 用途| 必要性
"paths.ute_root"| UTE 專案根目錄| 必要
"paths.llama_cpp"| llama.cpp 執行環境路徑| 依整合流程需要
"model"| 訓練使用的 Base Model| 訓練必要
"data_dir"| 訓練資料集目錄| 訓練必要
"quantize_bin"| GGUF 量化工具執行檔| 啟用 GGUF 量化時必要

其他已確認的預設值：

設定項目| 預設值
Python 執行命令| "python3"
Workspace| "workspace/ute"
Logs| "logs/ute"
Epochs| "3.0"
Learning Rate| "0.0001"
Max Length| "1024"
Batch Size| "1"
Gradient Accumulation| "4"
LoRA Rank（r）| "16"
LoRA Alpha| "32"
LoRA Dropout| "0.05"
Quantization| "none"
GGUF Quantization Type| "Q4_K_M"

Expert 部署相關預設值：

設定項目| 預設值
Port| "8101"
Context Size| "8192"
GPU Layers| "0"
Threads| "8"

設定注意事項

1. "ute_root" 必須指向實際下載的 UTE 專案目錄。
2. "llama_cpp" 必須指向實際可用的 llama.cpp 執行環境。
3. "model" 必須指向相容的訓練 Base Model。
4. "data_dir" 必須指向有效的訓練資料集目錄。
5. 如果啟用 GGUF 量化，必須提供有效的 "quantize_bin" 路徑。
6. "quantization" 設為 "none" 時，不應要求量化執行檔。
7. 使用者應依照自己的 CPU、RAM、GPU、Storage 與模型大小調整訓練參數。

重要： 上述是目前確認的設定項目與預設值，不代表所有欄位都使用相同的 JSON 巢狀結構。請保留 UTE 整合程式現有的 JSON 結構，依照實際設定檔的欄位位置填入，不要自行猜測或重建未知欄位。

9.7 Expert Registration — 專家模型註冊

UTE 與 MoE Router 之間可以建立整合流程。

UTE 負責產出模型與相關設定資料。

MoE Router 則負責讀取 Expert 設定並進行模型選擇。

             🧪 UTE
               │
               ▼
         Trained Model
               │
               ▼
         Model Validation
               │
               ▼
        Expert Configuration
               │
               ▼
         expert.json
               │
               ▼
            expert/
               │
               ▼
          🧬 MoE Router
               │
               ▼
        Expert Model Runtime

9.8 UTE Resource Awareness — 訓練資源管理

模型訓練通常比一般模型推理需要更多資源。

UTE 必須考慮：

- RAM
- CPU
- GPU / VRAM
- Storage
- Dataset Size
- Model Size
- Batch Size
- Context Length
- Training Framework
- Runtime Dependencies

因此：

UTE 可以在個人裝置上管理訓練流程，但不代表所有訓練任務都能在所有手機上完成。

必要時，可以在具備相容環境與足夠資源的其他平台執行訓練，再將產出的模型部署回 MyAI。

9.9 UTE Design Philosophy

«MyAI 負責使用模型。

MoE Router 負責選擇模型。

UTE 負責建立與擴充模型。»

需要完整訓練功能的使用者，請前往 UTE 獨立 Repository：

https://github.com/a370373/UTE-Universal-Training-Engine

---

## 🛠️ 10. Tool Framework — AI 的手腳

如果：

«🧠 Model = 大腦»

那麼：

«🛠️ Tools = 手腳»

MyAI 的 Tool Framework 負責管理 Agent 能使用的能力。

包含：

- Tool Registry
- Tool Manager
- Tool Parser
- Capability System
- Permission Handling

## 💻 Shell / Command Tool

讓 Agent 能夠操作 Runtime。

可以用於：

- 執行 Shell 指令
- 系統檢查
- Runtime 操作
- Script 執行
- Debug
- 開發環境操作
- 問題診斷

因此 Agent 不只是告訴你 Command。

它可以在權限允許的情況下：

真正執行 Command，然後讀取結果。

## 📁 File Tool

讓 Agent 能夠操作檔案。

包括：

- 搜尋
- 讀取
- 修改
- 建立
- 管理
- 分析

## 🌐 Browser Tool

提供 Browser Automation 能力。

包括：

- Browser Agent
- Browser Planner
- DOM Analysis
- Element Detection
- Element Scoring
- Page State
- Tab Management
- Failure Detection
- Recovery

## 📚 Knowledge Tool

管理：

- 專案知識
- 文件
- 技術資料
- 使用者資料
- Knowledge Base

## 🔍 Project Scanner

讓 Agent 可以檢查專案：
```
📁 Project
   ↓
🔍 Scan
   ↓
🗂️ Structure
   ↓
📄 Source
   ↓
🧠 Analysis
   ↓
🤖 Agent Understanding
```
可用於：

- 專案分析
- 架構理解
- Debug
- Source Inspection
- 開發輔助

---

## 🌐 11. Browser Agent — AI 的瀏覽器能力

Browser Agent 是 MyAI 的重要子系統。

架構：
```
🤖 MyAI
   ↓
🌐 Browser Agent
   ↓
🧠 Browser Planner
   ↓
🌐 Browser Runtime
   ↓
🔌 CDP
   ↓
🌐 Chromium
```
Browser Agent 可以根據：

- DOM
- Elements
- Page State
- Browser State
- Tool Results

決定下一步行動。

因此 Browser 不只是：

「幫我開網站。」

而是：

讓 Agent 能理解網頁狀態並操作網頁。

---

## 🌐 12. Chromium Runtime

MyAI 可以搭配獨立 Chromium "headless-shell" Runtime。

Repository 中包含 Chromium Runtime 所需要的相關元件。

這使 Browser Agent 可以使用受控的 Chromium 執行環境，而不需要完全依賴系統瀏覽器。

---

## 🐧 13. Linux RootFS — Chromium Runtime Environment

MyAI 包含 Linux RootFS。

它不是完整 Linux 作業系統。

主要用途是提供：

Chromium 與相關元件所需的 Linux 相容執行環境。

概念：
```
📱 Android
   │
   ▼
📦 Termux
   │
   ▼
🐧 Linux RootFS
   │
   ▼
🌐 Chromium
```
---

## 📱 14. Termux Runtime

Android 部署可以使用 Termux 作為基礎 Runtime。

Runtime 可以提供：

- Python
- Shell
- GCC
- Git
- Package Environment
- Development Tools
- Local AI Runtime

MyAI Core 不需要把整個 Agent 架構寫死在 Termux 裡。

Termux 更像是：

Android 上的執行環境。

---

## 💾 15. Memory System — AI 的記憶

MyAI 將 Memory 與目前 Task Context 分開。

可以包含：

- ⚡ Short-Term Memory：目前任務的暫時資訊。
- 🕐 Recent Memory：近期任務與工作狀態。
- 🧠 Long-Term Memory：需要長期保存的資訊。
- 📚 Knowledge Memory：專案與技術知識。

概念：
```
             💾 Memory
                 │
      ┌──────────┼──────────┐
      ▼          ▼          ▼
   Short       Recent     Long-Term
      │          │          │
      └──────────┼──────────┘
                 ▼
             Knowledge
```
---

## 🧩 16. Context System — 當前狀態

Context 負責保存 Agent 當前正在做什麼。

例如：

- Current Task
- Current Goal
- Tool Result
- Observation
- Task State
- Temporary Information

Context 是短期狀態。

Memory 則負責更長期的資訊保存。

---

## 💬 17. Conversation System — 對話與自我對話

MyAI 不只可以與使用者對話。

由於 Agent 可以自行產生下一個任務步驟，因此系統可以形成：

Self-Iteration / Self-Dialogue

例如：
```
🤖 MyAI
   ↓
「我需要檢查 Browser。」
   ↓
🤖 MyAI
   ↓
「檢查結果顯示……」
   ↓
🤖 MyAI
   ↓
「我發現另一個問題。」
   ↓
🤖 MyAI
   ↓
「我需要進一步測試。」
   ↓
        ↻
```
這可以用於：

- 任務分解
- Reflection
- 自動驗證
- Debug
- Self-Repair
- 長任務執行

Self-Iteration 必須受到最大迭代次數、Timeout、Token / Resource Budget、Goal Verification 與重複偵測等機制控制。

---

## 🛡️ 18. Security Layer — AI 不能想幹嘛就幹嘛

MyAI 擁有：

- 🛡️ Command Guard
- 🔐 Permission System
- ⚠️ Risk Analyzer
- 👤 Human Confirmation
- 🧩 Capability Control

概念：
```
🤖 Agent Action
       ↓
🔍 Capability Check
       ↓
⚠️ Risk Analysis
       ↓
 ┌─────┼─────┐
 ▼     ▼     ▼
低風險  高風險  禁止
 │      │      │
 ▼      ▼      ▼
執行   👤確認   ❌拒絕
```
能力越強，安全控制越重要。

---

## 🔧 19. Self-Repair — 自我檢查與修復

MyAI 的 Tool、Source Inspection 與 Execution 能力，使它可以朝 Self-Repair 發展。

理想流程：
```
👀 Inspect
   ↓
🔍 Diagnose
   ↓
🧠 Reason
   ↓
📝 Generate Fix
   ↓
💻 Modify
   ↓
🧪 Test
   ↓
🎯 Verify
   ↓
 ┌──────┴──────┐
 ▼             ▼
成功           失敗
 │              │
 ▼              ▼
完成          Recovery
```
看到問題 → 找原因 → 嘗試修復 → 測試 → 驗證。

---

## 🧬 20. Self-Extension — 自我建立工具

Tool Framework 的可擴充設計，使 MyAI 可以進一步支援：

Agent-generated Tools
```
🤖 發現能力缺口
        ↓
🧠 設計新 Tool
        ↓
💻 生成 Tool Code
        ↓
🧪 Test
        ↓
🔍 Validate
        ↓
🛡️ Permission
        ↓
📦 Register
        ↓
🛠️ 使用新能力
```
未來 MyAI 不一定只能使用開發者預先寫好的工具，也可以朝向自行建立新能力的方向發展。

---

## 🚀 21. Self-Upgrade — 自我升級

MyAI 的長期方向不一定是：
```
V1
 ↓
V2
 ↓
V3
 ↓
V4
```
而可以是：
```
🔍 Self Inspection
        ↓
🧠 Find Weakness
        ↓
📝 Propose Improvement
        ↓
💻 Modify
        ↓
🧪 Test
        ↓
📊 Benchmark
        ↓
🛡️ Validate
        ↓
🚀 Apply
        ↓
💾 Checkpoint
        ↓
↩️ Rollback if Failed
```
Self-Upgrade 不代表無限制修改自己。

安全的 Self-Upgrade 應該包含：

- Sandbox
- Tests
- Validation
- Permission
- Checkpoint
- Rollback
- Resource Limits

---

## 🧠 22. Replaceable Brain — 可替換的大腦

MyAI 不把模型當作整個產品。

模型只是：

Local AI Engine 的一部分。

                 🤖 MyAI
                    │
                    ▼
             Local AI Interface
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Model A   Model B   Model C

透過 MoE Expert Routing，可以在多個模型之間進行任務路由。

透過 UTE，可以建立、微調與產出專業模型。

---

## 🌍 23. Platform Independence — 不綁死平台

MyAI 的核心架構與底層 Runtime 分離。

設計目標不是只服務 Android。

理論上，只要平台能提供 MyAI 所需要的 Runtime 與相容依賴，就可以建立對應平台版本。

目前可規劃支援：

- 🤖 Android
- 🪟 Windows
- 🍎 macOS
- 🐧 Linux

不同平台可以替換平台相關元件：

- Runtime
- Native Binary
- Chromium
- System Dependencies
- AI Runtime
- Platform-specific Tools

同一個 Agent Core，不同的平台 Runtime。

---

## 💾 24. Backup & Migration

MyAI 可以將核心與 Runtime 拆分。
```
🤖 MyAI
│
├── Core
├── Tools
├── Memory
├── Knowledge
├── Expert Models
└── Config

⚙️ Runtime
│
├── Termux Runtime
├── Linux RootFS
└── Chromium Runtime
```
這使環境可以進行：

- 💾 Backup
- ♻️ Restore
- 🚚 Migration
- 🏷️ Version Management

---

## 🗂️ 25. Repository Structure
```
MyAI-Offline-Personal-AI-Agent-System-
│
├── 🤖 MyAI/
│   ├── core/
│   │   ├── agent_core.py
│   │   ├── goal_controller.py
│   │   └── ...
│   │
│   ├── config/
│   │   └── goal_config.json
│   │
│   ├── data/
│   ├── knowledge/
│   ├── memory/
│   ├── runtime/
│   ├── tests/
│   │
│   ├── tools/
│   │   ├── ute_config.json
│   │   └── ...
│   │
│   ├── 🧬 expert/
│   │   ├── .gitkeep
│   │   └── <expert-name>/
│   │       ├── expert.json
│   │       └── <expert-model>.gguf
│   │
│   ├── MoE.py
│   ├── agent.py
│   ├── command_guard.py
│   ├── context_manager.py
│   ├── file_manager.py
│   ├── memory_manager.py
│   ├── project_scanner.py
│   └── VERSION.md
│
├── 🌐 headless-shell/
│
├── 🐧 linux-root/
│
└── 📱 termux_usr/
```
«上述結構為架構示意，實際目錄與檔案名稱以 Repository 當前版本為準。»

---

## 🏗️ 26. System Stack
```
                    👤 USER
                       │
                       ▼
                🤖 MYAI AGENT
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       🧠 AI        💾 Memory     🛠️ Tools
       Engine       Context       Framework
          │
          ▼
      🧬 MoE Router
          │
     ┌────┴─────┐
     ▼          ▼
 Main Model  Expert Models
     │          │
     └────┬─────┘
          ▼
      llama.cpp
          │
          ▼
       GGUF Model
```
                    🛠️ Tools
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       💻 Shell      📁 File     🌐 Browser
                                     │
                                     ▼
                                    CDP
                                     │
                                     ▼
                                 Chromium
                                     │
                                     ▼
                              🐧 Linux RootFS
                                     │
                                     ▼
                               📱 Host Runtime

                 🧪 UTE
                   │
                   ▼
             Model Training
                   │
                   ▼
             Model Validation
                   │
                   ▼
             GGUF / Adapter
                   │
                   ▼
             Expert Deployment
                   │
                   ▼
              🧬 MoE Router

---

## 🔥 27. What Makes MyAI Different?

MyAI 並不是把：

LLM + Chat UI

簡單組合在一起。

它更接近：

Local AI + Multi-Model Routing + Agent + Goal Execution + Tools + Memory + Training + Runtime + Environment

讓 AI 從「回答問題」走向：
```
「理解問題」
      ↓
「制定計畫」
      ↓
「選擇合適的模型」
      ↓
「使用工具」
      ↓
「觀察結果」
      ↓
「反思與修正」
      ↓
「驗證目標」
      ↓
「完成任務」
```
```
更進一步：

使用能力
  ↓
檢查自己
  ↓
修復自己
  ↓
建立新能力
  ↓
訓練或擴充模型
  ↓
改善自己
```
---

## 🚀 28. Future Direction

MyAI 沒有必要被限制成：

「每一次進步都必須是一個新版本。」

更有趣的方向是：
```
🧠 Think
   ↓
🧬 Select Model
   ↓
🛠️ Act
   ↓
👀 Observe
   ↓
🤔 Reflect
   ↓
🎯 Verify Goal
   ↓
🔧 Repair
   ↓
🧬 Extend
   ↓
🧪 Train
   ↓
📊 Evaluate
   ↓
🚀 Improve
   ↓
        ↻
```
理想狀態：

讓 MyAI 成為一個可以持續擴充、維護與改善自身能力的 Agent System。

---

## ⚠️ 29. Important Notes

MyAI 的 Self-Repair、Self-Extension、Self-Upgrade 等方向，代表的是：

軟體層面的 Agent 自我維護與能力擴充。

這不代表：

- ❌ AI 產生自我意識
- ❌ AI 自動獲得不可控制的自主權
- ❌ AI 能無限制修改系統
- ❌ AI 一定能自行提升智慧
- ❌ UTE 能在任何裝置上執行任何模型的訓練

任何涉及自我修改、模型訓練或高風險操作的能力，都應該受到：

- Permission
- Testing
- Validation
- Backup
- Rollback
- Sandbox
- Resource Limits
- Human Confirmation

控制。

MoE Expert Routing 也不代表 Expert Model 能繞過 Agent Core 的安全機制。

UTE 產出的模型也應經過驗證，才能進入正式的 Expert Runtime。

---

## 📦 30. Requirements

MyAI 是一個模組化系統。

使用者需要依照自己的平台準備相應 Runtime。

Local AI 部分需要：

llama.cpp
    +
Compatible GGUF Model

使用 MoE Expert Routing 時，還可以依照需求準備額外的 Expert GGUF 模型。

使用 UTE 時，則需要依照選擇的訓練流程準備相應的：

- Python Environment
- Training Framework
- Base Model
- Dataset
- Storage
- RAM / VRAM
- Model Conversion Dependencies

不同平台可以使用不同的 Runtime、Binary、Browser 與 Dependencies。

---

## 📊 31. Project Status

MyAI 是一個持續演進中的開源專案。

目前架構已包含或正在開發：

- 🤖 Agent Core
- 🧠 Local AI Engine
- 🧬 MoE Expert Routing Foundation
- 🎯 Goal Mode
- 🛠️ Tool Framework
- 💻 Shell / Command
- 📁 File Operations
- 🌐 Browser Agent
- 🔌 CDP
- 🌐 Chromium Runtime
- 🐧 Linux RootFS
- 📱 Termux Runtime
- 💾 Memory
- 🧩 Context
- 🛡️ Security
- 🔧 Recovery / Self-Correction
- 🔍 Project Scanner
- 🌍 Network Tools
- 🧪 UTE Integration
- 💾 Backup / Migration

31.1 MoE Expert Routing Status

目前已完成：

- Expert Directory Scanning
- JSON-based Expert Configuration
- Keyword-based Expert Selection
- Expert Server Management Foundation
- Main Model Fallback
- Agent Core Integration

已驗證：

- 無符合 Expert 時，能正常回退至 Main Model。

仍待進一步驗證：

- 實際 Expert GGUF 模型啟動。
- Expert 完整推論流程。
- Expert 失敗情況下的完整 Fallback 流程。

31.2 Goal Mode Status

目前已完成本輪 Goal Controller 修復：

- Reflection Prompt 整理。
- Goal History 記錄流程改善。
- Reflection 與 Pending Action 結果分開記錄。
- 保留既有 Pending Action 確認流程。
- 保留原有 Goal 執行控制與迭代機制。

修復 Commit：

"41643b3c"

Branch：

"fix/conversation-context"

仍應透過實際 Goal 任務測試，確認完整的多輪執行、反思、歷史紀錄與 Pending Action 流程。

31.3 UTE Status

UTE 是獨立的通用模型訓練引擎專案。

目前定位：

- Hugging Face Causal LM
- Supervised Fine-Tuning（SFT）
- LoRA / QLoRA
- Adapter Management
- Adapter Merge
- GGUF Conversion
- Model Validation

UTE 的實際功能與版本，請以獨立 Repository 的文件為準。

MyAI 端負責整合與使用符合條件的模型，不將 UTE 所有訓練功能宣稱為 MyAI 內建功能。

---

## 🎯 32. Philosophy

«AI 不應該只能聊天。

給它一顆大腦。 🧠

給它多個專家。 🧬

給它記憶。 💾

給它工具。 🛠️

給它目標。 🎯

給它訓練與擴充能力。 🧪

給它一個環境。 ⚙️

讓它能觀察、行動、反思、修正與成長。 🤖

然後看看它能做到什麼。 🚀»

---

## 🏆 Ecosystem & Showcase — 生態合作與展示 ✨ 官方特邀入駐 / Featured Showcase

- 本專案受邀進駐由 熾光時代、香港科技大學（廣州）、紫金山實驗室、國際AI算力協會 等機構協辦的 Agent2048 全球智能體大賽平台，擔任項目進駐方。

- 官方網站：https://agent2048.com/zh

- 專案網址：https://agent2048.com/zh/projects/s1s53knto6pr

---

## 📬 聯繫創作者

- Gmail: b0953166696@gmail.com
- 本人17歲 🤔 做的不好請見諒
- 獨立開發 ＆ AI 協作
- 緩慢更新 ＆ 除錯
- 純手機 Termux 開發 👀
- 持續開發中…

---

## 👀 作品 & 產品集

- [MySSH](https://github.com/a370373/MySSS-Server/tree/main)
- [UTE-Universal Training Engine](https://github.com/a370373/UTE-Universal-Training-Engine)
- [0-or-1](https://github.com/a370373/0-or-1)
- [MyDNS](https://github.com/a370373/MyDNS/tree/main)
- [Cyber-Fly-Android-Bridge](https://github.com/a370373/Cyber-Fly-Android-Bridge)
- [My-ADB-Shell](https://github.com/a370373/My-ADB-Shell/tree/main)
- [Cyber-Fly](https://github.com/a370373/Cyber-Fly)
- [MyOS](https://github.com/a370373/MyOS)
- [RWM-1:1 Real World Minecraft](https://github.com/a370373/RWM-Real-World-Minecraft)
- [MyAI - Offline Personal AI Agent System](https://github.com/a370373/MyAI-Offline-Personal-AI-Agent-System-/tree/main)
- [WCL - Web Clone Lab](https://github.com/a370373/web-clone-lab/)
- 持續增加中… 👀

---

## 🤖 AI 協作

MyAI 由 a370373/XRH 發起、設計與開發。

開發過程中使用 OpenAI ChatGPT 作為 AI 協作夥伴，協助進行技術分析、程式碼檢查、除錯與文件整理。

產品方向、設計理念與最終決策由專案創作者負責。
