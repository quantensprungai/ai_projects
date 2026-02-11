Romeo Dean | April 2025
Training RunsTraining Compute in Fp16 FLOP (log scale)
GPT-4 (2e25)GPT-4.5 (2e26)1000xGPT-4 (2e28)Dec 2024Jun 2025Dec 2025Jun 2026Dec 2026Jun 2027Dec 202710^2510^2610^2710^28
Agent-1Agent-0Agent-2Agent-3Agent-4
ai-2027.com

Figure 1: The training runs in AI 2027, informed and justified by our compute production, compute distribution and compute usage sections.
Summary

Compute is one of the key inputs to AI progress. In this supplement we only consider AI-relevant compute. We frequently refer to H100-equivalents (H100e) throughout the supplement, which we define as AI-relevant compute with processing performance converted into units of the Nvidia H100 GPU. Processing performance is most directly relevant to training compute, but is also a strong proxy for inference compute too.

In this supplement we model AI-relevant compute production in Section 1 by looking at supply chain bottlenecks and estimates that the globally available AI-relevant compute will grow by a factor of 10x by December 2027 (2.25x per year) relative to March 2025 to 100M H100e.
chip efficiency
1.35x
chip production
1.65x
Global AI compute
2.25x/year
Compound effect of efficiency × production
Mar 2025 10M H100e
Dec 2027 100M H100e
= 1M H100e
ai-2027.com

Figure 2: We project the global stock of AI-relevant compute to grow 10x by December 2027.

In Section 2 we model the distribution of compute among relevant actors, breaking this down both by owners of the compute and end-users that either rent or also own the compute. We expect usage to concentrate in the hands of leading AGI companies (e.g., OpenAI, Anthropic, xAI) and the AGI-focused development efforts within larger tech companies (e.g., Google, Meta), the largest two or three of which will have a 15-20% share of the globally available AI compute by the end of 2027 (around 15-20M H100e) up from a 5-10% share today (around 500k H100e).
Compute breakdown by AI companies2024 estimate and 2027 projection, H100-equivalents
0M5M10M15M20M25MOpenBrainUS 2nd in AGIdevelopmentUS 3rd in AGIdevelopmentUS 4th in AGIdevelopmentRest of US andnon-AGI-developmentDeepCentRest of China andnon-AGI-developmentRest of World7%6%5%5%49%1%11%14%20%16%14%9%20%10%2%9%December 2024 estimate
December 2027 projection
ai-2027.com

Figure 3: We project the global distribution of AI-relevant compute to concentrate in leading AI companies (with their shares of the global compute stock roughly tripling) and China to maintain a roughly constant share of global compute (around 12%) but to unify it towards a single national AI effort.
global compute
2.25x
share of global
1.5x
Leading AI Company compute
3.4x/year
Compound effect of global compute × share
Dec 2024 500K H100e
Dec 2027 20M H100e
= 125K H100e
ai-2027.com

Figure 4: We project the compute available to the leading AI company to grow 40x by December 2027, with a factor of ~10x coming from the global stock of AI-relevant compute growing and ~4x coming from their usage share of the total stock.
Global AI Compute with Leading Company ShareH100 equivalents (log scale)
2.25x / year3.4x / yearDec 2023Dec 2024Dec 2025Dec 2026Dec 2027100K1M10M
100MGlobal AI ComputeLeading US Company
ai-2027.com

Figure 5: Trend in global compute growth (2.25x/year) and the growing share used by the leading AI company (1.5x/year) through December 2027. The compound effect is a 3.4x/year increase in compute for the leading AI company. FLOP numbers assume 40% model flop utilization.

In Section 3 we describe how we expect leading AI companies to use their compute resources, with shifts away from pretraining and external deployment, towards post-training, synthetic data generation, and internal deployment (i.e. research automation and research experiments). We project a concentration of compute usage within the leading AI company to research automation, with a relatively small share (5-10%) used on actually running the AIs, and large shares for generating synthetic training data (20%) and giving the AIs large research experiment compute budgets (35%). Actual training runs and external deployment take up smaller shares (20%) but in absolute terms, the compute used on each is still more than 20x greater than in 2024.
OpenBrain's Compute Allocation, 2024 vs 202720242027estimateprojection
Research experiments TrainingData generationExternalDeployment
ResearchexperimentsRunning AIassistantsTrainingDatagenerationExternalDeployment
ai-2027.com

Figure 6: Compute use concentrates towards research automation. Data generation also increases.

In Section 4 we do an inference compute analysis for the expected AI research automation in 2027 with estimates on the copies and speed of the AI models deployed. Once they make significant algorithmic efficiency progress by the end of 2027, we expect a leading AI company to be able to deploy about 1M copies of superintelligent AIs at 50x human thinking speed (500 words per second), using 6% of their compute resources, mostly with specialized inference chips.
Research Automation Deployment Tradeoff
Mar 2027Jun 2027Sep 2027Speed (tokens/sec)Parallel Copies101001.00010.00010K100K1M10M200K copies30x Humanspeed300K copies50x Humanspeed
Human thinking speed10 words/sec10x Humanthinking speed100x Humanthinking speed
ai-2027.com

Figure 7: Our expected deployment of AI research assistants for research automation in 2027 using specialized inference chips. The green lines use 6% of the leading AI company’s H100e compute.

In Section 5 we look specifically at the training run, total cost, total revenue, and total power usage projections for the projected leading AI company through 2027. We project revenue and cost growth rates to both be around 3x/year, and power usage by the leading AI company to be around 10GW by December 2027, which implies that they use around 0.8% of the US power capacity, and AI in total uses 60GW globally, 50GW in the US, which is around 3.5% of projected US power capacity (1.35TW, up from 1.28TW today).
GLOBAL AI CAPEX
$2T
COST OF OWNERSHIP OF ACTIVE COMPUTE
KEY METRICS 2027
GLOBAL AI POWER
60GW
PEAK POWER
OPENBRAIN REVENUE
$140B
2027 ANNUAL
TOTAL CAPITAL EXPENDITURE
$400B
COST OF OWNERSHIP OF OPENBRAIN'S ACTIVE COMPUTE
SHARE OF US POWER ON AI
3.5%
50 GW OF 1.35TW CAPACITY
OPENBRAIN COMPUTE COSTS
$100B
2027 ANNUAL
OPENBRAIN POWER REQUIREMENT
10GW
PEAK POWER
ai-2027.com

