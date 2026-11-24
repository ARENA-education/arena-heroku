# System Requirements

What each day needs: GPU, runtime, which Colab runtime it needs, downloads, RAM and API keys. Click a row for the details, which also appear at the start of each day. Runtimes leave out downloads and API calls; GPU times measured on a 16 GB RTX A4000 (FP32 19.2 TFLOPs, BF16 77 TFLOPs).

**We recommend for most days renting something comparable to the A4000. Any modern-ish gaming GPU you have locally (3000/4000/5000 series) will probably also suffice, but you might find it tight on memory constrained days.** See [here](https://slop.sus.cat/infrastructure/gpu-availability/#) to get a glance at GPU rental availability.

- **GPU:** ⬜ not needed · 🟩 optional · 🟨 recommended · 🟧 16 GiB card · 🟥 bigger; peak VRAM (with `LOW_GPU_MEM`); * skips a section that needs more
- **Colab:** 🟩 free (T4) · 🟨 Pro recommended (slow on the free T4) · 🟧 needs Pro (L4) · 🟥 needs an A100 or G4 · ❓ not tested yet
- **Download:** ⬜ <0.3 GB · 🟩 <2 · 🟨 2–20 · 🟧 20–100 · 🟥 >100 GB
