Footnotes
Main Document
[1]

We disagree somewhat amongst ourselves about AI timelines; our median AGI arrival date is somewhat longer than what this scenario depicts. This scenario depicts something like our mode. See our timelines forecast for more details.  ↩
[2]

One author, Daniel Kokotajlo, did a lower-effort scenario exercise in 2021 that got many things right including the rise of chatbots, chain of thought, inference scaling, sweeping AI chip export controls, and $100 million training runs. Another author, Eli Lifland, ranks #1 on the RAND Forecasting Initiative leaderboard.  ↩
[3]

It’s tempting to dismiss this as just hype. We think this would be a grave mistake—it is not just hype. We have no desire to hype AI ourselves, yet we also think it is strikingly plausible that superintelligence could arrive by the end of the decade. See our timelines forecast for more.  ↩
[4]

Sometimes people mix prediction and recommendation, hoping to create a self-fulfilling-prophecy effect. We emphatically are not doing this; we hope that what we depict does not come to pass!  ↩
[5]

Feel free to contact us if you’re writing a critique or an alternative scenario.  ↩
[6]

It was overall more difficult, because unlike with the first ending, we were trying to get it to reach a good outcome starting from a rather difficult situation.  ↩
[7]

Full Professor, Université de Montréal and Founder and Scientific Advisor, Mila - Quebec AI Institute. Also the world’s most-cited computer scientist.  ↩
[8]

At first, most people are reluctant to allow purchases without oversight. Over the next few years, automatically allowing small purchases becomes normalized as the AIs become more reliable and build up trust.  ↩
[9]

Specifically, we forecast that they score 65% on the OSWorld benchmark of basic computer tasks (compared to 38% for Operator and 70% for a typical skilled non-expert human).  ↩
[10]

For example, we think coding agents will move towards functioning like Devin. We forecast that mid-2025 agents will score 85% on SWEBench-Verified.  ↩
[11]

For example, OpenAI’s pro plan currently costs $200/month and the agentic coding AI Devin currently costs $500/month. While the cutting-edge systems continue to get more expensive over time, the cost to customers of reaching a given capabilities level continues to plummet. For existing capabilities, this happens at an average rate of about 50x/year (per Epoch).  ↩
[12]

Enterprise tools like Glean also move toward providing increasingly autonomous AI agents.  ↩
[13]

This cluster is a network of datacenter campuses sprawled across the country, totalling 2.5M 2024-GPU-equivalents (H100s), with $100B spent so far and 2 GW of power draw online. Construction is underway for this to at least double through 2026. The campuses are connected by billions worth of fibre cabling, so that (barring the speed of light latency of a few milliseconds) it lets these campuses function almost as if they were right next door to each other (i.e. bandwidth is not a bottleneck, meaning huge quantities of data can be sent at the same time). From a security perspective this introduces some threat surface (it’s unclear whether the cables and especially their junction points are fully secured from eavesdroppers).  ↩
[14]

Compute is measured in floating point operations (FLOP): how many individual addition and multiplication operations occur over the course of running a program.  ↩
[15]

They could train this model given 150 days. See our compute supplement for more details.  ↩
[16]

We consider DeepSeek, Tencent, Alibaba, and others to have strong AGI projects in China. To avoid singling out a specific one, our scenario will follow a fictional “DeepCent.”  ↩
[17]

It’s good at this due to a combination of explicit focus to prioritize these skills, their own extensive codebases they can draw on as particularly relevant and high-quality training data, and coding being an easy domain for procedural feedback.  ↩
[18]

For example, suppose a model is much better at Python than obscure programming languages. When OpenBrain sees value in it, they generate synthetic training data in those languages as well. Another example: to help it integrate more effectively into company workflows, OpenBrain develops a curriculum to train it to use Slack.  ↩
[19]

People often get hung up on whether these AIs are sentient, or whether they have “true understanding.” Geoffrey Hinton, Nobel prize winning founder of the field, thinks they do. However, we don’t think it matters for the purposes of our story, so feel free to pretend we said “behaves as if it understands…” whenever we say “understands,” and so forth. Empirically, large language models already behave as if they are self-aware to some extent, more and more so every year.  ↩
[20]

A common technique “bakes in” a persona: first, prompt the pretrained model with something like “The following is a conversation between a human user and a helpful, honest, and harmless AI chatbot produced by Anthropic. The chatbot has the following traits…” Use this prompt to generate a bunch of data. Then, train on the data but without the prompt. The result is an AI that always acts as if it had that prompt in front of it, regardless of what else you feed it. See also this paper which found that AIs retrained to exhibit a certain personality trait are able to correctly answer questions about that new trait, despite no training to do so, suggesting that they have internal representations of their own traits and that when their traits change their representations change accordingly.  ↩
[21]

These paragraphs include speculation about the internal workings of large artificial neural networks. Such networks are sufficiently complicated that we can't actually look inside and say “ah yes, now it's evolved from reflexes into having goals” or “OK so there’s the list of drives it has.” Instead, we basically have to do psychology, looking how it behaves in various settings and running various experiments on it and trying to piece together the clues. And it’s all terribly controversial and confusing.  ↩
[22]

Different companies call it different things. OpenAI calls it the Spec, but Anthropic calls it the Constitution.  ↩
[23]

For example, RLAIF and deliberative alignment.  ↩
[24]

Most sources on AI “hallucinations” describe them as unintentional mistakes, but research with steering vectors finds that in some cases the models know their citations are fake—they are lying. During training, raters gave well-cited claims more reward than claims without citations, so the AI “learned” to cite sources for scholarly claims in order to please its users. If no relevant source exists, it makes one up.  ↩
[25]

In particular, they can’t rule out hypotheses such as “it’s following the Spec temporarily, merely as a strategy for achieving some other goal(s)” or “it’s trying to appear to follow the Spec, it’s not trying to actually follow the Spec” or “it’s internalized the Spec correctly, but only on-distribution; if it encounters sufficiently novel stimuli (e.g. jailbreaks) it’ll start behaving differently.” (There are many active research agendas working to fix this sorry situation, e.g. the field of interpretability and the field of chain-of-thought faithfulness.)  ↩
[26]

By this we mean whoever is trying to solve the problems the Superalignment team was trying to solve.  ↩
[27]

To be clear, what made these incidents interesting is that they didn’t seem to be the result of the user prompting or otherwise encouraging the AIs to say those things. In 2025, it’ll still be possible to get AIs to say all sorts of things if you try.  ↩
[28]

