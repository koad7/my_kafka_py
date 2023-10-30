Can you identify issues with the current architecture? If so, list all possible issues.
 - The timers could fire at incorrect times due to clocks on the machines drifting.
 - Due to systems being dependent if the first system doesn't finish before the timer, then the second system will be operating with an in complete state.
 - If all of the jobs haven't finished and stored their results in the final storage when the reports run the reports will be incorrect. 
 - If someone wants a report quickly, they are forced to wait until the timer fires. 
 - When code changes are made to the system the feed back loop is the longer, as you have to wait for the timer to run.  


Think about what you can do it make it more modulur and resilient.
 - We can change the timers to events. This will allow the systems tell downstreams when to run. Meaning that if a system is going slower or faster then normal the speed of the system scales with it.
 - We can prevent systems directly dependent, by not passing events to the next system directly, but instead passing the event into a message bus, like Kafka. This will allow the downstream system to pick up the message once it's ready to start the next bit of work. 
 -  If we start using the message bus and we want to try a new system, we can have it start listening to new messages but not writing to the same customer facing storage. This way we can experiment without the risk of impacting customers. This also shortens the development cycle by letting us re-play old events to test new and existing systems.

What if the database is offline? How to we prevent complete system failures?
 - While we can't prevent every failure, what we can do is let messages in Kafka build up until the database is back online. Once the database is back online we can start procesing all of the delayed events and have reports flowing again without waiting for a timer.


There are some drawbacks to use this new system tho. For example if we accidentally replay old events without the correct state around them we could produce incorrect data. Debugging the system at large can become complicated as the message bus and the data-store could get out of sync. Meaning that old events may exist in the message bus, but the data they reference in data-store is gone. 
It's also more complex then what we had before, there are more moving parts and more things to keep running.