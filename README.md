# OR-Tools Experience Minimal

未経験から「OR-Tools を触ったことがある」ではなく、**小さな最適化問題を自分でモデル化し、解き、結果を説明できる**状態になるためのミニマムな学習リポジトリです。

Google OR-Tools は、割当、パッキング、スケジューリング、ルーティング、ネットワークフロー、整数・線形計画などを扱える最適化ツール群です。このリポジトリでは、最初の到達点を CP-SAT と Routing に絞ります。

## ゴール

このリポジトリを終えると、次のことができます。

- 変数・制約・目的関数を Python コードに落とす
- CP-SAT で割当・ナップサック・シフト表を解く
- Routing Solver で小さな巡回・配送問題を解く
- 解けた結果を「なぜその答えなのか」と説明する
- 小さな業務問題を `data/` に置いて、自分のモデルに変換する

## セットアップ

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

uv を使う場合:

```bash
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

## 実行順序

```bash
python examples/01_cp_sat_basic.py
python examples/02_assignment_cp_sat.py
python examples/03_knapsack_cp_sat.py
python examples/04_shift_scheduling_cp_sat.py
python examples/05_tsp_routing.py
pytest
```

## 学習ロードマップ

| Step | ファイル | 学ぶこと |
|---|---|---|
| 1 | `01_cp_sat_basic.py` | 変数、制約、探索、ステータス |
| 2 | `02_assignment_cp_sat.py` | 0/1変数、割当、目的関数 |
| 3 | `03_knapsack_cp_sat.py` | 容量制約、価値最大化 |
| 4 | `04_shift_scheduling_cp_sat.py` | スケジューリング、充足制約、業務っぽい制約 |
| 5 | `05_tsp_routing.py` | Routing Solver、距離行列、経路最適化 |

## 経験者に見えるためのチェックリスト

- [ ] 「変数」「制約」「目的関数」を分けて説明できる
- [ ] CP-SAT は整数中心でモデル化する、と説明できる
- [ ] `solver.StatusName(status)` を見て結果を確認できる
- [ ] 小さな表データを OR-Tools の入力に変換できる
- [ ] 解が出ない場合に、制約が強すぎる可能性を疑える
- [ ] Routing と CP-SAT の使い分けを説明できる

## 次に広げるなら

- ジョブショップスケジューリング
- 複数車両配送問題 VRP
- 時間窓付き配送 VRPTW
- Min-Cost Flow
- pandas / CSV 入力対応
- FastAPI で最適化 API 化

## 参考

- Google OR-Tools 公式ドキュメント
- OR-Tools Python Reference
- CP-SAT modeling recipes
