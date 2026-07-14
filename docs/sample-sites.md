# 参考サイト

## 1. Google OR-Tools（必須）

[google/or-tools](https://github.com/google/or-tools?utm_source=chatgpt.com)

ライブラリ本体。

見るべきディレクトリは

* `examples/python`
* `ortools/constraint_solver`
* `examples/notebook`

です。

ここで

* TSP
* VRP
* Time Windows
* Capacity Constraints

などの基本が全て分かります。([GitHub][1])

---

## 2. GitHub Topics: vehicle-routing（おすすめ）

[GitHub Topics: vehicle-routing](https://github.com/topics/vehicle-routing?o=asc&s=stars&utm_source=chatgpt.com)

これがかなり面白いです。

OR-Toolsを使ったプロジェクトが大量に出てきます。

例えば

* FastAPI
* Leaflet
* React
* OR-Tools

を組み合わせたものが見つかります。([GitHub][2])

---

## 3. dynamic-route-optimization

GitHub Topicsの中でも特に実務に近いものです。

特徴

* FastAPI
* OR-Tools
* Leaflet地図表示
* マルチ車両対応

つまり

```text
Browser
   ↓
FastAPI
   ↓
OR-Tools
```

という典型的な構成になっています。([GitHub][2])

---

## 4. VRPTW Python + React

[Vehicle Routing Problem Time Windows Solver Comparison](https://github.laiyagushi.com/arnobt78/Vehicle-Routing-Problem-Time-Windows-Solver-Comparison--VRPTW-Python-React?utm_source=chatgpt.com)

これは研究寄りですが、

構成が非常に参考になります。

```
React
    ↓
FastAPI
    ↓
Solver
        ├─ OR-Tools
        ├─ HGS
        ├─ ACO
        └─ SA
```

となっていて、

Solverを交換できる設計になっています。([GitHub][3])

---

## 5. Bosch Route Optimisation

[Vehicle Route Optimisation (Bosch Hackathon)](https://rohitdavas.github.io/Vehicle-Route-Optimisation/?utm_source=chatgpt.com)

学生コンテストですが、

かなり完成度が高く、

READMEも読みやすいです。([Rohit Kumar Portfolio][4])

---

# 私が一番おすすめする見方

あなたの場合は、

**「Solverのコード」より「リポジトリ構造」**

を見る方が何倍も勉強になります。

例えば、

```text
backend/
    api/
    services/
    optimization/
        solver.py
        distance_matrix.py
        constraints.py

frontend/
    map/
    dashboard/

data/

docker-compose.yml

README.md
```

こういう構造になっている理由を考えると、

「Solverは業務システム全体の一部でしかない」

ということが自然に理解できます。

---

## あなた向けにもう一段おすすめしたいテーマ

あなたはこれまで

* Kubernetes
* GitOps
* Rancher
* Cloud Native

を体系的に整理してきました。

同じ発想で、

**「Optimization Architecture Study」**

という視点でGitHubを眺めると面白いと思います。

例えば、

* 地図（Google Maps / OSRM / GraphHopper）
* 距離行列生成
* OR-Tools
* REST API
* Dispatcher Dashboard
* PostgreSQL
* バッチ実行
* KPIダッシュボード

という**業務アーキテクチャ全体**を対象にすると、単なるアルゴリズム学習ではなく、「物流最適化システムはどう設計されるのか」というレベルまで理解できます。これは、コンサルティング案件や実運用システムにかなり近い視点です。

[1]: https://github.com/google/or-tools?utm_source=chatgpt.com "GitHub - google/or-tools: Google's Operations Research tools: · GitHub"
[2]: https://github.com/topics/vehicle-routing?o=asc&s=stars&utm_source=chatgpt.com "vehicle-routing · GitHub Topics · GitHub"
[3]: https://github.laiyagushi.com/arnobt78/Vehicle-Routing-Problem-Time-Windows-Solver-Comparison--VRPTW-Python-React?utm_source=chatgpt.com "GitHub - arnobt78/Vehicle-Routing-Problem-Time-Windows-Solver-Comparison--VRPTW-Python-React: A full-stack (R&D) Vehicle Routing Problem with Time Windows (VRPTW) comparison platform. Run and benchmark metaheuristic algorithms HGS, ACO, SA, GLS (v0.6.3) & ILS (v0.13+), visualize routes, tune parameters, and explore Solomon benchmark datasets—with an optional AI-assisted RAG Q&A and parameter tuning capabilities. · GitHub"
[4]: https://rohitdavas.github.io/Vehicle-Route-Optimisation/?utm_source=chatgpt.com "Vehicle-Route-Optimisation | Solving VRP problem using ORTOOLS routing library"
