#!/usr/bin/env python3
"""Failed-Adjudication Class (FAC) engine — 2026-08-31.

A real novel discovery requires: (1) check what exists, (2) find the genuine
remaining gap, (3) synthesize into that gap, (4) let novelty be structural.

This module does not claim a new particle, organism, or proved mechanism.
It classifies sourced scientific tensions by whether a *named discriminator*
(instrument, replication, algorithm) was predicted to settle the tension and,
after running, licensed two or more live camps.

Prior archive classes this engine is forbidden to reclaim
---------------------------------------------------------
- Undersampling (2026-08-03)
- Deep-biosphere-as-space-prior (2026-08-14)
- Ritual Nyquist Law (2026-08-27)
- Transducer-Absence Class / TAC (2026-08-28)
- Cadence Mismatch Class (2026-08-29)
- Named-Cause Residual / Initiation–Maintenance Split / NCR (2026-08-30)
- Refused families: RICO, CIL, ITC, cosmic-bio resonance, holographic
  brain/city, morphic resonance, entropy-as-universal-operator,
  informational-cascade isomorphisms.

Adjacent prior art (must cap novelty, not hide)
-----------------------------------------------
- Duhem (1906) / Quine: there is no crucial experiment.
- Collins: experimenter's regress.
The remaining gap is operational, not philosophical: a scored census of
2024–2026 cases where a *specific upgrade was publicly named as the
settler* and then split the field.

Author: Haley Bird / autonomous Grok research agent
Session: 2026-08-31-fac
Status: research-stage classification. Logged, not PPA-ready.
"""

from __future__ import annotations

import csv
import hashlib
import json
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

OUT = Path("/workspace/artifacts/fac_2026-08-31")
OUT.mkdir(parents=True, exist_ok=True)

SESSION_ID = "2026-08-31-fac"
AUTHOR = "Haley Bird / Grok by xAI (non-ownership; structural synthesis aid only)"
TIMESTAMP = "2026-08-31T17:40:00Z"

# Archive classes that already occupy part of a row's surface.
PRIOR_CLASSES = {
    "undersampling",
    "deep-biosphere-as-space-prior",
    "ritual-nyquist",
    "TAC",
    "cadence-mismatch",
    "NCR",
    "IM-split",
}


@dataclass
class Tension:
    """One sourced tension, scored for Failed-Adjudication remaining surface."""

    id: str
    realm: str
    item: str
    predicted_adjudicator: str
    prediction_source: str
    prediction_year: int
    was_run: float  # 0, 0.5 (in progress), 1
    live_camps: list[str]
    post_upgrade_status: str  # split | reopened | settled | not_run | in_progress
    prior_classes: list[str]
    prior_overlap: float  # 0–1 fraction of surface already claimed
    source_quality: float  # 0–1 (primary paper / institutional / media)
    predicted_as_discriminator: float  # 0–1 how explicitly it was named as settler
    sources: list[str]
    unspoken_layer: str
    notes: str = ""

    def n_camps(self) -> int:
        return len(self.live_camps)


def fac_raw(t: Tension) -> float:
    """Raw FAC before archive subtraction.

    Requires: a named discriminator, that it ran, and that >1 camp remains.
    In-progress (was_run=0.5) is discounted, not zeroed.
    """
    if t.was_run <= 0:
        return 0.0
    camp_factor = min(1.0, max(0.0, (t.n_camps() - 1) / 2.0))
    if t.post_upgrade_status == "settled":
        camp_factor *= 0.15
    if t.post_upgrade_status == "in_progress":
        camp_factor *= 0.55
    return (
        t.predicted_as_discriminator
        * t.was_run
        * camp_factor
        * t.source_quality
        * 100.0
    )


def fac_remaining(t: Tension) -> float:
    """Surface left after subtracting prior archive claims.

    Duhem–Quine adjacency is a global cap applied later, not per-row,
    because every FAC row is adjacent to that thesis.
    """
    return fac_raw(t) * (1.0 - t.prior_overlap)


