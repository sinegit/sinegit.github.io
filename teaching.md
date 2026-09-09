---
title: Teaching
permalink: /teaching/
# layout: default
---

<style>
.tp{font-family:"Open Sans","Helvetica Neue",Helvetica,sans-serif}
.tp .lede{font-size:.92rem;line-height:1.65;color:#444;margin:0 0 2.2rem}
.course{border:1px solid #e6e6e6;border-top:4px solid #AA162C;border-radius:6px;
        padding:1.3rem 1.4rem 1.1rem;margin:0 0 1.6rem;background:#fff}
.course h3{margin:0 0 .15rem;font-size:1.12rem;color:#222;letter-spacing:-.01rem}
.course .sub{color:#AA162C;font-weight:600;font-size:.8rem;margin:0 0 .7rem}
.course p{font-size:.84rem;line-height:1.62;color:#454545;margin:0 0 .9rem}
.meta{font-size:.75rem;color:#777;border-top:1px solid #f0f0f0;padding-top:.7rem;margin-top:.2rem}
.meta a{color:#AA162C;font-weight:600;text-decoration:none}
.meta a:hover{text-decoration:underline}
.tp details{margin:.9rem 0 0;border-top:1px solid #f0f0f0;padding-top:.6rem}
.tp summary{cursor:pointer;font-size:.78rem;font-weight:600;color:#AA162C;list-style:none;
            text-transform:uppercase;letter-spacing:.04em}
.tp summary::-webkit-details-marker{display:none}
.tp summary::before{content:"▸ ";font-size:.8rem}
.tp details[open] summary::before{content:"▾ "}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:.9rem;margin:1rem 0 .4rem}
.deck{display:block;text-decoration:none;color:#333}
.deck img{width:100%;margin:0;border:1px solid #e2e2e2;border-radius:4px;display:block;
          transition:transform .16s ease, box-shadow .16s ease, border-color .16s ease}
.deck:hover img{transform:translateY(-3px);box-shadow:0 6px 16px rgba(0,0,0,.14);border-color:#AA162C}
.deck .cap{display:block;font-size:.66rem;line-height:1.35;margin-top:.35rem;color:#555}
.deck:hover .cap{color:#AA162C}
.sidecard{display:flex;gap:1.15rem;align-items:flex-start}
.sideshot{width:210px;flex:0 0 210px;margin:.15rem 0 0;border:1px solid #e2e2e2;border-radius:4px;display:block}
.sidebody{flex:1 1 auto;min-width:0}
.sidebody h3{margin-top:0}
@media (max-width:34em){.sidecard{flex-direction:column}.sideshot{width:100%;flex:none}}
.plaincard h3{margin-top:0}
.toons{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:1rem;margin:1rem 0 .3rem;align-items:end}
.toons a{display:block;text-decoration:none;color:#555}
.toons img{width:100%;margin:0;border:1px solid #e2e2e2;border-radius:4px;display:block;
           transition:transform .16s ease,box-shadow .16s ease,border-color .16s ease}
.toons a:hover img{transform:translateY(-3px);box-shadow:0 6px 16px rgba(0,0,0,.14);border-color:#AA162C}
.toons .cap{display:block;font-size:.66rem;margin-top:.35rem;line-height:1.35}
.toons a:hover .cap{color:#AA162C}
.past{font-size:.76rem;line-height:1.65;color:#666}
.past b{color:#222}
.talk{padding-top:0;overflow:hidden}
.hasbanner{padding-top:0;overflow:hidden}
.banner{width:calc(100% + 2.8rem);margin:0 -1.4rem 1.15rem;display:block;border:0;border-radius:0;
        cursor:zoom-in;transition:transform .3s ease}
.hasbanner:hover .banner{transform:scale(1.015)}
.talkshot{width:calc(100% + 2.8rem);margin:0 -1.4rem 1.1rem;display:block;border:0;border-radius:0;
          transition:transform .3s ease}
.talk:hover .talkshot{transform:scale(1.02)}
@media (max-width:40em){.grid{grid-template-columns:repeat(auto-fill,minmax(112px,1fr))}}
</style>

<div class="tp" markdown="0">

<p class="lede">Anna has taught probability and stochastic processes, signals and systems, and communication theory at the
undergraduate and graduate level, and has introduced graduate courses in machine learning and in modern power system
operations — demand response, renewable integration and cyber-physical security. Class sizes have ranged up to 280
students.</p>

<h2>Currently teaching at Cornell Tech</h2>

<div class="course hasbanner">
  <img class="banner" src="/images/teaching/ece5260-banner.jpg"
       alt="A clustered network of nodes and edges with one highlighted hub, beside a sparse adjacency matrix"
       loading="lazy" data-action="zoom">
  <h3>Graph-Based Data Science for Networked Systems</h3>
  <div class="sub">ECE 5260 / ORIE 5735</div>
  <p>The mathematics of networks and the data science built on it: graph algebra, incidence and Laplacian matrices,
  partitioning and centrality, random graph models, and dynamics on networks — consensus, epidemics and flows — through to
  modern graph learning: graph signal processing, graph convolutional networks, graph transformers and graphical models,
  applied to social, biological, financial and infrastructure networks.</p>
  <div class="meta">Offered Spring 2022, Fall 2022, Spring 2024, Spring 2025, Spring 2026 &nbsp;·&nbsp; <a href="/assets/teaching/ece5260/ece5260-syllabus.pdf">Syllabus (PDF)</a></div>
  <details open>
    <summary>Lecture slides — Spring 2026 (25 decks)</summary>
    <div class="grid">
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec00.pdf">
    <img src="/images/teaching/ece5260-lec00.jpg" alt="Notes — Notation and hints" loading="lazy">
    <span class="cap"><b>Notes</b></span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec01.pdf">
    <img src="/images/teaching/ece5260-lec01.jpg" alt="Lecture 1 — Introduction" loading="lazy">
    <span class="cap"><b>Lecture 1</b>&nbsp;· Introduction</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec02.pdf">
    <img src="/images/teaching/ece5260-lec02.jpg" alt="Lecture 2 — Graph topologies and characteristics" loading="lazy">
    <span class="cap"><b>Lecture 2</b>&nbsp;· Graph topologies and characteristics</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec03.pdf">
    <img src="/images/teaching/ece5260-lec03.jpg" alt="Lecture 3 — The algebra of network graphs" loading="lazy">
    <span class="cap"><b>Lecture 3</b>&nbsp;· The algebra of network graphs</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec04.pdf">
    <img src="/images/teaching/ece5260-lec04.jpg" alt="Lecture 4 — The incidence matrix" loading="lazy">
    <span class="cap"><b>Lecture 4</b>&nbsp;· The incidence matrix</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec05.pdf">
    <img src="/images/teaching/ece5260-lec05.jpg" alt="Lecture 5 — The Laplacian Matrix" loading="lazy">
    <span class="cap"><b>Lecture 5</b>&nbsp;· The Laplacian Matrix</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec06.pdf">
    <img src="/images/teaching/ece5260-lec06.jpg" alt="Lecture 6 — Graph Partion - centrality" loading="lazy">
    <span class="cap"><b>Lecture 6</b>&nbsp;· Graph Partion - centrality</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec07.pdf">
    <img src="/images/teaching/ece5260-lec07.jpg" alt="Lecture 7 — Centrality - node features" loading="lazy">
    <span class="cap"><b>Lecture 7</b>&nbsp;· Centrality - node features</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec08.pdf">
    <img src="/images/teaching/ece5260-lec08.jpg" alt="Lecture 8 — More features - random graphs" loading="lazy">
    <span class="cap"><b>Lecture 8</b>&nbsp;· More features - random graphs</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec09.pdf">
    <img src="/images/teaching/ece5260-lec09.jpg" alt="Lecture 9 — Random Graph Models and Real Networks" loading="lazy">
    <span class="cap"><b>Lecture 9</b>&nbsp;· Random Graph Models and Real Networks</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec10.pdf">
    <img src="/images/teaching/ece5260-lec10.jpg" alt="Lecture 10 — Random Graph models and real networks" loading="lazy">
    <span class="cap"><b>Lecture 10</b>&nbsp;· Random Graph models and real networks</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec11.pdf">
    <img src="/images/teaching/ece5260-lec11.jpg" alt="Lecture 11 — Random walk consensus" loading="lazy">
    <span class="cap"><b>Lecture 11</b>&nbsp;· Random walk consensus</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec12.pdf">
    <img src="/images/teaching/ece5260-lec12.jpg" alt="Lecture 12 — Epidemic" loading="lazy">
    <span class="cap"><b>Lecture 12</b>&nbsp;· Epidemic</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec13.pdf">
    <img src="/images/teaching/ece5260-lec13.jpg" alt="Lecture 13 — General dynamics -flow networks" loading="lazy">
    <span class="cap"><b>Lecture 13</b>&nbsp;· General dynamics -flow networks</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec14.pdf">
    <img src="/images/teaching/ece5260-lec14.jpg" alt="Lecture 14 — _social-new" loading="lazy">
    <span class="cap"><b>Lecture 14</b>&nbsp;· _social-new</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec15.pdf">
    <img src="/images/teaching/ece5260-lec15.jpg" alt="Lecture 15 — Biological" loading="lazy">
    <span class="cap"><b>Lecture 15</b>&nbsp;· Biological</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec16.pdf">
    <img src="/images/teaching/ece5260-lec16.jpg" alt="Lecture 16 — _financial_collaboration" loading="lazy">
    <span class="cap"><b>Lecture 16</b>&nbsp;· _financial_collaboration</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec17.pdf">
    <img src="/images/teaching/ece5260-lec17.jpg" alt="Lecture 17 — _infrastutures" loading="lazy">
    <span class="cap"><b>Lecture 17</b>&nbsp;· _infrastutures</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec18.pdf">
    <img src="/images/teaching/ece5260-lec18.jpg" alt="Lecture 18 — _NetworkEmbedding-Shallow" loading="lazy">
    <span class="cap"><b>Lecture 18</b>&nbsp;· _NetworkEmbedding-Shallow</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec19.pdf">
    <img src="/images/teaching/ece5260-lec19.jpg" alt="Lecture 19 — _GSPintroduction" loading="lazy">
    <span class="cap"><b>Lecture 19</b>&nbsp;· _GSPintroduction</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec20.pdf">
    <img src="/images/teaching/ece5260-lec20.jpg" alt="Lecture 20 — _algGSP-Shallow-methods" loading="lazy">
    <span class="cap"><b>Lecture 20</b>&nbsp;· _algGSP-Shallow-methods</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec21.pdf">
    <img src="/images/teaching/ece5260-lec21.jpg" alt="Lecture 21 — _ChebyshevGCN" loading="lazy">
    <span class="cap"><b>Lecture 21</b>&nbsp;· _ChebyshevGCN</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec22.pdf">
    <img src="/images/teaching/ece5260-lec22.jpg" alt="Lecture 22 — _GNNApplications" loading="lazy">
    <span class="cap"><b>Lecture 22</b>&nbsp;· _GNNApplications</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec23.pdf">
    <img src="/images/teaching/ece5260-lec23.jpg" alt="Lecture 23 — _Graph_Transformers" loading="lazy">
    <span class="cap"><b>Lecture 23</b>&nbsp;· _Graph_Transformers</span>
  </a>
  <a class="deck" href="/assets/teaching/ece5260/ece5260-lec24.pdf">
    <img src="/images/teaching/ece5260-lec24.jpg" alt="Lecture 24 — _Graphical Models" loading="lazy">
    <span class="cap"><b>Lecture 24</b>&nbsp;· _Graphical Models</span>
  </a>
    </div>
  </details>
</div>

<div class="course hasbanner">
  <img class="banner" src="/images/teaching/ece5235-banner.jpg"
       alt="Isometric schematic of a power delivery system: generation, transmission, solar, wind, storage and a city"
       loading="lazy" data-action="zoom">
  <h3>Sustainable Urban and Energy Delivery Systems</h3>
  <div class="sub">ECE 5235</div>
  <p>The operation of the electric power system, from physics and system theory through to markets: power flow and
  optimal power flow, state estimation, three-phase distribution network modeling, energy markets and locational marginal
  pricing, flexible demand and demand response, forecasting, and machine learning for grid inference.</p>
  <div class="meta">Offered 2023, 2024, 2025 &nbsp;·&nbsp; <a href="/assets/teaching/ece5235/ece5235-syllabus.pdf">Syllabus (PDF)</a></div>
</div>

<h2>Beyond the classroom</h2>

<div class="course talk">
  <a href="/assets/teaching/talks/pint-of-science-2026.pdf">
    <img class="talkshot" src="/images/teaching/pint-of-science.jpg"
         alt="The World's Most Important Machine Has Trust and Decision Issues — Pint of Science 2026" loading="lazy">
  </a>
  <h3>The World&#39;s Most Important Machine Has Trust and Decision Issues</h3>
  <div class="sub">Pint of Science &nbsp;·&nbsp; New York City, May 2026</div>
  <p>A public talk at the Pint of Science festival on the electric grid: why keeping it running is a problem of trust,
  and of decisions taken continuously across a continent. Anna&#39;s own summary of it &mdash;
  <i>&ldquo;a 3,000-mile-wide panic attack keeping your lights on.&rdquo;</i></p>
  <div class="meta"><a href="/assets/teaching/talks/pint-of-science-2026.pdf">Slides (PDF, 27 pages)</a></div>
</div>

<div class="course sidecard">
  <a href="https://www.youtube.com/playlist?list=PLfMzjeGTdcav8saj5RIySjRByViHuxFdI">
    <img class="sideshot" src="/images/teaching/small-bits.jpg"
         alt="Cartoon characters A and B from the Information in Small Bits animations" loading="lazy">
  </a>
  <div class="sidebody">
    <h3>Information in Small Bits</h3>
    <div class="sub">Information theory for kids &nbsp;·&nbsp; IEEE Information Theory Society</div>
    <p>A book that explains information theory through story and pictures. It began as a joke: Anna drew each story as an
    8&times;11 pencil sketch and sent the cartoons to Christina Fragouli, who was serving on the committee choosing
    narratives to celebrate the Claude Shannon centennial &mdash; an effort aimed at teenagers. Christina thought the
    cartoons had value, and wrote the educational explanations that accompany the drawings. The IEEE Information Theory
    Society published the result as a non-profit outreach project.</p>
    <p>The mathematics under the drawings is exact, and the jokes reward a reader who already knows it: when B steps onto
    the scale, the weight it reads is the information carried by the letter B in the English alphabet. Catching that takes
    a fairly mature reader &mdash; the pictures never give it away.</p>
    <div class="meta">
      <a href="https://www.amazon.com/dp/B07HD64KW4">The book</a> &nbsp;·&nbsp;
      <a href="https://www.youtube.com/playlist?list=PLfMzjeGTdcav8saj5RIySjRByViHuxFdI">Animated video series</a>
    </div>
  </div>
</div>

<div class="course plaincard">
  <h3>WeCREATE Inspiration Session</h3>
  <div class="sub">van der Schaar Lab &nbsp;·&nbsp; 8 June 2022</div>
  <p>One of three speakers at the first WeCREATE Inspiration Session, presenting alongside Cheng Zhang (Microsoft
  Research) and Setareh Maghsudi (University of T&uuml;bingen), hosted by Mihaela van der Schaar. WeCREATE is a
  van der Schaar Lab initiative that encourages women students and early-career researchers towards machine learning
  and AI.</p>
  <div class="meta"><a href="https://www.vanderschaar-lab.com/wecreate-inspiration-session-1/">Session page</a></div>
</div>

<div class="course plaincard">
  <h3>Cartoons for <i>IEEE Signal Processing Magazine</i></h3>
  <div class="sub">Humor column &nbsp;·&nbsp; 2018</div>
  <p>Three strips drawn for the magazine&#39;s humor page, each a joke that only works if you know the mathematics:
  a feedback loop whose necklace improves her memory but leaves her looking unstable; two vectors breaking up because one
  wants to be linearly independent; and a tube of toothpaste promising
  <i>E[(Ux)(Ux)<sup>T</sup>] = I</i>, with PCA inside.</p>
  <div class="toons">
    <a href="/assets/teaching/cartoons/good-feedback-2018.pdf">
      <img src="/images/teaching/toon-good-feedback.jpg" alt="Good Feedback cartoon" loading="lazy">
      <span class="cap"><b>Good Feedback</b>&nbsp;· March 2018</span></a>
    <a href="/assets/teaching/cartoons/independence-2018.pdf">
      <img src="/images/teaching/toon-independence.jpg" alt="Independence cartoon" loading="lazy">
      <span class="cap"><b>Independence</b>&nbsp;· May 2018</span></a>
    <a href="/assets/teaching/cartoons/extreme-whitening-2018.pdf">
      <img src="/images/teaching/toon-extreme-whitening.jpg" alt="Extreme Whitening cartoon" loading="lazy">
      <span class="cap"><b>Extreme Whitening</b>&nbsp;· July 2018</span></a>
  </div>
  <div class="meta">With Raksha Ramakrishna on <i>Extreme Whitening</i>. Published in IEEE Signal Processing Magazine,
  vol. 35, 2018.</div>
</div>

<details>
  <summary>Previously taught</summary>
  <p class="past" style="margin-top:1rem">
  <b>Arizona State University</b> — EEE 598 Bayesian Methods in Machine Learning; EEE 598 Demand Response and Renewable
  Integration; EEE 455 Communication Systems; EEE 554 Random Signals; EEE 552 Digital Communications; EEE 350 Random
  Signal Analysis.<br><br>
  <b>University of California, Davis</b> — EEC 289 SmartGrid Networks; EEC 289 Mobile Communications; EEC 265 Digital
  Communications; EEC 260 Random Signals and Noise; EEC 161 Probability; ENG 06 Engineering Problem Solving.<br><br>
  <b>Cornell University, Ithaca</b> — ECE 567 Digital Communications; ECE 568 Mobile Communications; ECE 468
  Telecommunication Systems II; ECE 411 Random Signals in Communications and Signal Processing; ECE 220 Signals and
  Systems; ENGRG 150 Freshman Advising Seminar.<br><br>
  <b>University of New Mexico</b> — EE 595-091 Digital Communications; EE 595-011 Spread Spectrum Communications.<br><br>
  <b>University of Minnesota</b> — EE 3025 Statistical Methods in Electrical and Computer Engineering.
  </p>
</details>

</div>