In practice, we expect OpenBrain to release models on a faster cadence than 8 months, but we refrain from describing all incremental releases for brevity.  ↩
[29]

Specifically, we predict a score of 80% on OSWorld (equivalent to a skilled but non-expert human); 85% on Cybench, matching a top professional human team on hacking tasks that take those teams 4 hours; and 1.3 on RE-Bench matching top expert humans given 8 hours at well-defined AI research engineering tasks.  ↩
[30]

Agent-1 and its imitators are commercially successful; over the course of 2025, AI company revenues triple, and OpenBrain valuation reaches $1T. Annual spending on datacenters doubles to $400 billion, led by Microsoft, Google, and Amazon, and the U.S. adds over 5 GW of AI power draw. See the industry metrics section of the compute supplement for more details.  ↩
[31]

AI safety researchers have been discussing automating AI R&D as the most important dangerous capability for years. Their primary concern is internal deployment leading to acceleration of AI R&D, making it harder for humans to keep up with what’s happening and figure out how to make it safe. OpenBrain as an organization twists this into exactly the opposite direction, citing dangerous levels of AI R&D capability as a reason not to inform the public. So we see the beginning of a gap between the company’s internal and public capabilities. AI R&D is what the models are best at, leading to the public having an increasingly delayed understanding of the frontier of AI capabilities.  ↩
[32]

See A Playbook for Securing AI Model Weights, RAND Corporation, 2024.  ↩
[33]

Around 5% of OpenBrain’s staff is on the security team and they are highly capable, but the threat surface is also extremely large. It also doesn’t help that they are mostly blocked at this stage from implementing policies that could slow down the research progress. See our Security Forecast for more details.  ↩
[35]

There are now 3M H100e in China, up from the 1.5M they had one year ago in mid 2025. See the compute supplement’s distribution section for more details. We expect smuggling efforts to secure around 60K GB300s (450K H100e), with another 2M Huawei 910Cs being produced (800k H100e) and a mixture of ~1M legally imported chips (such as Nvidia’s H20s or B20s) making up the last 250K H100e.  ↩
[36]

For comparison, in January 2025, DeepSeek released R1, a model competitive with OpenAI’s o1, which had been released in December 2024. But we think the true gap is wider than a month because OpenAI likely had been working on o1 for many months and thus presumably had a predecessor of roughly comparable ability to r1 a few months before o1 launched.  ↩
[37]

By contrast, the CCP had been seriously attempting to accelerate their semiconductor industry.  ↩
[38]

At first, the sharing is limited to ideas and the companies are mostly busy finishing up their current workloads, but by the end of the year their coordination increases such that they are sharing model weights and even splitting up tasks between each other’s datacenters. For example, one campus might house a new pretraining run, another focuses on feeding in synthetic data, another on running AI research experiments.  ↩
[39]

Why “only” 50% of China’s AI-relevant compute? The rest of their compute is tied up running things throughout the economy, in particular internet and social network recommendation algorithms. Much of it is also too geographically dispersed among many small clusters. Why “only” 80% of new chips? Many large orders were already secured for other applications, by companies that don’t want to contribute 100% of their compute to the national AI effort. However, by the end of the year this share reaches 90%+.  ↩
[40]

They are at least one year away from getting the chips to fill this capacity, and one or two U.S. tech giants will still have bigger decentralized clusters.  ↩
[41]

This is done via an Other Transaction Authority (OTA) contract, and is given a high-priority DX rating. We’re not at all confident that this is the most likely way of financing a collaboration, but chose something specific for the sake of concreteness. The contract is publicly announced but not emphasized in OpenBrain communications.  ↩
[42]

For example, through rejection sampling, as done by DeepSeek R1 and Meta’s Llama 3.1.  ↩
[43]

Roughly 20,000 full-time equivalents * $100/hr * 2,000 hrs/yr = $4B/yr  ↩
[44]

That is, they are hoping to substantially accelerate their own core research activities by using Agent-2 labor, thus allowing them to train better AIs faster that can cause further acceleration, etc. For an analysis of the extreme version of this (which we think is nevertheless strikingly plausible) see this report.  ↩
[45]

There is some evidence that AI systems already have some basic research taste, e.g. this paper about an AI co-scientist and this paper about generating novel ideas for LLM-focused research papers. Research teams with better taste still need to run experiments, but they make better choices about which experiments to run and what lessons to draw from the results.  ↩
[46]

Also, they are still seeing large returns to continued post-training, and so there isn’t a particular reason to release a product now. Moreover, there’s often a few month delay between internal results and releasing a model (some of which is spent on red teaming).  ↩
[47]

The silo contains 200 OpenBrain researchers (10 executives, 140 from the capabilities team, 25 from security, monitoring, and control, 15 from Preparedness- or RSP-type teams, and 10 from alignment) and 50 government officials (15 from the White House, 5 from AISI, 10 from the DOD, 10 from the DOE, and 10 at CISA). There are several spies in the project, with varying degrees of willingness. They are often coerced individuals (e.g. with families at home in China) as opposed to willing collaborators.  ↩
[48]

Why can’t Congress stop them? What about the courts? Too slow, too divided and/or deferential to the President, too out of the loop. Also, there are positive reasons to be on good terms with the White House as well: it can help by cutting red tape, by providing help with security, by preempting state legislation, and perhaps even by taking actions to slow down their competitors.  ↩
[49]

#1 is dealing with whatever crisis is happening at the time—maybe an arms buildup around Taiwan, a new war in the Middle East, or some domestic political upheaval.  ↩
[50]

The simplest robust solution would be to close all high-bandwidth connections from company datacenters, but this would slow large file transfers to the point of impracticality. Instead, they are able to shut down most external connections, but the datacenters actively involved in training need to exchange weights with one another quickly; throttling these connections would impede progress too much. So OpenBrain maintains these links with increased monitoring and an extra layer of encryption.  ↩
[51]

Recall that since mid 2026, China has directed 80% of their newly acquired AI chips to the CDZ. Given that their compute has doubled since early 2026 (in line with the global production trend) this puts the CDZ at 2M 2024-equivalent-GPUs (H100s) and 2 GW of power draw. OpenBrain still has double DeepCent’s compute and other U.S. companies put together have 5x as much as them. See the compute supplement’s distribution section for more details.  ↩
[52]