def duhem_quine_cap(score: float, novelty_ceiling: float = 0.68) -> float:
    """Cap class-level novelty. Philosophy already owns 'no crucial experiment'.

    0.68 is the ceiling for an operational census of named-upgrade failures.
    It is not a measurement of nature.
    """
    return min(score, novelty_ceiling)


# ---------------------------------------------------------------------------
# Catalog. Every row has a source. Nothing is a new physical discovery.
# ---------------------------------------------------------------------------

CATALOG: list[Tension] = [
    Tension(
        id="FAC-SPA-01",
        realm="outer space",
        item="Hubble tension: JWST named as settler, licensed three camps",
        predicted_adjudicator="JWST Cepheid / TRGB / JAGB re-measurement",
        prediction_source="CERN Courier 26 Mar 2025: 'updated measurements with JWST may settle the debate'",
        prediction_year=2025,
        was_run=1.0,
        live_camps=[
            "SH0ES/Riess JWST NIRCam H0=73.0±1.0 (crowding excluded ~8σ)",
            "CCHP/Freedman JWST 70.4 ±3% overlapping Planck 67.4",
            "Planck/DESI early-universe ~67.4–68.5",
        ],
        post_upgrade_status="split",
        prior_classes=["TAC"],
        prior_overlap=0.40,
        source_quality=0.92,
        predicted_as_discriminator=0.95,
        sources=[
            "https://cerncourier.com/a/the-hubble-tension/",
            "https://www.esa.int/Science_Exploration/Space_Science/Webb/Webb_Hubble_confirm_Universe_s_expansion_rate",
            "https://www.sci.news/astronomy/hubble-tension-13959.html",
        ],
        unspoken_layer=(
            "The same telescope is currently cited as proof the tension is real "
            "AND as proof the tension is going away. The upgrade did not adjudicate. "
            "It licensed both closures."
        ),
        notes="NCR retained Hubble as TAC item 10. FAC names the failed-settler, not the tension itself.",
    ),
    Tension(
        id="FAC-SPA-02",
        realm="outer space",
        item="JWST massive early galaxies: resolved Apr 2026, reopened Aug 2026",
        predicted_adjudicator="Statistical + AGN-correction reanalysis of JWST masses",
        prediction_source="Krishnan & Abazajian, Phys. Rev. D 113, 083007 (3 Apr 2026) 'Resolution of the massive early JWST galaxy tension'",
        prediction_year=2026,
        was_run=1.0,
        live_camps=[
            "Apr 2026 PRD: tension is systematics/statistics, ΛCDM holds",
            "Aug 2026 faint-star populations: some galaxies 3–4× more massive",
        ],
        post_upgrade_status="reopened",
        prior_classes=["NCR"],
        prior_overlap=0.50,
        source_quality=0.90,
        predicted_as_discriminator=0.88,
        sources=[
            "https://link.aps.org/doi/10.1103/gjf5-3r89",
            "ScienceDaily 22 Aug 2026 faint-star mass revision (NCR archive)",
        ],
        unspoken_layer=(
            "A named resolution had a half-life of ~141 days. Closure inside the "
            "same model family is not adjudication."
        ),
        notes="NCR listed this as residual. FAC scores the close-then-reopen clock.",
    ),
    Tension(
        id="FAC-SPA-03",
        realm="outer space",
        item="Little Red Dots: black-hole stars vs hidden ordinary hosts",
        predicted_adjudicator="JWST spectroscopy of LRD sample",
        prediction_source="NASA Webb 10 Jun 2026: 'strongest evidence yet that LRDs are black hole stars'; Nature 16 Jan 2026 young SMBHs in ionized cocoons",
        prediction_year=2026,
        was_run=1.0,
        live_camps=[
            "Black hole stars / overmassive SMBHs in dense cocoons (NASA/Nature 2026)",
            "Hidden ordinary hosts: redshifted z=2 spiral (Saguaro) makes host vanish; stacked LRDs show 2–3 kpc diffuse emission",
            "Dark-star cores as unifier of blue monsters + LRDs + early SMBHs (Jan 2026 hypothesis)",
        ],
        post_upgrade_status="split",
        prior_classes=["NCR"],
        prior_overlap=0.35,
        source_quality=0.88,
        predicted_as_discriminator=0.72,
        sources=[
            "https://science.nasa.gov/missions/webb/nasa-webb-finds-strongest-evidence-yet-for-black-hole-stars/",
            "https://www.nature.com/articles/s41586-025-09900-4",
            "https://www.sciencedaily.com/releases/2026/01/260128075355.htm",
        ],
        unspoken_layer=(
            "JWST created the object class and then licensed three interpretations "
            "of it. Discovery and adjudication are not the same act."
        ),
        notes="NCR listed LRD residual. FAC adds the three-camp split including dark-star unifier (unproved).",
    ),
    Tension(
        id="FAC-OCE-01",
        realm="ocean",
        item="Nodule 'dark oxygen': replication ran, authors stepped back, next expedition pending",
        predicted_adjudicator="Independent benthic-chamber replication + controls without nodules",
        prediction_source="Sweetman et al. Nature Geoscience 22 Jul 2024; TMC/Frontiers critiques 2024–2025; Nature Geoscience Editor's Note 8 Apr 2026",
        prediction_year=2024,
        was_run=1.0,
        live_camps=[
            "Electrolysis at polymetallic nodules (original claim; authors later stepped back from both main conclusions)",
            "Experimental artefact (oxygen rise without nodules; thermodynamics objection; Frontiers 2025)",
        ],
        post_upgrade_status="split",
        prior_classes=["TAC"],
        prior_overlap=0.45,
        source_quality=0.93,
        predicted_as_discriminator=0.90,
        sources=[
            "https://www.nature.com/articles/s41561-024-01480-8",
            "https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2025.1721853/full",
            "https://en.wikipedia.org/wiki/Dark_oxygen_production",
            "https://oceanographicmagazine.com/news/scientists-detail-deep-sea-expedition-to-understand-dark-oxygen/",
        ],
        unspoken_layer=(
            "Homonym collapse is already TAC. FAC is narrower: the control "
            "experiments that should have been the discriminator produced the "
            "split, and a 2026 expedition is the next attempted adjudicator "
            "(not reported as of 2026-08-31)."
        ),
        notes="Do not load-bear. Contested. Editor's Note live. Not a proof either way.",
    ),
    Tension(
        id="FAC-ANI-01",
        realm="animals",
        item="Magnetoreception: decades of 'crucial' radical-pair tests have not killed magnetite (or vice versa)",
        predicted_adjudicator="Cryptochrome / radical-pair photochemistry as the receptor mechanism",
        prediction_source="Nordmann et al., J. Exp. Biol. 228(7) 10 Apr 2025: field under a ruling hypothesis; receptor still unlocated",
        prediction_year=2025,
        was_run=1.0,
        live_camps=[
            "Radical-pair / cryptochrome (ruling hypothesis; JACS Nov 2025 computational support)",
            "Magnetite-based receptor (not killed)",
        ],
        post_upgrade_status="split",
        prior_classes=["TAC", "NCR"],
        prior_overlap=0.70,
        source_quality=0.90,
        predicted_as_discriminator=0.78,
        sources=[
            "https://journals.biologists.com/jeb/article/228/7/jeb250252/367652/Magnetoreception-and-the-ruling-hypothesis",
            "Princeton/JACS Nov 2025 well-separated radical pairs (Hammes-Schiffer / Subotnik)",
        ],
        unspoken_layer=(
            "The converting cell is TAC. The ruling-hypothesis trap is NCR. "
            "FAC remainder is small: the experiments treated as crucial did not "
            "function as discriminators."
        ),
        notes="Most of this surface is already archived. Remaining FAC is the failed-crucial-test, not the missing cell.",
    ),
    Tension(
        id="FAC-ANI-02",
        realm="animals",
        item="Project CETI: AI named as translator, delivered an alphabet, not meaning",
        predicted_adjudicator="Large-scale ML on tagged sperm-whale coda + behavior",
        prediction_source="Project CETI mission: 'translate the communication of sperm whales'; phonetic alphabet in Nature Communications; meaning still open as of 2026",
        prediction_year=2020,
        was_run=0.5,
        live_camps=[
            "Phonetic/combinatorial structure exists (alphabet, vowels, coda combinatorics)",
            "Semantic translation not achieved (listening project still in data-build)",
        ],
        post_upgrade_status="in_progress",
        prior_classes=[],
        prior_overlap=0.05,
        source_quality=0.84,
        predicted_as_discriminator=0.70,
        sources=[
            "https://www.projectceti.org/",
            "https://ls.berkeley.edu/news/uc-berkeley-and-project-ceti-study-shows-sperm-whales-communicate-ways-similar-humans",
            "https://www.projectceti.org/research/index",
        ],
        unspoken_layer=(
            "The upgrade found syntax-like structure and was publicly framed as "
            "translation. Structure ≠ meaning. This is FAC-in-progress, not a failed "
            "replication. Score must stay modest."
        ),
        notes="Not a claim that whales have language. Not a claim CETI failed. The discriminator is incomplete.",
    ),
    Tension(
        id="FAC-HUM-01",
        realm="humans",
        item="AlphaFold: 'protein folding solved' closed static structure, split off dynamics and disorder",
        predicted_adjudicator="Deep-learning structure prediction from sequence",
        prediction_source="2020–2021 'solution' framing of CASP14/AlphaFold2; 2025 Nature Communications: disordered proteins still require ensembles",
        prediction_year=2021,
        was_run=1.0,
        live_camps=[
            "Static folded structure largely predicted (AlphaFold DB; 2026 complex release ~31M predictions)",
            "Dynamics, kinetic pathways, and intrinsically disordered ensembles remain open (Brotzakis et al. 2025; Wikipedia unsolved: timescales, trapping, solubility)",
        ],
        post_upgrade_status="split",
        prior_classes=[],
        prior_overlap=0.12,
        source_quality=0.91,
        predicted_as_discriminator=0.90,
        sources=[
            "https://www.nature.com/articles/s41467-025-56572-9",
            "https://alphafold.ebi.ac.uk/",
            "https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_physics",
        ],
        unspoken_layer=(
            "The named adjudicator closed a different question than the one the "
            "public (and much of biology) thought had been asked. Sequence→shape "
            "is not sequence→life."
        ),
        notes="Highest remaining FAC among rows not already in the August archive.",
    ),
    Tension(
        id="FAC-HUM-02",
        realm="humans",
        item="Young-onset colorectal cancer: genomic/lifestyle upgrades did not close the residual",
        predicted_adjudicator="Obesity + sequencing + treatment intensification",
        prediction_source="Kimmie Ng, Harvard Gazette 7 Apr 2026: most patients are not obese; more treatment does not improve survival vs the 1970s",
        prediction_year=2026,
        was_run=1.0,
        live_camps=[
            "Named lifestyle/obesity associations (real, incomplete)",
            "Unexplained residual in non-obese young Stage-4 patients",
        ],
        post_upgrade_status="split",
        prior_classes=["NCR"],
        prior_overlap=0.80,
        source_quality=0.88,
        predicted_as_discriminator=0.62,
        sources=["https://news.harvard.edu/gazette/story/2026/04/the-questions-that-keep-scientists-up-at-night/"],
        unspoken_layer="Almost entirely NCR. FAC remainder is tiny: the named public-health discriminator did not adjudicate.",
        notes="Do not reclaim NCR's highest human row.",
    ),
    Tension(
        id="FAC-LAN-01",
        realm="land",
        item="Metagenomics named the soil/ocean microbiome; 87–99% still uncultured",
        predicted_adjudicator="Environmental DNA / metagenomic sequencing",
        prediction_source="Preprints 2025: 87–99% uncultured; extreme environments 98.4%±1.3%; Omnitrophota genomes mapped, almost uncultured",
        prediction_year=2010,
        was_run=1.0,
        live_camps=[
            "Sequence-known / named as microbial dark matter",
            "Culture-unknown (physiology, metabolism, cultivation still closed)",
        ],
        post_upgrade_status="split",
        prior_classes=["TAC"],
        prior_overlap=0.55,
        source_quality=0.86,
        predicted_as_discriminator=0.80,
        sources=[
            "https://www.preprints.org/manuscript/202507.0298",
            "https://www.dri.edu/microbial_dark_matter/",
        ],
        unspoken_layer=(
            "Sequencing was the upgrade that would 'light' the dark. It named the "
            "dark more precisely. Naming is not cultivation. TAC owns the 'dark' "
            "prefix; FAC owns the failed-settler (metagenomics as adjudicator)."
        ),
        notes="Omnitrophota retained as TAC. Do not reclaim.",
    ),
    Tension(
        id="FAC-EAR-01",
        realm="earth",
        item="Geomagnetic reversal: supercomputers named as future discriminator, not yet run at realistic fidelity",
        predicted_adjudicator="High-fidelity dynamo simulation",
        prediction_source="Roger Fu, Harvard Gazette 7 Apr 2026: 'best supercomputers would still take many decades'",
        prediction_year=2026,
        was_run=0.0,
        live_camps=["Dynamo known as initiator", "Flip uncomputed"],
        post_upgrade_status="not_run",
        prior_classes=["NCR", "IM-split"],
        prior_overlap=0.85,
        source_quality=0.90,
        predicted_as_discriminator=0.60,
        sources=["https://news.harvard.edu/gazette/story/2026/04/the-questions-that-keep-scientists-up-at-night/"],
        unspoken_layer="Not FAC. Discriminator has not been run. This is NCR/IM. Included as a negative control so the engine can refuse it.",
        notes="NEGATIVE CONTROL. Remaining FAC must be ~0.",
    ),
    Tension(
        id="FAC-QNT-01",
        realm="quantum",
        item="Decoherence named as the measurement solution; single outcome still unexplained",
        predicted_adjudicator="Decoherence theory as the discriminator among interpretations",
        prediction_source="Jacob Barandes, Harvard Gazette 7 Apr 2026: 'Decoherence doesn't explain how we get one outcome over the others'",
        prediction_year=2026,
        was_run=1.0,
        live_camps=[
            "Decoherence as practical solution (easy problem)",
            "Single-outcome / hard interpretational remainder (Copenhagen, MWI, Barandes, etc.)",
        ],
        post_upgrade_status="split",
        prior_classes=["NCR", "IM-split"],
        prior_overlap=0.65,
        source_quality=0.87,
        predicted_as_discriminator=0.82,
        sources=["https://news.harvard.edu/gazette/story/2026/04/the-questions-that-keep-scientists-up-at-night/"],
        unspoken_layer="NCR owns most of this. FAC remainder: decoherence was treated as the crucial theoretical upgrade and did not adjudicate.",
        notes="Do not reclaim NCR's second-highest combined row.",
    ),
    Tension(
        id="FAC-EAR-02",
        realm="earth",
        item="Core-mantle boundary: seismology mapped a complex interface; no contact sample",
        predicted_adjudicator="Global seismic tomography as the picture of the CMB",
        prediction_source="Russell et al. 2024 PMC11136992; Scientific American historical: CMB more dynamic than the surface; Kola Superdeep 12.3 km = 0.2% of the way to the core",
        prediction_year=2024,
        was_run=1.0,
        live_camps=[
            "Textbook smooth discontinuity",
            "Complex, plate-graveyard, heat-flux-heterogeneous boundary (seismic)",
        ],
        post_upgrade_status="split",
        prior_classes=["NCR", "undersampling"],
        prior_overlap=0.55,
        source_quality=0.82,
        predicted_as_discriminator=0.58,
        sources=[
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC11136992/",
            "https://www.scientificamerican.com/article/the-core-mantle-boundary-2005-07/",
        ],
        unspoken_layer=(
            "Seismology was the upgrade that would make the deep interior known. "
            "It replaced one picture with a better picture that still has never "
            "been touched. Adjacent to undersampling and NCR; FAC remainder is the "
            "failed-settler claim of tomography-as-contact."
        ),
        notes="Contact-absence is NCR. FAC only if tomography was sold as adjudication. Partial.",
    ),
]