Figure 8: A summary of the projections in Section 5.

All estimates are based on publicly available information which is scarce and uncertain. Broadly speaking, Sections 1 and 2 are relatively informed and independent of the AI 2027 scenario, while Sections 3, 4 and 5 are far more conditional on the rapid AI capabilities progression that occurs in AI 2027.
Section 1: Compute Production
How much compute will be produced?
Compute Production
Section 2: Compute Distribution
Who will the compute go to?
OpenAI
Google
Anthropic
Others
Section 3: Compute Usage
What will they use it on?
Training
External Deployment
Internal
Section 4: Inference Compute
Internal Agents
Section 5: Industry Metrics
Revenue
Costs
Power

Acknowledgements: David Schneider-Joseph, Erich Grunewald, Konstantin Pilz, Lennart Heim, Mauricio Baker, Tao Lin.
Introduction

Computing power is one of the key inputs to AI progress. Most computations used in AI training and inference can be completed in parallel, so AI chips or AI accelerators are computational devices (e.g., GPUs) which are particularly efficient at such parallel computation, making them far more effective than traditional processors like CPUs for AI computing workloads.

Indeed, in this supplement we only consider AI-relevant compute which we define specifically as any computational unit capable of achieving Total Processing Performance (TPP) of at least 4,000 and Performance Density (PD = TPP / die size) of at least 4. This definition is set just below the A100 SXM GPU, NVIDIA's state of the art chip in 2021. For reference, Nvidia's H100 GPU has a marketed ~15,800 TPP and 19.4 PD. Intuitively you can think of our definition as ‘anything at least ¼ as efficient as the H100 counts’.

We frequently use H100-equivalents (H100e) as units of AI-relevant comute throughout the supplement, which we define as compute processing performance (in TPP) converted into units of H100 processing power (~15,800 TPP). The choice to focus on TPP makes the analysis herein most directly relevant to training compute, but is also a strong proxy for inference compute too. Nonetheless, in the section on inference compute for running research agents we perform calculations in terms of memory bandwidth instead of TPP.
Section 1. Compute Production

Status: Uncertain but informed. This section is an informed forecast based on public information.
chip efficiency
1.35x
chip production
1.65x
Global AI compute
2.25x/year
Compound effect of efficiency × production
Mar 2025 10M H100e
Dec 2027 100M H100e
= 1M H100e
ai-2027.com

Figure 9: Summary of our compute production forecast.

We expect the total stock of AI-relevant compute in the world will grow 2.25x per year over the next three years, from 10M H100e today to 100M H100e by the end of 2027. We estimate this by decomposing growth in total compute availability, measured in H100e, into improvements in (A) chip efficiency and (B) chip production, contributing a baseline growth rates of 1.35x and 1.65x respectively.
	2023	2024	2025	2026	2027
Performance density (PD) multiplier on average chips produced (H100 = 1x)	.66x	.9x	1.22x	1.64x	2.4x
Total AI chip area produced (H100-sized chip = 1)	3M	5.5M	9M	16M	25M
Total AI chips produced in H100e processing performance (TPP)	2M	5M	11M	25M	60M
Cumulative H100e available	4M	8.5M	18M	40M	100M
Total cost of ownership per H100e	$50k	$40k	$25k	$20k	$15k
Total AI datacenter spending	$110B	$270B	$400B	$600B	$1T
Total datacenter power requirement per H100e	1.3kW	1.0kW	750W	700W	550W
Total AI datacenter power requirement	5GW	9GW	15GW	29GW	62GW

See also the full spreadsheet model.
Chip efficiency

For improvements in chip efficiency, we extrapolate Epoch AI’s historical trend of 1.35x per year and find it is consistent with the already reported performance of upcoming chips such as NVIDIA’s GB200 as well as rumoured plans for the Rubin series detailed below.
Scaled to performance
Scaled to die size
H100
(1 x 10^15 FLOP/s)
B200
(2.5 x 10^15 FLOP/s)
R200*
(6 x 10^15 FLOP/s)
2023
2025
2027
*Expected
ai-2027.com

The widely adopted state of the art GPU in 2024 is NVIDIA’s H100, which has 1e15 FP16 FLOP in raw performance. In three years, we predict the widely adopted state of the art GPU to be NVIDIA’s Rubin GPU (R200), which we project to achieve a ~2.4x improvement over the B200 (widely used in 2025-2026) to 6e15 FP16 FLOP performance. We think this will be achieved through a 1.2x increase in die size, a 1.7x increase given the transition from TSMC’s N4 to N3 process, and a 1.1x increase from other miscellaneous improvements.

To avoid confounding efficiency with the increase in die size, we need to adjust this overall 6x increase in the SOTA GPU performance from the H100 to the R200 down for the roughly 2.4x increase in die size between these chips. This means we get an overall 2.5x increase in chip efficiency over the next three years, matching the 1.35x per year historical trend. We assume that the trend on frontier NVIDIA GPUs is a good proxy for the trend on the average GPUs available each year, not only because they will make up most of the chips, but also because the performance of other popular chips (such as Google’s TPU series) should rely on highly correlated upstream factors such as TSMC’s manufacturing process advances.
Chip production
AI Chip Production Forecast Summary, 2025-2027Chip manufacturingChip Design
1.6x production, 1x share1.1x production, 1.5x share1.6x production, 1x shareSK HynixMicronSamsungTSMCOthersTSMCOthersNvidiaGoogleAmazonAMDHBMWafersPackagingLegendAI-relevant
Non-AI
ai-2027.com

Figure 10: Summary of our chip production model.

For increases in chip production we further decompose into three key components driving production: (B.1) wafer production, mainly fulfilled by TSMC’s N5 and N3 processes, (B.2) advanced packaging capacity, also mainly serviced by TSMC’s CoWoS technology, and (B.3) high bandwidth memory (HBM), mainly supplied by SK Hynix, and increasingly so by Micron and Samsung.

We estimate 1.2M H100e to have been shipped in 2023 by Nvidia and for these to have made up about 60% of the total AI compute market, mostly due to Google’s in-house TPU production supported by Broadcom, for a total of 2M H100e in 2023. We expect this to have increased to 5M H100e in 2024, again with roughly 60% coming from Nvidia.

We mainly focus on production numbers for TSMC, and SK Hynix since they make up about 90% and 60% of their respective market shares, and expect trends in the rest of the market to be similar. Overall, over the next three years, we project AI chip production to be bottlenecked by advanced packaging and HBM production to about 1.65x per year.
Wafer Production