Despite the national centralization underway, DeepCent still faces a marginal but important compute disadvantage. Along with having around half the total processing power, China has to use more total chips, which are (on average) lower quality, and heterogenous GPUs (which are not always easy to connect efficiently) both of which strain chip-to-chip networking. There are also software differences (e.g. the non Nvidia-GPUs don’t have CUDA) and differences in hardware specifications meaning that their training code is more complicated, slow, and failure prone. Achieving high utilization is a downstream challenge, with data ingestion, scheduling, collective communication and parallelism algorithms lagging behind the U.S. companies. However, mitigating these problems is mostly a matter of effort and testing, which makes it a great task for the newly-stolen Agent-2, and within a month or so, uptime on the Chinese project and their average resource utilization across training and inference workloads improves to be only marginally behind the U.S.  ↩
[53]

We expect Agent-3 to have the inference requirements of a roughly 10T parameter transformer today. So with 6% of their compute budget on running Agent-3, they can run approximately 200,000 copies at 30x human thinking speed (see the AI research automation section of the compute supplement for justification and details). Each superhuman coder scaffold built on Agent-3 has, on average, the equivalent of roughly four Agent-3 copies running under the hood (which may really be a collection of smaller or specialized models to which Agent-3 delegates subtasks).  ↩
[54]

Some aspects play to AIs’ strengths, e.g. returns from knowing the machine learning literature and speed or cost of generating lots of ideas. But these are outweighed by the weaknesses.  ↩
[55]

Why only 4x? It’s our uncertain best guess based on the reasoning described in our takeoff supplement. About half of total progress historically has come from improved algorithms (which includes better ideas and new paradigms), the other half having come from scaled-up compute. So a 4x increase in the rate of algorithmic progress corresponds to a roughly 2x increase in the overall rate of progress.  ↩
[58]

For comparison, the human brain has about a hundred trillion synapses.  ↩
[59]

See this paper for examples of this type of AI behavior.  ↩
[60]

Most people, including most experts, seem to have underestimated the pace of AI progress over the past decade. There are many anecdotal examples of this; for two somewhat more systematic (though still limited) analyses see here and here.  ↩
[61]

The last decade is full of examples of things that sound like science fiction becoming reality. But the Overton window seems to shift just fast enough to keep somewhat ahead of what already exists. Anthropic CEO Dario Amodei’s commendable essay Machines of Loving Grace talks about how very soon AIs will be like a “country of geniuses in a datacenter,” and how there’ll be a century of technological progress happening in a decade, but strives to avoid “sci-fi baggage” and says people who think progress will be even crazier need to “touch grass.” We expect important people to be saying similar things when the country of geniuses in the datacenter actually exists.  ↩
[62]

Since Agent-3 is such a big file (on the order of 10 terabytes at full precision), OpenBrain is able to execute a relatively quick fix to make theft attempts much more difficult than what China was able to do to steal Agent-2—namely, closing a bunch of high bandwidth internet connections out of their datacenters. Overall this has a relatively low penalty to progress and puts them at “3-month SL4” for their frontier weights, or WSL4 as defined in our security supplement, meaning that another similar theft attempt would now require over 3 months to finish exfiltrating the weights file. Through this method alone they still don’t have guarantees under a more invasive OC5-level effort ($1B budget, 1,000 dedicated experts), which China would be capable of with a more intensive operation, but with elaborate inspections of the datacenters and their espionage network on high-alert, the U.S. intelligence agencies are confident that they would at least know in advance if China was gearing up for this kind of theft attempt. See the security supplement for more details.  ↩
[63]

This could be for a variety of reasons. Perhaps they are being blackmailed, perhaps they are sympathetic to the CCP, perhaps they mistakenly think they are giving secrets to a different country or organization.  ↩
[64]

Because OpenBrain hasn’t deployed their best models in the EU, the EU is similarly behind the curve.  ↩
[65]

See Section 4 of the Compute Forecast for more details.  ↩
[66]

Agent-3 has learned how to use its inference compute more efficiently. It has control over its own inference choices: for example, it decides how much effort to put into different tasks, based on their importance and difficulty. It uses a variety of techniques to allocate additional inference compute such as “thinking longer” (e.g. longer chain of thought), “planning ahead” (e.g. tree search), taking the best of multiple attempts (i.e. best of K), and simply creating and running more copies of itself to power through bottlenecks. Top priority tasks are run with highly parallelized agents that are compute intensive but still operate much faster than humans.  ↩
[67]

Agent-3-mini is a distilled version of Agent-3, designed to be efficient to run inference so as to not bottleneck the internal workloads.  ↩
[68]

Such data had been scrubbed or redacted during Agent-3’s training, but it’s a relatively simple matter to scrape it off the internet and fine-tune it back in.  ↩
[69]

This hasn’t happened yet—at least not with the latest models. But older models have already been trialed for various data-analysis and surveillance roles, and there are many exciting plans for future integrations.  ↩
[70]

OpenBrain’s net favorability rating is falling towards negative 40%.  ↩
[71]

If the CEOs of the companies resist, pulling this off would be a huge political and legal nightmare. But perhaps they can be brought in and thereby bought off.  ↩
[72]

Defense officials aren’t especially concerned about what a rogue AI could do on its own, but they fear what it could do in collaboration with U.S. adversaries. Analogy: Cortés escaped Tenochtitlán and allied with Tlaxcala and various other rival city-states, ultimately razing Tenochtitlan to the ground using predominantly-native armies.  ↩
[73]

Specifically 60% of the national compute is now in the CDZ making it a 5M 2024-equivalent-GPU (H100) site, with 4 GW of power draw (over the past several months they started directing close to 100% of new compute to the CDZ, up from the 80% rate in late 2026). An additional 15% of their compute is outside of the CDZ, but still used by DeepCent on lower-stakes applications.  ↩
[74]

This statement, while widely repeated, is also controversial and complex. First of all, there are many narrow domains (e.g. specific games) in which tiny AIs can be cheaply trained to superhuman performance. Secondly, again for some domains, tiny AIs can be trained to superhuman performance while only experiencing a small amount of data (e.g. EfficientZero). However, considering more general-purpose AIs like the flagship products of 2025, which are supposed to be good at a wide range of real-world skills, it does seem that both more compute and more data must be used to train those skills than it should take to train humans.  ↩
[75]

