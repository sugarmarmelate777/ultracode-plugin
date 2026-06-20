#!/usr/bin/env python3
"""
Syndicate-30000 Semantic Vector Router.

Replaces in-context LLM computation of TF-IDF + cosine similarity.
LLMs hallucinate vector math --- real computation MUST be done by actual code.

Architecture:
- Parses 7 Micro_Domains_Batch_X.md files (770 domains across 75 sectors)
- Builds bilingual corpus: Russian domain names + Russian parenthetical clarifications
  + English sector keywords (from sector headers like "Pure Mathematics")
- Computes TF-IDF vectors with IDF-weighted cosine similarity
- Returns ranked JSON results

Usage:
    python syndicate_router.py "Galois group irreducible quartic polynomial"
    python syndicate_router.py --json "quantum resistant blockchain consensus"

Programmatic:
    from syndicate_router import route_query
    results = route_query("machine learning for medical diagnosis")
    # Returns: [{"sector_id": "...", "cosine_score": 0.87}, ...]
"""

import sys
import re
import json
import math
from pathlib import Path
from typing import Dict, List, Optional

# --- Configuration ---
BASE_DIR = Path(__file__).parent.parent  # c:/Projects
BATCH_DIR = BASE_DIR  # Micro_Domains_Batch_X.md files
BATCH_COUNT = 7

# Verify batch files exist — fall back to repo root if they are not under BATCH_DIR
_batch_check = BATCH_DIR / "Micro_Domains_Batch_1.md"
if not _batch_check.exists():
    _alt = Path(__file__).parent.parent.parent
    _alt_check = _alt / "Micro_Domains_Batch_1.md"
    if _alt_check.exists():
        BATCH_DIR = _alt

# Stop words (Russian + English)
STOP_WORDS = {
    # English
    'the', 'of', 'and', 'for', 'with', 'from', 'in', 'to', 'a', 'an', 'is', 'are',
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
    'will', 'would', 'could', 'should', 'may', 'might', 'can', 'shall', 'but', 'or',
    'not', 'no', 'if', 'then', 'else', 'when', 'where', 'which', 'who', 'whom',
    'this', 'that', 'these', 'those', 'it', 'its', 'on', 'at', 'by', 'as', 'so',
    'than', 'into', 'about', 'up', 'out', 'after', 'before', 'between', 'under',
    'over', 'again', 'further', 'once', 'here', 'there', 'all', 'both', 'each',
    'every', 'any', 'few', 'more', 'most', 'other', 'some', 'such', 'only',
    'own', 'same', 'new', 'just', 'also', 'now', 'well', 'back', 'still',
    'very', 'much', 'even', 'too', 'yet', 'already',
    # Russian
    'и', 'в', 'на', 'с', 'по', 'для', 'к', 'от', 'из', 'о', 'об', 'за', 'до',
    'при', 'под', 'над', 'между', 'через', 'или', 'не', 'да', 'но', 'а',
    'это', 'как', 'так', 'что', 'то', 'все', 'еще', 'уже', 'быть', 'был',
    'быть', 'была', 'было', 'были', 'есть', 'который', 'свой', 'весь',
    'один', 'два', 'три', 'мой', 'твой', 'наш', 'ваш', 'их', 'его', 'ее',
}

