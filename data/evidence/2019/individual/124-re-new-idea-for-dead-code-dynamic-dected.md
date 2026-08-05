# Evidence: Re: New idea for Dead code dynamic dected

## Source
- **File:** `Re  New idea for Dead code dynamic dected.msg`
- **Date:** 2019-09-25
- **Ingested:** 2026-08-04
- **Channel:** email_archive
- **Category:** General / Other

## Email Metadata
- **From:** "YU, Stephen" <stephen.yu@philips.com>
- **To:** "Vellal; Dattatreya" <dsvellal@philips.com>; "Jiang; Chao"	<chao.jiang@philips.com>
- **CC:** "Williams; Simao" <simao.williams@philips.com>; "Jagadeesan; Sundaresan"	<sundaresan.j@philips.com>
- **Date:** 2019-09-25T23:38:12-04:00
- **Thread depth:** 15
- **Is reply:** True
- **Attachments:** 3
  - `image001.png` (image/png, 51273 bytes)
  - `image002.png` (image/png, 63285 bytes)
  - `image003.png` (image/png, 13950 bytes)

## Datta's Involvement
- **Role at time:** Competency Specialist – Software Excellence, Software Center of Excellence
- **Involvement type:** Direct recipient — explicitly mentioned/praised

## Key Quotes
> To: "Vellal; Dattatreya" <dsvellal@philips.com>; "Jiang; Chao"	<chao.jiang@philips.com>

> Thanks Datta, we have a brief view of your plugin and we think it will be really helpful, because we intend to combine these things(memory objects profile, ES plugin, object usage trend) together.

> To: Vellal, Dattatreya <dsvellal@philips.com>; Jiang, Chao <chao.jiang@philips.com>

> Thanks for your advice about putting the memory profiling data in ES then we can trace historical data and do the analysis.

> Thanks a lot for your great support.

## Full Email Content

```
Subject: Re: New idea for Dead code dynamic dected
From: "YU, Stephen" <stephen.yu@philips.com>
To: "Vellal; Dattatreya" <dsvellal@philips.com>; "Jiang; Chao"	<chao.jiang@philips.com>
CC: "Williams; Simao" <simao.williams@philips.com>; "Jagadeesan; Sundaresan"	<sundaresan.j@philips.com>
Date: 2019-09-25T23:38:12-04:00

--- Latest Reply ---
Thanks Datta, we have a brief view of your plugin and we think it will be really helpful, because we intend to combine these things(memory objects profile, ES plugin, object usage trend) together.


  1.  Collect the classes(interface abstract class) which defined in the whole project.
  2.  Continually do the memory profiling(snapshot) to find which objects are using, syn data to ES using plugin.
  3.  After some time, the objects usage trend will be displayed, also the objects which defined but not uploaded in memory(at snapshot time) can be found.

Best regards,
Stephen.

--- Previous Message (1) ---
Date: Monday, September 23, 2019 at 1:12 PM
To: "YU, Stephen" <stephen.yu@philips.com>, "Jiang, Chao" <chao.jiang@philips.com>
Cc: "Williams, Simao" <simao.williams@philips.com>, "Jagadeesan, Sundaresan" <sundaresan.j@philips.com>
Subject: RE: New idea for Dead code dynamic dected

Hello Stephen, here’s the metrics client that I have written: https://docs.philips.com/:f:/g/personal/dsvellal_philips_com/EtIzIh-I0ohChq4RL1czYQsBrq8EFVYsqwUGMbZ1s0oBYw?e=tnkpnr<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdocs.philips.com%2F%3Af%3A%2Fg%2Fpersonal%2Fdsvellal_philips_com%2FEtIzIh-I0ohChq4RL1czYQsBrq8EFVYsqwUGMbZ1s0oBYw%3Fe%3Dtnkpnr&data=02%7C01%7C%7C238372cbbd834f2accc408d74232f554%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C637050658940620971&sdata=9bmjexR9Nt%2BOaJqrbDPYT5EmEvZufyzxslBf3u6b6O4%3D&reserved=0>
I’d be happy to help go through the program. Let me know.

--- Previous Message (2) ---
Datta

--- Previous Message (3) ---
Sent: Friday, September 20, 2019 1:52 PM
To: Vellal, Dattatreya <dsvellal@philips.com>; Jiang, Chao <chao.jiang@philips.com>
Cc: Williams, Simao <simao.williams@philips.com>; Jagadeesan, Sundaresan <sundaresan.j@philips.com>
Subject: Re: New idea for Dead code dynamic dected

Hi Datta,

Thanks for your advice about putting the memory profiling data in ES then we can trace historical data and do the analysis.

Currently we are doing these things to detect “dead code”(for java/spring framework projects) ,
·         1. We are creating a tool/agent to expose a web hook to expose the “thread dead lock” detection data(reading from JVM), if a “dead lock” is happened after the program running for some time, and the web hook be invoked, then the data can feed to some monitoring system like Prometheus we are currently using.
·         2. Most of our projects in CDI are java/Spring web framework based, according to objects that Spring managed, we can trace the reference chain between the objects, then there is opportunity that some object without referral can be detected(defined but not used).


Please let us know your thought about above items.

By the way, could you provide us the plugin/introduction you mentioned to us? We can check how to  integrate it into our projects then benefit the projects.

Thanks a lot for your great support.

Best regards,
Stephen.

--- Previous Message (4) ---
Date: Friday, September 20, 2019 at 2:15 PM
To: "Jiang, Chao" <chao.jiang@philips.com<mailto:chao.jiang@philips.com>>, "YU, Stephen" <stephen.yu@philips.com<mailto:stephen.yu@philips.com>>
Cc: "Williams, Simao" <simao.williams@philips.com<mailto:simao.williams@philips.com>>, "Jagadeesan, Sundaresan" <sundaresan.j@philips.com<mailto:sundaresan.j@philips.com>>
Subject: RE: New idea for Dead code dynamic dected

Hi Chao, Stephen,
Dynamically identifying dead-code in production is a great idea to implement. While the approach suggested (doing CPU & memory profiling) can reveal a lot data about usage of classes/methods and memory, it may not lead to dead-code detection directly. One approach that I’d like you guys to consider is to see if we can start leaving tracers (in terms of log statements, metrics injected into elastic search etc.) and see if we can trend the tracers over a time period. This coupled with the CPU and memory profiling data, will definitely help identify a lot of data-points.

I can work with your team in identifying & making this happen. Infact, if the code-base is in Java, I have already written a client-plugin, that’s customizable to the relevant elastic-search instance, to start injecting metrics data from any program. I would be happy to share that code as well.

Let me know.

--- Previous Message (5) ---
Datta

--- Previous Message (6) ---
Sent: Friday, September 6, 2019 1:30 PM
To: Jiang, Chao <chao.jiang@philips.com<mailto:chao.jiang@philips.com>>; Williams, Simao <simao.williams@philips.com<mailto:simao.williams@philips.com>>; Vellal, Dattatreya <dsvellal@philips.com<mailto:dsvellal@phi

[... truncated, full content in database ...]
```