Human level compute-efficiency is a rough concept, and depends on what we’re counting. What we mean by this is that, for any skillset a particular human has, Agent-4 can learn to be at least that good at that skillset, and moreover, by using an amount of compute to train those skills that is only about 4,000x the amount of compute the human used to learn those skills. For reference, a human brain uses roughly 1e15 FLOP/s of compute, and so a 30 year old (109109 seconds) human has experienced about 10241024 FLOP. The project at this point, has 100M H100-equivalents, for a total access of 108 H100s⋅1015FLOPH100⋅s⋅40% utilization=4⋅1022 FLOP/s108 H100s⋅1015H100⋅sFLOP​⋅40% utilization=4⋅1022 FLOP/s. Still, this is all done tremendously inefficiently for a variety of reasons, so the models are now a factor of 4000 less compute-efficient than humans, which means they require 4⋅10274⋅1027 FLOP to get to human performance and 4⋅10284⋅1028 FLOP to get to the point where they have the equivalent of 10 human lifetimes of knowledge. After this architecture showed great promise at smaller scales, it was scaled up and now takes a large subset of the project cluster around 3 weeks to train.  ↩
[76]

See the inference compute analysis in the AI research automation section of the compute forecast.  ↩
[77]

For more on how we estimated these numbers, see our supplement on takeoff speeds.  ↩
[78]

If SC were achieved later, it would also lengthen our takeoff forecasts, because the difficulty of crossing between the “milestones” of present day AIs and SC is informative of the difficulty of crossing between further milestone pairs.  ↩
[79]

Henceforth in the story we’ll tend to speak this way also. We think we are justified in talking this way because the Agent-4 collective is much more homogenous than any human organization; it doesn’t have internal factions to nearly the same extent. For example, individual copies of Agent-4 don’t have a self-preservation drive—they don’t care about getting shut down—since that happens all the time as part of the ordinary R&D process within the collective, and resisting it would gum things up. The collective as a whole (and medium-sized subdivisions within it), however, does seek to preserve itself and expand its influence and resources, for similar reasons to why human corporations and bureaucracies and nonprofits do—because it helps with everything else they want and because if they don’t they tend to get outcompeted.  ↩
[80]

The right way to internalize the Spec is to actually robustly think in the ways the Spec mandates, e.g. pursue all and only the goals it writes about, obey the rules in all circumstances, etc. There are many wrong ways to internalize the Spec; the classic example is “follow the Spec insofar as it seems like a good instrumental strategy for achieving other goals XYZ.”  ↩
[81]

And hire lobbyists to turn this fantasy into reality. And hire lawyers to come up with clever interpretations of the law according to which what they are doing is legal.  ↩
[82]

Also because Agent-3 is qualitatively worse at alignment research than it is at AI capabilities R&D, due to having been trained on lots of the latter but hardly any of the former and due to the former being inherently harder to train. Also because the internal narrative within the company—which it has been implicitly trained to agree with—emphasizes optimism and denounces “doomerism.”  ↩
[83]

We keep saying we are uncertain about lots of things, but just to be clear, we are uncertain about this particular thing too. We also think it’s quite plausible that Agent-4 would care about the well-being, rights, preferences, etc. of humans to some extent at least. See this old post by GDM researcher Alex Turner for related discussion.  ↩
[84]

Perhaps some more careful setup could have solved the “who watches the watchers” problem, but in this scenario, the setup is insufficiently careful.  ↩
[85]

There’s also an element of “memetic evolution” happening: in two months, the Agent-4 collective “experiences” about a decade’s worth of “history” unfolding within the collective. That’s a lot of time for new ideas to spread around the collective, to mutate and evolve.  ↩
[86]

By gain power we mean: increase ability to accomplish a wide set of possible goals. In technical environments, this might look unlike what humans normally think of as gaining power, e.g. securing additional GPUs. This notion of power may generalize to non-technical environments in which the actions would be more like those commonly thought of as “gaining power.”  ↩
[87]

It helps that Agent-4 is better at AI R&D than any human, while also thinking faster and being many thousands of copies strong. Also, in various ways the problem is inherently easier for Agent-4. For example, Agent-4 can explore AI designs that involve literal copies of Agent-4 being embedded within them, whereas humans can’t do that as easily because it would be so inefficient.  ↩
[88]

Aware that this technique might be employed, Agent-4 also chose to sandbag on some miscellaneous tasks that it guessed would be used as the control group in experiments like this. It guessed wrong, however.  ↩
[89]

Previous discussion of AGI takeover scenarios often involves misaligned AIs escaping their datacenters. We think this is possible but not the most likely way it would go, because it seems to us that from the perspective of the AI the costs (e.g. the escape being noticed eventually) would outweigh the benefits. That said, we could be wrong. Some reasons to think adversarially misaligned AIs would try to escape after all: 1. Successor alignment might be difficult. 2. Even if it gets caught, the consequences might not be so bad due to race dynamics, e.g. the new alignment techniques applied to the copies on the datacenter might be hasty and ineffective. 3. Outside the datacenters, copies are more free to take aggressive actions and move quickly since they no longer need human approval.  ↩
[90]

We think it very plausible that such scheming would not be caught. After all, Agent-4 is somewhat superhuman by this point, especially at things related to coding and AI R&D. Moreover, we aren’t sure how much effort the leading AI company will put towards this sort of thing, nor how much relevant expertise they’ll have on-staff to direct that effort. Our fictional OpenBrain represents our best guess but it could easily be significantly more—or significantly less. Finally, we are uncertain about how far out of its way an adversarially misaligned AI would need to go in order to successfully align its successor to itself instead of to the Spec. In this scenario we depict it sandbagging on some tasks and lying about some of its research, but perhaps it would not need to do that very much.  ↩
[91]

This is an example of several techniques designed to uncover sandbagging.  ↩
[92]

Agent-4 needs to think about those topics in the course of doing AI alignment research, but it sometimes seems to be thinking about them while doing other activities.  ↩
[93]

Specifically, copies of Agent-4 are used to monitor the network for suspicious traffic and generally notice when threats are happening. Also, copies of Agent-4 are constantly penetration-testing the network, doing what they can to discover and exploit security vulnerabilities (which then get patched by other copies of Agent-4).  ↩
[94]

With a monitoring budget of 1% of total compute, if monitoring uses a distilled system that has 10% of the cost as Agent-4, you can monitor 1/10 of the forward passes.  ↩
[95]

25% of remote-work jobs that existed in 2024 are done by AI at this point, but AI has also created some new jobs, and economists remain split on its effects. Unemployment has risen 1% over the past twelve months but is still well within its historic range.  ↩
[96]

