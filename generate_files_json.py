import pathlib, json, re

base = pathlib.Path(__file__).parent
order = ['[입문] 배열_문자열_함수.md', '[입문] 정수론.md', '[입문] 재귀.md', '[입문] 시간복잡도_공간복잡도.md', '[초급] 정렬.md', '[초급] 선형자료구조.md', '[초급] 컨테이너_STL.md', '[초급] 집합_맵.md', '[초급] 브루트포스.md', '[초급] 백트래킹.md', '[초급] 탐욕법.md', '[초급] DFS_BFS.md', '[초급] 클래스_객체지향.md', '[중급] 분할정복.md', '[중급] 이분탐색_투포인터.md', '[중급] 누적합_슬라이딩윈도우.md', '[중급] 조합론.md', '[중급] 비트마스크.md', '[중급] 동적계획법.md', '[중급] 트리순회.md', '[중급] 최단경로.md', '[중급] 유니온파인드_MST_위상정렬.md', '[고급] 세그먼트트리_레이지.md', '[고급] 펜윅트리_스파스테이블.md', '[고급] 최소공통조상_LCA.md', '[고급] 강한연결요소_2SAT.md', '[고급] 문자열_KMP_트라이.md', '[고급] 기하_CCW_볼록껍질.md', '[고급] 네트워크플로우_이분매칭.md', '[고급] 동적계획법_심화.md']

files = []
all_files = ["목차.md"] + order
for fname in all_files:
    path = base / fname
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    m = __import__('re').search(r'^#\s+(.+)$', text, flags=__import__('re').MULTILINE)
    title = m.group(1).strip() if m else fname
    level = "목차"
    if "[입문]" in fname: level = "입문"
    elif "[초급]" in fname: level = "초급"
    elif "[중급]" in fname: level = "중급"
    elif "[고급]" in fname: level = "고급"
    files.append({"name": fname, "path": fname, "level": level, "title": title})

with open(base / "files.json", "w", encoding="utf-8") as f:
    json.dump(files, f, ensure_ascii=False, indent=2)
print(f"Regenerated files.json with {len(files)} entries")
