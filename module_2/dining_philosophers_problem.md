# Module 2 Project

## Part 1: Dining Philosophers Proiblem

### Description

To recap, here's the problem description:

> Five silent philosophers sit at a round table with bowls of noodles. One chopstick is placed between each pair of adjacent philosophers.

> Each philosopher must alternately think and eat. However, a philosopher can only eat noodles when they have both left and right chopsticks. Each chopstick can be held by only one philosopher and so a philosopher can use the chopstick only if it is not being used by another philosopher. After an individual philosopher finishes eating, they need to put down both chopsticks so that the chopsticks become available to others. A philosopher can take the chopstick on their right or the one on their left as they become available, but cannot start eating before getting both chopsticks.

> Eating is not limited by the remaining amounts of noodles or stomach space; an infinite supply and an infinite demand are assumed.

> The problem is how to design a discipline of behavior (a concurrent algorithm) such that no philosopher will starve; i.e. each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think.

The given procedure (that needs to be improved) is:
> * eat for a set amount of time once they are holding both chopsticks
> * set down the right chopstick
> * set down the left chopstick
> * pick up the left chopstick as soon as it becomes available
> * pick up the right chopstick as soon as it becomes available
> * repeat

The problem is this can lead to a deadlock where two philosophers each only have one chopstick, yet don't put it down because they hgaven't eaten yet. What we want is to devise a way for a philosopher to either *not pick up* a chopstick *if* the person next to them already has one, or to *place down* a chopstick if the person next to them already has one.

### Assignment

> So that everyone gets to eat, there are some situations in which philosophers *should* pick up a chopstick, and some situations in which they should NOT (because another philosopher needs to use it).

> Write a better solution to the dining philosophers problem so that deadlock does NOT occur.

### My proposed solution

Here's how I propose to modify the above procedure: 
* eat for a set amount of time once they are holding both chopsticks
* set down the right and left chopsticks
* pick up the left chopstick **if** the philosopher on their left has 0 chopsticks
* pick up the right chopstick **if** the philosopher on their right has 0 chopsticks
* **NEW:** place down the left chopstick if the philosopher on their left has 1 chopstick
* **NEW:** place down the right chopstick if the philosopher on their right has 1 chopstick

### Analysis

Does this solution avoid deadlocks? What happens when 2 philosophers each have 1 chopstick?

First, assume they're *not* right next to each other. Since there are 5 philosophers, that means that precisely *one* other philosopher must be eating. (There can't be 2 other eating philosophers because there are only 5 chopsticks; if 4 of them are being used to eat, there's only 1 chopstick remaining for someone to hold.) That means there are 3 chopsticks being shared among 4 non-eating philosophers, in which case 2 of them must be right next to each other.

In other words, no matter what, if 2+ philosophers have 1 chopstick, at least 2 of them must be right next to each other.

Then, per the new rules outlined above, one of them will place down their chopstick, depending on seat placement--e.g., if A is on the left of B, and B only has their left chopstick, they'll place it down (A would keep theirs because they would only have **their** left chopstick).

Therefore, it appears that my new procedure avoids deadlocks.
