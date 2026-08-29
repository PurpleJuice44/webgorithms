# 알고리즘 클래스 - GitHub Pages 배포 가이드

이 폴더는 GitHub Pages로 바로 배포할 수 있는 정적 사이트입니다.

## 구조
```
algorithm_class/
├── index.html              # 진입점 (목차를 띄우는 SPA)
├── files.json              # 31개 md 파일 목록 (자동 생성)
├── generate_files_json.py  # 새 md 추가 시 목록 재생성 스크립트
├── 목차.md                 # 메인 페이지 (기본 로드)
├── [입문] *.md / [초급] *.md / [중급] *.md / [고급] *.md  # 30개 알고리즘 문서
├── .mermaid_images/        # PDF용 mermaid 렌더링 캐시 (웹에서는 미사용, 클라이언트 렌더링)
└── .nojekyll               # GitHub Pages가 _* 파일을 무시하지 않도록
```

## 로컬에서 보기
```bash
cd algorithm_class
python -m http.server 8000
# 브라우저에서 http://localhost:8000 접속
# 또는
npx serve .
```

> **주의:** 파일을 `file://`로 직접 열면 `fetch()`가 차단되어 md를 불러올 수 없습니다. 반드시 HTTP 서버로 실행하세요.

## GitHub Pages 배포

### 방법 1: 이 폴더를 리포지토리 루트로 푸시
```bash
cd algorithm_class
git init
git add .
git commit -m "feat: 알고리즘 클래스 30개 + 목차 + 웹 뷰어"
git branch -M main
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```
GitHub > Settings > Pages > Source: `Deploy from a branch` > Branch: `main` / `root`

### 방법 2: 기존 리포지토리의 `docs/`로 복사
```bash
cp -r algorithm_class/* <your-repo>/docs/
# .nojekyll도 함께 복사
cp algorithm_class/.nojekyll <your-repo>/docs/
```
Settings > Pages > Source: `main` / `docs`

## 업데이트 방법 (추후 새 md 추가 시)

1. 새 파일을 `[난이도] 이름.md` 형식으로 추가 (예: `[중급] 투포인터_심화.md`)
2. 목록 재생성:
```bash
python generate_files_json.py
```
3. 커밋 & 푸시하면 사이트에 자동 반영 (사이드바에 새 항목 표시)

`generate_files_json.py`는 `목차.md`에 정의된 권장 순서(`order` 배열)를 기준으로 `files.json`을 다시 생성합니다. 새 파일을 목차 순서에 맞게 끼워 넣으려면 `order` 배열에 파일명을 추가하세요.

## 동작 방식
- `index.html`은 `files.json`을 읽어 사이드바를 구성
- 클릭 시 `fetch()`로 해당 `*.md`를 불러와 `marked`로 HTML 변환, `mermaid`로 도식 렌더링, `highlight.js`로 코드 하이라이트
- URL 해시(`# [입문] 재귀.md`)로 딥링크 지원 — 링크 복사/새로고침 시 해당 문서가 그대로 열림
- 목차 내부의 상대 링크(`[입문] 배열_문자열_함수.md`)도 자동 가로채서 SPA 내에서 열림

## PDF는?
웹 뷰어가 생기면서 PDF 생성은 선택 사항이 되었습니다. 필요하면 기존 스크립트로 재생성할 수 있습니다:
```bash
python /tmp/md2pdf_kr.py  # 또는 generate_pdf_with_images.py
```