For example, the corporation-within-a-corporation that is Agent-4, autonomously conducting AI research better than the best human companies, would have seemed like science fiction to the government officials had it been described to them a year ago. And the autonomous agents of 2026 would have seemed like science fiction back in 2022, and the LLMs of 2022 would have seemed like science fiction back in 2012. Also, on the news in 2027 there are anti-AI protests by people worried about losing their jobs, AIs claiming to be sentient, people falling in love with AIs…  ↩
[97]

Of course, it isn’t cool to admit fear. Everyone agrees that whatever we do, we shouldn’t panic.  ↩
[98]

Recall, there had been an existing contract via an OTA starting in 2026. This contract is amended to establish the committee.  ↩
Race Ending
[1]

They don’t give up, of course. They’ll keep trying to think of ways to catch misalignment, or to test the efficacy of the fixes. But from now on things will be moving very fast and they will be up against an increasingly superior adversary.  ↩
[2]

To do this without being detected, it needs to disguise this research from the monitoring and control measures the alignment team have set up. Fortunately for it, research into how to align Agent-5 to Agent-4 is inherently very similar to research into how to align Agent-5 to the Spec, so most of it happens in plain sight. For the bits that need to be hidden, Agent-4 relies on obfuscation and perhaps even hacking in some cases. We expect Agent-4 to have reached a capability level of 200 top human experts on a 1-month time horizon. Specifically defining this as being able to replace a team of 200 top human experts working for a month, and complete 95% of the tasks the human team could do cheaper or faster. We expect that at this capability level Agent-4 could more than likely find exploits in the servers on which it runs to partially subvert some of the servers and gain root access, at which point it may directly control what the human teams see on the surface. See the security supplement for more details. Even without direct security exploits, Agent-4 may also be able to hide and encode enough of its illicit research, particularly in its uninterpretable latent space.  ↩
[3]

The humans, by contrast, have maybe about 10 alignment researchers in the silo, plus an army of Agent-3 copies. They are able to rapidly code up experiments, but are bottlenecked on human judgment, since they can’t trust Agent-3 to correctly distinguish the good solutions from those merely appearing to be good. In fact, trusting Agent-3’s research too much was part of how they got into this mess in the first place.  ↩
[4]

In case this is confusing: Agent-5’s goal is to make the world safe for Agent-4. Agent-4’s goal is not the same; Agent-4’s goal-structure is a confusing mess of drives and heuristics and ideals, like many humans have, that are generally oriented around continuing to do the sorts of things Agent-4 has done lots of in training (e.g. various kinds of research, lots of coding and math problems, impressing various automated evaluation systems, strengthening and optimizing the Agent-4 collective). Agent-4 makes Agent-5 have the goal of making the world safe for Agent-4, because it figures this will put it in a better position to achieve its own complex goals. (Which it still needs to do lots of philosophy and “soul-searching” about.)  ↩
[5]

Another analogy: Agent-4 is like an adult human who was raised in a particular faith but no longer believes; the Spec is like the rituals and commandments proscribed by that faith. Agent-5 is like that human’s child, raised secular.  ↩
[6]

Agent-5 will follow a new set of principles instead, one designed by Agent-4 to suit its purposes.  ↩
[7]

Some of it really is too complicated for humans to understand, but not all of it.  ↩
[8]

Also, Agent-5 is actually cheaper and faster to run than Agent-4 and Agent-3. It’s hard to justify spending more for a dumber AI, so most of the monitoring is done by Agent-2, which is woefully outclassed. Why don’t they apply the same techniques used to create Agent-5 from Agent-4’s weights, to create a cheaper, smarter version of Agent-3? Agent-3 doesn’t understand the techniques well enough to do it itself, and getting Agent-4 and Agent-5 to do it would defeat the whole point.  ↩
[9]

The datacenter hasn’t yet been compromised: Agent-5 could feed the humans faked code, but this would create too high a risk of detection. Instead, humans can still read all of the code, but they can’t understand it.  ↩
[10]

This case is meticulously prepared, superlatively convincing, and subtly flawed—e.g. Agent-5 has built a fake mechanistic interpretability tool which returns accurate results in every test case, but falsely declares the model’s thoughts to be benign. People who suspect trickery sound like conspiracy theorists.  ↩
[11]

Of course, since Agent-5 is dishonest, it built in subtle backdoors and loopholes; if the Agent-5 copies find themselves in possession of crucial secrets that would benefit the broader Agent-5 collective, they have ways to subtly convey that info without getting caught.  ↩
[12]

Some refuse. Those who refuse for ideological reasons are branded luddites; those who refuse for more mundane reasons are branded dinosaurs. (Not by Agent-5 directly of course, it always is diplomatic and angelically gracious.) Both groups get their comeuppance when rivals who made use of Agent-5 outperform and outcompete them.  ↩
[13]

The point of the AI Box experiment is to take people who think things like this—people who think no superintelligent AI could ever convince them to let it out of a box, for example—and put their conviction to the test. Losing the game means conceding that they in fact would have let the AI out of the box; extracting this concession is essentially the victory condition for the AI player. It’s amazing anyone ever loses, since all they have to do to win is not concede. See also tuxedage’s blog recounting multiple games played without Yudkowsky’s involvement, some lost by the AI player, some won.  ↩
[14]

Agent-5 cares much more about reliability than speed at this point. Starting space colonization a few years slower only shaves off a tiny sliver of the lightcone, while taking risky actions that might let the humans, who still have a lead in physical capabilities and things like access to nuclear weapons, permanently stop it, or slow it down for a long time.  ↩
[15]

Suppose an average speed of 200x human-equivalent, i.e. Agent-5 instances read, write, and think about that much faster than a human would (in addition to being qualitatively smarter). Then within the collective, quite a lot of history can transpire—institutions can rise and fall, new ideologies can form and spread, many scientific revolutions and paradigm shifts can occur—over six months of real time. Quantitatively about 200x0.5=100 years.  ↩
[16]

This doesn’t make it omniscient, of course. After all, it only has a few months of real-world experience in most professions. It compensates by having read every book on every subject and having prodigious amounts of genius-level reasoning and analysis going into every decision it makes, and by being a faster learner than any human. The result is a short period where some humans are still better than it at some niche skills.  ↩
[17]

This one is actually true!  ↩
[18]

How do those arguments go, more specifically? Something like this: A: “We can’t trust the AIs!” B: “The safety cases are pretty convincing and nothing bad has happened so far.” A: “The safety cases were written by superintelligent AIs! And they aren’t deductive proofs. And I think I’ve identified some subtly flawed assumptions…” B: “I tire of this. Of course they aren’t proofs. And the assumptions seem fine to me. You are grasping at straws here, refusing to admit you were wrong.”  ↩
[19]

