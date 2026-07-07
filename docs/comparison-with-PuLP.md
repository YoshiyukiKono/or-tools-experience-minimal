
## PuLPとは

PuLP は、

> **数理最適化モデルを書くためのモデリングライブラリ**

です。

PuLP自身は解きません。

例えば、

```python
x = LpVariable(...)
```

などと書いてモデルを作り、

* CBC
* Gurobi Optimizer
* IBM ILOG CPLEX Optimization Studio

などのソルバーに渡します。

つまり

```
PuLP
    ↓
ソルバー(CBCなど)
```

という構成です。

---

## OR-Toolsとは

Google OR-Tools は、

モデリングライブラリでもあり、
ソルバーも持っています。

例えば

```
CP-SAT
Linear Solver
Routing Solver
```

など複数のソルバーが含まれています。

---

## 「ヒューリスティック」の意味

これは主に

**Routing Solver**

について言われることが多いです。

例えば

* 巡回セールスマン問題(TSP)
* 配送計画(VRP)

はNP困難なので、

1000地点

を厳密に解くのは現実的ではありません。

そこで

```
Greedy
Local Search
Tabu Search
Guided Local Search
Simulated Annealing
```

などを組み合わせて

> 良い解を高速に探す

仕組みになっています。

つまり

Routing Solver
≒
ヒューリスティック色が強い

ということです。

---

## しかしCP-SATは違う

一方、

OR-Toolsで現在一番人気なのは

**CP-SAT**

です。

これは

```
制約プログラミング
+
SAT
+
整数計画
```

を融合したソルバーです。

基本的には

* 分枝限定
* SAT探索
* カット生成
* 伝播

などを駆使して

**最適解を証明しながら探索**

します。

もちろん時間制限を付ければ途中終了しますが、

本質的には

> 厳密解法

です。

---

## PuLPとの比較

|            | PuLP  | OR-Tools   |
| ---------- | ----- | ---------- |
| 役割         | モデリング | モデリング＋ソルバー |
| 線形計画       | ○     | ○          |
| 整数計画       | ○     | ○          |
| CP         | ×     | ◎          |
| SAT        | ×     | ◎          |
| Routing    | ×     | ◎          |
| Scheduling | △     | ◎          |

---

## 学習順

1. **PuLP**で「数理モデルとは何か」を学ぶ
2. **OR-Tools CP-SAT**で現代的な制約最適化を学ぶ
3. **OR-Tools Routing**で配送・経路最適化を学ぶ

という順番が最も理解しやすいと思います。

実際、近年の業務システムでは「シフト作成」「生産計画」「配置計画」などはCP-SATが採用されるケースが増えており、一方で配送や巡回計画ではRouting Solverのヒューリスティックが強みを発揮します。つまり、「OR-Toolsはヒューリスティック」というよりも、**問題の種類に応じて厳密解法とヒューリスティックの両方を使い分けられる総合的な最適化ライブラリ**と捉えるのが適切です。

## 参考

(PuLPとOR-Tools (CP-SAT) の実装を見比べながらOR-Toolsの入門)[https://zenn.dev/fusic/articles/4f7e69bf13e7fb]