# English domain-level keyword enrichment per sector.
# Each entry contains the sector's English name + domain-specific query terms.
# When a user queries in English, these bridge to Russian domain names via TF-IDF overlap.
SECTOR_EN_MAP: Dict[int, str] = {
    # Keys = batch file sector IDs (1-75), NOT canonical SKILL.md numbering.
    # The two numberings diverge significantly from sector 3 onward.
    # See c:\Projects\compare_sectors.py for the full mapping.
    1: "pure mathematics algebra geometry topology number theory logic set theory "
       "category functor graph combinatorics analysis functional harmonic measure integration "
       "groups rings fields commutative algebraic geometry diophantine number theory "
       "galois group quartic polynomial extension ideal ring module field extension "
       "riemann manifold differential topology knot theory homology cohomology "
       "linear algebra multilinear vector space tensor matrix determinant eigenvalue "
       "complex analysis contour holomorphic meromorphic calculus theorem proof "
       "fourier series laplace transform pde ode dynamical system ergodic "
       "probability stochastic statistics bayesian regression hypothesis testing",
    2: "applied mathematics statistics probability optimization modeling simulation "
       "cryptography cryptanalysis quantum crypto coding theory information theory "
       "game theory decision analysis operations research linear programming "
       "differential equations numerical methods computational math finite element "
       "chaos theory bifurcation dynamical systems control theory signal processing",
    # Batch 3: Theoretical & Quantum Physics
    3: "theoretical physics quantum mechanics relativity particle field theory "
       "standard model higgs boson string theory gravitational dark matter energy "
       "quantum field theory qed qcd electroweak supersymmetry neutrino "
       "quantum information bell inequality EPR paradox wave function collapse "
       "quantum entanglement superposition decoherence Schrodinger Heisenberg "
       "classical mechanics lagrangian hamiltonian newton einstein planck",
    # Batch 4: Experimental & Applied Physics
    4: "experimental physics applied physics condensed matter solid state "
       "electromagnetism thermodynamics optics waves particle accelerator "
       "atomic molecular optical plasma spectroscopy laser semiconductor "
       "superconductor fluid mechanics acoustics nuclear reactor fusion fission "
       "instrumentation measurement detector sensor metrology calibration",
    # Batch 5: Chemistry
    5: "chemistry organic inorganic physical analytical polymer biochemistry "
       "chemical reaction synthesis spectroscopy chromatography crystallography "
       "molecular orbital valence bond periodic table element compound acid base "
       "quantum chemistry computational electrochemistry thermodynamics kinetics "
       "catalysis reagent solvent titration distillation extraction filtration",
    # Batch 6: Biology — Cellular, Molecular & Genetics
    6: "molecular biology cell biology genetics genomics DNA RNA protein genome "
       "crispr transcription translation replication gene expression epigenetics "
       "microbiology bacteriology virology immunology antibody antigen cell signaling "
       "stem cell cloning PCR sequencing bioinformatics proteomics metabolomics "
       "laboratory technique microscope culture assay stain blot gel electrophoresis",
    # Batch 7: Biology — Zoology, Botany & Evolution
    7: "zoology botany evolution ecology biodiversity species population ecosystem "
       "taxonomy phylogenetics darwin natural selection adaptation speciation extinction "
       "animal behavior ethology ornithology entomology herpetology ichthyology "
       "plant physiology photosynthesis mycology lichen algae fungi biome habitat "
       "marine biology freshwater terrestrial conservation wildlife field study",
    # Batch 8: Earth Sciences
    8: "earth sciences geology meteorology oceanography seismology climate volcano "
       "plate tectonics mineral rock fossil earthquake tsunami atmosphere weather "
       "hydrology geochemistry geophysics soil science paleoclimate ice core",
    # Batch 9: Astronomy, Astrophysics & Cosmology
    9: "astronomy astrophysics cosmology stellar galaxy exoplanet radio telescope "
       "black hole neutron star supernova dark matter dark energy redshift hubble "
       "big bang cosmic microwave background interstellar planet formation orbit "
       "observatory spectroscopy photometry celestial navigation solar system",
    # Batch 10: Clinical Medicine & Surgery
    10: "clinical medicine surgery diagnostics internal pediatrics geriatrics "
        "cardiology neurology oncology endocrinology gastroenterology pulmonology "
        "nephrology rheumatology dermatology ophthalmology ENT otolaryngology "
        "hematology immunology disease diagnosis treatment symptom patient "
        "clinical trial evidence based emergency medicine primary care "
        "general surgery neurosurgery cardiac thoracic vascular plastic transplant "
        "orthopedic trauma laparoscopic robotic minimally invasive anesthesia "
        "preoperative postoperative wound healing surgical instrument scalpel suture",
    # Batch 11: Pharmacology & Toxicology
    11: "pharmacology pharmacokinetics toxicology drug design medication pharmacy "
        "dose response clinical trial FDA approval adverse effect contraindication "
        "antibiotic antiviral antifungal analgesic anesthetic antihypertensive "
        "poison antidote overdose controlled substance prescription pharmacovigilance",
    # Batch 12: Specialized Healthcare
    12: "specialized healthcare dentistry orthodontics periodontics endodontics "
        "implantology prosthodontics oral surgery dental hygiene optometry podiatry "
        "physical therapy occupational therapy speech therapy audiology "
        "nursing midwifery paramedic emergency medical technician radiology "
        "medical imaging MRI CT ultrasound x-ray nuclear medicine rehabilitation",
    # Batch 13: Veterinary Medicine
    13: "veterinary small animal equine exotic livestock pet dog cat horse cattle "
        "zoonotic disease animal health welfare surgery vaccination parasite "
        "wildlife medicine avian reptile amphibian fish veterinary pathology",
    # Batch 14: Public Health & Epidemiology
    14: "public health epidemiology biostatistics outbreak pandemic infectious disease "
        "mortality morbidity vaccination herd immunity contact tracing quarantine "
        "health policy health promotion sanitation hygiene environmental health "
        "disease surveillance global health WHO CDC community health preventive",
    # Batch 15: Neuroscience & Cognitive Science
    15: "neuroscience cognitive science brain neuron synapse neurotransmitter "
        "dopamine serotonin GABA glutamate EEG MRI fMRI PET scan connectome "
        "memory attention decision making consciousness perception learning "
        "neuroplasticity neural network neuroanatomy cognition behavior "
        "neurodegenerative alzheimer parkinson multiple sclerosis brain imaging",
    # Batch 16: Alternative & Holistic Medicine
    16: "alternative medicine holistic naturopathy homeopathy acupuncture "
        "traditional chinese medicine ayurveda herbal medicine chiropractic "
        "osteopathy reiki energy healing meditation yoga aromatherapy "
        "nutritional therapy functional medicine integrative wellness",
    # Batch 17: Psychology — Clinical & Behavioral
    17: "clinical psychology psychotherapy CBT psychodynamic DBT ACT therapy "
        "mental health counseling assessment diagnosis personality disorder "
        "anxiety depression trauma PTSD eating disorder addiction recovery "
        "behavioral therapy exposure therapy EMDR mindfulness intervention",
    # Batch 18: Psychology — Social & Profiling
    18: "social psychology profiling group dynamics conformity persuasion attitudes "
        "prejudice stereotype social influence obedience authority bystander "
        "criminal profiling offender profiling forensic psychology investigative "
        "organizational psychology industrial psychology consumer behavior",
    # Batch 19: Psychiatry & Psychotherapy
    19: "psychiatry psychotherapy psychopharmacology mental illness schizophrenia "
        "bipolar depression anxiety OCD ADHD autism spectrum mood disorder "
        "antidepressant antipsychotic mood stabilizer anxiolytic DSM diagnosis "
        "talk therapy psychoanalysis psychodynamic interpersonal group therapy",
    # Batch 20: Philosophy & Epistemology
    20: "philosophy epistemology ethics metaphysics logic ontology phenomenology "
        "existentialism stoicism nihilism utilitarianism deontology virtue ethics "
        "philosophy of mind consciousness free will determinism political philosophy "
        "epistemology knowledge belief truth justification skepticism rationalism "
        "empiricism idealism realism pragmatism continental analytic philosophy",
    # Batch 21: Ethics, Bioethics & AI Alignment
    21: "ethics bioethics AI alignment moral philosophy applied ethics medical ethics "
        "research ethics animal ethics environmental ethics business ethics "
        "technology ethics AI safety value alignment superintelligence existential risk "
        "autonomous weapons algorithmic bias fairness transparency accountability",
    # Batch 22: World Religions — Abrahamic
    22: "religion abrahamic judaism christianity islam catholic orthodox protestant "
        "sunni shia quran bible torah talmud theology scripture monotheism "
        "church mosque synagogue prayer worship ritual clergy priest rabbi imam",
    # Batch 23: World Religions — Dharmic & Taoic
    23: "religion dharmic hinduism buddhism jainism sikhism taoism confucianism "
        "shinto zen karma dharma nirvana meditation yoga sutra veda upanishad "
        "mandala mantra reincarnation enlightenment bodhisattva guru eastern religion",
    # Batch 24: Esotericism, Occultism & Mysticism
    24: "esoteric occult mysticism hermeticism kabbalah alchemy astrology tarot ritual "
        "magic theurgy divination gnosticism rosicrucianism golden dawn thelema "
        "numerology symbolism sacred geometry witchcraft wicca paganism neoplatonism",
    # Batch 25: Freemasonry, Secret Societies
    25: "freemasonry secret society fraternal order masonic lodge templar illuminati "
        "rite ritual initiation degree grand lodge scottish rite york rite "
        "esoteric symbolism brotherhood clandestine conspiracy fraternity",
    # Batch 26: Parapsychology & Fringe Sciences
    26: "parapsychology fringe science telepathy telekinesis ESP precognition "
        "clairvoyance psychokinesis near death experience reincarnation "
        "ufology cryptozoology ghost haunting paranormal anomaly pseudoscience "
        "remote viewing out of body experience mediumship spiritualism",
    # Batch 27: History — Ancient & Medieval
    27: "ancient history medieval history rome greece egypt mesopotamia byzantium "
        "middle ages crusades feudal castle viking anglo-saxon antiquity "
        "classical civilization empire kingdom dynasty archaeology artifact "
        "manuscript papyrus inscription excavation chronicle",
    # Batch 28: History — Modern & Contemporary
    28: "modern history contemporary world war cold war industrial revolution "
        "colonialism decolonization nation state twentieth century globalization "
        "civil rights movement cold war modern era political revolution "
        "enlightenment renaissance reformation napoleon victorian",
    # Batch 29: Archaeology & Paleontology
    29: "archaeology paleontology fossil excavation artifact carbon dating "
        "dinosaur vertebrate invertebrate micropaleontology precambrian "
        "cambrian jurassic cretaceous extinction field method stratigraphy "
        "prehistoric neolithic bronze age iron age hominid human evolution",
    # Batch 30: Anthropology & Ethnology
    30: "anthropology ethnology cultural physical linguistic visual human evolution "
        "society tribe kinship ritual custom tradition indigenous people "
        "fieldwork participant observation ethnography material culture "
        "human origins primatology hunter gatherer pastoral nomadic civilization",
    # Batch 31: Sociology & Demography
    31: "sociology demography social stratification class race gender inequality "
        "migration fertility mortality census population urbanization statistics "
        "social network deviance criminology social movement social change "
        "urban rural community family marriage education religion and society",
    # Batch 32: Political Science & Government
    32: "political science government governance democracy constitution parliament "
        "congress senate president prime minister election voting party system "
        "comparative politics political theory ideology liberalism conservatism "
        "socialism communism fascism authoritarianism public policy administration",
    # Batch 33: Geopolitics & International Relations
    33: "geopolitics international relations diplomacy foreign policy treaty alliance "
        "security studies globalization sovereignty nation state UN NATO EU "
        "conflict resolution peacekeeping sanctions soft power hard power "
        "diplomatic embassy ambassador consulate multilateral bilateral summit",
    # Batch 34: Law — Constitutional & Public
    34: "constitutional law public law civil rights human rights judicial review "
        "supreme court constitution bill of rights amendment separation of powers "
        "federalism administrative law regulatory law legislation statute "
        "public interest litigation environmental law immigration law",
    # Batch 35: Law — Criminal & Penal
    35: "criminal law penal code crime felony misdemeanor prosecution defense "
        "prison sentence punishment parole probation death penalty capital "
        "theft assault murder manslaughter fraud white collar crime drug offense "
        "juvenile justice criminal procedure arrest warrant indictment",
    # Batch 36: Law — Corporate, Commercial & Maritime
    36: "corporate law commercial law maritime law contract business corporation "
        "LLC partnership merger acquisition intellectual property patent trademark "
        "copyright trade secret antitrust competition shipping admiralty "
        "international trade WTO arbitration mediation negotiation",
    # Batch 37: Forensic Sciences & CSI
    37: "forensic science CSI crime scene investigation DNA ballistics digital "
        "toxicology evidence trace fingerprint autopsy blood spatter hair fiber "
        "forensic psychology forensic accounting forensic anthropology "
        "chain of custody expert witness laboratory analysis criminalistics",
    # Batch 38: Macroeconomics & Microeconomics
    38: "macroeconomics microeconomics GDP inflation unemployment fiscal monetary "
        "supply demand market equilibrium elasticity competition monopoly oligopoly "
        "economic growth recession trade deficit exchange rate central bank "
        "keynesian classical chicago school development economics behavioral econ",
    # Batch 39: Finance, Banking & Investment
    39: "finance banking investment stock market bond portfolio risk management "
        "hedge fund private equity venture capital asset management mutual fund "
        "ETF derivative option future swap fintech cryptocurrency digital banking "
        "insurance wealth management retirement planning credit loan mortgage",
    # Batch 40: Accounting & Corporate Taxation
    40: "accounting auditing taxation IFRS GAAP bookkeeping financial statement "
        "balance sheet income statement cash flow tax return corporate tax VAT "
        "payroll cost accounting managerial accounting internal audit external audit "
        "tax planning tax compliance transfer pricing depreciation amortization",
    # Batch 41: Business Administration & Management
    41: "business management administration strategy operations HR human resources "
        "leadership organizational behavior change management corporate governance "
        "project management agile scrum lean six sigma KPI OKR balanced scorecard "
        "supply chain procurement team building negotiation stakeholder CEO COO",
    # Batch 42: Marketing, PR & Reputation Management
    42: "marketing PR public relations reputation brand advertising digital marketing "
        "content marketing social media SEO SEM influencer marketing email marketing "
        "market research consumer behavior campaign analytics conversion funnel "
        "crisis communication media relations press release corporate communication",
    # Batch 43: Logistics & Supply Chain
    43: "logistics supply chain procurement warehousing distribution transportation "
        "last-mile delivery inventory management freight shipping cargo maritime "
        "rail trucking air freight reverse logistics cold chain lean logistics",
    # Batch 44: Computer Science
    44: "computer science algorithms data structures complexity theory automata "
        "turing machine computability graph algorithm sorting searching P NP "
        "lambda calculus recursion programming language compiler interpreter "
        "operating system distributed systems concurrency parallel computing "
        "database theory formal verification type theory information theory",
    # Batch 45: Software Engineering & Architecture
    45: "software engineering architecture design patterns database SQL NoSQL "
        "DevOps CI/CD testing QA agile scrum kanban version control git "
        "microservices monolith API REST GraphQL backend frontend fullstack "
        "deployment containerization kubernetes docker cloud AWS Azure "
        "code review refactoring technical debt clean code SOLID principles",
    # Batch 46: AI & Machine Learning
    46: "artificial intelligence machine learning deep learning natural language "
        "neural network transformer GPT BERT LLM large language model attention "
        "computer vision CNN GAN reinforcement learning supervised unsupervised "
        "MLOps training inference fine-tuning RAG retrieval augmented generation "
        "classification regression clustering dimensionality reduction feature "
        "tensorflow pytorch scikit learn numpy pandas jupyter notebook embedding",
    # Batch 47: Blockchain, Web3 & Decentralized Tech
    47: "blockchain web3 smart contract DeFi DAO zero knowledge ZK cryptocurrency "
        "bitcoin ethereum solana consensus proof of work stake rollup layer2 NFT "
        "tokenomics decentralized exchange DEX liquidity mining yield farming "
        "distributed ledger hash mining node validator governance token",
    # Batch 48: Quantum Computing & Quantum Information
    48: "quantum computing qubit superposition entanglement algorithm cryptography "
        "error correction quantum supremacy annealing gate model circuit simulator "
        "shor grover quantum key distribution QKD quantum network quantum memory "
        "trapped ion superconducting transmon topological qubit majorana",
    # Batch 49: Cybersecurity — Offensive
    49: "offensive cybersecurity pentesting exploitation reverse engineering red team "
        "ethical hacking vulnerability CVE exploit buffer overflow SQL injection XSS "
        "CSRF privilege escalation lateral movement persistence command control C2 "
        "metasploit burp suite nmap wireshark kali linux payload shellcode fuzzing",
    # Batch 50: Cybersecurity — Defensive & OSINT
    50: "defensive cybersecurity OSINT SOC threat intelligence forensics incident "
        "response EDR SIEM firewall IDS IPS blue team threat hunting malware "
        "analysis phishing open source intelligence reconnaissance SOC analyst "
        "MITRE ATT&CK cyber kill chain detection monitoring logging alert triage "
        "ransomware APT threat actor IOCs TTPs cyber threat intelligence",
    # Batch 51: Data Science & Big Data
    51: "data science big data analytics mining wrangling visualization predictive "
        "ETL pipeline SQL pandas spark hadoop kafka streaming dashboard tableau "
        "power BI statistical analysis A/B testing feature engineering "
        "data warehouse lakehouse snowflake databricks airflow orchestration",
    # Batch 52: Game Dev, VR/AR & Interactive Media
    52: "game development VR AR virtual reality augmented reality game engine "
        "Unity Unreal 3D graphics multiplayer networking game design level design "
        "game mechanic rendering shader physics engine animation motion capture "
        "mobile game console PC game indie AAA esports interactive media",
    # Batch 53: Hardware Engineering & Microelectronics
    53: "hardware engineering microelectronics CPU GPU FPGA PCB embedded systems "
        "semiconductor chip design VLSI ASIC Verilog VHDL system on chip SoC "
        "ARM x86 RISC-V microcontroller firmware circuit board soldering JTAG",
    # Batch 54: Mechanical Engineering & Mechatronics
    54: "mechanical engineering mechatronics robotics automation CNC manufacturing "
        "UAV drone automotive vehicle engine thermodynamics fluid mechanics "
        "CAD CAM 3D modeling actuator sensor motor gear bearing hydraulics "
        "pneumatics industrial robot factory assembly line quality control",
    # Batch 55: Civil Engineering & Urban Planning
    55: "civil engineering urban planning structures geotechnical smart city "
        "infrastructure bridge road highway tunnel dam construction building "
        "surveying BIM structural analysis concrete steel foundation zoning",
    # Batch 56: Aerospace & Aeronautics
    56: "aerospace aeronautics aerodynamics avionics propulsion jet engine spacecraft "
        "aircraft helicopter drone satellite rocket launch orbital mechanics "
        "wind tunnel CFD flight control navigation GPS autopilot pilot training",
    # Batch 57: Space Colonization & Astronautics
    57: "space colonization astronautics interplanetary Mars moon base habitat "
        "terraforming space mining asteroid resource extraction life support "
        "space station orbital mechanics EVA spacesuit radiation shielding "
        "in-situ resource utilization ISRU space agriculture hydroponics",
    # Batch 58: Electrical & Energy Engineering
    58: "electrical engineering energy power generation renewable nuclear solar "
        "wind hydro smart grid transmission distribution battery storage "
        "circuit electronics transformer generator turbine photovoltaic "
        "geothermal tidal wave hydrogen fuel cell carbon capture clean energy",
    # Batch 59: Materials Science & Nanotechnology
    59: "materials science nanotechnology metallurgy polymer graphene composite "
        "ceramic semiconductor thin film coating 3d printing additive manufacturing "
        "nanoparticle nanotube nanowire self-assembly biomaterial smart material "
        "corrosion fatigue fracture testing characterization microscopy AFM SEM TEM",
    # Batch 60: Fashion, Textile & Apparel
    60: "fashion textile apparel clothing garment design luxury brand manufacturing "
        "smart textile wearable technology fabric pattern sewing tailoring "
        "sustainable fashion fast fashion haute couture prêt-à-porter runway",
    # Batch 61: Agriculture, Agronomy & Forestry
    61: "agriculture agronomy forestry farming crop soil irrigation fertilizer "
        "pesticide herbicide harvest livestock poultry dairy aquaculture "
        "hydroponics vertical farming precision agriculture agri-tech GMO "
        "organic farming sustainable agriculture silviculture timber logging",
    # Batch 62: Food Science & Culinary Arts
    62: "food science culinary molecular gastronomy baking enology wine safety "
        "nutrition cooking chef kitchen recipe ingredient fermentation "
        "food processing preservation pasteurization HACCP sensory analysis "
        "flavor texture aroma taste food chemistry dietetics food engineering",
    # Batch 63: Architecture & Interior Design
    63: "architecture interior design parametric landscape restoration building "
        "urban design residential commercial sustainable green building "
        "architectural drawing blueprint CAD BIM space planning furniture "
        "lighting acoustics materials finishes decoration ergonomics",
    # Batch 64: Visual Arts, Design & Aesthetics
    64: "visual arts design painting graphic UI UX industrial illustration "
        "photography sculpture printmaking typography color theory composition "
        "digital art animation motion graphics branding visual identity "
        "aesthetics beauty art history museum gallery curator exhibition",
    # Batch 65: Performing Arts & Entertainment
    65: "performing arts directing acting cinematography film movie theater stage "
        "screenplay script drama comedy musical opera ballet dance choreography "
        "entertainment production sound design editing VFX special effects "
        "costume set design lighting design producer director screenwriter",
    # Batch 66: Linguistics, Philology & Translation
    66: "linguistics translation philology phonetics phonology morphology syntax "
        "semantics pragmatics sociolinguistics psycholinguistics NLP natural language "
        "etymology comparative linguistics language family dialect idiolect "
        "bilingual multilingual interpretation localization transliteration",
    # Batch 67: Literature & Poetry
    67: "literature poetry theory criticism creative writing narrative fiction novel "
        "prose verse rhyme meter epic sonnet haiku literary analysis "
        "comparative literature world literature author novelist poet playwright "
        "genre literary movement romanticism modernism postmodernism realism",
    # Batch 68: Journalism, Mass Media & Broadcasting
    68: "journalism media broadcasting investigative reporting fact-checking news "
        "documentary radio television podcast print digital journalism "
        "editor columnist correspondent anchor press freedom censorship "
        "media ethics fake news misinformation disinformation propaganda",
    # Batch 69: Education, Pedagogy & Andragogy
    69: "education pedagogy andragogy didactics edtech gamification learning theory "
        "curriculum teaching instruction assessment evaluation classroom "
        "online learning e-learning MOOC distance education adult learning "
        "special education early childhood higher education university school",
    # Batch 70: Military Science, Strategy & Tactics
    70: "military science warfare strategy tactics doctrine logistics insurgency "
        "counterinsurgency COIN combined arms maneuver defense offense deterrence "
        "navy army air force marines special forces artillery armor infantry "
        "battlefield command control intelligence surveillance reconnaissance",
    # Batch 71: Intelligence, Espionage & Covert Operations
    71: "intelligence espionage HUMINT SIGINT OSINT tradecraft covert operation "
        "counterintelligence surveillance reconnaissance agent handler dead drop "
        "cryptography signals analysis satellite imagery cyber intelligence "
        "spy agency CIA MI6 Mossad FSB GRU mole defector double agent",
    # Batch 72: Cognitive Warfare & PsyOps
    72: "cognitive warfare psyops propaganda narrative memetic reflexive control "
        "information operations psychological operations disinformation misinformation "
        "social media manipulation influence campaign hybrid warfare perception "
        "information warfare active measures cognitive security brainwashing",
    # Batch 73: Ecology, Conservation & Environmental Science
    73: "ecology environment climate conservation toxicology biodiversity "
        "ecosystem pollution carbon footprint sustainability renewable green "
        "climate change global warming endangered species habitat loss "
        "environmental impact assessment circular economy zero waste rewilding",
    # Batch 74: Sports Science, Kinesiology & Human Performance
    74: "sports science physiology biomechanics nutrition training athletics "
        "exercise performance recovery injury prevention kinesiology coaching "
        "strength conditioning endurance flexibility speed agility power "
        "sports medicine doping anti-doping Olympic athlete fitness health",
    # Batch 75: Survivalism, Bushcraft & Tactical Preparedness
    75: "survival preparedness bushcraft navigation field medicine emergency "
        "wilderness first aid shelter water fire food foraging self reliance "
        "orienteering compass map prepper disaster preparedness homesteading "
        "tactical gear outdoor survival knife axe camping hiking trekking"
}


