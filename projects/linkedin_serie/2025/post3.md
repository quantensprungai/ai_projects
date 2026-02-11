
YouYou Tech-Reality-Translator | Future Impact ResearchTech-Reality-Translator | Future Impact Research 4mo • Edited • 
 4 months ago • Edited • Visible to anyone on or off LinkedIn
EMPIRISCHE REALITÄT vs. TIMELINE-DEBATTE

KI-Forscher Ryan Greenblatt zeigt https://lnkd.in/erbHZwx5: AGI-Entwicklung 2025 langsamer als extreme Prognosen. METR-Daten dokumentieren 7-Monats-Verdoppelungszyklen - exponentiell, aber bisher vorhersagbar statt explosive takeoff.

Gleichzeitig heute: Salesforce CEO: "4.000 Entlassungen, weil ich weniger Köpfe mit KI brauche."

→ Timeline-Debatten sind akademisch
→ Arbeitsplatz-Effekte passieren JETZT
→ Von 1-Sekunden-Tasks zu 1-Stunden-Tasks in 6 Jahren = strukturelle Transformation

Deutsche Planung übersieht: Auch "langsamere" KI-Entwicklung hat bereits heute Auswirkungen auf Arbeitsmärkte.

Was siehst du in deinem Umfeld? 


Zeitnah: Teil 4 meiner AGI Strategic Navigation Serie
hashtag#StrategicPlanning hashtag#AI hashtag#FutureOfWork hashtag#Innovation hashtag#Hochschulentwicklung


My AGI timeline updates from GPT-5 (and 2025 so far)
by ryan_greenblatt
20th Aug 2025
AI Alignment Forum

As I discussed in a prior post, I felt like there were some reasonably compelling arguments for expecting very fast AI progress in 2025 (especially on easily verified programming tasks). Concretely, this might have looked like reaching 8 hour 50% reliability horizon lengths on METR's task suite[1] by now due to greatly scaling up RL and getting large training runs to work well. In practice, I think we've seen AI progress in 2025 which is probably somewhat faster than the historical rate (at least in terms of progress on agentic software engineering tasks), but not much faster. And, despite large scale-ups in RL and now seeing multiple serious training runs much bigger than GPT-4 (including GPT-5), this progress didn't involve any very large jumps.

The doubling time for horizon length on METR's task suite has been around 135 days this year (2025) while it was more like 185 days in 2024 and has been more like 210 days historically.[2] So, progress was maybe around 50% faster than it was historically as judged by this metric. That said, the data seem consistent with this being driven by a one-time bump as of the o3 release, with progress since then being closer to the historical average rate. I expected somewhat more improvement on agentic software engineering tasks this year than we've seen thus far.

My current guess is that AI progress will feel relatively steady for the next year or two with a roughly similar rate of (qualitative) progress as we've seen on average over the last 2 years (which is pretty fast, but not totally crazy). I expect doubling times of around 170 days on METR's task suite (or similar tasks)[3] over the next 2 years or so which implies we'll be hitting 2 week 50% reliability horizon lengths around the start of 2028. I don't see particular reasons to expect qualitatively faster AI progress over the next 2 years, but I do think that there is a plausible case for slightly superexponential horizon lengths in this 2 year period based on generality arguments. (Longer term, I expect superexponentiality to make a bigger difference.[4] More generally, I think horizon lengths will stop being very meaningful beyond 1 month 80% reliability time horizons.[5] That said, I don't expect we'll have good benchmarks that can effectively measure horizon lengths this long.)

I do think that progress in 2025 looking on or somewhat above trend for SWE horizon length is an update toward continued pretty fast progress over a longer period, rather than hitting the top of the sigmoid shortly after GPT-4.

(Slower progress is plausible due to diminishing returns on RL from a fixed level of pretrained model. We haven't seen a long enough period of RL scaling to be very confident in continued returns and it is notable that pretraining appears to be delivering weaker returns than it did historically. From my understanding GPT-5 probably isn't based on a substantially better pretrained model which is some evidence that OpenAI thinks the marginal returns from pretraining are pretty weak relative to the returns from RL.)

