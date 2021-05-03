I am asked the below question in Rubrik System coding just yesterday. They focus a lot on concurrency. This is asked in the first screening round. I don't think I did a good job and I likely wouldn't be considered further. This is for a senior role.

Question
Implement following method of ScheduledExecutorService interface in Java

schedule(Runnable command, long delay, TimeUnit unit)
Creates and executes a one-shot action that becomes enabled after the given delay.

scheduleAtFixedRate(Runnable command, long initialDelay, long period, TimeUnit unit)
Creates and executes a periodic action that becomes enabled first after the given initial delay, and subsequently with the given period; that is executions will commence after initialDelay then initialDelay+period, then initialDelay + 2 * period, and so on.

scheduleWithFixedDelay(Runnable command, long initialDelay, long delay, TimeUnit unit)
Creates and executes a periodic action that becomes enabled first after the given initial delay, and subsequently with the given delay between the termination of one execution and the commencement of the next.