def tokenize(text: str) -> List[str]:
    """Lowercase, split on word boundaries, remove stop words and short tokens."""
    # Find all word-like tokens (Latin or Cyrillic, 2+ chars)
    tokens = re.findall(r'[a-zA-ZЀ-ӿ0-9]{2,}', text.lower())
    return [t for t in tokens if t not in STOP_WORDS]


def parse_micro_domains() -> List[Dict]:
    """Parse all 7 Micro_Domains_Batch_X.md files.

    Returns list of sector dicts with: id, name, domains (list of {idx, name, tokens})
    Deduplicates sectors that span multiple batch files (e.g., sector 10 in batch 1 + batch 2).
    """
    hierarchy = []
    sector_map: Dict[int, Dict] = {}  # sector_id -> sector dict (dedup)
    current_sector = None

    for i in range(1, BATCH_COUNT + 1):
        file_path = BATCH_DIR / f"Micro_Domains_Batch_{i}.md"
        if not file_path.exists():
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                # Sector header: "## Сектор 01: Pure Mathematics (Чистая математика)"
                sector_match = re.match(r'^##\s*Сектор\s*(\d+):\s*(.+)$', line, re.IGNORECASE)
                if sector_match:
                    sector_id = int(sector_match.group(1))
                    sector_name = sector_match.group(2).strip()
                    if sector_id in sector_map:
                        current_sector = sector_map[sector_id]
                    else:
                        current_sector = {
                            "id": sector_id,
                            "name": sector_name,
                            "domains": []
                        }
                        sector_map[sector_id] = current_sector
                        hierarchy.append(current_sector)
                    continue

                # Domain: "1. Common name (clarification)"
                if current_sector:
                    domain_match = re.match(r'^\d+\.\s*(.+)$', line)
                    if domain_match:
                        raw = domain_match.group(1).strip()

                        # Build bilingual token set
                        # 1. Russian name before parentheses
                        main_name = raw.split('(')[0].strip() if '(' in raw else raw

                        # 2. Russian parenthetical clarification
                        match = re.search(r'\(([^)]+)\)', raw)
                        paren_text = match.group(1) if match else ''

                        # 3. English sector keywords
                        sector_id = current_sector["id"]
                        en_keywords = SECTOR_EN_MAP.get(sector_id, '')

                        # Combine all sources
                        combined = f"{main_name} {paren_text} {en_keywords}"
                        combined = re.sub(r'[:;,/]', ' ', combined)

                        tokens = tokenize(combined)
                        current_sector["domains"].append({
                            "idx": len(current_sector["domains"]) + 1,
                            "name": raw,
                            "tokens": tokens
                        })

    # No need to flush current_sector — already in sector_map
    return hierarchy