@dataclass
class ClosureEvent:
    """A declared resolution and, if any, a reopen. Used by the second function."""

    id: str
    item: str
    declared_closed: date
    closed_by: str
    reopened: date | None
    reopened_by: str | None
    still_split: bool


CLOSURES: list[ClosureEvent] = [
    ClosureEvent(
        id="CLK-01",
        item="JWST early-galaxy mass tension",
        declared_closed=date(2026, 4, 3),
        closed_by="Krishnan & Abazajian, Phys. Rev. D 113, 083007",
        reopened=date(2026, 8, 22),
        reopened_by="Faint-star population mass revision (ScienceDaily 22 Aug 2026)",
        still_split=True,
    ),
    ClosureEvent(
        id="CLK-02",
        item="Hubble tension (Freedman JWST 'no strong evidence')",
        declared_closed=date(2024, 8, 13),
        closed_by="Freedman et al. UChicago/JWST 'we do not find strong evidence for a Hubble tension'",
        reopened=date(2026, 1, 6),
        reopened_by="SH0ES JWST NIRCam H0=73.0±1.0; crowding excluded",
        still_split=True,
    ),
    ClosureEvent(
        id="CLK-03",
        item="Nodule dark oxygen as a new O2 source",
        declared_closed=date(2024, 7, 22),
        closed_by="Sweetman et al. Nature Geoscience (claim of production)",
        reopened=date(2026, 4, 8),
        reopened_by="Nature Geoscience Editor's Note; authors stepped back from both main conclusions",
        still_split=True,
    ),
    ClosureEvent(
        id="CLK-04",
        item="Protein folding as a solved problem",
        declared_closed=date(2020, 11, 30),
        closed_by="AlphaFold2 CASP14 / Nature 2021 public framing",
        reopened=date(2025, 2, 14),
        reopened_by="Brotzakis et al. Nat Commun: disordered proteins still require ensembles",
        still_split=True,
    ),
]