TSMC’s 4N node (within their N5 process) has been chosen for Nvidia’s next generation of Blackwell GPUs, while the N3 process will likely be used for the Rubin GPUs projected to enter mass production in late 2026. In 2023 AI accelerators likely used at most 3% of TSMC’s combined N5 and N3 production lines, and given reports of these production lines sometimes running at as little as 70% capacity, wafer production is very unlikely to bottleneck AI chip production over the next three years. Even if production doubles each year, AI chip production shouldn’t reach more than ~40% of the fabrication capacity by 2027, even ignoring new production capacity coming online (at a rate of ~15% expansion per year). Notably, beyond 2027, we’d expect wafer production limits to slow the growth rate of chip production from 1.65x to around 1.25x.
Advanced Packaging

AI accelerators require advanced packaging to create dense connections between logic and memory for the high throughput required by AI workloads. Currently TSMC’s advanced packaging capacity is mostly used by AI accelerators and has been reported to have expanded 2.5x from 2023 to 2024. Given TSMC’s expectation of 50% annual growth rate in AI demand, we don’t expect them to expand these production lines too aggressively, in fact they have announced plans to increase capacity by 1.6x per year through 2026. Though given the ~2.5x expansion seen in 2024, we expect raw production expansion to beat expectations and continue at around 2x/year. Though at the same time advancing chip efficiency will require the difficulty of manufacturing processes required to also beat expectations (specifically moving to 3D packaging or future advances). Therefore, while we model the raw production capacity grow at 2x/year (ignoring increased difficulty), we then adjust down by 1.2x/year for the manufacturing difficulty (e.g., due to lower yields,changing production lines to meet new requirements) for an overall rate of 1.65x per year over the next 3 years.
High Bandwidth Memory

AI workloads are memory intensive and require expensive, fast High Bandwidth Memory (HBM). HBM production is an advanced process that involves precisely stacking and connecting several DRAM chips. SK Hynix were the first to develop this technology, and are the first to be producing the latest generation HBM3e. Micron and Samsung are also catching up with roadmaps to be competitive with SK Hynix for future HBM4 generations and beyond. HBM production lines have been reported to be expanded 2.5x in 2024 compared to 2023, but SK Hynix are only projecting a 1.6x increase in demand going forwards. Similar to advanced packaging, we expect HBM production (ignoring difficulty) to beat these expectations and grow at 2x, but again adjust down by 1.2x given the increasing manufacturing difficulty (in particular the move from 8-Hi, to 12-Hi and 16-Hi stacks) to give a rate of 1.65x per year over the next three years.
Hardware R&D automation

In line with our broader capabilities and AI R&D projections, we expect leading AI companies in 2027 to automate specialized chip designs and increase in-house chip production. There are early signs of such ambitions, such as OpenAI’s hiring of prolific Google TPU designers and plans to design their first in-house chip in 2025. Though as 1.35x per year improvements in chip efficiency keep getting harder and harder to achieve, and our expectation that research automation will mostly be directed elsewhere, we expect most these effects to provide a marginal increase in effect on the average chip efficiency to 2.4x the H100 (rather than 2.2x which would match the baseline trend), mostly through a wave of production of inference specialized chips.
Section 2. Compute Distribution

Status: Uncertain but informed. This section should be read as an informed forecast based on limited public information.
Compute Breakdown by End-User, H100e
OpenAIGoogle AGI developmentRest ofGoogleRest ofMetaRest ofthe USRest ofChinaRest of the world
OpenAIAnthropicGoogle AGIdevelopmentRest ofGooglexAIMeta AGIdevelopmentRest of MetaRest ofthe USChina AGIdevelopmentRest of the world0.5M0.6M1.3M0.7M2.0M1M1.5M20M14M16M5M9M7M7M10M10M9M20242027estimateprojection
ai-2027.com

Figure 11: Summary of our compute distribution projection to the end users of the compute.

In this section we project the share of the world’s AI-relevant compute owned by compute providers and the share of AI compute utilized by end-users, through 2027. Compute owners are entities that own and operate AI compute clusters. End-users are entities that use the compute clusters for their AI workloads. In some cases, entities are both providers and end-users (e.g., Google, Meta, xAI). In other cases, owners mostly rent out their compute to other entities (e.g., Microsoft renting to OpenAI, Amazon renting to Anthropic, Oracle renting to OpenAI). We use the following exhaustive taxonomy of owners and end-users.
Taxonomy of relevant actors
Owners	End-users
Microsoft	OpenAI
Google	Anthropic
Amazon	Google AGI development
Meta	Rest of Google
xAI	Meta AGI development
Oracle	Rest of Meta
China Big Four (Bytedance, Alibaba, Tencent, Baidu)	xAI
Leading AI Company	China AGI development
Rest of the US	Rest of the US
Rest of the world	Rest of the world

According to our projections, leading AI companies will have 20-40x as much AI compute by December 2027 in absolute terms, compared to December 2024, with a factor of 10x coming from the previously covered growth in compute availability, and a factor of 3x coming from increased concentration of compute in leading AI companies and their AGI development efforts.
Compute owners
Recent past

In the compute production section we estimated there being 4M H100e of AI-relevant compute available globally at the end of 2023, and 8.5M by the end of 2024. Previous work by Epoch AI in Appendix B of Can scaling continue through 2030? estimates that Meta and Microsoft each had 150,000-600,000 H100e at the start of 2024, and that Google and Amazon each had 400,000-1.4M H100e. Our point estimates for the start of 2024 (December 31st 2023) are uncertain given the scarcity of public information, but they fall in the middle of Epoch AI’s ranges and align with several overlapping sources. We use this report of 2024 production and purchases to produce estimates for the resulting December 2024 distribution.
Historical breakdown by compute ownersEstimated, H100e
0K500K1000K1500K2000KMicrosoftGoogleAmazonMetaxAIRest of the USChina Big FourRest of the world300K800K600K450K10K500K300K450K1.1M1.8M1.3M1.0M200K1.4M800K800KDecember 2023
December 2024
ai-2027.com

Figure 12: Estimated historical AI compute breakdown in H100e among owners of the compute.