class TfidfRouter:
    """Pure Python TF-IDF + cosine similarity router.

    Computes IDF-weighted sparse vectors and cosine similarity
    without any LLM or external API dependency.
    """

    def __init__(self):
        self.sectors = []
        self.domain_entries = []  # [{sector_id, sector_name, domain, vector: {term: tfidf}}]
        self.idf = {}  # {term: idf_score}
        self.corpus_size = 0
        self._build()

    def _build(self):
        """Parse batches, compute IDF, build normalized TF-IDF vectors."""
        self.sectors = parse_micro_domains()

        # Flatten all domains
        all_domains = []
        for sector in self.sectors:
            for domain in sector["domains"]:
                all_domains.append({
                    "sector_id": sector["id"],
                    "sector_name": sector["name"],
                    "domain": domain,
                    "token_set": set(domain["tokens"])
                })

        self.corpus_size = len(all_domains)
        if self.corpus_size == 0:
            return

        # Document frequency
        df = {}
        for entry in all_domains:
            for token in entry["token_set"]:
                df[token] = df.get(token, 0) + 1

        # IDF: log(N / df). No smoothing --- rare terms should dominate.
        N = float(self.corpus_size)
        self.idf = {t: math.log(N / c) for t, c in df.items()}

        # Build normalized TF-IDF vectors
        for entry in all_domains:
            vector = {}
            for token in entry["token_set"]:
                vector[token] = 1.0 * self.idf[token]  # TF=1 (binary presence)

            # Normalize to unit vector
            norm = math.sqrt(sum(v * v for v in vector.values()))
            if norm > 0:
                vector = {k: v / norm for k, v in vector.items()}

            self.domain_entries.append({
                "sector_id": entry["sector_id"],
                "sector_name": entry["sector_name"],
                "domain_idx": entry["domain"]["idx"],
                "domain_name": entry["domain"]["name"],
                "vector": vector
            })

    def _vectorize_query(self, query: str) -> Dict[str, float]:
        """Convert query to a normalized TF-IDF vector."""
        tokens = tokenize(query)
        if not tokens:
            return {}

        # TF: count term occurrences in query
        tf = {}
        for token in tokens:
            if token in self.idf:
                tf[token] = tf.get(token, 0) + 1

        # TF-IDF
        vector = {t: c * self.idf[t] for t, c in tf.items()}

        # Normalize
        norm = math.sqrt(sum(v * v for v in vector.values()))
        if norm > 0:
            vector = {k: v / norm for k, v in vector.items()}

        return vector

    def _cosine(self, q_vec: Dict[str, float], d_vec: Dict[str, float]) -> float:
        """Cosine similarity between two UNIT-NORMALIZED vectors = dot product."""
        if not q_vec or not d_vec:
            return 0.0
        score = sum(q_vec.get(t, 0.0) * w for t, w in d_vec.items())
        return max(0.0, min(1.0, score))

    def route(self, query: str, top_n: int = 10) -> List[Dict]:
        """Route a query to the most relevant domains.

        Returns ranked list of {sector_id, sector_name, domain_idx, domain_name, cosine_score}
        """
        if not self.domain_entries:
            return []

        q_vec = self._vectorize_query(query)
        if not q_vec:
            return []

        results = []
        for entry in self.domain_entries:
            score = self._cosine(q_vec, entry["vector"])
            if score > 0:
                results.append({
                    "sector_id": entry["sector_id"],
                    "sector_name": entry["sector_name"],
                    "domain_idx": entry["domain_idx"],
                    "domain_name": entry["domain_name"],
                    "cosine_score": round(score, 4)
                })

        results.sort(key=lambda x: x["cosine_score"], reverse=True)
        return results[:top_n]