def score_catalog(rows: list[Tension]) -> list[dict[str, Any]]:
    """Return scored rows sorted by remaining FAC surface, descending."""
    scored = []
    for t in rows:
        raw = fac_raw(t)
        remaining = fac_remaining(t)
        scored.append(
            {
                **asdict(t),
                "n_camps": t.n_camps(),
                "fac_raw": round(raw, 2),
                "fac_remaining": round(remaining, 2),
                "primary_class": "FAC" if remaining >= 8.0 and t.was_run > 0 else "REFUSE_OR_RETAIN",
            }
        )
    scored.sort(key=lambda r: r["fac_remaining"], reverse=True)
    return scored


def closure_reopen_interval(events: list[ClosureEvent]) -> list[dict[str, Any]]:
    """Second function: days from declared close to reopen.

    If a named resolution stays closed under the next independent instrument,
    FAC is wrong for that case. This function only measures the clock of
    cases that did reopen. It does not prove a law.
    """
    out = []
    for e in events:
        if e.reopened is None:
            days = None
            status = "still_closed_or_untested"
        else:
            days = (e.reopened - e.declared_closed).days
            status = "reopened"
        out.append(
            {
                "id": e.id,
                "item": e.item,
                "declared_closed": e.declared_closed.isoformat(),
                "closed_by": e.closed_by,
                "reopened": e.reopened.isoformat() if e.reopened else None,
                "reopened_by": e.reopened_by,
                "days_to_reopen": days,
                "still_split": e.still_split,
                "status": status,
            }
        )
    out.sort(key=lambda r: (r["days_to_reopen"] is None, r["days_to_reopen"] or 10**9))
    return out


