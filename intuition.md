# Intuition for the talk

## The one thing
If people remember one sentence, it's: our work proposes a proxy to measure faithfulness in autoformalization. 

## Story arc (rough)
- Open with: What is autoformalization, why it's important, and why faithfulness is a problem. 
- The "aha": Maybe use the figure from the paper intro showing the roundtrip framework. Intuititevely, if T2 is correct, then an unfaithful T1 translation will be caught by the UNSAT check. Don't get into the details of the SAT/UNSAT check. Just give a high-level idea of what motivates the roundtirp method, and how it can be used to measure faithfulness.
- Then the method, at the level of: just the idea. This time we have repair too. So you gotta use the full figure from the paper. 
- Results: Make sure you start with explaining the domains first. Then you have to talk about our NLI signal and what we mean by drift. Use the flowchart categorizing NLI signals. Then I guess you can present the figure 4 in the paper showing SAT ones drift more than UNSAT ones. I'd like to show the table of results too (table 1), showing that full repair is a good choice under the condition that diagnosis is done properly. And there are ablations too. So make sure to decoupel these concepts and explain them clearly. I trust your gut. 
- Mention failure modes mentioned in the paper. 
- End on: Talk about limitations. Also add another limitation that in real-world we might have multiple faithful encodings for a singel natural language statement (Give an example in Lean). Add future work interest in how do design reward models for faithfulness to drive RL/post-training of LLMs for more faithful autoformalization.
- We do some formalization in the paper of the roundtrip method, and have a psuedocode for it too. These are FM people and will think the work is solid if they see formalizations, instead of just prompting LLMs. If you find a nice way to incorporate it, please do. 
- I also want you to mention that it was accepted into the findings of Association for Computational Linguistics: EMNLP 2026. 

## Emphasize
- ...

## Downplay or skip
- Related work mostly can be skipped I believe. No need to contaimnate the talk with too many other people's work. Read the paper and select best ones, where we can positino ourselves against them.
- Things that can live in backup slides: Figures and tables in the appendix. 

## Running example
- We don't have one in the paper, so I think it's fine to skip this. I don't want you to pick a dirty running example that the encoding is not straightforward and followable. 

## Where people get confused
- None

## Time budget (rough)
- Motivation ~X min, method ~Y, results ~Z: I leave this allocation decision to you. Total is 20 minutes (hard limit). 

## Don'ts
- Do not use em dash/hyphens or semicolons anywhere in the talk. Use commas or parantheses instead.
- Do not use advanced English vocabulary (don't try to to be fancy)
- Do not try to show off and oversell anything 