#!/usr/bin/env python3
"""Iterate: camp-citation symmetry.

FAC's tell is not 'two interpretations exist' (that is ordinary science).
The tell is: *both camps cite the same upgrade as supporting evidence*.

This function takes the scored catalog and a hand-coded citation map
(sourced; not inferred) and returns a symmetry flag per row.

If symmetry is false, the row is ordinary disagreement, not FAC.
"""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path("/workspace/artifacts/fac_2026-08-31")

# Sourced: each camp's public claim about the SAME upgrade.
SYMMETRY = {
    "FAC-SPA-01": {
        "upgrade": "JWST",
        "camp_a_cites_as": "proof crowding is gone, local H0=73 is real (SH0ES/ESA)",
        "camp_b_cites_as": "proof tension is weakening, H0=70.4 overlaps Planck (Freedman/Sci.News 2025)",
        "symmetric": True,
        "source": "CERN Courier 2025; ESA Webb/Hubble confirmation; Sci.News 3 Jun 2025",
    },
    "FAC-SPA-02": {
        "upgrade": "JWST mass catalog + reanalysis",
        "camp_a_cites_as": "statistical resolution of the tension (PRD 3 Apr 2026)",
        "camp_b_cites_as": "faint-star populations make some systems 3–4× more massive (Aug 2026)",
        "symmetric": True,
        "source": "Phys. Rev. D 113, 083007; ScienceDaily 22 Aug 2026",
    },
    "FAC-SPA-03": {
        "upgrade": "JWST LRD spectroscopy/imaging",
        "camp_a_cites_as": "strongest evidence yet for black hole stars (NASA 10 Jun 2026)",
        "camp_b_cites_as": "host-hiding: a redshifted ordinary spiral vanishes into an LRD",
        "symmetric": True,
        "source": "NASA Webb 10 Jun 2026; Nature 16 Jan 2026; NCR archive Saguaro study",
    },
    "FAC-OCE-01": {
        "upgrade": "benthic-chamber oxygen sensors + nodule-free controls",
        "camp_a_cites_as": "oxygen production at the abyssal seafloor (Sweetman 2024)",
        "camp_b_cites_as": "the same chambers produce O2 without nodules (Frontiers 2025)",
        "symmetric": True,
        "source": "Nature Geoscience 2024; Frontiers Mar Sci 2025; Editor's Note 8 Apr 2026",
    },
    "FAC-HUM-01": {
        "upgrade": "AlphaFold2/3 structure prediction",
        "camp_a_cites_as": "folding problem solved at static 3D accuracy (CASP14 framing)",
        "camp_b_cites_as": "disordered proteins still require ensembles (Nat Commun 2025)",
        "symmetric": True,
        "source": "Brotzakis et al. 2025; AlphaFold DB 2026 complex release",
    },
    "FAC-LAN-01": {
        "upgrade": "metagenomic sequencing",
        "camp_a_cites_as": "the microbiome is now knowable from DNA",
        "camp_b_cites_as": "87–99% remain uncultured after sequencing (2025 preprints)",
        "symmetric": True,
        "source": "preprints.org/manuscript/202507.0298",
    },
    "FAC-ANI-01": {
        "upgrade": "cryptochrome/radical-pair assays",
        "camp_a_cites_as": "computational support for radical-pair compass (JACS 2025)",
        "camp_b_cites_as": "ruling-hypothesis trap; receptor still unlocated (JEB 2025)",
        "symmetric": True,
        "source": "Nordmann et al. JEB 2025; Princeton JACS 2025",
    },
    "FAC-ANI-02": {
        "upgrade": "CETI ML on whale codas",
        "camp_a_cites_as": "phonetic alphabet / vowels (Nat Commun)",
        "camp_b_cites_as": None,
        "symmetric": False,
        "source": "projectceti.org — meaning camp is absence, not a competing citation of the same model",
    },
    "FAC-HUM-02": {
        "upgrade": "obesity/lifestyle + genomic oncology",
        "camp_a_cites_as": "associations exist",
        "camp_b_cites_as": "most young Stage-4 patients are not obese (Ng 2026)",
        "symmetric": False,
        "source": "Harvard Gazette — this is NCR residual, not two camps citing one upgrade as proof",
    },
    "FAC-EAR-01": {
        "upgrade": "exascale dynamo simulation",
        "camp_a_cites_as": None,
        "camp_b_cites_as": None,
        "symmetric": False,
        "source": "not run",
    },
    "FAC-EAR-02": {
        "upgrade": "seismic tomography",
        "camp_a_cites_as": "maps a complex CMB",
        "camp_b_cites_as": None,
        "symmetric": False,
        "source": "the textbook-smooth camp is inertia, not a citation of tomography",
    },
    "FAC-QNT-01": {
        "upgrade": "decoherence theory",
        "camp_a_cites_as": "practical solution to apparent collapse",
        "camp_b_cites_as": "does not select one outcome (Barandes 2026)",
        "symmetric": True,
        "source": "Harvard Gazette 7 Apr 2026",
    },
}


def apply_symmetry(scored_path: Path) -> dict:
    data = json.loads(scored_path.read_text())
    n_true = 0
    n_false = 0
    kept = []
    refused = []
    for row in data["rows"]:
        sym = SYMMETRY.get(row["id"], {"symmetric": False, "source": "unmapped"})
        row["citation_symmetric"] = bool(sym.get("symmetric"))
        row["symmetry_note"] = {
            "upgrade": sym.get("upgrade"),
            "camp_a_cites_as": sym.get("camp_a_cites_as"),
            "camp_b_cites_as": sym.get("camp_b_cites_as"),
            "source": sym.get("source"),
        }
        if row["citation_symmetric"] and row["fac_remaining"] >= 8:
            n_true += 1
            kept.append(row["id"])
        else:
            n_false += 1
            refused.append(row["id"])
            # Ordinary disagreement is not FAC. Zero remaining if not symmetric.
            if not row["citation_symmetric"]:
                row["fac_remaining_after_symmetry"] = 0.0
            else:
                row["fac_remaining_after_symmetry"] = row["fac_remaining"]
        if row["citation_symmetric"]:
            row["fac_remaining_after_symmetry"] = row["fac_remaining"]
        else:
            row["fac_remaining_after_symmetry"] = 0.0

    data["symmetry_audit"] = {
        "kept_as_FAC": kept,
        "refused_as_ordinary_disagreement_or_prior": refused,
        "n_symmetric": n_true,
        "rule": (
            "FAC requires both live camps to cite the same upgrade as evidence. "
            "If only one camp cites it, the row is ordinary disagreement or NCR."
        ),
    }
    out = OUT / "fac_scores_symmetric.json"
    out.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return {
        "kept": kept,
        "refused": refused,
        "path": str(out),
        "n_symmetric_kept": n_true,
    }


if __name__ == "__main__":
    result = apply_symmetry(OUT / "fac_scores.json")
    print("SYMMETRY AUDIT")
    print("kept as FAC:", ", ".join(result["kept"]))
    print("refused:    ", ", ".join(result["refused"]))
    print("wrote", result["path"])
