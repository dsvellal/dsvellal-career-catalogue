# DoTheRightThing PSRewritePerformanceImprovements December16th2014

> Converted from presentation `DoTheRightThing_PSRewritePerformanceImprovements_December16th2014.pptx`


## Slide 1: IF Plan SelectionRewrite and Data Layer adoption

- Improvements
- 1


## Slide 2: Artifacts repository

- SVN: svn://172.17.10.60/onegate/branches/3.3.2.10-hix-portlet-rewrite-poc/
- Dev: http://ogapp3.3.2.10prtlrewrt.og.devexeter.com:7004/web/guest
- Test: http://ogapp3.3.2.10prtltestrewrt.og.devexeter.com:7004/web/guest
- Reference Deployment tickets:
- http://172.17.0.100:8080/jira/browse/ONEGATECORE-23764
- http://172.17.0.100:8080/jira/browse/ONEGATECORE-23491
- Hudson Jobs: http://172.17.0.77:8080/hudson/view/3.3.2.10prtlrewrt/
- 2


## Slide 3: Approach

- Layered approach
- Data Layer
- Abstraction of Siebel Entities into OneGate Entities
- UI messages
- Application properties
- UI Layer
- Self painting and self-validating pages
- Centralized tags
- Centralized UI model
- Configurable UI flows*
- Biz. Layer
- Centralized transformations
- Centralized Utilities
- * Work In Progress. Configurations need to move to DB. They currently reside in code.
- 3


## Slide 4: Abilities

- Ability to
- Configure UI Page-order
- Support breadcrumbs on Plan Selection
- Extensively log using a single logging framework
- Pull context based entities/message via xpaths
- Support multiple languages
- Implement DL session-context share across portlets
- Support CORE v/s State v/s Implementation flavors of configurations and messages
- 4


## Slide 5: Improvements

- Improved maintainability
- Reduced lines of code
- Improved comments
- Unit-tested methods
- Centralized & Structured UI model (style-sheets, tags, jsps)
- Improved readability
- Structured and templatised coding practices
- Java-docs and comments
- Improved adoptability
- Easy to adopt the design into other portlets
- High degree of reusability
- 5


## Slide 6: % Reductions

- * - projected no, includes pages that are yet to be implemented. We are currently at 10 jsp’s.
- 6


## Slide 7: Flow wise Old v/s New

- 7


## Slide 8: Page-wise Timers on the new flow

- 8


## Slide 9: Further Enhancements

- All Siebel writes through data-layer (DL)
- Biz. methods sit on DL (rating(), remediate())
- One-UI adherence
- Field level Audit trail capability
- DL fine-tuning and performance improvements
- Error handling framework with useful error pages
- 9


## Slide 10: IF Plan SelectionRewrite and Data Layer adoption

- Backup Slides
- 10


## Slide 11: Backup slides

- 11
- No. of lines of jsp codes – before v/s after


## Slide 12: Backup slides

- 12
- Performance Run – 1HHM on 3.3.2.10 revamped flow.


## Slide 13: Backup slides

- 13
- Performance Run – 1HHM on 3.3.2.10 old flow.
