My Jupyter Notebook
===================
# 目的 #
俺のノートブック

# 前提 #
| ソフトウェア   | バージョン   | 備考        |
|:---------------|:-------------|:------------|
| python          |3.7.0    |             |


# 構成 #
1. [構築](#構築 )
1. [配置](#配置 )
1. [運用](#運用 )
1. [開発](#開発 )

## 構築
### sphinxのセットアップ
```
pip install sphinx
```
### プロジェクトの作成
+ Separate source and build directories (y/n) [n]: y
+ Project name: my_notebooks
+ Author name(s): k2works
+ Project version []: 1.0.0
+ Project language [en]: ja

```
sphinx-quickstart
```
### デザインテーマの変更
```
pip install sphinx_rtd_theme
```
### 

### PlantUML対応
```
pip sphinxcontrib-plantuml
```

### 自動ビルド対応
```
pip install sphinx-autobuild
make livehtml
```

### Jupyterノートブック取り込み
```
pip install nbsphinx
```
`conf.py`
```
extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
]
exclude_patterns = ['_build', '**.ipynb_checkpoints']
```

**[⬆ back to top](#構成)**

## 配置
**[⬆ back to top](#構成)**

## 運用
**[⬆ back to top](#構成)**

## 開発
**[⬆ back to top](#構成)**

# 参照 #
+ [SPHINX](http://www.sphinx-doc.org/ja/stable/index.html)
+ [sphinx でドキュメント作成からWeb公開までをやってみた](https://qiita.com/kinpira/items/505bccacb2fba89c0ff0)
+ [reStructuredTextチートシート](http://teambtrb.com/2017/08/20/post-464/)
+ [Sphinxを便利にして、みんなに使ってもらいたい](https://qiita.com/kinpira/items/505bccacb2fba89c0ff0)
