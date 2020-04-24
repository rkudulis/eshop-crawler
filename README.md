# E-Shop crawler

Some real time problems could be solved in hour of manual work but why bother doing it in the ordinary way?

Few days ago I have surfed [geradovana.lt](https://www.geradovana.lt) for a gift. It was quite tough to choose the best one without gathering information in one place.

So I decided to write tiny little web spider to do the job for me. It took about 1 hour reading Scrapy documentation and 1 hour making it alive. The result is quite impressive. Scrapy library is such a handy tool to build a spyder in a reasonable amount of time.

It's my first web crawler after working directly with Beautifulsoup library.

#### Run Spider

```
pip install scrapy=2.0.1
```

Run following command ignoring DEBUG information
```
$ scrapy crawl gera_dovana -L ERROR
```

The script will take about minute and  produce `json` file on the root directory.
