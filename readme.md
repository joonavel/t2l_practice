# Text to SQL 프로젝트 관련 간단한 실행 코드 입니다.

## 세팅
### 1. .env
.env 파일에 다음을 작성한 뒤 저장하세요
OPENAI_API_KEY="your api key"
LANGCHAIN_TRACING_V2=false
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="your api key"
LANGCHAIN_PROJECT="test"
db_uri="sqlite:///chinook.db"


### 2. db 다운로드
터미널에 다음 코드를 입력하여 zip 파일을 다운받고 .git과 동일한 디렉토리에 압축 해제하세요
wget https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip -O chinook.zip


### 3. 실행
각 py 파일의 question을 원하는 질문으로 채우면 됩니다.