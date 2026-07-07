# Modeling Notes

## OR-Tools で考える基本形

最適化問題は、だいたい次の形に分解する。

1. 何を決めるか: decision variables
2. 何を守るか: constraints
3. 何を良くするか: objective
4. 解いた結果をどう読むか: solution interpretation

## CP-SAT の感覚

CP-SAT は「整数・真偽値の組み合わせ問題」に強い。割当、スケジュール、組合せ選択などに向く。

よく使う変数:

- `NewBoolVar`: する / しない
- `NewIntVar`: 整数範囲

よく使う制約:

- `Add`
- `AddExactlyOne`
- `AddAtMostOne`
- `AddAllowedAssignments`

## Routing Solver の感覚

Routing Solver は、配送・巡回・車両ルートなどに向く。最初は「距離行列を作って、最短ルートを探す」と考えればよい。

## ミニマム経験者の説明テンプレート

> この問題では、まず何を決めるかを BoolVar / IntVar として定義しました。次に、業務上守るべき条件を制約として追加し、最後にコスト最小化または価値最大化の目的関数を置きました。解が出ない場合は、制約が強すぎるか、入力データに矛盾がある可能性を確認します。