If we extrapolate out 170 day doubling times until we see 80% reliability on 1 month long tasks, we get that this is 4 years away. At 1 month long horizon lengths, I think AI R&D progress might start speeding up substantially due to automation. I don't feel very confident extrapolating things out for 4 years, especially because compute scaling will likely start slowing down around the end of this period and substantially superexponential improvements in horizon length seem plausible as we reach this level of generality.

So how do our observations this year update my overall timelines? I now think that very short timelines (< 3 years to full AI R&D automation) look roughly half as likely and my timelines are generally somewhat longer. At the start of this year, I was thinking around 25% probability that we see AI capable of full automation of AI R&D by the start of 2029 (4 years away at the time) and around a 50% chance of this by the start of 2033 (8 years away at the time). I now would put ~15% probability by the start of 2029 and a 45% chance by the start of 2033.

My lower probability on full automation of AI R&D by the start of 2029 is driven by thinking that:

    We're pretty unlikely (25%?) to see 80% reliability at 1 month tasks by the start of 2028. (This would require 96 day doubling times on average which is substantially faster than I expect and 2x faster than the longer term historical trend.) At the start of 2025, I thought this was much more likely.
    The gap between 80% reliability at 1 month tasks and full automation of research engineering seems substantial, so I expect this would probably take substantially more than 1 year even taking into account AI accelerating AI R&D (at least without a single large breakthrough). I do think this will happen substantially faster if we condition on 80% reliability on 1 month tasks prior to the start of 2028, but it still seems like it would probably take a while.
    The gap between full automation of research engineering and full automation of AI R&D also seems significant, though this might be greatly accelerated by AIs automating AI R&D. Maybe this gap is in the rough ballpark of 3 months to 1.5 years. (Again, this gap would be somewhat smaller conditional on seeing full automation of research engineering in less than 3 years. That said, part of the story for how the gap between 80% reliability at 1 month tasks and full automation of research engineering could be small is that automating research engineering ended up being surprisingly easy; in this case, we'd expect the gap between research engineering automation and full automation to be bigger.)

In summary: 80% reliability at 1 month tasks by the start of 2028 seems unlikely and even conditional on that, it seems unlikely to go from there to full automation of AI R&D in the time required which lowers my probability somewhat further.[6]

I think there is a reasonable case that observations in 2025 should increase our chance of seeing full automation by 2033 due to increasing our confidence in extrapolating out the METR time horizon results with a pretty fast doubling time, but I don't think this argument outweighs other downward updates from not seeing atypically fast progress in 2025 (which I thought was pretty plausible).

It now looks to me like most timelines where we see full AI R&D automation before the start of 2028 involve some reasonably large trend-breaking breakthrough rather than just relatively steady fast progress using mostly known approaches.

    And mostly saturating SWE-bench verified without needing extra inference compute, and getting to perhaps 75-80% on Cybench. ↩︎

    This is using public release dates for models, so o3 is included in 2025. ↩︎

    The current METR task suite (and other benchmarks) might fail to effectively measure horizon lengths beyond around 8 hours or so. So, when I talk about longer time horizons, imagine an extension of METR's task suite that draws from roughly the same distribution but with longer/harder tasks. ↩︎

    My view is that superexponentiality is likely to make a big difference eventually, but is unlikely to make a huge difference (as in, causing much faster doubling times on average) prior to 1 month 80% reliability. I think this because: (1) the data thus far doesn't look that consistent with aggressive superexponentiality kicking in prior to 1 month (we've seen a decent amount of doublings and pure exponential still looks like a pretty good fit while superexponentiality is more complex), (2) my sense is that for humans, full generality kicks in around more like a few months than at around a week or a day (as in, the skills humans apply to do tasks that take a few months are the same as for a few years, but the skills used for tasks that take a day or a week aren't sufficient for tasks that take several months), and (3) I expect that generality will kick in later for AIs than for humans. (This footnote was edited in after this post was first published.) ↩︎

    As in, horizon lengths will no longer have a clear interpretation and the relationship between horizon lengths and what AIs can do in practice will become less predictable. ↩︎

    My biggest disagreements with Daniel Kokotajlo are: (1) I think that aggressive superexponentiality prior to 80% reliability on 1 month tasks is substantially less likely (I think it's around 10% or 15% likely while Daniel thinks it's more like 35% likely when operationalized as "2x faster average doubling times than the 170 day trend I expect due to superexponentiality") and (2) I think that the gap from 80% reliability on 1 month (benchmark) tasks to full automation of research engineering is probably pretty large (my median is maybe around 2 years, and minimally I think >1 year is more likely than not), even after accounting for AI R&D acceleration from AI automation and the possibility of significant superexponentiality. ↩︎

New to LessWrong?

Getting Started

FAQ

Library
1.

And mostly saturating SWE-bench verified without needing extra inference compute, and getting to perhaps 75-80% on Cybench.
2.

This is using public release dates for models, so o3 is included in 2025.
3.

The current METR task suite (and other benchmarks) might fail to effectively measure horizon lengths beyond around 8 hours or so. So, when I talk about longer time horizons, imagine an extension of METR's task suite that draws from roughly the same distribution but with longer/harder tasks.
4.

My view is that superexponentiality is likely to make a big difference eventually, but is unlikely to make a huge difference (as in, causing much faster doubling times on average) prior to 1 month 80% reliability. I think this because: (1) the data thus far doesn't look that consistent with aggressive superexponentiality kicking in prior to 1 month (we've seen a decent amount of doublings and pure exponential still looks like a pretty good fit while superexponentiality is more complex), (2) my sense is that for humans, full generality kicks in around more like a few months than at around a week or a day (as in, the skills humans apply to do tasks that take a few months are the same as for a few years, but the skills used for tasks that take a day or a week aren't sufficient for tasks that take several months), and (3) I expect that generality will kick in later for AIs than for humans. (This footnote was edited in after this post was first published.)
5.

As in, horizon lengths will no longer have a clear interpretation and the relationship between horizon lengths and what AIs can do in practice will become less predictable.
6.

My biggest disagreements with Daniel Kokotajlo are: (1) I think that aggressive superexponentiality prior to 80% reliability on 1 month tasks is substantially less likely (I think it's around 10% or 15% likely while Daniel thinks it's more like 35% likely when operationalized as "2x faster average doubling times than the 170 day trend I expect due to superexponentiality") and (2) I think that the gap from 80% reliability on 1 month (benchmark) tasks to full automation of research engineering is probably pretty large (my median is maybe around 2 years, and minimally I think >1 year is more likely than not), even after accounting for AI R&D acceleration from AI automation and the possibility of significant superexponentiality.
1.

Which also include troubles with fitting context into the attention span, since the IMO, consisting of short problems, mostly fell to unreleased LLMs. Amelioration of the limits could likely require large memory processed deep inside the model, making the neuralese internal thoughts a likely candidate.
2.

However, there is DeepSeek V3.1, released on Aug 20 or 21.
3.

Which could also be a separate model working with the CoT only, allowing the black box to be integrated into many different models.
169
Ω 57
Mentioned in
2422025 in AI predictions
155Trust me bro, just one more RL scale up, this one will be the real scale up with the good environments, the actually legit one, trust me bro
53Yes, AI Continues To Make Rapid Progress, Including Towards AGI
52AIs will greatly change engineering in AI companies well before AGI
34AI #131 Part 2: Various Misaligned Things
My AGI timeline updates from GPT-5 (and 2025 so far)
34snewman
22Vladimir_Nesov
21Bogdan Ionut Cirstea
15Josh You
8HiroSakuraba
5StanislavKrym
7yrimon
4james oofou
4yrimon
3Vladimir_Nesov
3christianvuye
3testingthewaters
2emile delcourt
2samuelshadrach
New Comment


14 comments, sorted by top scoring
Click to highlight new comments since: Today at 8:33 AM
[-]
snewman6mo3421

Nice analysis. I can't add anything substantive, but this writeup crystallized for me just how much we're all focusing on METR's horizon lengths work. On the one hand, it's the best data set we have at the moment for quantitative extrapolation, so of course we should focus on it. On the other hand, it's only one data set, and could easily turn out to not imply what we think it implies.

My only points are (a) we shouldn't weight the horizon length trends too heavily, and (b) boy do we need additional metrics that are both extrapolatable, and plausibly linked to actual outcomes of interest.
Reply
5
[-]
Vladimir_Nesov6moΩ7220

    GPT-5 probably isn't based on a substantially better pretrained model which is some evidence that OpenAI thinks the marginal returns from pretraining are pretty weak relative to the returns from RL

The model seems to be "small", but not necessarily with less pretraining in it (in the form of overtraining) than RLVR. There are still no papers I'm aware of on what the compute optimal (or GPU-time optimal) pretraining:RLVR ratio could be like. Matching GPU-time of pretraining and RLVR results in something like 4:1 (in terms of FLOPs), which would only be compute optimal (or GPU-time optimal) by unlikely coincidence.

If the optimal ratio of pretraining:RLVR is something like 1:10 (in FLOPs), then overtraining even smaller models is unimportant. But it could also be more like 40:1, in which case overtraining becomes a must (if inference cost/speed and HBM capacity of the legacy 8-chip servers force the param count to be smaller than compute optimal given the available training compute and the HBM capacity of GB200 NVL72).
Reply
[-]
Bogdan Ionut Cirstea6mo217

I think I agree directionally with the post.

But I've been increasingly starting to wonder if software engineering might not be surprisingly easy to automate when the right data/environments are used at much larger scale, e.g. Github issues (see e.g. D3: A Large Dataset for Training Code Language Models to Act Diff-by-Diff) or semi-automated pipelines to build SWE RL environments (see e.g. Skywork-SWE: Unveiling Data Scaling Laws for Software Engineering in LLMs), which seem potentially surprisingly easy to automatically scale up. It now seems much more plausible to me that this could be a scaling data problem than a scaling compute problem, and that progress might be fast. Also, it seems likely that there might be some flywheel effect of better AIs -> better automated collection + filtering of SWE environments/data -> better AIs, etc. And 'Skywork-SWE: Unveiling Data Scaling Laws for Software Engineering in LLMs' has already shown data scaling laws:


Also, my impression is that SWE is probably the biggest bottleneck in automating AI R&D, based on results like those in Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers
and especially based on the length of the time horizons involved in the SWE part vs. other parts of the AI R&D cycle. 
Reply
[-]
Josh You6mo151

    But I've been increasingly starting to wonder if software engineering might not be surprisingly easy to automate when the right data/environments are used at much larger scale

I've had similar thoughts: I think there's still low-hanging fruit in RL, and in scaffolding and further scaling of inference compute. But my general take is that the recent faster trend of doubling every ~4 months is already the result of picking the low-hanging RL fruit for coding and SWE, and fast inference scaling. So this kind of thing will probably lead to a continuation of the fast trend, not another acceleration.

Another source of shorter timelines, depending on what timeline you mean, is the uncertainty from translating time horizon to real-world AI research productivity. Maybe models with an 80% time horizon of 1 month or less are already enough for a huge acceleration of AI R&D, with the right scaffold/unhobbling/bureaucracy that can take advantage of lots of parallel small experiments or other work, or good complementarities between AI and human labor, 
Reply
[-]
HiroSakuraba6mo8-2

OpenAI delivering an iterative update rather than a revolutionary one has lengthened many people's timelines.  My take is that this incentivizes many more players into trying for the frontier.  Xai's Grok has gone from non-existent in 2022 to a leading model.  The rollout pace of improvements to the newest version of Grok are far more frequent than other leading companies.  Nvidia has also recently begun releasing open larger source models as well as the accompanyin datasets.  Meta is another player that is now all-in.  The failure of Llama and moderate updates by OpenAI likely pushed Zuckerberg into realizing that his favored relentless A/B testing at scale could work. Twenty-nine billion for new datacenters and huge payout for top minds is like a beacon for sovereign wealth / hedge funds to notice that the science fiction reality is now here.  When the prize is up for grabs much more captial will be thrown into the arena than if the winner was a foregone conclusion.  

 

So, my timelines have shortened due to market sentiment conditions and dawning realizations rather than benchmarks improving.  While tech stocks may fall, bubbles may burst, and benchmarks could stagnate; I still believe the very idea of taking the lead in AGI trumps all.
Reply
[-]
StanislavKrym6mo51

I mostly agree with this, but the key aspect is not just many more players, but many more methods waiting to be tried. The SOTA AI architecture is a MoE LLM with a CoT and augmented retrieval. If the paradigm has hit its limits[1] in a manner similar to the plateau of GPT4-GPT4o or Chinese models,[2] then the researchers will likely begin to explore new architectures. 

For example, there is the neuralese with big internal memory and lack of interpretability. Another potential candidate is a neuralese black box[3] choosing the places in the CoT where the main model will pay attention. While the black box can be constructed to understand the context as well as one wishes, the main model stays fully transparent. A third potential candidate is Lee's proposal. And a fourth candidate is the architecture first tried by Gemini Diffusion.

In a manner similar to the Fermi paradox, this makes me wonder why none of these approaches led to the creation of new powerful models. Maybe Gemini Diffusion is already finishing the training run and will win the day?

    ^

    Which also include troubles with fitting context into the attention span, since the IMO, consisting of short problems, mostly fell to unreleased LLMs. Amelioration of the limits could likely require large memory processed deep inside the model, making the neuralese internal thoughts a likely candidate.
    ^

    However, there is DeepSeek V3.1, released on Aug 20 or 21.
    ^

    Which could also be a separate model working with the CoT only, allowing the black box to be integrated into many different models.

Reply
[-]
yrimon6mo73

I doubt that METR's graph stays linear (on a log to date scale). I accomplish long tasks by tackling a series of small tasks. Both these small tasks and the administrative task of figuring out what to do next (and what context i need a s refresher on to accomplish it) are less than a day long. So at some point I expect a team of agents (disguised as a monolith) with small individual task length success to pass a critical mass of competence and become capable of much longer tasks. 
Reply
[-]
james oofou6mo43

It doesn't follow from an AI being able to do the components of a task that the AI can do the task itself. This is because the ability to carry out the subcomponents of a task does not entail the knowledge that these are the subcomponents of the task. 

I do think that each subsequent doubling of time-horizons will be in some sense easier than the last. But this is counteracted by the fact that RL becomes more difficult as task lengths increase. One can imagine it being difficult to have a doubling time of, say, 2 months, when the AI is learning to do tasks of length 8 months. It might take the AI longer than 2 months just to spit out an attempt at one of the tasks! I think it's an open question which of these two forces is stronger.
Reply
[-]
yrimon6mo40

Doesn't the (relatively short) task my manager does, of breaking projects into component tasks for me to do entail knowledge of the specific subcomponents? Is there a particular reason to believe that this task won't be solved by an AI that otherwise knows to accomplish tasks of similar length?
Reply
[-]
Vladimir_Nesov6mo31

And automated adaptation (continual learning, test time training) should enable a lot of serial time that would overcome even issues with splitting a problem into subproblems (it's not necessarily possible to solve a 10-year problem in 2 years with any number of competent researchers and managers). So to the extent in-context learning implements continual learning, presence of any visible bounds on time horizons in capabilities indicates and quantifies limitations of how well it actually does implement continual learning. A genuine advancement in continual learning might well immediately do away with any time horizons entirely.
Reply
[-]
christianvuye6mo*30

I do wonder why the SWE-Bench and METR benchmarks are taken as THE best indicator of progress. SWE-Bench is a particular benchmark that only captures a small fraction of real-world software engineering. METR themselves have published work that shows the benchmark only captures very narrow algorithmic work, not software engineering holistically. Benchmarks tell a minimal story, so to extrapolate predictions from limited benchmarks is a good example of Goodhart’s law. Real-world impact from AI on software engineering is much smaller than progress on benchmarks such as SWE-Bench would imply.
Reply
[-]
testingthewaters6mo*31

In a very goal oriented, agency-required domain (hacking) GPT-5 seems notably better than other frontier models: https://xbow.com/blog/gpt-5

This actually updates me away from my previous position of "LLMs are insufficient and brain-like architectures might cause discontinuous capabilities upgrades" towards "maybe LLMs can be made sufficient with enough research manpower". I still mostly believe in the first position, but now the second position seems at least possible.
Reply
[-]
emile delcourt6mo20

What if work longer than one week was vastly sublinear in complexity for AI—meaning that doubling task duration doesn’t double difficulty for an agent? 

This could be a corollary to your point on superexponential results, but maybe less from a capability standpoint but environmental overhangs to which humans may not have fully optimized. Especially in a multi agentic direction.
Reply
[-]
samuelshadrach6mo20

I predicted 25% ASI by 2030. Good to know we agree. I define ASI as better than best humans on all tasks. Rich Sutton (e/acc) agrees.
Reply
Moderation Log