# --- Singleton ---
_router: Optional[TfidfRouter] = None


def load_corpus() -> TfidfRouter:
    """Load or return cached TfidfRouter singleton."""
    global _router
    if _router is None:
        _router = TfidfRouter()
    return _router


MAX_QUERY_LENGTH = 10000


def route_query(query: str, top_n: int = 10) -> List[Dict]:
    """Programmatic entry point.

    Args:
        query: Natural language query (English or Russian), max 10,000 characters
        top_n: Number of results (clamped to 1-100)

    Returns:
        Ranked [{sector_id, sector_name, domain_idx, domain_name, cosine_score}, ...]
    """
    # Validate inputs
    if not isinstance(query, str):
        query = str(query) if query else ""
    if len(query) > MAX_QUERY_LENGTH:
        query = query[:MAX_QUERY_LENGTH]
    top_n = max(1, min(top_n, 100))
    return load_corpus().route(query, top_n)


# --- CLI ---
def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Syndicate-30000 Semantic Vector Router (TF-IDF + cosine similarity)"
    )
    parser.add_argument("query", nargs="*", help="Search query")
    parser.add_argument("--json", action="store_true", help="Output as JSON array")
    parser.add_argument("--top", type=int, default=10, help="Number of results (default 10)")
    parser.add_argument("--verbose", action="store_true", help="Show corpus stats first")

    args = parser.parse_args()
    if not args.query:
        parser.print_help()
        sys.exit(1)

    query = " ".join(args.query)
    router = load_corpus()

    if args.verbose:
        print(f"Corpus: {router.corpus_size} domains / {len(router.sectors)} sectors", file=sys.stderr)
        print(f"Vocabulary: {len(router.idf)} unique terms", file=sys.stderr)
        print(f"Query: {query}", file=sys.stderr)
        print("-" * 50, file=sys.stderr)

    results = router.route(query, top_n=args.top)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        if not results:
            print("No matches found.")
        for i, r in enumerate(results, 1):
            print(f"{i:2d}. [{r['cosine_score']:.4f}] Sector {r['sector_id']:02d}: {r['sector_name']}")
            print(f"     Domain {r['domain_idx']:02d}: {r['domain_name']}")

    sys.exit(0 if results else 1)


if __name__ == "__main__":
    main()
