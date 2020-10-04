FROM python
WORKDIR /usr/src/app
COPY /resources .
COPY /uploads .
COPY credentials.json .
COPY requirements.txt .
CMD ['pip install -r requirements.txt']
COPY budget.py .
COPY parsingtesting.py .
COPY parsing.py .
COPY main.py .
COPY ocr.py .
EXPOSE 8000
CMD ['python main.py']