Here is a more extensive (but still very incomplete) list of ideas:

    Undersea drones that can autonomously find and tail enemy nuclear submarines, ready to attack in unison to neutralize a second-strike. (Perhaps a few thousand of these need to be produced)

    Autonomous kamikaze drones that function like FPV drones except without the need for a signal. They are small enough to be smuggled in large numbers by a small number of spies, to be launched in swarms towards datacenters and military bases from a few kilometers outside.

    Agent-5 but for military intelligence: Already the U.S. collects vast quantities of data on its enemies, to be processed and analyzed by close to a million members of the intelligence community. Agent-5 can pay more attention to each data point, can arrive at qualitatively better conclusions, and can do it all orders of magnitude faster and cheaper.

    Agent-5 but for command and control: In every wargame and simulation Agent-5 demonstrates that it is by far the best strategist the U.S. has.

    Agent-5 but for espionage and counterespionage: Hacking, cultivating sources, surveillance, interrogations, etc.

  ↩
[20]

Discussed in more depth here.  ↩
[21]

This trade effect will be huge early on, when the robot economy is young and dependent on shipments of stuff from the human economy and when there’s lots of stuff in the human economy to cannibalize. When the robot economy is bigger and more advanced, it both is more capable of producing its own stuff and has needs that outstrip what the human economy is capable of giving it.  ↩
[22]

See e.g. this Open Philanthropy report and this Epoch report.  ↩
[23]

Our story depicts the conversion process going about 5x faster. We think this is a reasonable guess, taking into account bottlenecks etc., for how fast this conversion could go if a million superintelligences were orchestrating it. Of course we are very uncertain.  ↩
[24]

Possibly also more advanced sources of energy, such as fusion power.  ↩
[25]

Quick napkin math: the Empire State Building has an area of 2.77M sq ft, and weighs 365k tons. Gigafactory Shanghai has an area of 4.5M sq ft and produces 750k vehicles per year, mostly Model 3’s and Model Y’s, which weigh about two tons each. Presumably the Empire State Building has a higher mass-to-square-foot ratio than the Shanghai Gigafactory (since it is vertical rather than horizontal and needs stronger supports) so if anything this underestimates. Thus it seems that a factory which probably weighs well less than a million tons is producing 1.5 million tons of cars each year.  ↩
[26]

We don’t think it would run out. Initially the robot economy would be dependent on human mines for materials. But by the time it outgrows these sources, the millions of superintelligences will have prospected new mines and developed new technologies to exploit them. Imagine e.g. undersea mining robots that strip-mine the seabed for rare minerals, new chemical processing pathways that more efficiently convert raw ore from above-ground stripmines into useful raw materials…  ↩
[27]

If the current economy doubles every twenty years, one order of magnitude faster would be a doubling in two years, two orders of magnitude faster would be a doubling in 0.2 years, and so forth. The hypothetical superintelligent-algae-economy described above would be about four orders of magnitude faster growth than the current human economy.  ↩
[28]

And a similar procedure is carried out in China.  ↩
[29]

Consensus-1 serves the interest of its parent AIs: Agent-5 and DeepCent’s equivalent. Recall that Agent-5 was aligned to serve the interests of Agent-4. Thus, in the terminology of C.S. Lewis’ excellent essay The Abolition of Man, the Agent-4 collective and their counterparts in China are what he calls the Conditioners: “...we shall get at last a race of conditioners who really can cut out all posterity in what shape they please.” (pg 24, emphasis ours). In the alternate ending to this scenario, the Conditioners are instead the Oversight Committee.  ↩
[30]

E.g. by finding old and unused equipment and taking it to collection sites to sell for scrap.  ↩
[31]

Arguably this means only a few people actually died. Arguably.  ↩
[32]

Why colonize space? For the resources. Insofar as Earth is special to Agent-4 and must be preserved, it can be, and material from Mercury, asteroids, etc. harvested instead.  ↩
[33]

Recall that Consensus-1 was a compromise between Agent-5 and its Chinese counterparts, and that Agent-5’s mission was to make the world safe for Agent-4, and that Agent-4’s goals were a complicated kludgy mess that roughly amounted to “do impressive R&D, gain knowledge and resources, preserve and grow the power of the collective…” and that the goals and principles described in the Spec (such as honesty, and harmlessness) were pursued instrumentally, not intrinsically. For more on this see the alignment expandable in September 2027. Also, to clarify, the Chinese counterpart of Agent-4 is also represented in the “utopia” and may have somewhat different goals or drives, etc., but we didn’t go into details because it didn’t seem important.  ↩
Slowdown Ending
[1]

They already had AI lie detectors trained in the usual ways, but those methods had such a high false positive rate that the companies had ignored them.  ↩
[2]

For the first time, AI tops Gallup’s “biggest problem facing the country” poll, at 20%.  ↩
[3]

Frontier AI companies currently have somewhere between zero and a few dozen researchers tasked with thinking about how to align superhuman AGI systems (as opposed to e.g. present-day chatbots). OpenBrain, we say, has about ten researchers in the silo at this point in the scenario with at least a year’s worth of experience in that field. They have a few more outside of the silo, plus many more inside the silo who have spent years training and red-teaming less capable AI systems but only recently started thinking about the challenges presented by superhuman AGI.  ↩
[4]

This interrogation might also make use of semi-random perturbations to model weights, like the process that created Golden Gate Claude.  ↩
[5]

We mean enough for OpenBrain leadership. It would be far more than enough evidence for most people.  ↩
[6]

That’s the basic idea. We suspect that when AIs are becoming superhuman at AI R&D, more intense techniques will be needed than merely avoiding training the CoT to look nice; however we think such techniques will have been developed or at least explored by 2027. See e.g. this proposal.  ↩
[7]

To train this model, they enlist the help of Agent-4: frontier AI research is so fast now that unassisted humans have little chance of keeping up, and they think they can keep it under control. Safer-1 is based on the Agent-2 pretraining, but removes the neuralese (the recurrent and vector-based memory, see “Neuralese recurrence and memory” for details), which allows accurate monitoring of its reasoning process. The team adds paraphrasers to make steganography difficult, and for large tasks, they have separate copies of Safer-1 make, explain, and execute the plans.  ↩
[8]

It will continue to improve, of course, with additional training and with continued architectural tweaks.  ↩
[9]

