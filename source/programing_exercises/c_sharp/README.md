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
+ ~~値が３ならばFizzを返す~~
+ ~~値が５ならばBuzzを返す~~
+ ~~値が１５ならばFizzBuzzを返す~~
+ ~~値が１ならば１を返す~~
+ ~~値が１０１ならば１０１を返す~~
+ ~~５回実行したら配列を返す~~
+ ~~１０回実行したら配列を返す~~
+ ~~タイプ１は値を返す~~
+ ~~タイプ２はFizzだけを返す~~
+ ~~タイプ３はBuzzだけを返す~~
+ ~~タイプ４は通常パターンを大文字に変換して返す~~
+ ~~タイプ５は２で割り切れたらFizz３で割り切れたらBuzz２と３で割り切れたならFIZZBUZZを返す~~


## 開発
+ データクラスの作成を通して[メンバー](https://docs.microsoft.com/ja-jp/dotnet/csharp/programming-guide/classes-and-structs/members)の概念を理解する
+ [バッキングフィールド](https://docs.microsoft.com/ja-jp/dotnet/csharp/programming-guide/classes-and-structs/properties)を使用したプロパティの実装をする
+ 選択ステートメントからswitch文を実装する
+ データクラスとロジッククラスの存在 -> メンバ変数にインライン化する
+ 外部に公開されたSetter -> カプセル化
+ case文 -> 抽象クラスの導入
+ プリミティブ強迫症
+ 一つのクラスに異なる責務
+ 長いメソッド・大きいクラス
+ 似たような処理の重複
+ マジックナンバーの使用
+ 副作用のある代入変数

### ふりかえり
#### Keep
#### Problem
#### Try

## 参照
+ [.NET Core と .NET Standard の単体テスト](https://docs.microsoft.com/ja-jp/dotnet/core/testing/)
+ [xUnit.net でユニットテストを始める](https://qiita.com/takutoy/items/84fa6498f0726418825d)
+ [C# プログラミング ガイド](https://docs.microsoft.com/ja-jp/dotnet/csharp/programming-guide/)
+ [ステートメントのキーワード (C# リファレンス)](https://docs.microsoft.com/ja-jp/dotnet/csharp/language-reference/keywords/statement-keywords)
+ [列挙型ではなく列挙型クラスを使用する](https://docs.microsoft.com/ja-jp/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/enumeration-classes-over-enum-types)