# Wiki Graph


![](https://raw.githubusercontent.com/suriyadeepan/wiki-graph/master/lowres.jpg)

The program takes a wiki url, say (https://en.wikipedia.org/wiki/Transhumanism) as input and crawls over wikipedia to find other article connected to it. This is done recursively, until the user manually stops the crawl. 

## Requirements


1. [scrapy](http://scrapy.org/)
2. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
3. [graph-tool](https://graph-tool.skewed.de/)

## How to run?


	-  Change the start_url list at line\#9 of [wiki-spider.py](/wiki-spider.py)
	-  Run the spider for an arbitrary amount of time.

```bash
scrapy runspider wiki-spider.py -o wiki.json
```

	- Add ']' to the last line of *wiki.json* 
	- Build the graph based on *wiki.json*

```bash
python3 wiki-graph.py
```
	- Adjust the parameters of **graph_draw( )** function to suit you
