# System Requirements

What each day needs: GPU, runtime, which Colab runtime it needs, downloads, RAM and API keys. Click a row for the details, which also appear at the start of each day. Runtimes leave out downloads and API calls; GPU times measured on a 16 GB RTX A4000 (FP32 19.2 TFLOPs, BF16 77 TFLOPs).

**We recommend for most days renting something comparable to the A4000**.
Any modern-ish gaming GPU you have locally (3000/4000/5000 series) will probably also suffice, but you might find it tight on memory constrained days.
See [here](https://slop.sus.cat/infrastructure/gpu-availability/#) to get a glance at GPU rental availability (which has been getting tight as of Q4 2026).

- **GPU:**
    - ⬜ not needed : The material doesn't use a GPU (e.g. an API heavy day), or the model is small enough that training it on CPU suffices.
    - 🟩 optional : The day runs faster on a GPU, but if you don't mind things running a bit slower or feedback loops being more sluggish, you can make do with CPU.
    - 🟨 recommended : *Technically* one could complete this day on CPU, but it would be frustrating, and you might be waiting hours for training runs to complete or skip some sections.
    - 🟧 16 GiB card : The day is de-facto impossible without a GPU, and VRAM requirements are non-trivial (expect to be loading and tinkering with LLMs).
    - 🟥 bigger : The day loads large VRAM hungry models for which a 16 GiB card won't be enough.
        - Every day has been adjusted to check for available VRAM, and then shrink things down (quantize the model, smaller batch size etc.)
          such that every day technically fits in 🟧, potentially at the cost of getting slightly different results.
- **Colab:**
    - 🟩 free : The free GPU (T4) on colab suffices.
    - 🟨 Pro recommended : T4 is an underpowered card, and lacks bf16 support, so these days run slow or tight on memory, and we recommend Colab Pro (L4).
    - 🟧 Pro : The day is so slow on T4 to be unusable, or we blow out the RAM/VRAM/Disk limits on Colab Free. Use an L4 GPU (next cheapest).
    - 🟥 Pro+ : Not even an L4 will do, will need an A100/G4 GPU (costly on compute credits!)
    - ❓ unknown: Not yet tested with colab.
- **Download:** ⬜ <0.3 GB · 🟩 <2 · 🟨 2–20 · 🟧 20–100 · 🟥 >100 GB
