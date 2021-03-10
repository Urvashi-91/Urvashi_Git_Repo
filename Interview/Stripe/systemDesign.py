'''
How is tha cart updated when the application is open in multiple pages?
There are multiple options.

When an item is added to the cart, store the update in the server. Therefore a page refresh on any tab will keep everything up to date.
If you don't want to rely on a refresh, you could try some sort of polling mechanism. If the web browser onFocus event happens (assuming it's there), poll the server for a quick update if there is one.
Could using local storage be a safe option?
What if the shopping cart service is down, how would you handle it?
This depends on what behaviour we want when the service is down. Ideally, we would have some replicas so if a node goes down we can just go to another one and get the same consistent data. If all nodes are down, there is no server communication. We can revert to using the local storage in the browser.

What if there are 10M requests at a time ?
We obviously would want to route these services. So if we have 10m requests at a time, does that mean 10m requests a second? Assuming so, that's an extremely high number, so we obviously would want a load balancer (or two, maybe in passive passive or passive active mode) which would route these requests of different nodes of our system. Assuming a beefed up web server today can handle 500k requests per second, we need 20 servers at the very least. Let's leave a margin of safety and have 30 servers all serving 333k requests per second. If we use AWS EC2 instances as nodes, we can use AWS ELB to build up to this scale. If we do everything ourselves, we would want to probably distribute the load, say, based on the hash of the user ID who is logged in. We can always add more nodes as needed if we employ consistent hashing.

How to build a checkout system?
This could be a separate application. There are a lot of questions to ask here, i.e. are we handling taxes ourselves, are we handling discounts/coupons, we can send an HTTP POST request to a service to initiate a checkout, assumning the user has already given us shipping destination and all that. I won't go into too much detail here.

To integrate payment options you can use something like Stripe to handle payments, or build something similar yourself. This is a non trivial task. You need to use HTTPS to take card number, expirt, CVC, etc and store things in a very secure place. I'm not sure if all that data is stored as is, non-hashed in a payment system, but you do not ever want to expose that data once you have received it. You can pass a hash of the card or a fingerprint to the frontend during checkout where they pick cards. You should only expose the last 4 digits of the card, card type, and perhaps the expiry month or year. You pass the hash of the card or something when they select a payment method, and use that.
'''