The top 5 US spenders on AI servers according to Omdia (and reported by the Financial Times) in 2024 are shown below, with our estimate of how many H100e they acquired and therefore their spending per H100e. Google’s strong spending effectiveness is due to their in-house TPUs, already in their 6th generation. Amazon and Meta also have significant in-house designs but they are in earlier stages of the R&D process. Microsoft and xAI bought almost entirely Nvidia chips.
	2024 spending on AI servers	H100e gain in 2024 vs. 2023	Spending per H100e
Microsoft	$32B	800K	$39k
Amazon	$26B	700K	$37k
Google	$22B	1M	$22k
Meta	$20B	550K	$36k
xAI	$7B	200K	$37k
Intermediate 2025 Projection
	Projected 2025 spending on AI servers	H100e gain in 2025 vs. 2024	2025 Spending per H100e
Microsoft	$56B	2.4M	$23k
Amazon	$48B	2.2M	$22k
Google	$44B	2.2M	$20k
Meta	$35B	1.6M	$22k
xAI	$30B	1.3M	$23k

For forecasting the 2025 compute distribution we look at the top 5 US companies by spending on AI and their 2024 share of spending on AI servers. We find the following:

    Microsoft has announced $80B in AI spending for 2025, and last year 55% of their spending went to AI servers ($31B out of $56B). We expect the share on AI servers to increase to 70%, producing an estimate of $56B spending on AI servers in 2025.

    Google has announced $75B in AI spending for 2025, and last year 42% of their spending was on AI servers ($22B out of $52B). We expect the share on AI servers to increase to 58%, producing an estimate of $44B spending on AI servers in 2025.

    Amazon has announced $100B in spending for 2025, and last year 33% of their spending went to AI servers ($26B out of $78B). We expect the share on AI servers to increase to 48%, producing an estimate of $48B spending on AI servers in 2025.

    Meta’s announced $65B in spending for 2025, and last year 50% of their spending went to AI servers ($20B out of $40B). We expect the share on AI servers to increase 54%, producing an estimate of $35B spending on AI servers in 2025.

    xAI announced (minute 1:05:00) around $30B spending on AI servers in 2025.

Projected breakdown by compute ownerProjection, in H100e
0M5M10M15M20MMicrosoftGoogleAmazonMetaxAIRest of the USChina Big FourRest of theworldLeading AIcompany3.5M4M3.5M2.6M1.5M2M1.5M1.3M7.5M7.5M6.5M4.6M4M4M3.5M2.5M1.5M18M18M18M9M9M9M8M5M6MDecember 2025December 2026
December 2027
ai-2027.com

Figure 13: Projected AI compute breakdown in H100e among owners of the compute.
2027 Projection
Compute Breakdown by Owner, H100e
MicrosoftGoogleAmazonMetaRest ofthe USChinaBig FourRest of the world
MicrosoftGoogleAmazonMetaxAIRest ofthe USChinaBig FourRest of the worldLeading AI company1.1M1.8M1.3M1M1.4M0.8M0.8M18M18M18M9M9M9M8M5M6M20242027estimateprojection
ai-2027.com

Figure 14: Projected AI compute owner shares, values in H100e.

By 2027, our compute production section has the total compute available growing to 100M H100e which corresponds to a 2.25x increase per year. We should expect this explosive level of growth to easily shake up the distribution of compute. We expect this growth to be driven by sustained trends in demand from end-user AI developers that start to have annual revenues in the tens of billions from their AI models.

We make the following projections:

    Microsoft (driven by their relationship to OpenAI) scale aggressively, going from 13% to 18% of the world’s compute share.

    Google’s existing compute overhang, leads to a lower rate of expansion and their compute share edges down from 21% to 18%.

    Amazon, scales aggressively with sustained demand from Anthropic and their own AI efforts justifying aggressive buildouts that inches their share up to 18%.

    Meta’s 12% share slips to 9% because revenues from their mostly open source AI models lag behind and don't justify the same degree of aggressive buildouts in 2026 and 2027. Note this still means their absolute compute increases 7x from 1.1M to 7.5M H100e.

    xAI scales aggressively, with total hardware capital expenditure reaching around $100B by 2027, backed by decent AI revenue and Elon Musk’s backing, growing their compute share from 2% to 9%.

    The rest of the US, which includes larger players like Oracle and Coreweave as well as smaller providers and owners, get somewhat crowded out and have slightly lower economic incentives to scale as aggressively as the bigger players. Overall, the rest of the US’s share falls from 18% to 9%.

    China’s Big 4 start to face marginally more difficulty in securing AI compute due to export controls, although China’s domestic production ramps up and produces chips in large quantities at a quality around 3 years behind Nvidia. Nonetheless their share only dips from 9% to 8% since US export controls stay poorly enforced, smuggling in significant quantities to other Chinese entities means the total compute in China is significantly higher. Domestic production also ramps up through SMIC but is years behind in efficiency.

    The rest of the world also gets somewhat crowded out for similar reasons to the smaller US players, and their share dips from 9% to 5%.

    Finally, we expect a future ‘leading AI company’ to decide to build their own datacenters in the latter end of 2026 and during 2027. We believe this is consistent with their revenues reaching an annualized run rate of $50B by the end of 2026, and their AI capabilities helping them develop specialized in-house GPUs in 2027. Overall, we predict that with about $90B of spending they will efficiently acquire around 6% of the world’s AI compute (excludes the R&D costs of in-house chip designs).

Compute end-users
Recent past

    OpenAI’s recent cost reports indicate that they are renting an average of around 250k H100s through 2024, which we expect to be tail-heavy reaching 460k by the end of the year, mainly supplied directly by Microsoft, but also through deals with Oracle and Coreweave. This puts their share of the global 8.5M H100e at around 5% by the end of the year.

    Anthropic's compute usage is expected to be slightly behind at 4%, given lower revenues, users, and therefore access to capital. We expect them to have access to around 360k H100e by the end of the year, a lot of this being recently added by a 400k Trainium2 cluster provided by Amazon.

    xAI has an expanding 200k H100 cluster, putting their share at 2%.

    Google and Meta’s AI compute fleets make up 21%, 13% of the world’s share, but we only expect them to be using around 30% of these clusters for AGI development. Most of the rest of Google and Meta’s AI compute is dedicated to developing and servicing their large suite of recommendation algorithms around the world.

    We expect most of the cloud service demand from the rest of Amazon, Microsoft, Neocloud and smaller providers fleets to be used by companies and startups throughout the rest of the US and rest of the world, each with shares of around 20%.

    We expect China to use essentially all of the compute owned by China’s Big 4, as well as around half of what is owned by the ‘rest of the world’ category, given how much of this is concentrated in Malaysia and Singapore, which is likely used by (or even directly smuggled into) China. This leads to an estimate for a total 14% compute usage, of which we expect 20% to be dedicated to AGI development in late 2024 for a total China AGI development share of 3%.

