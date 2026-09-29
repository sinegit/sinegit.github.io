---
title: Research
permalink: /research/
---

### Research Areas

Directed by Anna Scaglione, the Signal, Information, Networks and Energy (SINE) laboratory (formerly the CRISP Lab) was established at Cornell University in 2001. It was hosted by Cornell University (2001-2008), the University of California, Davis (2008-2014) and Arizona State University (2014-2021), before moving back to Cornell at the Cornell Tech campus in New York City. The lab works at the intersection of signal processing, machine learning, network science and energy systems. Most of our current work is on learning and inference for the electric power grid, with methods meant to be adopted by utilities and grid operators.

<hr>

#### Graph learning and foundation models for the power grid

<img src="{{site.baseurl}}/images/research/grid-foundation-model.jpg" width="100%" data-action="zoom" style="margin:10px 0">

Power grid measurements are signals on a graph, and the graph changes: feeders get reconfigured, lines trip, new devices connect. We develop graph signal processing and graph learning methods whose models transfer across topologies without retraining, work from sparse measurements, and certify when their output can be trusted. This is the basis of [GridMind (MIND FM)](https://gridmind.ece.cornell.edu/), a grid foundation model for monitoring, control and market analytics, developed with Tong Wu, Andrew Campbell and collaborators at Lawrence Berkeley National Laboratory. Sponsored by DoE and NSF.

- [Graph Transfer Learning via Shared Latent Geometry: Theory and Applications](https://arxiv.org/abs/2606.00716) (Wu, Campbell, Scaglione)
- [Universal Graph Learning for Power System Reconfigurations: Transfer Across Topology Variations](https://arxiv.org/abs/2509.08672) (Wu, Scaglione, Miguel, Arnold)
- NSF ECCS: Advancing Graph Signal Processing Techniques for Monitoring and Control of Electric Distribution Power Systems

<img src="{{site.baseurl}}/images/research/grid-agent-cockpit.jpg" width="100%" data-action="zoom" style="margin:10px 0">

#### Differential privacy for grid data

Utilities are reluctant to share their data, which holds back machine learning for the grid. We work on releasing grid data with formal differential privacy guarantees: privatize the load data once, then release synthetic measurements and power flow solutions that can be used for any downstream task. This includes the theory of privacy for graph filters and network parameters, and practical release mechanisms for distribution grid voltage phasors. Andrew Campbell and Chenyue Zhang work on this. Sponsored by the DoE GENESIS program and led by Lawrence Berkeley National Laboratory (lead PI), in collaboration with Lawrence Livermore National Laboratory and Kevala.

<img src="{{site.baseurl}}/images/research/dp-data-gateway.jpg" alt="The DP data gateway: each utility trains a differentially private model on its own private load data, generates synthetic samples, runs power flow and releases private outputs under a privacy budget; the released data becomes a reusable DP-certified corpus of labeled voltage phasors that trains a grid foundation model, which in turn supports certified operational decisions with uncertainty quantified over the grid representation manifold" width="100%" data-action="zoom" style="margin:10px 0">

- [Differentially Private Synthetic Voltage Phasor Release for Distribution Grids](https://arxiv.org/abs/2605.02390)
- [Decentralized differentially private power method](https://arxiv.org/abs/2507.22849)
- Differential Privacy of Network Parameters From a System Identification Perspective (ICASSP 2026)

#### AI data centers as grid loads

AI data centers are the fastest-growing new load on the grid. We model the power demand of AI computing from the job level down to the UPS, batteries and cooling, its flexibility for demand response, and how cyber attacks on the computing side show up as power system disturbances.

<img src="{{site.baseurl}}/images/research/datacenter-layers.png" alt="The five-layer population model of an AI data center: sessions, job requests, queue management, GPU service, and the UPS, battery and AC plant, with the quantities each layer passes to the one below it down to the point of connection with the grid" data-action="zoom" style="display:block; margin:16px auto; width:100%; max-width:430px">

Our model is a *population model with layers*. Instead of tracking a million devices it tracks what fraction of them is in each state, which keeps the model linear, and it cuts the site into five layers &mdash; sessions, job requests, queue management, GPU service, and the UPS, battery and AC plant. Each layer has its own state, its own clock and its own controller, and only a few quantities cross between them; the last one is the power the grid sees at the point of connection. The boundaries are where the interesting behavior lives: lowering the per-GPU power cap barely moves the demand of inference work, training jobs released together turn a swing that should grow like the square root of the device count into one that grows linearly, and a site-wide fail-safe can move more power, faster, than anything an operator would choose to do. Nadav Harel works on this, with Prof. Udit Gupta (Cornell Tech). Sponsored by DoE, in collaboration with Lawrence Livermore National Laboratory (lead PI).

#### Cyber-physical security of distributed energy resources

Detection and mitigation of cyber attacks on grid-connected inverters and distributed energy resources, and privacy-preserving collective defense across utilities. Yating Zhou and Yanqing Tao work on this. Sponsored by DoE CESER, in collaboration with Lawrence Livermore National Laboratory (lead PI):

- Mitigation via Analytics for Grid-Inverter Cybersecurity (MAGIC)
- Privacy-Preserving, Collective Cyberattack Defense of DERs
- Earlier: [Provable Anonymization of Grid Data for Cyberattack Detection](https://dst.lbl.gov/security/project/ceds-privacy/), [SPADES](https://dst.lbl.gov/security/project/ceds-spades/)

#### Distributed and federated learning

Multi-agent optimization and learning over networks, including federated learning for graph neural networks, robustness to adversarial agents, and compressed and sparse models for decentralized learning. Sponsored by ARO and NSF.

#### Electric vehicles and microgrids

Coordination of vehicle-to-microgrid services and logistics for medium and heavy-duty electric vehicles (ONR), and demand response and renewable integration more broadly.

<hr>

### Past projects

- [Neptune 2.0: Situation Awareness and Smart Reconfiguration of Ad-hoc Military Electric Grids Using a Digital-twin](/projects/neptune2_0) (ONR)
- [Evaluation of the LwM2M Protocol and 5G Networks Performance for wide-area Industrial Internet of Things](/projects/xylem) (Xylem)
- [LayBack: Layered SDN-Based Backhaul Architecture and Optimization Framework for Small Cells and Beyond](https://faculty.engineering.asu.edu/mre/research/layback/) (NSF NeTS)
- Cyber Resilient Energy Delivery Consortium (CREDC) (DoE)
- Synthetic Data for Power Grid R&D (ARPA-E GRID DATA); Stochastic Optimal Power Flow for Real-Time Management of Distributed Renewable Generation and Demand Response (ARPA-E NODES)
