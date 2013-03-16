################
Logical Failures
################

:Date:
    2013-03-16

:Speaker:
    Luke Sneeringer

Why this talk?
==============

+ Identifying logical steps in your thinking.
+ All programmers are professional logicians.
+ Logical mistakes are easy to make; easier than you may think.

A Question
==========

+ Linda is 3 years old, single, outspoken, and very bright. She majored in
  philosophy. As a student, she was deeply concerned with issues of
  discrimination and social justice, and also participated in anti-nuclear
  demonstrations.

+ Which is more likely?

  - She's a bank teller. (Yes. 90% of people choose this)
  - Shes a bank teller in a womans rights movement. (No. 10%)

+ NO conjunction can be more probably than any of its conjuncts.

  - It's more likely that she's a bank teller than that she is both.

Just Enough Logic
=================

+ Logical languages look a lot like programming

  - Booleans: True vs. False
  - Operators: not, and, or, xor, if, iff (if-and-only-if)

Validity
--------

+ A set of statements if any of its values are true: NO
+ A statement is valid if all permises are true and conclusions are also true
+ Validity does not entail truth

  - Invalid conclusions may be true

+ Necessary & Sufficient conditions

  - Necessary: if any condition not met: can't be true
  - Sufficient: the oppositeo

+ Epistemology: The study of how we know what we know.

  - True belief + faulty reasoning is still true

Fallacies
=========

1. Asserting the Consequent

   - Given a conditional, concluding its converse.
   - If P, then Q

     * Assume P, Conclude Q

   - Inverse (modus tollens)
   - Converse isn't true
   - Example: "If it's raining, then the (uncovered) grass will be wet."

     * Valid: '"Grass not wet, therefore not raining."
     * Invalid: "Grass wee, therefore raining"
     * Invalid: "Grass dry, not raining."

2. Questionable Cause

   - A group of fallacies centered on misidentifying caues
   - P occured, therefore Q happened.
   - "We never had a problem with the air conditioner until you moved into
     the house."
   - Sequence is necessary but insufficient condition for causality.
   - "The code hasn't changed, therefore it can't be the cause."

3. Hasty Generalization

   - Reaching a conclusion w/ insufficient evidence
   - "3 is prime, 5 is prime, 7 is prime, therefore all odd numbers are
     prime."
   - NM has towns named "Pie Town" and "Truth or Consequences", therefore all
     cities in NM have awesome names.
   - "It works on my machine, therefore not a code problem."
   - User inputs that break because we didn't expect that input type.
   - NoSQL for *every solution*!!

4. False Compromise

   - Assuming that a compromise between two statements is correct.
   - If John wants to build a bridge across a 10-mile river, and I don't.

     * You don't build have the bridge.

   - Incrementalism (let's do some of all the things we want)

5. Regression Fallacy

   - Misattribution of causality.
   - When a statistically extreme circumstance occurs, it is usually followed
     by a return to normal circumstances.
   - Misinterpreting this return to normalcy as being the result of a
     response.
   - "Traffic cameras stop accidents."

     * Often installed after a seris of traffic fatalities
   
   - "Observe high cpu, ctake action, CPU goes down."

6. Argument From Fallacy

   - Concluding that because an argument is invalid, its conclusion must be
     false.
   - Invalid args may nonetheless have true conclusions.
   - Take what you learn, expand it, and learn to spot poor reasoning.
   - Don't throw out the conlsusion, correct the reasoning