2027 Projection

For the sake of this section, we assume that OpenAI will be the leading AI company in 2027. The projections here are therefore just an illustration of how the compute breakdown would look under a scenario where OpenAI remains the leading AI company.**
Compute Breakdown by End-User, H100e
OpenAIGoogle AGI developmentRest ofGoogleRest ofMetaRest ofthe USRest ofChinaRest of the world
OpenAIAnthropicGoogle AGIdevelopmentRest ofGooglexAIMeta AGIdevelopmentRest of MetaRest ofthe USChina AGIdevelopmentRest of the world0.5M0.6M1.3M0.7M2.0M1M1.5M20M14M16M5M9M7M7M10M10M9M20242027estimateprojection
ai-2027.com

Figure 15: Projected AI compute end user shares, values in H100e.

    OpenAI and Anthopic both scale aggressively, motivating aggressive buildouts by their investors Microsoft and Amazon, eventually owning some of their own datacenters. OpenAI’s usage share of the world’s AI compute jumps from 5% at the end of 2024 to 20% and Anthropic from 4% to 11%.

    xAI continues to use the entirety of their owned compute explained in the compute owner section, so their usage share also goes from 2% to 12%.

    Google and Meta now dedicate 90% and 80% respectively of their compute to AGI development so Google’s AGI development share grows from 6% to 16%, and Meta’s AGI development share from 4% to 6%.

    China’s total compute share stays at around 13%, but now they dedicate 90% to AGI development as opposed to 40%, so the China AGI development share goes from 2% to 12%.

    Finally, for similar reasons to the providers section, we expect the rest of the US and rest of the world’s end users to be crowded out, and their usage shares to dip from 23% to 11% and 18% to 11% respectively.

Projected breakdown by compute end-userProjection, in H100e
0M5M10M15M20MOpenAIAnthropicGoogle AGIdevelopmentRest of GooglexAIMeta AGIdevelopmentRest of MetaRest of the USChina AGIdevelopmentRest of ChinaRest of the world2.0M1.3M2.2M1.8M1.5M1.3M1.3M3.6M404K1.6M2.6M6.0M4.0M5.6M1.9M4.0M3.2M1.4M5.2M2.2M1.8M4.6M20M14M16M2M9M7M2M10M10M2M9MDecember 2025December 2026
December 2027
ai-2027.com

Figure 16: Projected AI compute end user breakdown in H100e.
Section 3. Compute Usage

Status: Exploratory and uncertain, this section is a best guess not an informed forecast.
OpenBrain's Compute Allocation, 2024 vs 202720242027estimateprojection
Research experiments TrainingData generationExternalDeployment
ResearchexperimentsRunning AIassistantsTrainingDatagenerationExternalDeployment
ai-2027.com

Figure 17: Summary of our compute usage forecast.

We expect the following internal compute usage breakdown for a leading AI company using public evidence from today’s usage and educated guesses about their relative development, deployment, and research priorities going forwards. The rest of this section is structured as a row by row justification for the values in the following table.
	2024	2025	2026	Q1 ‘27	Q2 ‘27	Q3 ‘27	Q4 ‘27 (racing)
Total compute usage and costs	Average compute used in during the period (H100e)	250K	1M	4M	7M	9M	12M	15M
→ Compute spending during the period	$5.4B	$12.5B	$30B	$20B	$25B	$30B	$45B
→ Compute budget in fp16 FLOP, 30% utilization	2.5e27	1e28	4e28	2e28	2.5e28	3e28	4e28
Breakdown
Training	1) Training runs	40%	40%	40%	30%	27%	22%	20%
→ pre-training share	60%	50%	40%	10%	8%	5%	5%
→ post-training	40%	50%	60%	90%	92%	95%	95%
Internal Workloads	2) Synthetic data generation	20%	20%	20%	27%	23%	22%	22%
3) Research experiments	4%	5%	6%	14%	21%	28%	35%
4) Research automation	1%	3%	4%	6%	6%	6%	6%
Total Internal	25%	28%	30%	47%	51%	57%	63%
→ Capabilities share	95%	96%	97%	97%	97%	97%	97%
→ Alignment share	5%	4%	3%	3%	3%	3%	3%
External Inference	5) External deployment	33%	30%	28%	20%	19%	18%	13%
Other	6) Monitoring	2%	2%	2%	3%	3%	3%	4%
Total compute usage and costs

These rows are informed by our overall compute production and distribution projections to illustrate a typical leading AI company with a share of global compute usage growing from ~5% to ~20% from 2024 to 2027. In those sections we project the AI compute used by the leading AI company to grow 3.4x/year and computational price performance (FLOP/$) to improve roughly 1.4x/year. Read more on cost projections in the financials section.
Compute usage on training runs

In 2024 we estimate that OpenAI used an average of 40% of their compute on training. We expect most (around 60%) of this to be on trying to scale to next-generation pre-training runs, and the rest (around 40%) to be on reinforcement learning based post-training, with a focus on reasoning and agency. This is consistent with them doing a single pre-training run of about 3e26 fp16 FLOP of training, which corresponds to 100k H100s being used for 4 months, matching their historical scaling trend, and an average of 100k H100s being used on RL workloads for 2.5 months. OpenAI seems to have relatively centralized access to a single cluster of about 100k H100s, and given that they are sourcing their compute from at least three providers in Coreweave, Oracle and Microsoft, it is unlikely that chips are centralized and well connected enough between different datacenters to enable a larger training run than this. Furthermore, they have large compute requirements in internal and external deployment that more reasonably account for the rest of the total.

Going forwards we expect:

    Usage on training to fluctuate around 40% over the next two years.

    Increasingly large shares of training compute are dedicated to post-training.

    In 2027, there are no large pre-training runs and training compute is directed to almost purely post-training workloads of the large model trained in 2026.

Synthetic Data Generation

