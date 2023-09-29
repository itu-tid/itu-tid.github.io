
# Usability

Usability is a quality attribute that assesses how easy user interfaces are to use. It is usually thought as decomposable further in more precise qualities: 

1. **Learnability** - How easy is it for users to accomplish basic tasks the first time they encounter the design?

3. **Efficiency** - Once users have learned the design, how quickly can they perform tasks?

4. **Memorability** - When users return to the design after a period of not using it, how easily can they reestablish proficiency?

5. **Absence of Errors** - How many errors do users make, how severe are these errors, and how easily can they recover from the errors?

6. **Satisfaction** - How pleasant is the use of the design?

## Heuristics

Heuristics -- loosely defined rules that are likely to help, but are not laws - they can be "broken" if necessary. 

One of the most popular set of heuristics for interactive systems is the one of Jakob Nielsen. 

Published in 1994 in the book “Usability Inspection Methods” by Jakob Nielsen and Robert L. Mack. They were a refinement of an earlier set of heuristics by Nielsen and Molich --  a dane. 

1. [Visibility of system status](usability_examples/1_status.md)
2. [Match between system and the real world](usability_examples/2_match.md)
3. [User control and freedom](usability_examples/3_control.md)
4. [Consistency and standards](usability_examples/4_consistency.md)
5. [Error prevention](usability_examples/9_error_prevention.md)
6. [Recognition rather than recall](usability_examples/6_recognition_rather_than_recall.md)
7. [Flexibility and efficiency of use](usability_examples/7_flexibility_and_efficiency.md)
8. [Aesthetic and minimalist design](./usability_examples/8_aesthetics.md)
9. [Help users recognize, diagnose, and recover from errors](usability_examples/8_help_users_recover_from_errors.md)
10. [Help and documentation](usability_examples/10_documentation.md)


Heuristic evaluation is based _solely_ on an agreed set of recognized heuristics

Other sets of heuristics exist besides the Nielsen ones. E.g., [ISO standard 9241-110 from 2020](https://www.dialogdesign.dk/isos-dialogue-principles-2019/) proposes: 
- seven principles, 
- 20 categories of recommendations, 
- 65 recommendations, and about 
- 140 examples take up 15 densely printed pages in the standard 

Limitation of heuristic evaluation: usability is more complex than what can be captured in 10 rules. 

**For you:** Learn one set of heuristics. An expert _has the knowledge in their head_.


## Usability Testing

The golden standard of usability evaluation is usability testing. This is when you evaluate with users a prototype or an actual system.

Rules of thumb: 
- The more detailed and realistic, the more you can trust your results; the more effort it takes to make changes if you've made a wrong decision
- The less detailed, the less you invest in creating it, the earlier you can detect problems

Sometimes you don't start from scratch: evaluating an existing prototype for usability is even easier - you don't have to create the prototype. You go straight to the next steps.


### The Participants

Three kinds of participants
- The log keeper - writes down observations 
- The facilitator - explains and helps cautiously, when needed
- The users - test the prototype / system

### The Users

Must be representative for your target population.

Best is to have them think aloud. You can also just observe, but it's less valuable. 

After your first mockup, probably one or two users are sufficient -- if they are representative. You'll get sufficient feedback to go back to the drawing board. 

### The Tasks

You need to prepare a **set of tasks** that are representative or important for the system. Then you ask the users to try to solve them using the system. 

The tasks should be expressed from the POV of the user, not from the POV of the system. They should express a need or a problem that a typical user of the system encounters. 

Avoid suggesting which UI elements to be used. That will skew the results. 

Avoid trivial tasks. The tasks should be "something that should give the user a feeling of achievement when they are done". As Lauesen proposes, a task is something after which the user can tell himself: I've done that, I can go and have a coffee now. What does this mean about logging in as a task? 

### Test Report

The report ranks and prioritizes the problems discovered during the usability testing. It is different than the log. It summarizes the findings based on all the participants. 

One possible way of classifying the tasks severity is proposed by Lauesen who argues for five severity classes: 
- Missing functionality or bug
- Task failure 
- Cumbersome
- Medium problem: succeeds, but user is slow
- Minor: success with a bit of hesitation





## Bibliography

*Nielsen Heuristics with Examples*, Rolf Molich. [Web Page at Rolf Molich's Websitej](https://www.dialogdesign.dk/nielsens-heuristics-1994/)
*User Interface Design*, Søren Lauesen, Addison Wesley.
*Turn User Goals into Task Scenarios for Usability Testing*, Marieke McCloskey [Web Page at nngroup](https://www.nngroup.com/articles/task-scenarios-usability-testing/)

# Project Work 👬
- Evaluate the usability of your Lo-Fi prototype 
- Record brief notes of the usability test outcome 
- Write a usability report in which you prioritize the discovered issues
- Improve design if needed

