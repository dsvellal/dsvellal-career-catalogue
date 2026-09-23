# Social Media And The World Of Microservices

> Converted from presentation `Social Media And The World Of Microservices.pptx`


## Slide 1: Social Mediaand the world of Microservices

- Dattatreya S Vellal
- dsvellal@gmail.com


## Slide 2: Let’s play a game!

- Identify the icons!


## Slide 3: Facebook!

- 2.38 billion active users per month!
- 1.56 billion active users per day!
- 1.15 billion active users per day on mobile!
- 5 new profiles created every second!
- 300 million photos uploaded per day!
- Average time spent on Facebook – 20 mins
- 83 million fake profiles!
- Every 60 seconds - 510,000 comments are posted, 293,000 statuses are updated, 136,000 photos are uploaded
- As of May 2019 - https://zephoria.com/top-15-valuable-facebook-statistics/


## Slide 4

- 3.5 billion searches are made every day!
- 40000 searches per second!
- 100 Petabytes of data indexed with Google!
- 60% of Google searches are done via mobile devices!
- Google captures 95% of the mobile search engine market in the U.S.
- As of May 2019 - https://www.wordstream.com/blog/ws/2019/02/07/google-search-statistics


## Slide 5

- Over 1.9 billion logged in users per month!
- 8 out of 10 18-49 year-olds watch YouTube!
- YouTube is the world’s second largest search engine!
- YouTube is the third most visited site after Google and Facebook!
- 400 hours of video are uploaded to YouTube every minute!
- We watch over 1 billion hours of YouTube videos a day!
- There are 1,000,000,000 mobile video views per day!
- As of May 2019 - https://www.brandwatch.com/blog/youtube-stats/


## Slide 6

- Instagram has 1 billion monthly active users
- 64% of 18-29 year olds use Instagram
- Instagram has 2 million monthly advertisers
- The most-liked photo has 53 million likes
- Over 100 million photos are uploaded every day
- The most popular hashtag is #love
- Users spend 53 minutes a day on Instagram
- The platform gets 4.2 billion likes per day
- Over 100 million Instagrammers watch live video each day
- As of May 2019 - https://sproutsocial.com/insights/instagram-stats/


## Slide 7: Data-centers!

- Google: 16 data centers throughout the world. 900,000 servers in all its data centers based in world. 260 million watts of power consumption enough to consistently power 200,000 homes.
- Amazon has around 450,000 servers in its data centers in 7 locations around the world. Amazon stores around 40 billion objects on it and is basically in the cloud storage business. Amazon Web Services has around 40,000 servers dedicated to its cloud customers and gets around 17 million monthly visitors who access 410TB of data from its platform. Around 30 million of Amazon users stream around 40 PB of videos per month.
- Facebook: Facebook servers process around 2.4 billion pieces of content and 750TB (terabytes) of data every day. The standard storage rack in Facebook uses 8 Kilowatts of power. Facebook has data worth over 100 PB (petabytes) capacity. Facebook claimed that its users utilize a total of around 7PB of photo storage from its facility every month.
- Microsoft: With over 1 billion users and 100,000 individual servers, Microsoft has spent approximately $23 million on its data centers. In 1989, Microsoft came up with its first data center which was 89,000 square feet. In 2006, they designed their own data center with 500,000 square feet and in 2013, built a $112 million facility.
- As of May 2019 - https://www.ciena.com/insights/articles/Twelve-Mind-blowing-Data-Center-Facts-You-Need-to-Know.html


## Slide 8: MICRO-SERVICES

- 8
- ▫What are micro-services?
- ▫Why do we want them? Or maybe not..


## Slide 9: but ﬁrst…

- 9


## Slide 10: Ball of Mud



## Slide 11



## Slide 12



## Slide 13: MICRO-SERVICES

- 13
- ▫What are micro-services?
- ▫Why do	we	want them? Or maybe	not..


## Slide 14

- Marek Sotak  @sotak


## Slide 15: SIMPLE AND LIGHTWEIGHT

- A monolithic application puts all its  functionality into a single process…
- A microservices architecture puts  each element of functionality into a  separate service…
- 15


## Slide 16: INDEPENDENT PROCESSES

- 16


## Slide 17

- LANGUAGE AGNOSTIC APIS
- “be of the  web”
- 17


## Slide 18: DECOUPLED

- 18


## Slide 19: MICRO-SERVICES

- 19
- ▫What are	micro-services?
- ▫Why do we want them? Or maybe not..


## Slide 20: The right tool for the job

- 20


## Slide 21: RESILIENCE

- GET /status/ HTTP/1.1
- Host: internal.service.com
- HTTP/1.1 200 OK
- <?xml version="1.0" ?>
- <html>
- <body>
- <div id="healthchecks">
- <ul>
- <li class="up">application database</li>
- <li class="up">external service</li>
- </ul>
- </div>
- </body>
- </html>
- GET /status/ HTTP/1.1
- Host: internal.service.com
- //ssttaattuuss
- HTTP/1.1 503 Service Unavailable
- <?xml version="1.0" ?>
- <html>
- <body>
- <div id="healthchecks">
- <ul>
- <li class="up">application database</li>
- <li class="down">external service</li>
- </ul>
- </div>
- </body>
- </html>
- 21


## Slide 22: SCALING

- A monolithic application puts all its  functionality into a single process…
- … and scales by replicating the  monolith on multiple servers
- A microservices architecture puts  each element of functionality into a  separate service…
- … and scales by distributing these services  across servers, replicating as needed.
- 22


## Slide 23: DEPLOYMENT

- compile, unit  and
- functional test
- integration  test
- acceptance  test
- user acceptance	performance  test		test
- deploy to  production
- run on build  machine
- deployed on  build  machine
- deployed to  integration  environment
- deployed to  UAT
- environment
- deployed to  performance  environment
- 23


## Slide 24: REPLACEABLE SERVICES

- A microservices architecture puts  each element of functionality into a  separate service…
- 24


## Slide 25: Preparing for the unknown

- 25


## Slide 26: MORE INTEGRATION

- http://combio.gist.ac.kr/wp-content/uploads/2013/05/Gene-microRNA-Network3.2png


## Slide 27: MONITORING AND TESTING

- 33


## Slide 28: More conﬁguration management

- http://www.clker.com35


## Slide 29: Deployment

- compile, unit  and
- functional test
- integration  test
- acceptance  test
- user acceptance	performance  test		test
- deploy to  production
- run on build  machine
- deployed on  build  machine
- deployed to  integration  environment
- deployed to  UAT
- environment
- deployed to  performance  environment
- 29


## Slide 30: Q&A

- dsvellal@gmail.com
- http://bit.ly/2VMimKI