In 2024, we expect roughly 20% of OpenAI’s compute to be used on generating synthetic data, the main use case probably being on eliciting the reported ‘Orion’ model as well as weaker base models with inference time techniques (e.g., tree search based) and using grading and filtering (e.g., rejection sampling) to then produce data that is used for post-training models like o1 and the recently announced o3. This is an average of 50k H100s used throughout the year or 2.5e26 fp16 FLOP. An example of how this could be used is for 5T forward passes on Orion (assuming it is a 2T parameter dense-equivalent model served at fp8 precision), and 500T forward passes on GPT-4o. We’d guess the Orion forward passes are not filtered and are directly used as 5T tokens of high-quality training data, while the GPT-4o forward passes are roughly 16:1 in producing a high quality token (after search and grading) for another 30T tokens. This results in 35T total tokens generated, perhaps for post-training o1 and o3, which would allow for ~1e26 FLOP of GPT-4o post-training. We expect synthetic data generation to become increasingly important in tandem with post-training workloads, staying at around 20% and then growing to ~30% in 2027.
Research experiments

We expect research experiments to have been a significant priority in 2024, with an average of 10k H100s being used on average throughout 2024. This corresponds to about 1e26 fp16 FLOP in total, which is sizable and will have allowed a range of small and large training and architectural experiments. As the emphasis shifts from training runs and external deployment to AI R&D automation, particularly in 2027, we expect this to grow steadily as the growing algorithmic research effort requires an increased share of the experiment budget. With research labour becoming increasingly automated, experimentation compute will become an increasingly important bottleneck to progress, which is why project usage will spike from 4% in 2024 to 15% in early 2027 and 35% in late 2027. This would correspond to more than 2e28 fp16 FLOP of experiment compute in 2027.
Research automation

We expect internal research automation to have been minimal in 2024, limited to employee early access use of models like o1 and o3 to help with research tasks. An average of 1k H100s, or 2e25 fp8 FLOP would be enough for 250B forward passes on Orion (using our best guess of it being 2T parameter dense-equivalent) or models like o1 or o3 which may have similar inference costs. As a sanity check, assuming 1000 employees, this amounts to 250M tokens per employee, or approximately 800k tokens per day. At 8:1 chain-of-thought ratios and 100 tokens/sec throughput, this represents about 1000 seconds or 16 minutes of generation time per employee per day, which seems like a reasonable average. Going forwards, as internal models become more capable, we expect them to scale this significantly, both in the number of copies of the model they run per employee, and in the scaffolding regimes (and therefore inference-time compute multiples) they typically deploy them at. This spikes particularly in 2027 with the push to automate their R&D workflows using expensive models from 1% today to around 6%, but doesn’t go higher given the abundance of research labour and lack of experiment compute this would cause.
Compute usage on external deployment

We expect OpenAI to be using roughly 30% of their compute on external deployment through 2024 which is an average of 75k H100s throughout the year. If they achieve an average of 10% inference utilization (across output and input tokens) on severed models (where it is expected to be difficult to batch requests) this corresponds to about 800T GPT-4o forward passes, or ~2T tokens per day.

This seems roughly right given that in February 2024, Sam Altman tweeted that OpenAI was generating 100 billion words per day. Assuming this roughly tripled by the middle of the year (slightly outpacing revenue with margins tightening slightly) to 400B tokens and roughly quadrupled with the release of o1-preview, o1, and o1-pro which use a disproportionate amount of inference compute to 1.6T tokens, assuming a 1:1 average input:output tokens ratio (given document and other inputs), this puts us at an average of roughly 1T tokens each per day throughout the year, for 2T total.

Going forwards we expect:

    The share should stay roughly the same through 2025 and then start to decrease as internal priorities grow and the release of frontier models in 2027 are delayed due the capabilities enabling significant productivity boosts on internal AI R&D efforts.

    Throughout the next three years, we expect revenue shares to shift increasingly towards corporate customers, as the business model shifts from being dominated by the ‘online chatbot’ to a ‘drop-in remote worker service’.

    Note that even a decreased share will still be a very large absolute jump, from 75k H100s in 2024 to 2M in 2027, which is roughly proportional to the increase in revenue we expect.

Compute usage on monitoring

As a very rough heuristic, we expect a model with an average inference cost around 10x lower than the average inference-cost of deployed models to be checking roughly half of all input/output tokens in various settings (either monitoring external deployment or, in later years, in potentially broader AI control setups, including for research automation). Therefore we add the external deployment and research assistant shares and divide by 20 to get our estimate for the share of compute on monitoring, and see that it stays roughly constant throughout at around 2-4%.
Section 4. AI research automation

Status: Uncertain but informed. This section is an informed forecast based on public information.
Research Automation Deployment Tradeoff
Mar 2027Jun 2027Sep 2027Speed (tokens/sec)Parallel Copies101001.00010.00010K100K1M10M200K copies30x Humanspeed300K copies50x Humanspeed
Human thinking speed10 words/sec10x Humanthinking speed100x Humanthinking speed
ai-2027.com

Figure 18: Summary of the AI research agent deployment tradeoff we expect OpenBrain to face using 6% of their H100e compute, as forecasted in the research automation compute usage section.

This subsection contains an analysis on the inference tradeoff between speed and parallel copies when serving an AI model, focusing on concrete AI models that we think might be used for AI research automation in AI 2027. In inference workloads, total aggregate memory bandwidth is the most direct measure of performance because decoding tokens sequentially requires maintaining a growing KV cache in fast memory and loading it, along with model weights, into processors for each token generated. Therefore, in this section we work in H100-bandwidth-equivalents (H100-Be), so units of 3.6TB/s of total aggregate bandwidth (anchored to halfway between the H100 NVL and H100 SXM assuming these were produced roughly evenly).
Existing Hardware Roadmaps
Nvidia GPUs
	GPU bandwidth	H100-Be	Memory capacity	Memory generation	Peak usage	Cost of ownership
NVIDIA H100	~3.6 TB/s	1	90 GB	HBM3	2023-2024	$40k
NVIDIA H200	4.8 TB/s	1.3	141 GB	HBM3e	2024-2025	$40k
NVIDIA B200	8 TB/s	2.2	192 GB	8x8Hi HBM3e	2025-2026	$50k
NVIDIA R200 Ultra	19.2 TB/s	5.3	768 GB	12x16Hi HBM4	2027	$100k
NVIDIA R300 Ultra	25.6TB/s	7.1	1TB	16x16-Hi HBM4	2027-2028	$120k
Wafer Scale Inference chips
	GPU bandwidth	H100-Be	Memory capacity	Memory type	Peak usage	Cost of ownership