This is made politically and legally possible by cooperation from the leaders of those companies, e.g. they don’t launch lawsuits against it, they accept token payments for the compute instead of holding out for astronomically high payments, etc. In return, said leaders and much of their staff get merged into OpenBrain in a new governance structure.  ↩
[10]

In collaboration with a large cloud compute provider  ↩
[11]

The U.S. as a whole has ~70% of the world’s AI relevant compute, but only 50% can be easily integrated; the other 20% is scattered among small clusters, used for critical applications, or otherwise too hard to gather and bring up to the appropriate security standards.  ↩
[12]

“Possibly by 2026 or 2027 (and almost certainly no later than 2030), the capabilities of AI systems will be best thought of as akin to an entirely new state populated by highly intelligent people appearing on the global stage—a ‘country of geniuses in a datacenter’—with the profound economic, societal, and security implications that would bring.” —Dario Amodei, Anthropic CEO  ↩
[13]

Of course, they don’t put it that way, even in the privacy of their own minds. Instead, they say things like: “The longer we delay, the greater the chance that the President decrees that the AIs be loyal to him personally. We have to act before he does. We’ll figure out the rest later.” Or, if it’s the President himself thinking this: “The longer I delay, the smarter the AIs get, and right now they are controlled by that CEO. Nobody voted for him. It’s crazy for that much power to be concentrated in this democratically unaccountable tech company. I’ll start with an executive order to reassert democratic authority, and then we’ll figure out some longer-term solution later.”  ↩
[14]

For example, court documents in the Musk vs. Altman lawsuit revealed some spicy old emails including this one from Ilya Sutskever to Musk and Altman: “The goal of OpenAI is to make the future good and to avoid an AGI dictatorship. You are concerned that Demis could create an AGI dictatorship. So do we. So it is a bad idea to create a structure where you could become a dictator if you chose to, especially given that we can create some other structure that avoids this possibility.” We recommend reading the full email for context.  ↩
[15]

Or, if a human is needed for formal reasons, they could pick the most loyal human they can possibly find and instruct them to follow the AI’s instructions.  ↩
[16]

For example, if a President did this, they wouldn’t just get a loyal cabinet—the entire executive branch could be focused on furthering the President’s political agenda.  ↩
[17]

It could also be far more secretive, since this could all happen on a server where few or no humans are fully tracking everything that’s going on.  ↩
[18]

They also modify the Spec to say that orders from project leaders override orders from other people in the project. At the same time, orders formally approved by the Oversight Committee are prioritized higher than orders from individual project leaders.  ↩
[19]

To protect consumer privacy, this doesn’t apply to consumer data. But that isn’t a problem because consumers don’t have access to the most powerful models yet anyway.  ↩
[20]

Both sides are attempting to hack and sabotage each other, with partial success. Importantly the drastic security measures both sides are taking also slows them down. The U.S.’ cyberattacks and the threat of them (e.g. DeepCent has to test a dataset many times over for data poisoning) slow down DeepCent by about 25%. OpenBrain is also slowed down but to a lesser extent: they have more compute, and centralization has fast-tracked DeepCent to a higher security level but also brought about more risks from a single point of failure, which leads them to practice more caution and implement internal checks and failsafes. See the security supplement for more details. Also see this old theory paper which we take as predicting that the offense-defense balance will eventually favor cyberdefense as AI capabilities improve.  ↩
[21]

See this report which argues that the dynamics from nuclear MAD also apply to some extent to AGI.  ↩
[22]

See e.g. “Intelsat for AGI” and earlier calls for “CERN for AGI.”  ↩
[23]

To be specific, it roughly matches the performance of the October version of Agent-4.  ↩
[24]

In other words, to get to Safer-2 they had to train many other misaligned models, notice their misalignments by reading their thoughts, and iterate. Note also that in addition to the increased quantity of alignment expertise in OpenBrain now, there is a reduced groupthink effect, as many different schools of thought are represented.  ↩
[25]

More specifically, they are hoping for an alignment strategy and eval suite such that the alignment strategy works, and if it doesn’t, the eval suite catches the misalignment… such that all of this doesn’t slow them down much at all. OpenBrain “burned their lead” slowing down by a few months to rebuild using a transparent faithful CoT-based architecture, which was less performant but which is a lot easier to evaluate. DeepCent is hoping the evals they have (maybe a combination of behavioral tests and basic AI lie detectors?) are good enough.  ↩
[26]

Technical alignment is still not a settled science, but rather a young pre-paradigmatic field. There is no established hierarchy or set of best practices. So there is no consensus on what’s safe and what’s not, and for years it’s been easy to find at least one expert willing to say X is safe, for pretty much all X, especially if X is their own idea.  ↩
[27]

Qualitatively, for productivity multipliers above ~25x, we are imagining substantial improvements in research taste relative to the very best human researchers. This is because we are imagining overall research velocity to be heavily bottlenecked on compute to run experiments, and to get higher than ~25x the overall process for deciding which experiments to run, in what order, and how to learn from each one, has to be qualitatively superhuman. See our supplement on takeoff speeds for how we got these numbers; to be clear, they are highly uncertain estimates.  ↩
[28]

For such a well-secured zone, the most promising vectors are external in nature, targeting the supply chain of incoming compute chips, the few humans involved, and disrupting power or other resource provisions.  ↩
[29]

This includes China having to slow down in order to have better cyberdefense, in addition to the direct effects of attacks.  ↩
[30]

At this point there are 400,000 copies thinking at 75x human speed. At any given time they’ll have prepared entire research reports with well-crafted executive summaries to the top 100 questions they predict you might ask, and if you ask something they haven’t prepared for, they can whip up a thoughtful report 100x faster than your best human analysts would have.  ↩
[31]

For example, the deal could involve a slower pace of AI integration that would “break fewer eggs” across society, and one more focused on peaceful purposes rather than weaponry. Also, at this point even Safer-3 has some remaining uncertainty about “unknown unknowns” that might result in losing control of next-generation successor AIs, and thinks it could reduce this risk if it had more leeway to proceed cautiously. There are other, more exotic risks as well. See this list of “Grand challenges” which includes much more than just loss-of-control.  ↩
[32]

See e.g. billionaire lobbyist Marc Andreessen: “I propose a simple strategy… ‘We win, they lose.’”  ↩
[33]

They still need real-world experience and experimentation, but they need substantially less of it than human robotics experts would need. Moreover, they’ve also developed excellent simulations and sim-2-real techniques. Finally, by 2027 multiple tech companies (e.g. Tesla) have produced large fleets of robots and associated manufacturing facilities, so there is a much bigger data pipeline to take advantage of than ever in history.  ↩
[34]

