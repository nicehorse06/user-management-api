# 使用官方的 Python 映像作為基礎
FROM python:3.12-slim

# 設置工作目錄
WORKDIR /app

# 將 requirements.txt 複製到容器中
COPY requirements.txt .

# 安裝 Python 依賴
RUN pip install --no-cache-dir -r requirements.txt

# 將當前目錄內容複製到容器中
COPY . .

# 暴露端口 8000
EXPOSE 8000

# 運行 FastAPI 應用
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
