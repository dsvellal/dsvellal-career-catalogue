# Reference Pipelines

> Converted from presentation `Reference Pipelines.pptx`


## Slide 1: Reference pipelines



## Slide 2: Basic blocks & pluggable task

- Note: Pluggable task can be executed locally and/or globally


## Slide 3: Stage

- …
- …
- Note: Pluggable stage can be executed locally and/or globally


## Slide 4: Pipeline

- Note: Pluggable pipeline can be executed locally and/or globally


## Slide 5: Monitoring & it’s responsibilities

- Monitoring generates a triplet (timestamp, key, value)
- There are time, frequency, statistics based counters listening to key-value pairs.
- 1:1, 1:many, many:1, many:many, key-value-pairs: counters are configurable.
- Counters trigger alerts based on rules.
- Rules to trigger alerts of the counters are configurable.
- Examples of alert rules:
- (1:1, frequency) - Alert if there is <at least> <1> failed unit-test
- (1:many, time) - Alert if <within 10hrs> there are <1000> exceptions
- (many:1, time) - Alert if <CPU Usage> goes <above> <90%> && <RAM Usage> is <greater than> <85%>
- (many:many, statistics) - Alert if the <90th percentile> of <avg. response time> is <greater than> <100 ms>


## Slide 6: Actions and its responsibilities

- Actions work on alerts.
- There can be 1:1, 1:many, many:1, many:many – alert:action configurations.
- Multiple alerts can be configured to be aggregated to trigger one or more actions.
- Multiple alert aggregates can be configured to trigger one or more actions.
- Examples of actions:
- (1:1) – Upon unit test execution failure alert, send email notification to configured recipients.
- (1:many) – Functional test failure alert, upload the report to a central location and send email notification with the link to the report, to configured recipients.
- (many:1) – Upon receiving CPU usage > 90 alert and Memory usage > 90%, send email notification for environment stability and infrastructure issues to the configured recipients


## Slide 7: Sample pluggable task:

- Pluggable stage: Local: Quality-at-desk
- Pluggable task:
- Artifact
- Source: Code repository
- Analysis execution:
- Compiler warnings for java
- Analyzer:
- Xlint
- Monitoring:
- Regex: [warning]
- Source: log
- Action:
- Fail build on first compiler warning
- Send email to:
- Recipients:
- dsvellal@philips.com
- simao.williams.@philips.com
- Publish metrics
- Source: metrics-url-source.
- Other pluggable tasks:
- Linter violations per language
- Duplication detection per language
- Similarity detection per language
- Dead code detection per language
- Cyclomatic complexity per method
- Static-analysis of asserts per unit-tests
- Spellcheck per language
- Grammar check for relevant file-types (md)
- Dead-url checker for relevant file-types
- Commit-size check
- Commit-traceability check
- Commit-comment syntax check
- Unit test execution
- Mutation testing
- NFR testing
- Performance testing
- Security testing
- UAT etc.


## Slide 8: Sample pipeline – on developer machine



## Slide 9: Sample pipeline – on build machine



## Slide 10: Sample pipeline of pipeline – on customer environment

- Deployment on customer staging environment
- Deployment on customer production environment


## Slide 11: Sample implementation *staged execution*

- https://tfsemea1.ta.philips.com/tfs/TPC_Region21/PS_I2M/_git/IoT.SuperPOM?path=%2Fpom.xml&version=GBmaster
- https://tfsemea1.ta.philips.com/tfs/TPC_Region21/PS_I2M/_git/Processing_Common?path=%2Fcerberus.gradle&version=GBmaster
- https://github.com/philips-software/docker-blackduck
- https://github.com/philips-software/sonar-scanner-action
- https://github.com/philips-software/cerberus/actions