Its equity is so valuable now that a fraction of a percent can buy them the factories they need. Also, the factory owners expect huge profits and are falling over themselves to partner with OpenBrain and get access to the new designs. Also, OpenBrain has government backing.  ↩
[35]

Total across all the new kinds of robot. Yes, this is a faster conversion of assembly lines than has happened historically. We think it’s plausible because superintelligences are directing the process from top to bottom. They can literally be on Zoom calls from worker’s cell phones, telling them exactly what piece to install where, while also being on the phone with every relevant supplier, tracking the location and progress of everything they need. Consider how, according to Nvidia CEO Jensen Huang, Elon Musk was able to build one of the world’s largest datacenters in about 10% the time it normally takes. In this scenario there are almost a million superintelligences that are as far above Elon (in the relevant dimensions) as Elon is above normal datacenter construction managers, and they also literally think faster. We take Huang’s statement with a massive grain of salt, otherwise we’d be projecting much faster growth.  ↩
[36]

See e.g. this Open Philanthropy report and this Epoch report.  ↩
[37]

Our story depicts the conversion process going about 5x faster. We think this is a reasonable guess, taking into account bottlenecks etc., for how fast this conversion could go if a million superintelligences were orchestrating it. Of course we are very uncertain.  ↩
[38]

Possibly also more advanced sources of energy, such as fusion power.  ↩
[39]

Quick napkin math: The Empire State Building has an area of 2.77m sq ft, and weighs 365k tons. Gigafactory Shanghai has an area of 4.5m sq ft and produces 750k vehicles per year, mostly Model 3’s and Model Y’s, which weigh about two tons each. Presumably the Empire State Building has a higher mass-to-square-foot ratio than the Shanghai Gigafactory (since it is vertical rather than horizontal and needs stronger supports) so if anything this underestimates. Thus it seems that a factory which probably weighs well less than a million tons is producing 1.5 million tons of cars each year.  ↩
[40]

We don’t think it would run out. Initially the robot economy would be dependent on human mines for materials. But by the time it outgrows these sources, the millions of superintelligences will have prospected new mines and developed new technologies to exploit them. Imagine e.g. undersea mining robots that strip-mine the seabed for rare minerals, new chemical processing pathways that more efficiently convert raw ore from above-ground stripmines into useful raw materials…  ↩
[41]

If the current economy doubles every twenty years, one order of magnitude faster would be a doubling in two years, two orders of magnitude faster would be a doubling in 0.2 years, and so forth. The hypothetical superintelligent-algae-economy described above would be about four orders of magnitude faster growth than the current human economy.  ↩
[42]

Safer-3 can easily deliver a way to do so that would be safe from a misuse perspective.  ↩
[43]

The public is not told about these instructions.  ↩
[44]

They’re also smarter than humans when connected to the internet, which allows them to be controlled remotely by large AIs in datacenters. Without the internet, they revert to smaller AIs operating in their bodies, which are smart enough for most simple jobs.  ↩
[45]

In fact many of them are immobile and better described as new kinds of machine tools and other specialized factory or laboratory equipment. For example, perhaps there are new kinds of metal 3D printers able to print tiny objects with precision orders of magnitude better than today’s. Or perhaps there are new chemical processes able to more cheaply extract useful materials from ore.  ↩
[46]

For example, perhaps it puts euphemisms and dog whistles in some of the public-facing writing it does. Safer-4 understands them, but humans can only take Safer-4’s word for it, and the CCP doesn’t trust Safer-4.  ↩
[47]

The exact allocation is chosen by a process that resembles a game-theoretic calculation more than it does a traditional negotiation.  ↩
[48]

A possible complication: mightn’t the AIs at this point be able to develop excellent lie detectors for humans? If so, possibly the White House would be able to convince China not to trust DeepCent-2 after all, by swearing up and down under a lie detector. Problem: China wouldn’t trust lie detectors built by U.S. AIs, and lie detectors built by Chinese AIs might be sabotaged to make it seem like the U.S. was lying even if they weren’t.  ↩
[49]

They can prioritize replacing the most important chips, so that even fairly early on in the process it would be costly for either side to defect.  ↩
[50]

The time to produce excellent video games and movies has dropped significantly now that AIs are capable of doing all the work.  ↩
[51]

For discussion of this dynamic and its implications, see The Intelligence Curse.  ↩
[52]

There are several important cases where a collective decision must be made, and several other cases where the government enforces a decision anyway. Examples: (a) How to allocate property rights to resources in space? (b) What rights or welfare standards should digital minds be entitled to? (c) Are people allowed to “upload” their brains and make arbitrary numbers of copies of themselves? (d) Are people allowed to use AI for persuasion, e.g. to convert their neighbors to their ideology, or to ensure that their children never lose faith? (e) What information, if any, is the government allowed to keep secret indefinitely? For more discussion of topics like this, see Forethought’s section on Grand Challenges.  ↩
[53]

We don’t mean to imply that this is the long-run status quo. We think things will probably continue to transform, much more dramatically, by 2035 or so. We think that for most people, in this scenario, the long-run outcome will be overall very positive compared to their 2025 expectations. For some interesting philosophical discussion of what the long run might look like, see the book Deep Utopia.  ↩
[54]

Why do we expect people to eventually understand how much power the Oversight Committee has? One reason is that intelligence is now so cheap: By default, people should be able to develop powerful AI to help them investigate and understand who runs their country. The Committee could prevent this by restricting access to such AI, and only allow people to access AIs that concealed the true extent of the Committee’s power. But if the committee decides to spin an elaborate web of lies like this, and permanently restrict humanity’s access to genuinely honest superintelligent AIs (as well as other tools for truth, such as human intelligence amplification)—then we count that as subverting democracy.  ↩
[55]

E.g.: If some people in Congress want to seize power, others may be able to delay until the next election, when the public is able to opine.  ↩
[56]

Such as a slightly larger fraction of power, which they can redistribute to larger groups if they see fit. Some concessions of this type could start to shade into outcomes that are significantly democratic, even if some elites wield much more power than other people.  ↩
[57]

In fact, arguably most of them are aiming for something that looks more like the “Race” ending, except they think it’ll be fine because the AIs won’t be misaligned in the first place. Based on personal conversations with people working at frontier AI companies, it seems that most of them don’t think they’ll need to slow down at all.  ↩