Cerebras WSE-3	21,000 TB/s	5800	44 GB	SRAM	2025-2026	$2-3M
WSE-2027	34,000 TB/s	9500	72 GB	SRAM	2027-2028	$3-4M
2027 In-House Inference Chip

This table contains a forecast on the typical inference chip in 2027 (2027-IC) that will be available to the leading AI company. As described in the hardware R&D automation subsection, we expect leading AI companies in 2027 to automate specialized chip designs and increase in-house chip production in 2027. There are early signs of such ambitions, such as OpenAI’s hiring of prolific Google TPU designers and plans to design their first in-house chip in 2025.
	TSMC process	Die size	H100e	GPU bandwidth	H100-Be	Memory capacity	Memory generation	Cost of ownership
2027 -IC	3nm	60xH100	100	720 TB/s	200	17.8 TB	HBM4e	$600k
Scaled to performance
Scaled to die size
H100
(7.2 TB/s)
2027-IC
(720 TB/s)
2023
2027
*Expected
ai-2027.com
	Q1 2027	Q2 2027	Q3 2027	Q4 2027 (racing)
Compute used on research automation	Research automation share	6%	6%	6%	6%
Compute budget for research automation (H100e)	400K	600K	800K	1M
Bandwidth budget for research automation (2027-ICs)	4K	6K	8K	10K
Bandwidth budget for research automation (H100-Be)	800K	1.2M	1.6M	2M
Breakdown
Deployment tradeoffs	Copies deployed (instances x average batch size)	300K	400K	500K	600K
Avg. raw speed (forward passes / second)	230	290	360	430
Model size (parameters, fp8, dense-equivalent, average across deployed models)	10T	10T	5T	2T
AI R&D progress
Effect on AI R&D Progress (average during period)	Research Capability Level Milestone	Superhuman Coder	Superhuman Coder	Superhuman AI Researcher	Artificial Superintelligence
AI R&D Progress Multiplier	4x	10x	50x	2000x
Frontier Model Size and Architecture

In early 2027, we expect frontier training runs to have reached around 2e28 FLOP (4e28 FLOP at fp8 precision) based on the compute usage estimates. Based on the ratio to GPT-4 ~1000x, we naively predict that such an AI model would have roughly 10T active parameters. Given the degree of AI research automation predicted by AI 2027, we expect significant distillation effects to reproduce the same level of capabilities in much smaller more efficient models. Our expectation is that AI companies will deploy a whole range of both smaller models, and new checkpoints of their largest model which they are continuously post-training to higher capabilities. Nonetheless, we perform our speed and copies calculations in units of a fixed 10T parameter dense-equivalent model for simplicity, and assume that mixture of experts or other future architectures can be converted into ‘dense-equivalent’ parameters based on their inference economics. We then adjust speed/copies calculations in future periods according to the decreasing model size. Notably, we expect the most intelligent model to fall from around 10T dense-equivalent parameters to 2T parameters by the end of 2027, even as the qualitative ability of the model increases from a median human researcher to a vastly superintelligent researcher, due to algorithmic efficiency exploding and nearing the limits of intelligence.
Compute and memory available

According to our compute distribution projection the leading AI company in 2027 will have 15-20% of the world’s compute and according to our internal usage projection they will use 6% of this on running AIs for research automation, giving them around 4K 2027 In-House Inference Chips (2027-ICs) in bandwidth budget for Q1 2027, and 10K 2027-ICs by Q4 2027. We perform calculations in terms of 1K 2027 In-House Inference Chips (1k 2027-ICs) equivalent to 100K H100s in compute and 200K H100s in bandwidth and then use to back out Q1 to Q4 deployment tradeoff curves.
Trading off parallel copies and speed

When running inference you can trade off running more parallel copies with slower speed and vice versa, where the trade-off is limited by memory bottlenecks (when scaling up copies) and latency bottlenecks (when scaling down copies, maximizing speed). In other words, if you scale up parallel copies beyond what fits in the HBM total memory of your GPU server, or group of well connected GPU servers, you would start to see significant slowdowns from having to use slower memory bandwidth connections, while if you scale down too aggressively, by reducing the batch size, and/or by increasing tensor/model parallelism (which means spreading the model across more GPUs), each request needs to travel across more chips in a cluster, leading to communication bottlenecks.
Scaling up parallel copies

Assuming inference is run at fp4 precision, 10T parameters would require 5TB of memory. On one of the 2027-IC chips, this would leave 12.8TB of HBM free, of which we might assume 1.8TB is reserved for miscellaneous purposes, and 11TB is left for the KV cache. Assuming an average sequence length of 20k tokens, a hidden dimension of 50k, and 250 total layers, this could support a maximum batch size of 440. So with 1000 instances (1 per 2027-IC chip) this would correspond to 440K parallel copies. Each batch would require 16TB/tok of bandwidth, so the inference speed would be 45 tokens/second.
Scaling down parallel copies

In theory you could scale down to just 1 model instance across all 1000 servers, but this would suffer majorly from communication bottlenecks. More reasonably, we might assume that you would have a model instance spread over 10 2027-IC chips and have a batch size of just 10. This would leave you with just 1,000 parallel copies. Each batch would require 5.3 TB/tok of bandwidth, so the inference speed would be 1,350 tokens/second, assuming sufficient interconnect between the 10 chips for there to be no inter-chip communication bottleneck.
Projected Deployment Tradeoff

Putting together these two ‘scale up parallel copies’ and ‘scale down parallel copies’ extremes, we can compute a range of deployment choices in between to get average deployment tradeoff curves for each time period as shown in Figure 16. These curves were not computed with full consideration of possible current or future parallelism techniques and chip-to-chip communication bottlenecks, though we are relatively confident that these would be unlikely to affect the curves significantly.
Research Automation Deployment Tradeoff
Mar 2027Jun 2027Sep 2027Speed (tokens/sec)Parallel Copies101001.00010.00010K100K1M10M200K copies30x Humanspeed300K copies50x Humanspeed
Human thinking speed10 words/sec10x Humanthinking speed100x Humanthinking speed
ai-2027.com

Figure 19: AI research agent deployment tradeoff we expect OpenBrain to face using 6% of their H100e compute, as forecasted in the research automation compute usage section.

