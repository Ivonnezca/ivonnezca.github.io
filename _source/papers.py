# Research themes and selected papers for Ivonne Zavala's page.
# Edit here, then run build.py to regenerate index.html.
# "arxiv": arXiv id, or None to link to an INSPIRE title search instead.

THEMES = [
    {
        "id": "string-phenomenology",
        "title": "String Phenomenology",
        "question": "How does the geometry of extra dimensions shape the physics of our four-dimensional world?",
        "subtopics": [
            {
                "title": "Moduli, supergravity and quantum gravity",
                "text": "Warped throats, anti-branes and non-linear supergravity, and the swampland conjectures that constrain which effective theories can come from quantum gravity.",
                "papers": [
                    ("A guide to frames, 2π’s, scales and corrections in string compactifications", "B. Valeixo Bento, D. Chakraborty, S. Parameswaran, I. Zavala", "Int. J. Mod. Phys. D 34 (2025) 2530003", "2301.05178"),
                    ("The Stückelberg Path to Pure de Sitter Supergravity", "S. Bansal, S. Nagy, A. Padilla, I. Zavala", "Phys. Rev. D 111 (2025)", "2411.05710"),
                    ("Gravity at the Tip of the Throat", "B. Valeixo Bento, D. Chakraborty, S. L. Parameswaran, I. Zavala", "JHEP 09 (2022) 208", "2204.02086"),
                    ("Anti-D3 branes and moduli in non-linear supergravity", "M. P. García del Moral, S. Parameswaran, N. Quiroz, I. Zavala", "JHEP 10 (2017) 185", "1707.07059"),
                    ("Warping the Weak Gravity Conjecture", "K. Kooner, S. Parameswaran, I. Zavala", "Phys. Lett. B 759 (2016) 402", "1509.07049"),
                ],
            },
            {
                "title": "Heterotic orbifolds and their symmetries",
                "text": "Coupling selection rules, discrete R-symmetries and modular symmetry, and moduli stabilisation in heterotic string models close to the Standard Model.",
                "papers": [
                    ("Discrete R-symmetries and Anomaly Universality in Heterotic Orbifolds", "N. G. Cabo Bizet, T. Kobayashi, D. K. Mayorga Peña, S. L. Parameswaran, M. Schmitz, I. Zavala", "JHEP 02 (2014) 098", "1308.5669"),
                    ("R-charge Conservation and More in Factorizable and Non-Factorizable Orbifolds", "N. G. Cabo Bizet, T. Kobayashi, D. K. Mayorga Peña, S. L. Parameswaran, M. Schmitz, I. Zavala", "JHEP 05 (2013) 076", "1301.2322"),
                    ("Revisiting Coupling Selection Rules in Heterotic Orbifold Models", "T. Kobayashi, S. L. Parameswaran, S. Ramos-Sánchez, I. Zavala", "JHEP 05 (2012) 008", "1107.2137"),
                    ("On Moduli Stabilisation and de Sitter Vacua in MSSM Heterotic Orbifolds", "S. Parameswaran, S. Ramos-Sánchez, I. Zavala", "JHEP 01 (2011) 071", "1009.3931"),
                    ("Oddness from Rigidness", "S. Förste, I. Zavala", "JHEP 07 (2008) 086", "0806.2328"),
                    ("Orientifold’s Landscape: Non-Factorisable Six-Tori", "S. Förste, C. Timirgaziu, I. Zavala", "JHEP 10 (2007) 025", "0707.0747"),
                ],
            },
        ],
    },
    {
        "id": "extra-dimensions",
        "title": "Extra Dimensions and Brane Worlds",
        "question": "What if our Universe is a brane in a spacetime with more dimensions?",
        "subtopics": [
            {
                "title": "Brane worlds and self-tuning",
                "text": "Our Universe as a brane in a higher-dimensional spacetime: self-tuning of the cosmological constant, brane geometries from gauged supergravities and accelerating brane cosmologies.",
                "papers": [
                    ("Nontrivial Cosmological Constant in Brane Worlds with Unorthodox Lagrangians", "S. Förste, H. P. Nilles, I. Zavala", "JCAP 07 (2011) 007", "1104.2570"),
                    ("General brane geometries from scalar potentials: Gauged supergravities and accelerating universes", "C. P. Burgess, C. Núñez, F. Quevedo, G. Tasinato, I. Zavala", "JHEP 08 (2003) 056", "hep-th/0305211"),
                    ("Branes on charged dilatonic backgrounds: Self-tuning, Lorentz violations and cosmology", "C. Grojean, F. Quevedo, G. Tasinato, I. Zavala", "JHEP 08 (2001) 005", "hep-th/0106120"),
                ],
            },
            {
                "title": "Supersymmetric large extra dimensions",
                "text": "Warped and axisymmetric solutions of six-dimensional chiral gauged supergravity (SLED), their stability, and what they say about the cosmological constant problem.",
                "papers": [
                    ("The Fate of Unstable Gauge Flux Compactifications", "C. P. Burgess, S. L. Parameswaran, I. Zavala", "JHEP 05 (2009) 008", "0812.3902"),
                    ("The 6D SuperSwirl", "S. L. Parameswaran, G. Tasinato, I. Zavala", "Nucl. Phys. B 737 (2006) 49", "hep-th/0509061"),
                    ("General axisymmetric solutions and self-tuning in 6D chiral gauged supergravity", "C. P. Burgess, F. Quevedo, G. Tasinato, I. Zavala", "JHEP 11 (2004) 069", "hep-th/0408109"),
                    ("Warped brane worlds in six dimensional supergravity", "Y. Aghababaie, C. P. Burgess, J. M. Cline, H. Firouzjahi, S. Parameswaran, F. Quevedo, G. Tasinato, I. Zavala", "JHEP 09 (2003) 037", "hep-th/0308064"),
                ],
            },
        ],
    },
    {
        "id": "string-cosmology",
        "title": "String Cosmology",
        "question": "Can the Universe we observe emerge from string theory?",
        "subtopics": [
            {
                "title": "Inflation from strings and branes",
                "text": "Building inflation from D-branes, warped throats and string axions, and asking what string compactifications predict for primordial black holes and gravitational waves.",
                "papers": [
                    ("String cosmology: From the early universe to today", "M. Cicoli, J. P. Conlon, A. Maharana, S. Parameswaran, F. Quevedo, I. Zavala", "Phys. Rept. 1059 (2024) 1–155. Review", "2303.04819"),
                    ("On chromonatural inflation in string theory", "J. Holland, I. Zavala, G. Tasinato", "JCAP 12 (2020) 026", "2009.00653"),
                    ("Mechanisms for Primordial Black Hole Production in String Theory", "O. Özsoy, S. Parameswaran, G. Tasinato, I. Zavala", "JCAP 07 (2018) 005", "1803.07626"),
                    ("Mirror quintic vacua: hierarchies and inflation", "N. Cabo Bizet, O. Loaiza-Brito, I. Zavala", "JHEP 10 (2016) 082", "1605.03974"),
                    ("Prospects for Primordial Gravitational Waves in String Inflation", "S. L. Parameswaran, I. Zavala", "Int. J. Mod. Phys. D 25 (2016) 1644011", "1606.02537"),
                    ("Warped Wilson Line DBI Inflation", "A. Avgoustidis, I. Zavala", "JCAP 01 (2009) 045", "0810.5001"),
                    ("Recombination of intersecting D-branes and cosmological inflation", "M. Gómez-Reino, I. Zavala", "JHEP 09 (2002) 020", "hep-th/0207278"),
                ],
            },
            {
                "title": "Time-dependent solutions in supergravity and string theory",
                "text": "S-branes and other time-dependent backgrounds as models of cosmological spacetimes: bouncing brane worlds, negative-tension branes and particle production.",
                "papers": [
                    ("Regular S-brane backgrounds", "G. Tasinato, I. Zavala, C. P. Burgess, F. Quevedo", "JHEP 04 (2004) 038", "hep-th/0403156"),
                    ("On bouncing brane worlds, S-branes and branonium cosmology", "C. P. Burgess, F. Quevedo, R. Rabadán, G. Tasinato, I. Zavala", "JCAP 02 (2004) 008", "hep-th/0310122"),
                    ("Instabilities and particle production in S-brane geometries", "C. P. Burgess, P. Martineau, F. Quevedo, G. Tasinato, I. Zavala", "JHEP 03 (2003) 050", "hep-th/0301122"),
                    ("Cosmological spacetimes from negative tension brane backgrounds", "C. P. Burgess, F. Quevedo, S. J. Rey, G. Tasinato, I. Zavala", "JHEP 10 (2002) 028", "hep-th/0207104"),
                ],
            },
            {
                "title": "Dark energy and de Sitter in string theory",
                "text": "Whether string theory admits de Sitter vacua or quintessence, how well controlled those constructions are, and how to confront them with data.",
                "papers": [
                    ("Rolling with modular symmetry: quintessence and de Sitter in heterotic orbifolds", "H. Gordillo-Ruiz, M. Hernández-Segura, I. Portillo-Castillo, S. Ramos-Sánchez, I. Zavala", "JHEP 04 (2026) 211", "2509.22781"),
                    ("Exponential quintessence: curved, steep and stringy?", "D. Andriot, S. Parameswaran, D. Tsimpis, T. Wrase, I. Zavala", "JHEP 08 (2024) 117", "2405.09323"),
                    ("De Sitter vacua: when are ‘subleading corrections’ really subleading?", "B. Valeixo Bento, D. Chakraborty, S. Parameswaran, I. Zavala", "JHEP 11 (2023) 075", "2306.07332"),
                    ("A new de Sitter solution with a weakly warped deformed conifold", "B. Valeixo Bento, D. Chakraborty, S. L. Parameswaran, I. Zavala", "JHEP 12 (2021) 124", "2105.03370"),
                    ("Runaway Quintessence, Out of the Swampland", "Y. Olguín-Trejo, S. L. Parameswaran, G. Tasinato, I. Zavala", "JCAP 01 (2019) 031", "1810.08634"),
                    ("Dark energy, D-branes and pulsar timing arrays", "D. Chowdhury, G. Tasinato, I. Zavala", "JCAP 11 (2023) 090", "2307.01188"),
                    ("De Sitter Vacua from Non-perturbative Flux Compactifications", "J. Blåbäck, D. Roest, I. Zavala", "Phys. Rev. D 90 (2014) 024065", "1312.5328"),
                ],
            },
        ],
    },
    {
        "id": "inflation",
        "title": "Cosmological Inflation",
        "question": "What happened in the first instant, when several fields shaped the expansion?",
        "subtopics": [
            {
                "title": "Multifield inflation and turning trajectories",
                "text": "Inflation driven by several fields whose trajectory bends in field space: from Spinflation to rapid and sharp turns, heavy fields, the η-problem and vector fields during inflation.",
                "papers": [
                    ("Sharp turns in axion monodromy: primordial black holes and gravitational waves", "S. Bhattacharya, I. Zavala", "JCAP 04 (2023) 065", "2205.06065"),
                    ("Rapid-turn inflation in supergravity is rare and tachyonic", "V. Aragam, R. Chiovoloni, S. Paban, R. Rosati, I. Zavala", "JCAP 03 (2022) 002", "2110.05516"),
                    ("Fat Inflatons, Large Turns and the η-problem", "D. Chakraborty, R. Chiovoloni, O. Loaiza-Brito, G. Niz, I. Zavala", "JCAP 01 (2020) 020", "1908.09797"),
                    ("Anisotropic Inflation with Derivative Couplings", "J. Holland, S. Kanno, I. Zavala", "Phys. Rev. D 97 (2018) 103534", "1711.07450"),
                    ("Effects of the speed of sound at large-N", "I. Zavala", "Phys. Rev. D 91 (2015) 063005", "1412.3732"),
                    ("Statistical Anisotropy from Vector Curvaton in D-brane Inflation", "K. Dimopoulos, D. Wills, I. Zavala", "Nucl. Phys. B 868 (2013) 120", "1108.4424"),
                    ("Spinflation", "D. Easson, R. Gregory, D. Mota, G. Tasinato, I. Zavala", "JCAP 02 (2008) 010", "0709.2666"),
                ],
            },
            {
                "title": "Observational signatures",
                "text": "Non-Gaussianity, reheating, the inflaton field range and tensor modes, and what CMB data can and cannot tell us about the inflationary potential.",
                "papers": [
                    ("Squeezed tensor non-Gaussianity in non-attractor inflation", "O. Özsoy, M. Mylova, S. Parameswaran, C. Powell, G. Tasinato, I. Zavala", "JCAP 09 (2019) 036", "1902.04976"),
                    ("Subleading Effects and the Field Range in Axion Inflation", "S. Parameswaran, G. Tasinato, I. Zavala", "JCAP 04 (2016) 008", "1602.02812"),
                    ("Lyth bound of inflation with a tilt", "J. García-Bellido, D. Roest, M. Scalisi, I. Zavala", "Phys. Rev. D 90 (2014) 123539", "1408.6839"),
                    ("Can CMB data constrain the inflationary field range?", "J. García-Bellido, D. Roest, M. Scalisi, I. Zavala", "JCAP 09 (2014) 006", "1405.7399"),
                    ("Kähler potentials for Planck inflation", "D. Roest, M. Scalisi, I. Zavala", "JCAP 11 (2013) 007", "1307.4343"),
                    ("Modulated Reheating and Large Non-Gaussianity in String Cosmology", "M. Cicoli, G. Tasinato, I. Zavala, C. P. Burgess, F. Quevedo", "JCAP 05 (2012) 039", "1202.4580"),
                    ("Non-standard primordial fluctuations and non-gaussianity in string inflation", "C. P. Burgess, M. Cicoli, M. Gómez-Reino, F. Quevedo, G. Tasinato, I. Zavala", "JHEP 08 (2010) 045", "1005.4840"),
                ],
            },
        ],
    },
    {
        "id": "dark-universe",
        "title": "The Dark Universe",
        "question": "What are dark energy and dark matter, and what can the newest data tell us about them?",
        "subtopics": [
            {
                "title": "Dark energy meets data",
                "text": "Quintessence motivated by quantum gravity, bounded and phantom-crossing dark energy, and data-driven reconstructions with Bayesian and machine-learning tools.",
                "papers": [
                    ("Data-Driven Discovery of a Simple Phantom-Crossing Dark Energy Parametrization", "G. Borghetto, A. Malhotra, S. Arora, A. De Felice, S. Mukohyama, G. Tasinato, I. Zavala", "Preprint (2026)", "2606.17951"),
                    ("Bounded dark energy", "G. Borghetto, A. Malhotra, G. Tasinato, I. Zavala", "Phys. Rev. D 112 (2025) 023521", "2503.11628"),
                    ("Cosmological tests of quintessence in quantum gravity", "S. Bhattacharya, G. Borghetto, A. Malhotra, S. Parameswaran, G. Tasinato, I. Zavala", "JCAP 04 (2025) 086", "2410.21243"),
                    ("Cosmological constraints on curved quintessence", "S. Bhattacharya, G. Borghetto, A. Malhotra, S. Parameswaran, G. Tasinato, I. Zavala", "JCAP 09 (2024) 073. One of IOP Publishing’s most impactful UK publications of 2024", "2405.17396"),
                    ("The CosmoVerse White Paper: Addressing observational tensions in cosmology with systematics and fundamental physics", "E. Di Valentino et al. (CosmoVerse Network), including I. Zavala", "Phys. Dark Univ. 49 (2025) 101965", "2504.01669"),
                ],
            },
            {
                "title": "Coupled dark sectors and dark matter",
                "text": "Interactions between dark energy and dark matter, multi-field dynamical systems, and how dark matter relics depend on the expansion history of the early Universe.",
                "papers": [
                    ("Extending the Dynamical Systems Toolkit: Coupled Fields in Multiscalar Dark Energy", "D. Licciardello, S. Rahimy, I. Zavala", "JCAP 04 (2026) 057", "2509.02539"),
                    ("Deciphering coupled scalar dark sectors", "S. Rahimy, E. M. Teixeira, I. Zavala", "Phys. Rev. D 112 (2025) 043512", "2503.01961"),
                    ("D-brane Disformal Coupling and Thermal Dark Matter", "B. Dutta, E. Jimenez, I. Zavala", "Phys. Rev. D 96 (2017) 103506", "1708.07153"),
                    ("Dark Matter Relics and the Expansion Rate in Scalar-Tensor Theories", "B. Dutta, E. Jimenez, I. Zavala", "JCAP 06 (2017) 032", "1612.05553"),
                    ("Dark D-brane Cosmology", "T. Koivisto, D. Wills, I. Zavala", "JCAP 06 (2014) 036", "1312.2597"),
                ],
            },
        ],
    },
    {
        "id": "gravitational-waves",
        "title": "Gravitational Waves",
        "question": "Can gravitational waves from the early Universe reveal physics at the highest energies?",
        "subtopics": [
            {
                "title": "Primordial gravitational waves",
                "text": "Enhanced tensor spectra, scalar-induced gravitational waves and primordial black holes, and reconstructing primordial perturbations with LISA.",
                "papers": [
                    ("Bayesian reconstruction of primordial perturbations from induced gravitational waves", "A. Ghaleb, A. Malhotra, G. Tasinato, I. Zavala", "Phys. Rev. D 112 (2025) 123538", "2505.22534"),
                    ("Reconstructing primordial curvature perturbations via scalar-induced gravitational waves with LISA", "J. E. Gammal et al. (LISA Cosmology Working Group), including I. Zavala", "JCAP 05 (2025) 062", "2501.11320"),
                    ("The rise of the primordial tensor spectrum from an early scalar-tensor epoch", "D. Chowdhury, G. Tasinato, I. Zavala", "JCAP 08 (2022) 010", "2204.10218"),
                    ("A new mechanism to enhance primordial tensor fluctuations in single field inflation", "M. Mylova, O. Özsoy, S. Parameswaran, G. Tasinato, I. Zavala", "JCAP 12 (2018) 024", "1808.10475"),
                ],
            },
            {
                "title": "Detecting the gravitational-wave background",
                "text": "Anisotropies and circular polarisation of the stochastic background with pulsar timing arrays, astrometry, the SKA and the Einstein Telescope.",
                "papers": [
                    ("Probing Kinematic Anisotropies in the Stochastic Gravitational Wave Background with the SKA", "N. M. J. Cruz, A. Malhotra, G. Tasinato, I. Zavala", "Preprint (2026)", "2606.25845"),
                    ("Astrometry meets Pulsar Timing Arrays: Synergies for Gravitational Wave Detection", "N. M. J. Cruz, A. Malhotra, G. Tasinato, I. Zavala", "Phys. Rev. D 112 (2025)", "2412.14010"),
                    ("Measuring the circular polarization of gravitational waves with pulsar timing arrays", "N. M. J. Cruz, A. Malhotra, G. Tasinato, I. Zavala", "Phys. Rev. D 110 (2024) 103505", "2406.04957"),
                    ("Measuring kinematic anisotropies with pulsar timing arrays", "N. M. J. Cruz, A. Malhotra, G. Tasinato, I. Zavala", "Phys. Rev. D 110 (2024) 063526", "2402.17312"),
                    ("On the response of the Einstein Telescope to Doppler anisotropies", "D. Chowdhury, G. Tasinato, I. Zavala", "Phys. Rev. D 107 (2023) 083516", "2209.05770"),
                    ("Effect of extra dimensions on gravitational waves from cosmic strings", "E. O’Callaghan, S. Chadburn, G. Geshnizjani, R. Gregory, I. Zavala", "Phys. Rev. Lett. 105 (2010) 081602", "1003.4395"),
                    ("The effect of extra dimensions on gravity wave bursts from cosmic string cusps", "E. O’Callaghan, S. Chadburn, G. Geshnizjani, R. Gregory, I. Zavala", "JCAP 09 (2010) 013", "1005.3220"),
                ],
            },
        ],
    },
]
