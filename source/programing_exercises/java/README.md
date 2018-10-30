# FizzBuzz

## 仕様
+ 3で割り切れる場合は「Fizz」を出力する
+ 5で割り切れる場合は「Buzz」を出力する
+ 両方で割り切れる場合は「FizzBuzz」を出力する
+ 上記以外の場合は数字を返す
+ 繰り返し実行できるようにする
+ タイプごとに出力を変える

## 設計
### TODOリスト
+ ~~3ならばFizzを返すようにする~~
+ ~~5ならばBuzzを返すようにする~~
+ ~~15ならばFizzBuzzを返すようにする~~
+ ~~上記以外の場合は数字を返す~~
+ ~~5回連続実行されたならば配列を返すようにする~~

## 開発
### ふりかえり
#### KEEP
#### PROBLEM
+ Javaのプロジェクト構成のセットアップにはまる
+ パッケージスコープではまる
+ 配列のテストケースではまる
+ Javaのシングルクォートとダブルクォートの扱いにはまる
+ ゲッター・セッターの実装を調べる
+ データクラスとロジッククラスの存在
+ 一つのクラスに異なる責務
+ 長いメソッド・大きいクラス
+ 似たような処理の重複
+ マジックナンバーの使用
+ 外部に公開されたSetter
+ 副作用のある代入変数


#### TRY
+ Gradleを理解する
+ Javaのスコープを理解する
+ Javaの配列を理解する

## 参照
+ [Gradle 覚書](https://qiita.com/summer/items/ba5393e703f3d5a74e8a)
+ [Gradle4.6 からの JUnit5 実行方法](https://mike-neck.hatenadiary.com/entry/2018/03/02/073000)
+ [Organizing Gradle Projects](https://docs.gradle.org/current/userguide/organizing_gradle_projects.html)
+ [Build Init Plugin](https://docs.gradle.org/current/userguide/build_init_plugin.html)
+ [JUnit5 テストの記述](http://www.ne.jp/asahi/hishidama/home/tech/java/junit/5/assertion.html)