We naively speculate that through 2027 there will be a roughly even preference for high parallel copies and high speed with the deployment tradeoff averaging to around 300K average copies and an average speed around 20x human thinking speed. Out of the scope of this piece, we expect the preference to shift slightly towards serial workloads in 2028 as there are increasingly diminishing returns to more copies of the model towards the limits of intelligence, and new hardware inventions from mid-late 2027 have time to be manufactured and widely in-use.
	Q1 2027	Q2 2027	Q3 2027	Q4 2027
Parallel copies	300K	400K	500K	600K
Speed	230 tok/sec	290 tok/sec	360 tok/sec	430 tok/s
parameters	10T	10T	5T	2T
Section 5. Industry Metrics

Status: Uncertain but informed. This section is an informed forecast based on public information.

This section presents a projection of leading AI company frontier training runs through 2028, and discusses the associated projections in costs, revenues, and power requirements.
Training runs
Training RunsTraining Compute in Fp16 FLOP (log scale)
GPT-4 (2e25)GPT-4.5 (2e26)1000xGPT-4 (2e28)Dec 2024Jun 2025Dec 2025Jun 2026Dec 2026Jun 2027Dec 202710^2510^2610^2710^28
Agent-1Agent-0Agent-2Agent-3Agent-4
ai-2027.com

Figure 20: The training runs in AI 2027.

Our compute production forecast has the global AI-relevant compute growing at 2.25x per year between 2024 and 2027. With the leading AI company’s share of the global stock growing 1.4x per year, and their internal usage on training runs staying at 40% until 2027 when it drops to 20%. Putting this all together we project the following training runs.
Model	Training period	Global compute during training period (H100e)	Share of global compute	Share of internal usage	Training compute
Agent-0	Oct 2024 - May 2025	10M	6%	40%	1e27
Agent-1	Jul 2025 - Feb 2026	18M	9%	40%	4e27
Agent-2	Apr 2026 - Mar 2027	38M	14%	36%	2e28
Agent-3	Mar 2027 - Aug 2027	60M	16%	24%	+1e28^
Agent-4	Aug 2027 - Dec 2027	80M	18%	20%	+1e28^^
Chips in use

Using our compute production and compute distribution sections, we illustrate what we expect to be the chips to be in use by the leading AI company through 2027. We expect the bulk to be Nvidia chips along with in-house inference chips emerging in 2027.
GPU Deployment by Chip Type
Jan 2025Jul 2025Jan 2026Jul 2026Jan 2027Jul 2027Jan 2028H100 Equivalents (H100e)2.0M4.0M6.0M8.0M10.0M12.0M14.0M16.0M18.0M20.0MH100sGB200sGB300sVR200s
Inference chips
ai-2027.com

Figure 21: Chips in use by the leading AI company through December 2027.
Financials

In this subsection we project the leading AI company’s costs and revenues through 2027. We anchor on OpenAI to understand the pre-2025 trend and then use our other projections to extrapolate forwards.
Leading AI Company Revenue & Cost ProjectionsValue (USD)
Jan 2025Jul 2025Jan 2026Jul 2026Jan 2027Jul 2027Jan 20280$50B$100B$150B$200BAnnualized RevenueAnnualized Compute CostsAnnual2024$4B$6BAnnual2025$14B$20BAnnual2026$50B$50B
Annual2027$150B$120B
ai-2027.com

Figure 22: Approximate cost and revenue projections for OpenBrain, the leading AI company.
Compute cost projection

The New York Times reported that OpenAI anticipates $5.4B in computing costs in 2024, and GPT-4 which was trained in mid 2022 over 3 months, is estimated to have cost around $100M to train. Assuming GPT-4 training was 20-40% of their compute spending that year, that means they saw a roughly 11-22x/year increase in their compute spending from 2022 to 2024.

Meanwhile, computational price performance (FLOP/$) doubled from the A100 to H100 in 16 months, which we expect to have been a slight outlier to a trend closer to around 1.4x/year on frontier AI chips. Going forwards, we can take our 3.4x/year projection for a leading AI company’s compute and adjust down by 1.5x improvement in FLOP/$ to get an average 2.4x/year projection in spending on AI compute by the Leading AI Company. Though we expect this growth to be faster in the first year or two and then slow due to increasing competitiveness of in-house chip designs.
Revenue projection

We use OpenAI’s 2023 revenue of $1B and 2024 revenue around $4B to to piece together a short term trend that we expect to slow down gradually, but see sustained exponential growth through 2027 due to agentic models attracting high paying subscribers for products such as ‘drop in remote workers.’
	2023	2024	2025	2026	2027
Annual Revenue	$1B	$4B	$14B	$45B	$140B
Revenue Y/Y Growth	-	300%	250%	221%	211%
Annual Compute Cost	$1.8B	$6B	$16B	$40B	$100B
Compute Cost Y/Y Growth	-	233%	166%	150%	150%

FutureSearch projected how OpenBrain’s revenue might grow to reach $100B in mid-2027. They looked at the overall speed of the fastest companies to scale from $1B to $100B and found that the time to make that transition has been decreasing over time. A leading company making the jump in only 4 years would be the fastest ever, but also is on trend. They also examined the types of Agents that might be in highest demand - from consumer service representatives to R&D researchers - along with their price points, to produce a detailed sketch of where OpenBrain’s revenue most likely would come from. For more see FutureSearch's full report.
Power requirements

Finally, we model the power requirements for the compute used by the leading AI company through 2028 based on reported and projected power efficiency of the key Nvidia chips we expect to be in use. Using this we can back out the total power required by the leading AI company as well as the implied total AI datacenter power used globally (assuming the leading AI company has an average power usage efficiency ratio).
	Performance (fp16, FLOP/s)	Peak usage	Datacenter peak power usage	Energy efficiency
NVIDIA H100/200 GPU	1 x 1015	2023-2024	1000W	1.0
NVIDIA B100/200 GPU	2.5 x 1015	2025-2026	1700W	1.47
NVIDIA R100/200 GPU	6 x 1015	2027-2028	~3300W	1.81
Global, US, and Leading Company AI PowerPower Capacity Requirement
Jan 2025Jul 2025Jan 2026Jul 2026Jan 2027Jul 2027Jan 2028010 GW20 GW30 GW40 GW50 GW60 GW0.5%1.5%2.5%3.5%Global AI powerUS AI powerLeading US AI CompanyShare of US Power on AIDec 202410 GW7 GW0.5 GW
Dec 202760 GW50 GW10 GW
ai-2027.com

Figure 23: Power requirement projections through December 2027.