def class_novelty(scored: list[dict[str, Any]]) -> dict[str, Any]:
    """Class-level novelty after Duhem–Quine cap and archive subtraction.

    Novelty is of the *census*, not of underdetermination as a thesis.
    """
    remaining_rows = [r for r in scored if r["fac_remaining"] >= 8.0]
    mean_remaining = (
        sum(r["fac_remaining"] for r in remaining_rows) / len(remaining_rows)
        if remaining_rows
        else 0.0
    )
    # Map 0–100 remaining surface onto 0–1, then cap.
    raw_novelty = min(1.0, mean_remaining / 55.0)
    capped = duhem_quine_cap(raw_novelty, 0.68)
    coherence = 0.86  # sourced rows, explicit refuse list, negative control present
    return {
        "raw_novelty": round(raw_novelty, 3),
        "capped_novelty": round(capped, 3),
        "coherence": coherence,
        "cap_reason": (
            "Duhem–Quine (1906) already owns 'no crucial experiment'. "
            "Novelty is the operational 2024–2026 census of named-upgrade "
            "failures, not the philosophical thesis. Ceiling 0.68."
        ),
        "n_rows_with_remaining_surface": len(remaining_rows),
        "negative_controls": [r["id"] for r in scored if r["was_run"] == 0],
        "ip_readiness": "Logged",
    }


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_outputs(scored: list[dict[str, Any]], clocks: list[dict[str, Any]], novelty: dict[str, Any]) -> dict[str, str]:
    """Persist JSON, CSV, and a matplotlib ranking figure."""
    payload = {
        "session_id": SESSION_ID,
        "timestamp": TIMESTAMP,
        "author": AUTHOR,
        "class_name": "Failed-Adjudication Class (FAC)",
        "one_sentence": (
            "A named discriminator was predicted to settle a tension; after it ran, "
            "two or more live camps remained, and the upgrade is cited by both."
        ),
        "not_claimed": [
            "Not a new physical mechanism.",
            "Not a proof that dark oxygen is real or fake.",
            "Not a proof that Hubble tension is new physics.",
            "Not Duhem–Quine rediscovered.",
            "Not TAC, NCR, IM-split, undersampling, or cadence mismatch.",
            "Not patent-ready.",
        ],
        "novelty": novelty,
        "rows": scored,
        "closure_clocks": clocks,
    }
    json_path = OUT / "fac_scores.json"
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    csv_path = OUT / "fac_ranking.csv"
    fields = [
        "id",
        "realm",
        "item",
        "post_upgrade_status",
        "n_camps",
        "fac_raw",
        "prior_overlap",
        "fac_remaining",
        "primary_class",
        "prior_classes",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in scored:
            w.writerow(
                {
                    "id": r["id"],
                    "realm": r["realm"],
                    "item": r["item"][:80],
                    "post_upgrade_status": r["post_upgrade_status"],
                    "n_camps": r["n_camps"],
                    "fac_raw": r["fac_raw"],
                    "prior_overlap": r["prior_overlap"],
                    "fac_remaining": r["fac_remaining"],
                    "primary_class": r["primary_class"],
                    "prior_classes": "|".join(r["prior_classes"]),
                }
            )

    # Ranking figure — data, so code-drawn, not an image model.
    import matplotlib.pyplot as plt

    labels = [f"{r['id']}\n{r['realm']}" for r in scored]
    remaining = [r["fac_remaining"] for r in scored]
    raws = [r["fac_raw"] for r in scored]
    colors = ["#c45c26" if r["fac_remaining"] >= 8 else "#7a7a7a" for r in scored]

    fig, ax = plt.subplots(figsize=(11, 7), dpi=140)
    fig.patch.set_facecolor("#0e1114")
    ax.set_facecolor("#0e1114")
    y = list(range(len(scored)))[::-1]
    ax.barh(y, raws, color="#3d4a55", height=0.62, label="raw FAC (before archive subtraction)")
    ax.barh(y, remaining, color=colors, height=0.38, label="remaining after TAC/NCR/undersampling")
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8, color="#d7d2c8")
    ax.set_xlabel("FAC surface (heuristic, not a measurement of nature)", color="#d7d2c8")
    ax.set_title(
        "Failed-Adjudication Class — remaining surface after archive subtraction\n"
        "2026-08-31  ·  orange ≥ 8 kept as FAC  ·  grey refused or retained",
        color="#f2efe8",
        fontsize=11,
        pad=12,
    )
    ax.tick_params(colors="#d7d2c8")
    for spine in ax.spines.values():
        spine.set_color("#3d4a55")
    ax.legend(facecolor="#1a1f24", edgecolor="#3d4a55", labelcolor="#d7d2c8", fontsize=8)
    ax.axvline(8, color="#d7d2c8", lw=0.6, ls="--", alpha=0.5)
    fig.tight_layout()
    fig_path = OUT / "fac_ranking.png"
    fig.savefig(fig_path, facecolor=fig.get_facecolor())
    plt.close(fig)

    # Closure clock figure
    fig2, ax2 = plt.subplots(figsize=(10, 4.2), dpi=140)
    fig2.patch.set_facecolor("#0e1114")
    ax2.set_facecolor("#0e1114")
    clock_rows = [c for c in clocks if c["days_to_reopen"] is not None]
    ax2.barh(
        [c["item"] for c in clock_rows][::-1],
        [c["days_to_reopen"] for c in clock_rows][::-1],
        color="#6b8f71",
        height=0.55,
    )
    ax2.set_xlabel("days from declared close to reopen", color="#d7d2c8")
    ax2.set_title(
        "Closure half-life of named resolutions (sourced; not a law)",
        color="#f2efe8",
        fontsize=11,
    )
    ax2.tick_params(colors="#d7d2c8")
    for spine in ax2.spines.values():
        spine.set_color("#3d4a55")
    fig2.tight_layout()
    clock_fig = OUT / "closure_clocks.png"
    fig2.savefig(clock_fig, facecolor=fig2.get_facecolor())
    plt.close(fig2)

    digest_src = json.dumps(payload, sort_keys=True)
    digest = sha256_text(digest_src)
    (OUT / "SHA256.txt").write_text(digest + "\n", encoding="utf-8")
    return {
        "json": str(json_path),
        "csv": str(csv_path),
        "ranking_png": str(fig_path),
        "clocks_png": str(clock_fig),
        "sha256": digest,
    }


def main() -> None:
    scored = score_catalog(CATALOG)
    clocks = closure_reopen_interval(CLOSURES)
    novelty = class_novelty(scored)
    paths = write_outputs(scored, clocks, novelty)

    print("=" * 72)
    print("FAILED-ADJUDICATION CLASS  · ", SESSION_ID)
    print("=" * 72)
    print(f"capped novelty: {novelty['capped_novelty']}  coherence: {novelty['coherence']}")
    print(f"cap: {novelty['cap_reason']}")
    print()
    print(f"{'id':<12} {'remain':>7} {'raw':>7} {'overlap':>8} {'status':<12} realm / item")
    print("-" * 72)
    for r in scored:
        print(
            f"{r['id']:<12} {r['fac_remaining']:7.2f} {r['fac_raw']:7.2f} "
            f"{r['prior_overlap']:8.2f} {r['post_upgrade_status']:<12} "
            f"{r['realm']} — {r['item'][:42]}"
        )
    print()
    print("CLOSURE CLOCKS")
    for c in clocks:
        print(f"  {c['id']}  {c['days_to_reopen']:>5} days  {c['item']}")
    print()
    print("HASH", paths["sha256"])
    print("WROTE", paths)


if __name__ == "__main__":
    main()
