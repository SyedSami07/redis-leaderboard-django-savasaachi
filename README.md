## Try it out deploying on Heroku

<p>
    <a href="https://heroku.com/deploy" target="_blank">
        <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heorku" width="200px"/>
    <a>
</p>

<p>
    <a href="https://deploy.cloud.run/?dir=google-cloud-run" target="_blank">
        <img src="https://deploy.cloud.run/button.svg" alt="Run on Google Cloud" width="200px"/>
    </a>
    (See notes: How to run on Google Cloud)
</p>

## How to run on Google Cloud

<p>
    If you don't have redis yet, plug it in  (https://spring-gcp.saturnism.me/app-dev/cloud-services/cache/memorystore-redis).
    After successful deployment, you need to manually enable the vpc connector as shown in the pictures:
</p>

1. Open link google cloud console.

![1 step](https://github.com/redis-developer/basic-redis-leaderboard-demo-python/raw/master/docs/1.png)

2. Click "Edit and deploy new revision" button.

![2 step](https://github.com/redis-developer/basic-redis-leaderboard-demo-python/raw/master/docs/2.png)

3. Add environment.

![3 step](https://github.com/redis-developer/basic-redis-leaderboard-demo-python/raw/master/docs/3.png)

4. Select vpc-connector and deploy application.

![4  step](https://github.com/redis-developer/basic-redis-leaderboard-demo-python/raw/master/docs/4.png)

<a href="https://github.com/GoogleCloudPlatform/cloud-run-button/issues/108#issuecomment-554572173">
Problem with unsupported flags when deploying google cloud run button
</a>

## 1. How the data is stored

<ol>
    <li>The AAPL's details - market cap of 2,6 triillions and USA origin - are stored in a hash like below:
      <pre> <a href="https://redis.io/commands/hset">HSET</a> "company:AAPL" symbol "AAPL" market_cap "2600000000000" country USA</pre>
     </li>
    <li>The Ranks of AAPL of 2,6 trillions are stored in a <a href="https://redislabs.com/ebook/part-1-getting-started/chapter-1-getting-to-know-redis/1-2-what-redis-data-structures-look-like/1-2-5-sorted-sets-in-redis/">ZSET</a>.
      <pre><a href="https://redis.io/commands/zadd">ZADD</a>  companyLeaderboard 2600000000000 company:AAPL</pre>
    </li>
</ol>

<br/>



