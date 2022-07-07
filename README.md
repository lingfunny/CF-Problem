# CF-Problem

python + BeautifulSoup4

源代码：[test.py](/test.py)

效果如 [caught.txt](/caught.txt)。

格式之后会慢慢修。

参数：

```python
limit = -1 # 爬取 Round >= limit 的题目
url = 'https://codeforces.com/problemset/page/1?tags=3500-'
```

关于 `url`：

前面的 `https://codeforces.com/problemset/page/1?` 属于保留字串，后面可以添加形如：

- `tags=constructive algorithms` 筛选所有构造题
- `tags=constructive algorithms, 3000-3500` 筛选难度位于 $[3000, 3500]$ 的构造题
- `tags=fft,dp,3000-` 筛选难度位于 $[3000, +\infty)$ 且标签含有 fft、dp 的题
- `tags=data structure,-2000` 筛选难度位于 $(-\infty, 2000]$ 的数据结构题

比如：

```python
limit = 1000
url = 'https://codeforces.com/problemset/page/1?tags=data structure,-2000'
```

将会爬出所有难度在 $2000$ 以下且 ID 比 1000 大的所有数据结构题。
