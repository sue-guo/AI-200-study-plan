# Day 1: AI-200 大纲、环境搭建、Azure SDK 认证基础

日期：2026-05-28

## 今天目标

完成后你应该有：

- Python、Azure CLI、VS Code 可用
- 一个 `ai200-day01` 练习文件夹
- 一个 Python 虚拟环境
- 知道 AI-200 考什么
- 初步理解 Azure SDK 如何通过身份认证连接 Azure 服务

## 官方学习资料

- AI-200 Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200
- Azure AI Cloud Developer Associate: https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/
- Azure SDK for Python Overview: https://learn.microsoft.com/en-us/azure/developer/python/azure-sdk-overview
- Configure Python web app local environment: https://learn.microsoft.com/en-us/azure/developer/python/configure-python-web-app-local-environment

## 具体完成步骤

### 1. 检查工具

```powershell
python --version
az --version
code --version
git --version
```

如果 `az --version` 提示没有安装，可以用 Chocolatey 安装 Azure CLI。先用管理员权限打开 PowerShell，然后运行：

```powershell
choco install azure-cli -y
```

安装完成后关闭当前 PowerShell，重新打开一个新的 PowerShell，再检查：

```powershell
az --version
```

### 2. 登录 Azure CLI

```powershell
az login
az account show
```

如果暂时没有 Azure 账号，可以跳过这一步。Day 1 先完成本地环境、Python 虚拟环境、`azure-identity` 安装和 `DefaultAzureCredential` 概念学习即可。

后续需要真实 Azure 资源时，可以选择：

- Azure Free Account: 新 Azure 用户通常可获得限时免费额度和部分免费服务。
- Azure for Students: 如果你有符合条件的学校邮箱，可以优先考虑学生订阅。
- 工作或学校账号: 如果公司/学校提供 Azure 订阅，可以用它做实验，但要先确认费用规则。

没有账号时，今天的完成标准改为：能安装 Azure CLI，并理解 `az login` 是连接 Azure 订阅的步骤；不要求实际登录成功。

### 3. 建练习文件夹

```powershell
mkdir ai200-day01
cd ai200-day01
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

### 4. 安装今天需要的包

```powershell
pip install azure-identity python-dotenv
pip freeze > requirements.txt
```

### 5. 新建 `check_env.py`

```python
import sys
from azure.identity import DefaultAzureCredential

print("Python version:", sys.version)
print("DefaultAzureCredential object created successfully")

credential = DefaultAzureCredential()
print(type(credential).__name__)
```

### 6. 运行

```powershell
python check_env.py
```

今天不要求它真的访问 Azure 服务，只要能创建 `DefaultAzureCredential` 对象即可。真正调用 Azure 服务后续再做。

## 今天笔记

- [ ] AI-200 不是纯 AI 理论考试，而是 Azure 云开发 + AI 数据服务 + 容器 + 安全监控。
- [ ] 考试重点包括 containerized solutions、data management services、Azure service integration、security/monitoring/troubleshooting。
- [ ] Azure SDK for Python 分为 client libraries 和 management libraries。
- [ ] `azure-identity` 提供 Azure 身份认证能力。
- [ ] `DefaultAzureCredential` 会按顺序尝试多种认证来源，比如本地登录、环境变量、托管身份等。

## 完成标准

- [ ] 工具版本检查完成
- [ ] Azure CLI 能登录或至少确认安装成功
- [ ] 虚拟环境创建成功
- [ ] `requirements.txt` 生成成功
- [ ] `check_env.py` 能运行
- [ ] 读完 AI-200 官方大纲并记下考试四大模块
