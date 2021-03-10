'''
/*
## Setup

The flow of a dispute is as follows:
- A charge is created by an end customer.
- Stripe receives a dispute record from the bank.
- The business responds with evidence.
- If no second dispute is received within 30 days after evidence submission, the dispute is won. If a second dispute is
received, the dispute is lost.

Charge
(Maybe) Dispute Record
(Maybe) Evidence submission
(Maybe) Second Dispute Record

The raw tables generated from the API look like:

Charges
+---------------+-----------+
| charge_id | varchar |
| created | timestamp |
| amount | int |
| seller_id | varchar |
| customer_id | varchar |
+---------------|-----------+

Dispute Records
+----------------+-----------+
| dispute_id | varchar |
| created | timestamp |
| charge_id | varchar |
+----------------|-----------+

Evidence Submission
+-------------------+-----------+
| evidence_id | varchar |
| created | timestamp |
| charge_id | varchar |
+-------------------|-----------+

*/

/*

1. Can you design a unified dispute table that would allow us to compute things like the win rate, dispute rate, evidence
submission rate etc?

*/
'''

This depends if there is a possibility that there are >2 disputes or >1 evidence per charge_id. But if we are sure that max disputes is 2 and max evidences is 1, then we just join these tables and return 4 columns (charge, dispute1, evidence, dispute2):

select c.charge_id, d1.dispute_id, e.evidence_id, d2.dispute_id
from Charges as c
left join Disputes as d1
  on c.charge_id = d1.charge_id
left join Evidences as e
  on c.charge_id = e.charge_id
left join Disputes as d2
  on c.charge_id = d2.charge_id
where
  (d1.created is null or d1.created > c.created)
  and (e.created is null or e.created > d1.created)
  and (d2.created is null or d2.created > e.created)
Then we can count how many non-nullable columns there are. For example, win rate is sum(evidence is not null and dispute2 is null) / sum(evidence is not null).